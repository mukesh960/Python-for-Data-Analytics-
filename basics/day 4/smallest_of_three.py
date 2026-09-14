#FIND THE SMALLEST  NUMBER of 3 number

#take input 0f 3 number a,b,c from user  and compare

a=int(input("Enter your First number: "))
b=int(input("Enter your Second number: "))
c=int(input("Enter your third number: "))

#compare all number from each other and print the smallest number
if a<b and a<c:
   print("a is  smallest:  ",a)
elif b<c :
  print("b is smallest: ",b)
else:
 print("c is smallest: ",c)

