import threading
import time
import matplotlib.pyplot as plt
from collections import deque

class GameSimulation:
    def __init__(self, result_func, variable_names, trials=10000):
        self.result_func = result_func  # Function to simulate the game results
        self.trials = trials
        # How often to update the plot (in trials)
        self.plot_update_interval = 1

        # Initialize variables dynamically based on the provided variable names
        # Default all variables to 0 (flip counts)
        self.variables = {name: 0 for name in variable_names}
        self.internal_counter = 0  # Counter to track number of trials
        self.lock = threading.Lock()

        # Set up figure and axis for plotting
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, self.trials)
        self.ax.set_ylim(0, 1)
        self.ax.set_xlabel("Trials")
        self.ax.set_ylabel("Probability of Events")
        self.ax.set_title("Event Probabilities Over Time")

        # Plot lines for each tracked variable
        self.lines = {}
        for name in self.variables:
            line, = self.ax.plot([], [], lw=2, label=name)
            self.lines[name] = line

        self.ax.legend()
        self.prob_texts = {}  # Store text annotations for probabilities
        for name in self.variables:
            self.prob_texts[name] = self.ax.text(0.7, 0.95 - 0.05 * len(self.prob_texts), "", transform=self.ax.transAxes)

        # Event to signal the main thread to update the plot
        self.plot_event = threading.Event()

    def update_plot(self):
        """Update the plot with the current values of the simulation."""
        x = deque(maxlen=1000)
        # Dictionary to hold deque for each variable
        y = {name: deque(maxlen=1000) for name in self.variables}

        while self.internal_counter < self.trials:
            with self.lock:
                probabilities = {
                    name: self.variables[name] / self.internal_counter if self.internal_counter > 0 else 0 for name in self.variables}

            x.append(self.internal_counter)  # Append the trial count

            # Append probabilities to the corresponding deques for each variable
            for name in self.variables:
                y[name].append(probabilities[name])
                # Update line data for each variable
                self.lines[name].set_data(x, y[name])
                # Update probability text with 5 significant figures
                self.prob_texts[name].set_text(f"{name}: {probabilities[name]:.5g}")

            self.ax.relim()
            self.ax.autoscale_view()
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

            plt.pause(1/1000)  # Update the plot every 0.1 seconds

            if self.internal_counter >= self.trials:  # Stop displaying once the game is done
                break

    def run_result_func(self):
        """Run the result function in parallel to simulate trials."""
        while self.internal_counter < self.trials:
            result = self.result_func()

            with self.lock:
                for idx, name in enumerate(self.variables):
                    if result[idx]:
                        self.variables[name] += 1

            with self.lock:
                self.internal_counter += 1

            if self.internal_counter % self.plot_update_interval == 0:
                self.plot_event.set()

            time.sleep(0.001)

    def run(self):
        """Start both threads for running result_func and updating the plot."""
        # Start the thread for running result_func
        result_thread = threading.Thread(target=self.run_result_func)
        result_thread.start()

        plt.ion()
        while self.internal_counter < self.trials:
            self.plot_event.wait()

            self.update_plot()

            self.plot_event.clear()

        plt.ioff() 
        plt.show()

        # Wait for the result thread to finish
        result_thread.join()
