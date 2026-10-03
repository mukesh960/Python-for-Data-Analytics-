# Series: 5, 6, 8, 11, 15, 20, ...

num = int(input("Enter your number: "))

a = 5  # Initial value

for i in range(1, num + 1):
    a = a + i  # Add the current value of i
    print(a, end=" ")

# What I Learned
# - How to generate a number series using a for loop.
# - How the value of i changes automatically in each iteration.
# - How to update a variable using:a = a + i
# - How the difference between terms increases:+1, +2, +3, +4, +5...
# - How to use print(..., end=" ") to print values on the same line.
# - How range(1, num + 1) controls the number of terms.
