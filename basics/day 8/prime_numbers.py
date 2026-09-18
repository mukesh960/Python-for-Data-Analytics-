'''Question

Write a Python program to print all prime numbers between a given lower number and higher number.'''


lower_number=int(input("Enter a start number: "))
higher_number=int(input("Enter a range number: "))

#check prime number
for i in range(lower_number,higher_number+1):
   for j in range(2,i):
      if i%j==0:
       break
   else:
    #print number
    print(i)




'''What I Learned

How to take start and end numbers from the user.

How to use a nested for loop.

How to check whether a number is divisible using the modulus % operator.

How to use the break statement when a factor is found.

How to use for-else in Python.

How to identify prime numbers.

How to check every number within a range.

How nested loops can be used to solve logical problems.

Main Logic

Take a number
      ↓
Check divisibility from 2 to number-1
      ↓
If divisible → break → Composite
      ↓
No divisor found → for-else → Prime '''
