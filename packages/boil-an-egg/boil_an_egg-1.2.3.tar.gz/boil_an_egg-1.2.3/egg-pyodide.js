const output = document.getElementById("output");
const code = document.getElementById("code");

function addToOutput(s) {
    output.value += ">>>" + code.value + "\n" + s + "\n";
}

output.value = "Initializing...\n";

// init Pyodide
async function main() {
    let pyodide = await loadPyodide();
    await pyodide.loadPackage("micropip");
    const micropip = pyodide.pyimport("micropip");
    await micropip.install("boil-an-egg");
    output.value += "Ready!\n";
    return pyodide;
}
let pyodideReadyPromise = main();

async function evaluatePython() {
    let pyodide = await pyodideReadyPromise;
    try {
        pyodide.runPython(`
import boil_an_egg.utils as bae
import numpy as np

EGG_LENGTH_METRES = 7 / 100
YOLK_RADIUS_METRES = 1.5 / 100
WATER_TEMPERATURE_CELSIUS = 100
B = 0.05  # Egg shape parameter
nx, ny = 50, 50  # Number of grid points

# Lx, Ly domain dimensions
Lx = EGG_LENGTH_METRES  # Domain dimensions = egg length
# y dimension depends on how wide the egg is
Ly = float(np.max(np.sqrt(bae.egg_curve_squared(a=Lx, b=B, x=np.linspace(0, Lx, nx)))))

dx = Lx / (nx - 1)  # Spatial step size in x
dy = Ly / (ny - 1)  # Spatial step size in y

# Create grid
x = np.linspace(0, Lx, nx)
y = np.linspace(0, Ly, ny)

# Separate white and yolk
egg_domain = bae.create_egg_domain(
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
egg_to_equation_system_map = bae.compute_egg_to_equation_system_map(
    nx=nx, ny=ny, egg_domain=egg_domain
)
map_from_mesh_cell_numbers_to_coords = bae.map_mesh_cell_numbers_to_coords(
    egg_to_equation_system_map
)

map_from_coords_to_mesh_cell_numbers = bae.invert_dictionary(
    dictionary=map_from_mesh_cell_numbers_to_coords, are_values_unique=True
)

unstructured_egg_domain = bae.create_unstructured_array_from_structured_array(
    structured_array=egg_domain,
    map_from_mesh_cell_numbers_to_coords=map_from_mesh_cell_numbers_to_coords,
)

nearest_neighbors = bae.get_nearest_neighbors(
    nx=nx,
    ny=ny,
    map_from_mesh_cell_numbers_to_coords=map_from_mesh_cell_numbers_to_coords,
    egg_to_equation_system_map=egg_to_equation_system_map,
)
egg_boundary_mesh_cells = bae.get_egg_boundary_mesh_cells(
    nearest_neighbors=nearest_neighbors
)

# Initial condition
u_init = (273 + 20) * np.ones(len(nearest_neighbors))

# Main loop
# Initialize
N = len(u_init)
tmax = 60 * 5 # Total simulation time in seconds
dt = 1 # timestep in seconds
nt = int(tmax / dt) + 1

n_saves = nt

# Storage for solution at saved times
u_history = np.zeros((n_saves, N))
t_saved = np.zeros(n_saves)

# Initial condition
u = u_init.copy()
u_history[0] = u
t_saved[0] = 0

# Main time loop
timestep=1 # substitute this with the for loop in the crank_nicolson function
save_idx = 1
`);

        function compute_next_u() {
            pyodide.runPython(`
    u = bae.compute_next_u(
        u=u,
        dt=dt,
        dx=dx,
        dy=dy,
        unstructured_egg_domain=unstructured_egg_domain,
        nearest_neighbors=nearest_neighbors,
        egg_boundary_mesh_cells=egg_boundary_mesh_cells,
        water_temperature_celsius=WATER_TEMPERATURE_CELSIUS,
    )

    u_history[save_idx] = u
    t_saved[save_idx] = timestep * dt
    save_idx += 1


    u_celsius_structured = bae.kelvin_to_celsius(
        bae.convert_unstructured_array_to_structured(
            nx=nx,
            ny=ny,
            unstructured_arr=u,
            map_from_mesh_cell_numbers_to_coords=map_from_mesh_cell_numbers_to_coords,
        )
    )

    u_to_plot = bae.get_whole_egg(u_celsius_structured)
    `);
        }

        function heatmap_egg_quantity(egg_quantity, Lx, Ly) {
            const data = [{
                z: egg_quantity,
                type: "heatmap",
                colorscale: "Viridis",
                zmin: 20,
                zmax: 100,
                // Properly map array indices to the coordinate space
                x: Array.from(
                    { length: egg_quantity[0].length },
                    (_, i) => i * (2 * Ly) / (egg_quantity[0].length - 1),
                ),
                y: Array.from(
                    { length: egg_quantity.length },
                    (_, i) => i * Lx / (egg_quantity.length - 1),
                ),
            }];
            return data;
        }

        function plot_egg_temperature(pyodide) {
            const Ly = pyodide.runPython("Ly");
            const Lx = pyodide.runPython("Lx");
            const u_to_plot = pyodide.globals.get("u_to_plot").toJs();

            const data = heatmap_egg_quantity(u_to_plot, Lx, Ly);
            Plotly.react("temperature_plot", data);
        }

        const nt = pyodide.globals.get("nt");
        const dt = pyodide.globals.get("dt");

        // Set up initial plot
        const u_init = pyodide.globals.get("u_init").toJs();
        const Ly = pyodide.runPython("Ly");
        const Lx = pyodide.runPython("Lx");
        const data = [{
            z: u_init,
            type: "heatmap",
            colorscale: "Viridis",
            zmin: 20,
            zmax: 100,
            // Properly map array indices to the coordinate space
            x: Array.from(
                { length: u_init[0].length },
                (_, i) => i * (2 * Ly) / (u_init[0].length - 1),
            ),
            y: Array.from(
                { length: u_init.length },
                (_, i) => i * Lx / (u_init.length - 1),
            ),
        }];

        const layout = {
            title: "Heatmap",
            xaxis: {
                title: "X",
                range: [0, 2 * Ly],
                scaleanchor: "y",
                scaleratio: 1,
            },
            yaxis: {
                title: "Y",
                range: [0, Lx],
            },
        };

        Plotly.newPlot("temperature_plot", data, layout);

        async function runSimulation() {
            for (let step = 1; step < nt; step++) {
                compute_next_u();
                plot_egg_temperature(pyodide);

                // Add status indicator
                document.getElementById("status").textContent =
                    `Time elapsed (minutes): ${step * dt / 60}`;

                // Wait for the next animation frame to ensure the plot is rendered
                await new Promise((resolve) => setTimeout(resolve, 10));
            }
            document.getElementById("status").textContent =
                `Time elapsed (minutes): ${nt * dt / 60}. Simulation complete`;
        }
        await runSimulation();
    } catch (err) {
        addToOutput(err);
    }
}
