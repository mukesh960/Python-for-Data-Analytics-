
#Given 2 fractions, find the sum of those 2 fractions.Take the numerator and #denominator values of the fractions from the user.

# Write your code here
#n1=numerator1, n2=numerator2, denominator1,denominator 2
#take input n1,n2,d1,d2 from user
n1=int(input("enter a number 1st numerator: "))
d1=int(input("enter a number 1st denominator: "))
n2=int(input("enter a number 2nd numerator: "))
d2=int(input("enter a number 2nd denominator:"))

#add two fraction number 
#total numerator
nume=n1*d2+n2*d1
#total denominator
deno=d1*d2

#pint the total fraction
print(nume,"/",deno)
