# Question:
# Write a Python program that takes two numbers from the user and prints the pattern 2 22 222 2222 ... for the given number of terms.
# Repeated Number Pattern: 2, 22, 222, 2222, ...

num = int(input("Enter the number of terms: "))  # Number of terms
series = int(input("Enter the starting number: "))  # Starting digit

# Outer loop controls the number of terms
for i in range(1, num + 1):

    # Inner loop prints the digit i times
    for j in range(i):
        print(series, end="")

    # Space between each term
    print(end=" ")


# What I learned:
# - for loop
# - range()
# - print(end=" ")
# - Updating a variable inside a loop
# - Number pattern logic
# - series * 10 + 2 to create the next term
# Commit message:
# Add number pattern 2 22 222 using for loop
