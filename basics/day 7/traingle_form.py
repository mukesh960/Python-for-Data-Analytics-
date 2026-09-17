'''Problem 2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.'''


# Write code here
#take a  three angle from user
a1=int(input("Enter a first angle of Traingle: "))
a2=int(input("Enter a first angle of Traingle: "))
a3=int(input("Enter a first angle of Traingle: "))

#check it can be form triangle or not
#sum of all angle is traingle
if a1+a2+a3==180 :
 print("Triangle")
else:
 print("not Triangle")

