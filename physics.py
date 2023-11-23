import math

def quadratic_shot(a, b, c):
    # Calculate the quadratic formula and return the larger root if it's valid
    si = (b ** 2) - 4 * a * c
    if si >= 0:
        x1 = (-b + (si) ** 0.5) / (2 * a)
        x2 = (-b - (si) ** 0.5) / (2 * a)
        if x2 > x1:
            x1 = x2
        return x1

class Physics:
    def __init__(self):
        pass  # Initialize the class

    def ask_gravity(self):
        gravity = [3.7, 8.87, 9.8, 3.71, 24.79, 10.44, 8.87, 11.15]
        g = int(input("Select the planet your object is at:\n "
              "1. Mercury\n 2. Venus\n 3. Earth\n 4. Mars\n 5. Jupiter\n "
              "6. Saturn\n 7. Uranus\n 8. Neptune\n")) - 1  # Subtract 1 to match the list index
        return gravity[g]

    def parabolic_shot(self, velocity, angle, height, gravity):
        # Calculate the trajectory of a projectile
        angle = math.radians(angle)
        velocity_x = velocity * math.cos(angle)
        velocity_y = velocity * math.sin(angle)
        time = quadratic_shot(1/2 * gravity, velocity_y, height)  # Using quadratic formula
        x_f = velocity_x * time  # Calculate final position
        print("The travel time is:", time, "and the distance the object travels is:", x_f)

    def mcua(self, frequency, radius):
        # Calculate angular and linear velocities for circular motion
        w = 2 * math.pi * frequency
        velocity = w * radius ** 2
        print(f"The angular velocity is:", w, "and the linear velocity is:", velocity)

    def freefall(self, height, gravity):
        # Simulate freefall motion and print height at different times
        T = (2 * height / gravity) ** 0.5
        T2 = int(T // 1)
        for t in range(T2):
            y = height - 0.5 * gravity * t ** 2
            print("At t =", t, "s the height is", y, "m")
        y = height - 0.5 * gravity * T ** 2
        print("At t =", T, "s the height is", y, "m")

    def inclined_plane(self, mass, angle, static_friction_coefficient, dynamic_friction_coefficient, gravity, applied_force=0):
        # Calculate forces and acceleration on an inclined plane
        angle_radians = math.radians(angle)
        normal_force = mass * gravity * math.cos(angle_radians)
        force_due_to_gravity_parallel = mass * gravity * math.sin(angle_radians)
        max_static_friction = static_friction_coefficient * normal_force
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
        # Calculate final velocity and displacement for uniform accelerated motion
        if acceleration != 0:
            final_velocity = initial_velocity + acceleration * time
            displacement = initial_velocity * time + 0.5 * acceleration * (time ** 2)
            return final_velocity, displacement
        else:
            final_velocity = initial_velocity
            displacement = initial_velocity * time
            return final_velocity, displacement
