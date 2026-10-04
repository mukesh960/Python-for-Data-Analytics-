# Question
# Write a Python program that takes the number of terms from the **user** and prints the first `num` terms of the Fibonacci series using a `for` loop.

# Output: 0 1 1 2 3 5 8 13 21 3

# Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, ...

num = int(input("Enter the number of terms: "))

# Starting two terms
a = 0
b = 1

for i in range(num):
    print(a, end=" ")

    # Find the next term
    temp = a + b

    # Move to the next two terms
    a = b
    b = temp

#What I Learned — Important Logic
# 1. Initialize two starting values
#    a = 0b = 1
# 2. Loop num times
#    for i in range(num):
# 3. Print the current term
#    print(a, end=" ")
# 4. Calculate the next term
#    temp = a + b
# 5. Shift the values
#    a = bb = temp
# Main logic to remember:
# Print → Add → Shift → Repeat
