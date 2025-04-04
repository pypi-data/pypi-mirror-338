async function evaluatePython() {
    let pyodide = await pyodideReadyPromise;
    try {
        pyodide.runPython(`
# ... Some python code
`);

        function compute_next_u() {
            pyodide.runPython(`
# ... Some other python code
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
            let u_to_plot = pyodide.globals.get("u_to_plot").toJs();

            const data = heatmap_egg_quantity(u_to_plot, Lx, Ly);
            Plotly.react("temperature_plot", data);
        }

        const nt = pyodide.globals.get("nt");

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
                    `Computing step ${step}/${nt - 1}`;

                // Wait for the next animation frame to ensure the plot is rendered
                await new Promise((resolve) => setTimeout(resolve, 200));
            }
            document.getElementById("status").textContent =
                "Simulation complete";
        }
        await runSimulation();
    } catch (err) {
        addToOutput(err);
    }
}
