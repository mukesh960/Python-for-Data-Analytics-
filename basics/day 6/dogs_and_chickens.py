'''Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
For example: Input: heads -> 4 legs -> 12
Output: dogs -> 2 chicken -> 2'''


# Take the total number of heads and legs from the user
heads = int(input("Enter total number of heads: "))
legs = int(input("Enter total number of legs: "))

# Calculate the total number of dogs
dogs = (legs - 2 * heads) / 2

# Calculate the total number of chickens
chickens = heads - dogs

# Print the total number of heads and legs
print("Heads", heads, "Legs", legs, sep="->")

# Print the total number of dogs and chickens
print("Dogs", int(dogs), "Chickens", int(chickens), sep="->")

'''What I Learned
Taking user input using input()
Converting input into an integer using int()
Using variables to store values
Using arithmetic operators (-, *, /)
Using a mathematical formula to solve a problem
Using one variable's value to calculate another
Using print() with multiple values
Using sep in print()'''