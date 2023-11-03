import math

class Physics:
    def __init__(self):
        # Gravitational values for different celestial bodies
        self.gravity = [3.7, 8.87, 9.8, 3.71, 24.79, 10.44, 8.87, 11.15]

    def freefall(self, height, gravity_index):
        # Calculate freefall motion and print the height at different times
        g = self.gravity[gravity_index]  # Gravitational force at given index
        T = (2 * height / g) ** 0.5  # Total fall time (float)
        T2 = int(T // 1)  # Total fall time (integer)

        for t in range(T2):
            # Calculate the height at each time and print
            y = height - 0.5 * g * t ** 2  # Position function
            print("At t =", t, "s the height is", y, "m")

        # Calculate and print the final height at the total fall time
        y = height - 0.5 * g * T ** 2
        print("At t =", T, "s the height is", y, "m")

    def inclined_plane(self, mass, angle, static_friction_coefficient, dynamic_friction_coefficient, gravity, applied_force=0):
        # Calculate the forces and acceleration on an inclined plane
        angle_radians = math.radians(angle)  # Convert angle to radians
        normal_force = mass * gravity * math.cos(angle_radians)  # Normal force
        force_due_to_gravity_parallel = mass * gravity * math.sin(angle_radians)  # Force due to gravity

        max_static_friction = static_friction_coefficient * normal_force  # Maximum static friction

        # Calculate the forces and net force on the plane
        if applied_force < max_static_friction:
            friction_force = applied_force
            net_force = force_due_to_gravity_parallel - friction_force - applied_force
            acceleration = net_force / mass
        else:
            friction_force = dynamic_friction_coefficient * normal_force
            net_force = force_due_to_gravity_parallel - friction_force - applied_force
            acceleration = net_force / mass
            
        return max_static_friction, acceleration

    def uniform_accelerated_rectilinear_motion(self, initial_velocity, acceleration, time):
        # Calculate motion under constant acceleration
        if acceleration != 0:
            # Calculate final velocity and displacement when acceleration is not zero
            final_velocity = initial_velocity + acceleration * time
            displacement = initial_velocity * time + 0.5 * acceleration * (time ** 2)
            return final_velocity, displacement
        else:
            # Calculate final velocity and displacement when acceleration is zero
            final_velocity = initial_velocity
            displacement = initial_velocity * time
            return final_velocity, displacement
