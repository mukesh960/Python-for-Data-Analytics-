# Full Question

# Write a Python program to solve a quadratic equation of the form ax² + bx + c = 0.

# The program should:

# Take the values of a, b, and c as input from the user.
# Calculate the discriminant using the formula:
# D = b² - 4ac
# Check the value of the discriminant:
# If D > 0, calculate and display two different real roots.
# If D == 0, calculate and display one repeated real root.
# If D < 0, display that the equation has no real roots.
# Use the quadratic formula:
# x₁ = (-b + √D) / (2a)
# x₂ = (-b - √D) / (2a)
# Use Python's conditional statements (if, elif, else) to implement the logic.
# Display the result clearly.

# Example:
# For 2x² + 5x + 2 = 0, the program should calculate the discriminant and display the two real roots.
import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)

    print("Two real roots:")
    print("x1 =", x1)
    print("x2 =", x2)

elif D == 0:
    x = -b / (2*a)

    print("One real repeated root:")
    print("x =", x)

else:
    print("No real roots. The roots are imaginary/complex.")
