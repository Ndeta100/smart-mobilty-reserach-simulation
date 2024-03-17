import numpy as np
import matplotlib.pyplot as plt

class TrafficSimulation:
    def __init__(self, length, density, bike_lane_start, bike_lane_end, num_simulations, num_groups):
        self.length = length  # Length of the road
        self.density = density  # Initial traffic density
        self.bike_lane_start = bike_lane_start  # Start index of the bike lane
        self.bike_lane_end = bike_lane_end  # End index of the bike lane
        self.num_simulations = num_simulations  # Number of simulations
        self.num_groups = num_groups  # Number of groups
        
        # List to store traffic density for each group
        self.traffic_density_data = [[] for _ in range(num_groups)]
        
        # Run simulations
        for _ in range(num_simulations):
            self.run_simulation()
        
    def run_simulation(self):
        # Initialize the road with vehicles randomly distributed
        road = np.random.choice([0, 1], size=(self.length,), p=[1-self.density, self.density])
        
        # List to store traffic density at each time step
        traffic_density_history = [self.calculate_traffic_density(road)]
        
        # Run simulation steps
        for _ in range(100):
            road = self.step(road)
            traffic_density_history.append(self.calculate_traffic_density(road))
        
        # Determine group index based on traffic density
        group_index = int(np.floor(self.calculate_traffic_density(road) * self.num_groups))
        group_index = min(group_index, self.num_groups - 1)  # Ensure group index is within bounds
        
        # Store traffic density data for this simulation in the appropriate group
        self.traffic_density_data[group_index].append(traffic_density_history[-1])
    
    def step(self, road):
        # Create a copy of the road to update the traffic flow
        new_road = road.copy()
        
        # Update the traffic flow based on simple rules with randomness
        for i in range(self.length):
            if road[i] == 1:  # If there is a vehicle at position i
                if np.random.rand() < 0.8:  # Allow 80% chance of moving forward
                    new_road[(i+1) % self.length] = 1
                    new_road[i] = 0
                elif np.random.rand() < 0.5:  # 50% chance of moving backward
                    new_road[(i-1) % self.length] = 1
                    new_road[i] = 0
        
        return new_road
    
    def calculate_traffic_density(self, road):
        return np.sum(road) / self.length
    
    def plot_boxplot(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Calculate positions for boxplots
        positions = np.arange(1, self.num_groups + 1)
        
        # Create box and whisker plot for each group
        for i in range(self.num_groups):
            ax.boxplot(self.traffic_density_data[i], positions=[positions[i]])
        
        # Set plot title and labels
        ax.set_title('Distribution of Traffic Density')
        ax.set_xlabel('Group')
        ax.set_ylabel('Traffic Density')
        ax.set_xticks(positions)
        ax.set_xticklabels([f'Group {i}' for i in range(1, self.num_groups + 1)])
        
        # Show plot
        plt.show()

# Parameters for typical scenario in Estonia
length = 200  # Longer road to represent urban area
density = 0.4  # Higher initial traffic density
bike_lane_start = 80  # Start index of the bike lane
bike_lane_end = 120  # End index of the bike lane
num_simulations = 100  # Number of simulations
num_groups = 8  # Number of groups

# Create and run the traffic simulation
simulation = TrafficSimulation(length, density, bike_lane_start, bike_lane_end, num_simulations, num_groups)

# Plot box and whisker plot
simulation.plot_boxplot()
