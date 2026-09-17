'''Problem 4: Write a menu-driven program -
cm to ft
km to miles
USD to INR
exit'''
# Conversion values
# 1 CM = 0.0328 FT
# 1 KM = 0.6214 Miles
# 1 USD = 95.25 INR

# Take a number from the user
num = int(input("Enter a number to convert: "))

# Display conversion menu
print("1. CM to FT")
print("2. KM to Miles")
print("3. USD to INR")
print("4. Exit")

# Take menu choice from the user
menu = input("Enter a menu number: ")

# Convert CM to FT
if menu == "1":
    cm_to_ft = num * 0.0328
    print("CM → FT:", cm_to_ft)

# Convert KM to Miles
elif menu == "2":
    km_to_miles = num * 0.6214
    print("KM → Miles:", km_to_miles)

# Convert USD to INR
elif menu == "3":
    usd_to_inr = num * 95.25
    print("USD → INR:", usd_to_inr)

# Exit the program
elif menu == "4":
    print("Exiting the program...")

# Handle invalid menu choice
else:
    print("Invalid menu choice")
```
