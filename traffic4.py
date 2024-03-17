import turtle
import random

class TrafficSimulation:
    def __init__(self, length, density):
        self.length = length
        self.density = density
        self.vehicles = []

        # Initialize the road with vehicles randomly distributed
        for _ in range(length):
            if random.random() < density:
                self.vehicles.append(1)  # Vehicle present
            else:
                self.vehicles.append(0)  # No vehicle
        
        self.screen = turtle.Screen()
        self.screen.setup(width=800, height=200)
        self.screen.tracer(0)  # Turn off animation

        self.draw_road()
        self.draw_vehicles()

    def draw_road(self):
        road = turtle.Turtle()
        road.penup()
        road.goto(-350, 0)
        road.pendown()
        road.forward(700)
        road.penup()
        road.goto(-350, -50)
        road.pendown()
        road.forward(700)

    def draw_vehicles(self):
        for i, vehicle in enumerate(self.vehicles):
            if vehicle == 1:
                self.draw_vehicle(-350 + i * 10)

    def draw_vehicle(self, x):
        vehicle = turtle.Turtle()
        vehicle.penup()
        vehicle.shape("square")
        vehicle.color("black")
        vehicle.shapesize(stretch_wid=1, stretch_len=2)  # Adjust the size of the vehicle
        vehicle.goto(x, -25)
        vehicle.setheading(90)  # Point the vehicle upwards
        vehicle.stamp()  # Stamp the vehicle on the screen

    def step(self):
        # Update the traffic flow based on simple rules
        for i in range(self.length):
            if self.vehicles[i] == 1:
                if random.random() < 0.8:  # 80% chance of moving forward
                    self.vehicles[i] = 0
                    if i + 1 < self.length:
                        self.vehicles[i + 1] = 1

    def update_screen(self):
        self.screen.update()

    def run_simulation(self):
        while True:
            self.step()
            self.draw_vehicles()
            self.update_screen()


# Parameters for the simulation
length = 70
density = 0.4

# Create and run the traffic simulation
simulation = TrafficSimulation(length, density)
simulation.run_simulation()
