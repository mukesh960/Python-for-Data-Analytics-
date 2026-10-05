# PALINDROME NUMBERS - 121 <--> 121
# Question
# Write a Python program to find and count all palindrome numbers between 100 and 303.
# count = 0

for i in range(100, 304):
    a = str(i)          # Convert number to string
    b = a[::-1]         # Reverse the string

    if a == b:          # Check palindrome
        print(i, end=" ")
        count = count + 1

print("\nTotal palindrome numbers:", count)

# What I Learned — Logic Only
# - Convert each number into a string.
# - Reverse the string using [::-1].
# - Compare the original string with the reversed string.
# - If both are equal → Palindrome.
# - Increase count for every palindrome found.
# - Use a loop to check multiple numbers in a given range.
