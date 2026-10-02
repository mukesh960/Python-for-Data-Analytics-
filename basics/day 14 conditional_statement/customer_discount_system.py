# Question 1

# A retail store wants to implement a discount system to improve customer satisfaction and loyalty. The discount varies based on the customer type and the total purchase amount.

# The cashier will enter the customer type and purchase amount. The program should determine the applicable discount and calculate the final amount after applying the discount.

# The output should display:

# [Customer Type, Amount Purchased, Discount Applicable, Final Amount]

# Conditions:

# Regular Customers:

# No discount for purchases below $100.
# 5% discount for purchases between $100 and $500 (inclusive).
# 10% discount for purchases above $500.

# Premium Customers:

# 10% discount for purchases below $500.
# 15% discount for purchases above $500.

# VIP Customers:

# 20% discount for purchases below $1000.
# 30% discount for purchases above $1000.

    
coustomer_type=input("Enter your Coustomer Type:")
purchase_amount=float(input("Enter your Coustomer Amount: "))

#Regular Customers: 
if coustomer_type=="Regular" or coustomer_type=="regular":
     d1=0.05
     d2=0.10
    # No discount for purchases below $100
     if purchase_amount <100 :
         print(f"Coustomer Type: {coustomer_type}")
         print(f"Amount Purchased: ={purchase_amount}")
         print(f"Discount Applicable on : ={00.00}")
         print(f"Final Amount: {purchase_amount}")
         
    # 5% discount for purchases between $100 and $500 (inclusive).   
     elif purchase_amount >=100 and purchase_amount <=500:
         discount=purchase_amount*d1
         final_amount=purchase_amount-discount
         print(f"Coustomer Type: {coustomer_type}")
         print(f"Amount Purchased: ={purchase_amount}")
         print(f"Discount Applicable: {d1*100}% ={discount}")
         print(f"Final Amount: {final_amount}")
         
    # 10% discount for purchases above $500.
     else:
         discount=purchase_amount*d2
         final_amount=purchase_amount-discount
         print(f"Coustomer Type: {coustomer_type}")
         print(f"Amount Purchased: ={purchase_amount}")
         print(f"Discount Applicable: {d2*100}% ={discount}")
         print(f"Final Amount: {final_amount}")
         
# Premium Customers:     
elif coustomer_type=="Premium" or coustomer_type=="premium":
     d1=0.10
     d2=0.15
    # 10% discount for purchases below $500.
     if purchase_amount  <=500:
         discount=purchase_amount*d1
         final_amount=purchase_amount-discount
         print(f"Coustomer Type: {coustomer_type}")
         print(f"Amount Purchased: ={purchase_amount}")
         print(f"Discount Applicable: {d1*100}% ={discount}")
         print(f"Final Amount: {final_amount}")
         
     # 15% discount for purchases above $500.
     else :
         discount=purchase_amount*d2
         final_amount=purchase_amount-discount
         print(f"Coustomer Type: {coustomer_type}")
         print(f"Amount Purchased: ={purchase_amount}")
         print(f"Discount Applicable: {d2*100}% ={discount}")
         print(f"Final Amount: {final_amount}")

# VIP Customers:
elif  coustomer_type=="VIP" or coustomer_type=="vip":
     d1=0.20
     d2=0.30
    # 20% discount for purchases below $1000.
     if purchase_amount  <=1000:
         discount=purchase_amount*d1
         final_amount=purchase_amount-discount
         print(f" Coustomer Type: {coustomer_type}")
         print(f"Amount Purchased: ={purchase_amount}")
         print(f"Discount Applicable:  {d1*100}%={discount}")
         print(f"Final Amount: {final_amount}")
     else :
        # 30% discount for purchases above $1000.
         discount=purchase_amount*d2
         final_amount=purchase_amount-discount
         print(f"Coustomer Type: {coustomer_type}")
         print(f"Amount Purchased: ={purchase_amount}")
         print(f"Discount Applicable:  {d2*100}%={discount}")
         print(f"Final Amount: {final_amount}")

else:
    print("Invalid input")



# What I Learned From My Mistakes
# Input Data Types
# input() returns a string.
# Use float(input()) for purchase amounts.
# Python Indentation
# Code inside if, elif, and else must be indented.
# Nested if needs another indentation level.
# Standard: 4 spaces.
# Discount Calculation

# Discount amount:

# discount = amount * discount_rate

# Final amount:

# final_amount = amount - discount
# I initially used + instead of -.
# Percentage Conversion
# 5% = 0.05
# 10% = 0.10
# 20% = 0.20
# 30% = 0.30
# Formula:
# Percentage ÷ 100 = decimal
# Variable Naming & Spelling
# Avoid spelling mistakes such as:
# coutomer ❌ → customer ✅
# Premimum ❌ → Premium ✅

# Use clear names:

# customer_type
# purchase_amount
# discount_rate
# discount
# final_amount
# Missing Parentheses
# I forgot ) in some print() statements.
# Check matching (), especially in long f-strings.
# Condition Logic

# Learned to use:

# if
# elif
# else

# Also:

# and
# or
# Boundary Conditions
# Need to carefully check cases like:
# exactly 100
# exactly 500
# exactly 1000
# Don't leave gaps or overlaps in conditions.
# Invalid Input
# Don't automatically treat every unknown customer as VIP.
# Use a separate condition for VIP and an else for invalid input.
# 🎯 Your main weak areas right now

# 1. Indentation
# 2. Data types (input() vs float())
# 3. Calculation logic
# 4. Percentage conversion
# 5. Spelling/variable consistency

# These are the areas you should practice repeatedly before moving to harder conditional problems.
