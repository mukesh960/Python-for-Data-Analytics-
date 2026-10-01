'''Question 2: Electricity Bill Calculator

Write a Python program that calculates an electricity bill based on the number of units consumed.

Use these rates:

First 100 units: ₹5 per unit
Next 200 units (101–300): ₹7 per unit
Above 300 units: ₹10 per unit

Additional rule:

If the calculated bill is more than ₹5,000, add a 10% surcharge to the bill.
If the user enters 0 or a negative number, display "Please enter a valid unit".
unit = int(input("Enter your unit: "))'''

s1 = 5
s2 = 7
s3 = 10

if unit <= 0:
    print("Please enter a valid unit.")

else:
    print("Bill Summary:")

    # First 100 units → ₹5 per unit
    if unit <= 100:
        total_bill = unit * s1
        print(f"Bill calculation: {unit} × {s1} = {total_bill} Rs")

    # 101–300 units
    elif unit <= 300:
        total_bill = (100 * s1) + (unit - 100) * s2
        print(f"Bill calculation: 100 × {s1} + {unit-100} × {s2} = {total_bill} Rs")

    # Above 300 units
    else:
        total_bill = (100 * s1) + (200 * s2) + (unit - 300) * s3
        print(f"Bill calculation: 100 × {s1} + 200 × {s2} + {unit-300} × {s3} = {total_bill} Rs")

    # 10% surcharge if bill is above ₹5000
    if total_bill > 5000:
        surcharge = total_bill * 0.10
        total_bill = total_bill + surcharge

        print(f"10% surcharge: {surcharge} Rs")
        print(f"Final bill: {total_bill} Rs")


'''WHAT I LEARN AND HOW I THINK 
Step 1 → What is the input?
         → Units consumed

Step 2 → Are the units valid?
         → unit <= 0 → Invalid

Step 3 → Which slab does the unit belong to?
         → <= 100
         → <= 300
         → > 300

Step 4 → What rate applies to each slab?
         → First 100  = ₹5
         → Next 200   = ₹7
         → Above 300  = ₹10

Step 5 → Is the bill above ₹5000?
         → Yes → Add 10% surcharge
         → No  → No surcharge

Step 6 → Display the final bill'''
