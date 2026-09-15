'''Question

Write a Python program to take a number from the user and print its multiplication table from 1 to 10 using a while loop.'''

#enter a number  form user
num=int(input("Enter a number to perform tbale: "))
#initilization
i=1  
#condition
while i<=10:
  #print the table
  print(num,"*",i,"=",num*i) 
  #increament
  i+=1 #i=i+1

  '''What I Learned
Learned how to use a while loop.
Learned the 3 important parts of a loop:
Initialization: i = 1
Condition: i <= 10
Increment: i += 1
Learned that the condition controls how long the loop runs.
Learned that increment updates the loop variable and helps stop the loop.
Learned to use indentation for the statements inside the loop.'''