'''Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
Salary(Lakhs) : Tax(%)

Below 5 : 0%
5-10 : 10%
10-20 : 20%
aboove 20 : 30%'''
# Take salary amount from the user
amount = int(input("Enter your salary amount: "))

# HRA = 10%, DA = 5%, PF = 3%
hra = 0.10
da = 0.05
pf = 0.03

# Calculate total deduction percentage
total_deduction = hra + da + pf

# Calculate total HRA, DA, and PF deduction
deduction = amount * total_deduction


# Tax slab: Above 5 lakh and up to 10 lakh - 10% tax
if amount > 500000 and amount <= 1000000:
    tax = amount * 0.10
    print("Your salary after tax and other deductions:", amount - (tax + deduction))


# Tax slab: Above 10 lakh and up to 20 lakh - 20% tax
elif amount > 1000000 and amount <= 2000000:
    tax = amount * 0.20
    print("Your salary after tax and other deductions:", amount - (tax + deduction))


# Tax slab: Above 20 lakh - 30% tax
elif amount > 2000000:
    tax = amount * 0.30
    print("Your salary after tax and other deductions:", amount - (tax + deduction))


# Tax slab: 5 lakh or below - 0% tax
else:
    print("Your salary after other deductions:", amount - deduction)

'''What I Learned:

How to use if-elif-else statements.
How to apply multiple conditions using and.
How to create salary/tax ranges using >, <=.
How to use percentage in decimal form (10% = 0.1).
How to calculate a percentage of a given number.
How to use different calculations for different conditions.
How to use else when none of the previous conditions are true.'''