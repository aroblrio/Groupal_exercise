import math

class physics: 
    def __innit__(self):
        def freefall(height, gravity):
            g = [3.7, 8.87, 9.8, 3.71, 24.79, 10.44, 8.87, 11.15]
            T = (2 * height / gravity[g]) ** 0.5  # Total fall time (float)
            T2 = int(T // 1)  # Total fall time (integer)

            t = 0  # t is defined as a time during the fall
            for t in range(T2):
                y = height- 0.5 * gravity[g] * t ** 2  # Position function
                print("At t =", t, " s the height is", y, " m")
                t += 1

            y = height - 0.5 * gravity[g] * T ** 2
            print("At t =", T, " s the height is", y, " m")

        def inclined_plane(mass, angle, static_friction_coefficient, dynamic_friction_coefficient, gravity, applied_force=0):
            # Convert the angle to radians
            angle_radians = math.radians(angle)
    
            # Calculate the normal force acting on the object
            normal_force = mass * gravity * math.cos(angle_radians)
    
            # Calculate the force due to gravity acting parallel to the incline
            force_due_to_gravity_parallel = mass * gravity * math.sin(angle_radians)
    
            # Calculate the maximum static frictional force = minimun force to move
            max_static_friction = static_friction_coefficient * normal_force
    
            # Determine the frictional force and net force
            if applied_force < max_static_friction:
                friction_force = applied_force
                net_force = force_due_to_gravity_parallel - friction_force - applied_force
                acceleration = net_force / mass
            else:
                friction_force = dynamic_friction_coefficient * normal_force
                net_force = force_due_to_gravity_parallel - friction_force - applied_force
                acceleration = net_force / mass
            
            return max_static_friction, acceleration
        def uniform_accelerated_rectilinear_motion(initial_velocity, acceleration, time):
            # When acceleration is not equal to zero
            if acceleration != 0:
                final_velocity = initial_velocity + acceleration * time
                displacement = initial_velocity * time + 0.5 * acceleration * (time ** 2)
                return final_velocity, displacement

            # When acceleration is equal to zero
            else:
                final_velocity = initial_velocity
                displacement = initial_velocity * time
                return final_velocity, displacement

