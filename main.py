import physics
import calculus
import statistics
import algebra

def perform_physics_calculation():
    print("\nPhysics calculations:")
    physics_calculator = physics.Physics()
    while True:
        print("\nChoose a physics calculation:")
        print("1. Parabolic shot")
        print("2. Uniform accelerated circular motion")
        print("3. Freefall")
        print("4. Inclined plane")
        print("5. Uniform accelerated rectilinear motion")
        print("6. Back to main menu")

        phys_choice = input("Enter your choice (1-6): ")

        if phys_choice in ('1', '3', '4'):
            gravity = physics_calculator.ask_gravity()

        if phys_choice == '1':
            velocity = float(input("Enter velocity: "))
            angle = float(input("Enter angle (in degrees): "))
            height = float(input("Enter height: "))
            physics_calculator.parabolic_shot(velocity, angle, height)
        elif phys_choice == '2':
            frequency = float(input("Enter frequency: "))
            radius = float(input("Enter radius: "))
            physics_calculator.mcua(frequency, radius)
        elif phys_choice == '3':
            height = float(input("Enter height: "))
            physics_calculator.freefall(height, gravity)
        elif phys_choice == '4':
            mass = float(input("Enter mass: "))
            angle = float(input("Enter angle (in degrees): "))
            static_friction_coefficient = float(input("Enter static friction coefficient: "))
            dynamic_friction_coefficient = float(input("Enter dynamic friction coefficient: "))
            applied_force = float(input("Enter applied force: "))
            result = physics_calculator.inclined_plane(
                mass, angle, static_friction_coefficient,
                dynamic_friction_coefficient, gravity, applied_force
            )
            print("Max static friction:", result[0])
            print("Acceleration:", result[1])
        elif phys_choice == '5':
            initial_velocity = float(input("Enter initial velocity: "))
            acceleration = float(input("Enter acceleration: "))
            time = float(input("Enter time: "))
            result = physics_calculator.uniform_accelerated_rectilinear_motion(
                initial_velocity, acceleration, time
            )
            print("Final velocity:", result[0])
            print("Displacement:", result[1])
        elif phys_choice == '6':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def perform_algebra_calculation():
    print("\nAlgebra calculations:")
    algebra_calculator = algebra.LinearAlgebra()

    while True:
        print("\nChoose an algebra calculation:")
        print("1. Matrix Sum")
        print("2. Matrix Multiplication")
        print("3. Determinant of a Matrix")
        print("4. Matrix Range")
        print("5. Back to main menu")

        algebra_choice = input("Enter your choice (1-5): ")

        if algebra_choice == '1':
            print("\nMatrix Sum:")
            matrix1 = algebra_calculator.input_matrix()
            matrix2 = algebra_calculator.input_matrix()
            try:
                result = algebra_calculator.matrix_sum(matrix1, matrix2)
                print("Resultant Matrix:")
                for row in result:
                    print(row)
            except ValueError as e:
                print(e)
        elif algebra_choice == '2':
            print("\nMatrix Multiplication:")
            matrix1 = algebra_calculator.input_matrix()
            matrix2 = algebra_calculator.input_matrix()
            try:
                result = algebra_calculator.matrix_multiply(matrix1, matrix2)
                print("Resultant Matrix:")
                for row in result:
                    print(row)
            except ValueError as e:
                print(e)
        elif algebra_choice == '3':
            print("\nDeterminant of a Matrix:")
            matrix = algebra_calculator.input_matrix()
            try:
                result = algebra_calculator.determinant(matrix)
                print("Determinant:", result)
            except ValueError as e:
                print(e)
        elif algebra_choice == '4':
            print("\nMatrix Range:")
            matrix = algebra_calculator.input_matrix()
            result = algebra_calculator.matrix_range(matrix)
            print("Matrix Range:", result)
        elif algebra_choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def perform_statistics_calculation():
    print("\nStatistics calculations:")
    stats = statistics.Statistics()

    while True:
        print("\nChoose a statistics calculation:")
        print("1. Mean")
        print("2. Standard Deviation")
        print("3. Median")
        print("4. Variance")
        print("5. Back to main menu")

        stats_choice = input("Enter your choice (1-5): ")

        if stats_choice == '1':
            values = stats.get_values()
            mean = stats.calculate_mean(values)
            print(f"Mean: {mean}")
        elif stats_choice == '2':
            values = stats.get_values()
            std_deviation = stats.calculate_standard_deviation(values)
            print(f"Standard Deviation: {std_deviation}")
        elif stats_choice == '3':
            values = stats.get_values()
            median_value = stats.calculate_median(values)
            print(f"Median: {median_value}")
        elif stats_choice == '4':
            values = stats.get_values()
            variance = stats.calculate_variance(values)
            print(f"Variance: {variance}")
        elif stats_choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def perform_calculus_calculation():
    print("\nCalculus calculations:")
    calc = calculus.Calculus()

    while True:
        print("\nChoose a calculus operation:")
        print("1. Calculate Derivative")
        print("2. Polynomial Factorization")
        print("3. Indefinite Integral")
        print("4. Definite Integral")
        print("5. Solve Equation")
        print("6. Trigonometric Simplification")
        print("7. Draw Function")
        print("8. Back to main menu")

        calc_choice = input("Enter your choice (1-8): ")

        if calc_choice == '1':
            calc.calculate_derivative()
        elif calc_choice == '2':
            calc.polynomial_factorization()
        elif calc_choice == '3':
            calc.indefinite_integral()
        elif calc_choice == '4':
            calc.definite_integral()
        elif calc_choice == '5':
            calc.solve_equation()
        elif calc_choice == '6':
            calc.trigonometric_simplification()
        elif calc_choice == '7':
            calculus.draw_function()
        elif calc_choice == '8':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

def main():
    print("Welcome to the Calculator Interface!")
    while True:
        print("\nChoose a subject:")
        print("1. Physics")
        print("2. Analysis")
        print("3. Statistics")
        print("4. Algebra")
        print("5. Calculus")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            perform_physics_calculation()
        elif choice == '2':
            perform_calculus_calculation()
        elif choice == '3':
            perform_statistics_calculation()
        elif choice == '4':
            perform_algebra_calculation()
        elif choice == '5':
            perform_calculus_calculation()
        elif choice == '6':
            print("Exiting the Calculator Interface. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()