import numpy as np
import matplotlib as plt
import pandas as pd 
from sympy import symbols, diff, simplify, factor, integrate, solve, sin, cos, tan, log, pprint, simplify   

class Calculus:
    def calculate_derivative(self):
        x = symbols('x')
        expression = input("Enter a function in terms of x: ")

        try:
            func = simplify(expression)
            derivative = diff(func, x)
            print("Derivative:")
            pprint(derivative)

        except Exception as e:
            pprint("Error processing input:", e)

    def polynomial_factorization(self):
        x = symbols('x')
        expression = input("Enter a polynomial in terms of x: ")

        try:
            func = simplify(expression)
            factored = factor(func)
            print("Factored polynomial:")
            pprint(factored)

        except Exception as e:
            pprint("Error processing input:", e)

    def indefinite_integral(self):
        x = symbols('x')
        expression = input("Enter a function to integrate in terms of x: ")

        try:
            func = simplify(expression)
            integral = integrate(func, x)
            print("Indefinite integral:")
            pprint(integral)

        except Exception as e:
            pprint("Error processing input:", e)

    def definite_integral(self):
        x = symbols('x')
        expression = input("Enter a function to integrate in terms of x: ")
        lower_limit = float(input("Enter the lower limit: "))
        upper_limit = float(input("Enter the upper limit: "))

        try:
            func = simplify(expression)
            integral = integrate(func, (x, lower_limit, upper_limit))
            print("Definite integral:")
            pprint(integral)

        except Exception as e:
            pprint("Error processing input:", e)

    def solve_equation(self):
        x = symbols('x')
        equation = input("Enter an equation in terms of x: ")

        try:
            func = simplify(equation)
            solutions = solve(func, x)
            print("Solutions:")
            pprint(solutions)

        except Exception as e:
            pprint("Error processing input:", e)

    def trigonometric_simplification(self):
        x = symbols('x')
        expression = input("Enter a trigonometric expression in terms of x: ")

        try:
            func = simplify(expression)
            print("Simplified expression:")
            pprint(func)

        except Exception as e:
            pprint("Error processing input:", e)
def draw_function():
    function = input("Enter a mathematical function in terms of x: ")

    try:
        # Generate x values
        x = np.linspace(-10, 10, 100)  # Adjust the range as needed

        # Evaluate the function
        y = eval(function)

        # Create a pandas DataFrame
        data = pd.DataFrame({'x': x, 'y': y})

        # Plotting
        plt.figure(figsize=(8, 6))
        plt.plot(data['x'], data['y'], label=function)
        plt.title("Plot of " + function)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.show()

    except Exception as e:
        print("Error:", e)






   