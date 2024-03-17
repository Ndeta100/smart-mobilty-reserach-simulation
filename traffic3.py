import numpy as np
import matplotlib.pyplot as plt

class TrafficSimulation:
    def __init__(self, length, density, bike_lane_start, bike_lane_end):
        self.length = length  # Length of the road
        self.density = density  # Initial traffic density
        self.bike_lane_start = bike_lane_start  # Start index of the bike lane
        self.bike_lane_end = bike_lane_end  # End index of the bike lane
        
        # Initialize the road with vehicles randomly distributed
        self.road = np.random.choice([0, 1], size=(length,), p=[1-density, density])
        
        # List to store traffic density at each time step
        self.traffic_density_history = [self.calculate_traffic_density()]
        
    def step(self):
        # Create a copy of the road to update the traffic flow
        new_road = self.road.copy()
        
        # Update the traffic flow based on simple rules with randomness
        for i in range(self.length):
            if self.road[i] == 1:  # If there is a vehicle at position i
                if np.random.rand() < 0.8:  # Allow 80% chance of moving forward
                    new_road[(i+1) % self.length] = 1
                    new_road[i] = 0
                elif np.random.rand() < 0.5:  # 50% chance of moving backward
                    new_road[(i-1) % self.length] = 1
                    new_road[i] = 0
        
        # Update the road with the new traffic flow
        self.road = new_road
        
        # Update traffic density history
        self.traffic_density_history.append(self.calculate_traffic_density())
    
    def calculate_traffic_density(self):
        return np.sum(self.road) / self.length
    
    def plot(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plot filled area representing traffic density over time
        ax.fill_between(range(len(self.traffic_density_history)), self.traffic_density_history, color='skyblue', alpha=0.5)
        
        # Plot line representing traffic density over time
        ax.plot(range(len(self.traffic_density_history)), self.traffic_density_history, color='b', linestyle='-')
        
        # Set plot title and labels
        ax.set_title('Traffic Density over Time')
        ax.set_xlabel('Time Step')
        ax.set_ylabel('Traffic Density')
        
        # Set grid
        ax.grid(True)
        
        # Show plot
        plt.show()

# Parameters for typical scenario in Estonia
length = 200  # Longer road to represent urban area
density = 0.4  # Higher initial traffic density
bike_lane_start = 80  # Start index of the bike lane
bike_lane_end = 120  # End index of the bike lane

# Create and run the simulation
simulation = TrafficSimulation(length, density, bike_lane_start, bike_lane_end)

for step in range(100):
    simulation.step()

simulation.plot()
