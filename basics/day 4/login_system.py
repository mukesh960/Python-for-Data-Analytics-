'''Write a Python program to create a simple Login System.

Take email and password as input from the user.
Correct email: mukesh.dev@gmail.com
Correct password: 1234
If both email and password are correct, print "Welcome".
If the email is correct but the password is wrong, ask the user to enter the password again.
If the second password is correct, print "Welcome".
Otherwise, print "Tumse na ho payega".
If the email is incorrect, print "Incorrect Credentials".
Use if, elif, else and proper indentation.'''

#login program and identation
#email -> mukesh.dev@gmail.com
#password -> 1234

#take email and password as imput from user
email=input("Enter your email: ")
password=int(input("Enter your Password: "))

#Check email and password match
if email=="mukesh.dev@gmail.com" and password==1234:
 print("Welcome")

 #check again if email is correct and password is wrong
elif email=="mukesh.dev@gmail.com" and password!=1234:
       print("plz write again password")
       #take password again
       password=int(input("Enter your Password: "))
       #check password
       if password == 1234:
        print("Welcome")
       else:
        print("tumesa na ho payga") 
   #if gmail is note correct     
else:
  print("Incorrect Credentials")
