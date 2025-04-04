# This was cowritten by Claude AI and me

# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
from matplotlib import cm


# %%
def crank_nicolson_diffusion_2d(
    u_init,
    tmax,
    dt,
    dx,
    dy,
    boundary_conditions,
    egg_domain,
):
    """
    Solve the 2D diffusion equation C(u) * du/dt = d/dx(k(u) * du/dx) + d/dy(k(u) * du/dy) using Crank-Nicolson method.

    Parameters:
    -----------
    u_init : 2D array
        Initial condition for u
    tmax : float
        Maximum simulation time
    dt : float
        Time step size
    dx : float
        Spatial step size in x direction
    dy : float
        Spatial step size in y direction
    boundary_conditions : function
        Function that applies boundary conditions at each time step
    egg_domain: np.ndarray

    Returns:
    --------
    u_history : array
        Solution for selected time steps
    t_saved : array
        Saved time points
    """
    # Initialize
    ny, nx = u_init.shape
    nt = int(tmax / dt) + 1

    # We'll save fewer time steps to save memory
    save_interval = max(1, nt // 20)  # Save approximately 20 snapshots
    n_saves = nt // save_interval + 1

    # Storage for solution at saved times
    u_history = np.zeros((n_saves, ny, nx))
    t_saved = np.zeros(n_saves)

    # Initial condition
    u = u_init.copy()
    u_history[0] = u
    t_saved[0] = 0

    # Main time loop
    save_idx = 1
    for timestep in range(1, nt):
        u = compute_next_u(
            u=u,
            timestep=timestep,
            dt=dt,
            dx=dx,
            dy=dy,
            nx=nx,
            ny=ny,
            egg_domain=egg_domain,
            boundary_conditions=boundary_conditions,
        )

        # Save at specified intervals
        if timestep % save_interval == 0:
            u_history[save_idx] = u
            t_saved[save_idx] = timestep * dt
            save_idx += 1

    # Ensure the final state is saved
    if (nt - 1) % save_interval != 0:
        u_history[save_idx] = u
        t_saved[save_idx] = (nt - 1) * dt
        save_idx += 1

    return u_history[:save_idx], t_saved[:save_idx]


def compute_next_u(
    u,
    timestep,
    dt,
    dx,
    dy,
    nx,
    ny,
    egg_domain,
    boundary_conditions,
):
    # Update for nonlinearity: use simple fixed-point iteration
    max_iter = 10
    tolerance = 1e-6
    u_new = u.copy()

    for iteration in range(max_iter):
        A, b = build_matrix_and_b_equations(
            u=u,
            dt=dt,
            dx=dx,
            dy=dy,
            nx=nx,
            ny=ny,
            egg_domain=egg_domain,
        )

        # Apply boundary conditions
        A, b = boundary_conditions(A, b, u, timestep, dt, nx, ny)

        # Solve system
        u_flat = spsolve(A, b)
        u_new_iter = u_flat.reshape((ny, nx))

        # Check convergence
        if np.max(np.abs(u_new_iter - u_new)) < tolerance:
            u_new = u_new_iter
            break

        u_new = u_new_iter

        return u_new


def build_matrix_and_b_equations(
    u,
    dt,
    dx,
    dy,
    nx,
    ny,
    egg_domain,
):
    # Coefficients for the finite difference scheme
    rx = dt / (2 * dx**2)
    ry = dt / (2 * dy**2)

    # Number of unknowns
    N = nx * ny
    # Calculate coefficients based on current approximation
    C_values = C_func(u)
    k_values = k_func(u)

    # Calculate k at cell interfaces (i+1/2, i-1/2, j+1/2, j-1/2)
    # For simplicity, we use arithmetic mean
    k_x_plus = np.zeros_like(k_values)
    k_x_minus = np.zeros_like(k_values)
    k_y_plus = np.zeros_like(k_values)
    k_y_minus = np.zeros_like(k_values)

    # Interior points
    for j in range(1, ny - 1):
        for i in range(1, nx - 1):
            k_x_plus[j, i] = 0.5 * (k_values[j, i] + k_values[j, i + 1])
            k_x_minus[j, i] = 0.5 * (k_values[j, i] + k_values[j, i - 1])
            k_y_plus[j, i] = 0.5 * (k_values[j, i] + k_values[j + 1, i])
            k_y_minus[j, i] = 0.5 * (k_values[j, i] + k_values[j - 1, i])

    # Initialize sparse matrix data structures
    # For each interior point, we have a 5-point stencil
    # (center, left, right, up, down)
    nnz = 5 * (nx - 2) * (ny - 2)  # non-zero elements for interior points
    nnz += 2 * (nx + ny - 4)  # boundary points (simplified)

    # Initialize arrays for CSR format
    data = np.zeros(nnz)
    row_ind = np.zeros(nnz, dtype=int)
    col_ind = np.zeros(nnz, dtype=int)

    # Initialize right-hand side
    b = np.zeros(N)

    # Fill the matrix and right-hand side for interior points
    idx = 0
    for j in range(1, ny - 1):
        for i in range(1, nx - 1):
            # Global index for point (i, j)
            p = j * nx + i

            # Coefficients for implicit part
            # Center point
            center_coeff = (
                C_values[j, i]
                + rx * (k_x_plus[j, i] + k_x_minus[j, i])
                + ry * (k_y_plus[j, i] + k_y_minus[j, i])
            )

            # Neighboring points
            left_coeff = -rx * k_x_minus[j, i]
            right_coeff = -rx * k_x_plus[j, i]
            down_coeff = -ry * k_y_minus[j, i]
            up_coeff = -ry * k_y_plus[j, i]

            # Add center point
            row_ind[idx] = p
            col_ind[idx] = p
            data[idx] = center_coeff
            idx += 1

            # Add left point
            row_ind[idx] = p
            col_ind[idx] = p - 1
            data[idx] = left_coeff
            idx += 1

            # Add right point
            row_ind[idx] = p
            col_ind[idx] = p + 1
            data[idx] = right_coeff
            idx += 1

            # Add down point
            row_ind[idx] = p
            col_ind[idx] = p - nx
            data[idx] = down_coeff
            idx += 1

            # Add up point
            row_ind[idx] = p
            col_ind[idx] = p + nx
            data[idx] = up_coeff
            idx += 1

            # Right-hand side (explicit part)
            explicit_term_x = rx * (
                k_x_plus[j, i] * (u[j, i + 1] - u[j, i])
                - k_x_minus[j, i] * (u[j, i] - u[j, i - 1])
            )
            explicit_term_y = ry * (
                k_y_plus[j, i] * (u[j + 1, i] - u[j, i])
                - k_y_minus[j, i] * (u[j, i] - u[j - 1, i])
            )

            b[p] = C_values[j, i] * u[j, i] + explicit_term_x + explicit_term_y

    # Construct sparse matrix
    A = csr_matrix((data[:idx], (row_ind[:idx], col_ind[:idx])), shape=(N, N))
    # Apply boundary conditions
    A, b = boundary_conditions(A, b, u, n, dt, nx, ny)

    return A, b


def dirichlet_boundary_conditions(A, b, u, n, dt, nx, ny):
    """
    Apply Dirichlet boundary conditions for 2D problem.

    Parameters:
    -----------
    A : sparse matrix
        System matrix
    b : array
        Right-hand side
    u : array
        Current solution
    n : int
        Current time step
    dt : float
        Time step size
    nx, ny : int
        Grid dimensions

    Returns:
    --------
    A, b : updated matrix and right-hand side
    """

    # Bottom and top boundaries (y = 0 and y = Ly)
    for i in range(nx):
        # Bottom boundary (j = 0)
        p = i
        A.data[A.indptr[p] : A.indptr[p + 1]] = 0
        A[p, p] = 1.0
        b[p] = 273 + 100

        # Top boundary (j = ny-1)
        p = (ny - 1) * nx + i
        A.data[A.indptr[p] : A.indptr[p + 1]] = 0
        A[p, p] = 1.0
        b[p] = 273 + 100

    # Left and right boundaries (x = 0 and x = Lx)
    for j in range(ny):
        # Left boundary (i = 0)
        p = j * nx
        A.data[A.indptr[p] : A.indptr[p + 1]] = 0
        A[p, p] = 1.0
        b[p] = 273 + 100

        # Right boundary (i = nx-1)
        p = j * nx + (nx - 1)
        A.data[A.indptr[p] : A.indptr[p + 1]] = 0
        A[p, p] = 1.0
        b[p] = 273 + 100

    return A, b


def yolk_k(u):
    return 0.0008 * u + 0.395


def white_k(u):
    return 0.0013 * u + 0.5125


def yolk_C(u):
    return 3120 * (1037.3 - 0.0023 * u**2 - 0.1386 * u)


def white_C(u):
    return 3800


def k_egg(u, egg_domain):
    conditions = [egg_domain == 0, egg_domain == 1, egg_domain == 2]
    values = [0, white_k(u), yolk_k(u)]
    return np.select(condlist=conditions, choicelist=values)


def C_egg(u, egg_domain):
    conditions = [egg_domain == 0, egg_domain == 1, egg_domain == 2]
    values = [0, white_C(u), yolk_C(u)]
    return np.select(condlist=conditions, choicelist=values)


def is_point_outside_egg(i, j, egg_domain):
    # i and j are array indices

    # egg_domain = 0 is outside of egg
    return egg_domain[i, j] < 0.5


def egg_curve_squared(a: float, b: float, x: float | np.ndarray) -> float | np.ndarray:
    return x * 0.5 * ((a - b) - 2 * x + np.sqrt(4 * b * x + (a - b) ** 2))


def create_egg_domain(
    nx, ny, Lx, Ly, yolk_radius_metres, B_EGG_SHAPE_PARAM
) -> np.ndarray:
    # 0 = outside
    # 1 = white
    # 2 = yolk

    egg_domain = np.zeros(shape=(nx, ny))
    xx = np.arange(start=0, stop=Lx, step=Lx / nx)
    yy = np.arange(start=0, stop=Ly, step=Ly / ny)

    for i, _ in enumerate(egg_domain):
        for j, _ in enumerate(egg_domain[i]):
            x = xx[i]
            y = yy[j]

            if y**2 <= egg_curve_squared(a=Lx, b=B_EGG_SHAPE_PARAM, x=x):
                egg_domain[i, j] = 1

            if (x - 2 * Lx / 3) ** 2 + y**2 <= yolk_radius_metres**2:
                egg_domain[i, j] = 2

    return egg_domain


def compute_egg_to_equation_system_map(nx, ny, egg_domain):
    egg_to_equation_system_map = -np.ones((nx, ny))
    cell_number = 0
    for i in range(nx):
        for j in range(ny):
            if is_point_outside_egg(i, j, egg_domain):
                egg_to_equation_system_map[j, i] = cell_number
                cell_number += 1

    return egg_to_equation_system_map


def run_example_2d():
    # Simulation parameters
    EGG_LENGTH_METRES = 8 / 100
    YOLK_RADIUS_METRES = 1.8 / 100
    B = 0.09  # Egg shape parameter
    nx, ny = 20, 20  # Number of grid points

    # Lx, Ly domain dimensions
    Lx = EGG_LENGTH_METRES  # Domain dimensions = egg length
    # y dimension depends on how wide the egg is
    Ly = float(np.max(np.sqrt(egg_curve_squared(a=Lx, b=B, x=np.linspace(0, Lx, nx)))))

    dx = Lx / (nx - 1)  # Spatial step size in x
    dy = Ly / (ny - 1)  # Spatial step size in y
    tmax = 60 * 5  # Maximum simulation time
    dt = 1  # Time step size

    # Create grid
    x = np.linspace(0, Lx, nx)
    y = np.linspace(0, Ly, ny)
    X, Y = np.meshgrid(x, y)

    # Initial condition
    u_init = (273 + 20) * np.ones_like(X)

    # Separate white and yolk
    egg_domain = create_egg_domain(
        nx=nx,
        ny=ny,
        Lx=Lx,
        Ly=Ly,
        yolk_radius_metres=YOLK_RADIUS_METRES,
        B_EGG_SHAPE_PARAM=B,
    )

    # Egg is not square
    # => some gridpoints lie outside the egg.
    # => Fewer equations needed
    # => Need a way to map equation number (position in system of eqs.) to point in egg.
    egg_to_equation_system_map = compute_egg_to_equation_system_map(
        nx=nx, ny=ny, egg_domain=egg_domain
    )

    # Plot egg domain
    plt.figure()
    plt.imshow(egg_domain, extent=[0, Ly, 0, Lx])
    plt.title("Egg domain")
    plt.show()

    # Run simulation
    u_history, t_saved = crank_nicolson_diffusion_2d(
        u_init,
        tmax,
        dt,
        dx,
        dy,
        boundary_conditions=dirichlet_boundary_conditions,
        egg_domain=egg_domain,
    )

    # Plot results
    plot_times = [0, len(t_saved) // 4, len(t_saved) // 2, len(t_saved) - 1]

    fig = plt.figure(figsize=(16, 12))
    for i, time_idx in enumerate(plot_times):
        ax = fig.add_subplot(2, 2, i + 1, projection="3d")
        surf = ax.plot_surface(
            X, Y, u_history[time_idx], cmap=cm.viridis, linewidth=0, antialiased=True
        )
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("u")
        ax.set_title(f"t = {t_saved[time_idx]:.4f}")
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

    plt.tight_layout()
    plt.show()

    # Plot as 2D heat maps
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()

    for i, time_idx in enumerate(plot_times):
        im = axes[i].imshow(
            u_history[time_idx],
            origin="lower",
            extent=[0, Lx, 0, Ly],
            cmap="viridis",
            vmin=273,
            vmax=273 + 100,
        )
        axes[i].set_title(f"t = {t_saved[time_idx]:.4f}")
        axes[i].set_xlabel("X")
        axes[i].set_ylabel("Y")
        fig.colorbar(im, ax=axes[i])

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_example_2d()

# %% Trials


A, b = build_matrix_and_b_equations(
    u=u_init, dt=dt, dx=dx, dy=dy, nx=nx, ny=ny, egg_domain=egg_domain
)


plt.imshow(egg_to_equation_system_map)
plt.show()

# %%
