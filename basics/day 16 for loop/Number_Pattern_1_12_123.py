# Number Pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# ...

num = int(input("Enter your number: "))  # Number of rows

# Outer loop controls the rows
for i in range(num + 1):

    # Inner loop prints numbers from 1 to i
    for j in range(1, i + 1):
        print(j, end=" ")

    # Move to the next line after each row
    print()


# What I learned:
# - Nested for loops
# - Outer loop → controls rows
# - Inner loop → controls numbers in each row
# - range(1, i + 1)
# - print(end=" ")
# - Moving to the next line using print()
# Commit message:
# Add increasing number pattern using nested loops
# Number Pattern:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

num = int(input("Enter your number: "))  # Number of rows

# Outer loop controls the rows
for i in range(num + 1):

    # Inner loop prints the current number i times
    for j in range(1, i + 1):
        print(i, end=" ")

    # Move to the next line
    print()

# waht i learn
# Row number = Number of repetitions
