# Question Name

# Store Even Numbers in a List Using a for Loop

num=int(input("enter your number: "))
lis=[]
for  i in range(1,num+1):
    if i%2==0:
     print(lis[i])
print(lis)


# What I Learned
# How range() generates numbers one by one.
# How the variable i stores the current number.
# How to check even numbers using i % 2 == 0.
# Difference between accessing a list element and adding an element.
# lis[i] → accesses an existing element.
# lis.append(i) → adds i to the list.
# How to create and print a list of even numbers.
