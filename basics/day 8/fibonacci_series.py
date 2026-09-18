'''Problem 5 - Exercise 12: Display Fibonacci series up to 10 terms.
Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34'''


num1 = 0
num2 = 1

for i in range(10):
    print(num1)

    next = num1 + num2
    num1 = num2
    num2 = next

    '''What I Learned
How Fibonacci series works.
How to use two variables to store previous numbers.
How to use a for loop for repeated calculation.
How to calculate the next number:
next = num1 + num2
How to update variables after each iteration.
How a loop can generate a sequence step by step.'''
