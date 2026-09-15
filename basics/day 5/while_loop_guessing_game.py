#Gueesing game


#import random modules
import random
#Generate a random modules 1 to 100
jackpot=random.randint(1,100)
#take a input  number from  user
guess=int(input("Enter your number: "))

count=1;
#check  guees and random
while guess!=jackpot:
  if guess<jackpot:
    print("wrong! predict a greater no ")
  else:
    print("wrong! predict a lower no ")

  #take input again if guess and random not same
  guess=int(input("Enter your number: "))
  
  #total prediction count
  count+=1

else:
  print("Congratulation You are winnig the jackpot")
  print("You are winning at ",count,"times")

'''What I Learned from Guessing Game
I learned how to use a while loop to repeat the guessing process.
I learned how to use if-else inside a while loop.
I learned how to take user input repeatedly until the correct number is guessed.
I learned how to use random.randint() to generate a random number.
I learned how to use a counter variable to count the number of guesses.
I learned how to use while-else to display a message when the correct guess is made.'''



