#importe math module 
import math

num = int(input("Enter a number: "))

# handle the cases negative and zero  number
if num <= 0:
    print("Number is invalid")

else:
    # finding the square for given number
    root = math.sqrt(num)

    # if the number is whole number - perfect square
    # if the number is decimal number - not perfect square


    if root == int(root):
        # number is divisible by 2 then even if not the odd
        if num % 2 == 0:
            print("Number is perfect square and even")
        else:
            print("Number is perfect square and odd")
      
    else:
        print("Number is not a perfect square")

# What I learn
# 1. Input validation
# 2. if / else
# 3. Nested if
# 4. math.sqrt()
# 5. int()
# 6. % modulus operator
# 7. Perfect-square logic
# 8. Even/odd logic
# 9. Decision-tree thinking
# 10. Checking conditions step by step
