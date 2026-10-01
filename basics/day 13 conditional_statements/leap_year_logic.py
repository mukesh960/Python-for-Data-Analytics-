# LEAP YEAR LOGIC

year = 2024

# Check 1:
# % 4 == 0 checks whether the year is completely divisible by 4.
# Why? Most leap years occur every 4 years.
condition_1 = (year % 4 == 0 and year % 100 != 0)

# Check 2:
# % 100 != 0 checks that the year is NOT divisible by 100.
# Why? Century years (ending in 00) are NOT automatically leap years.
condition_2 = (year % 400 == 0)

# Final logic:
# A year is a leap year if:
# 1. It is divisible by 4 AND NOT divisible by 100
# OR
# 2. It is divisible by 400

if condition_1 or condition_2:
    print("Leap Year")
else:
    print("Not a Leap Year")


''' | Logic             | What does it check?     | Why do we use it?                             
| ----------------- | ----------------------- | --------------------------------------------- |
| `year % 4 == 0`   | Checks **4**            | Most leap years occur every 4 years           |
| `year % 100 != 0` | Checks **100**          | Removes century years from the normal rule    |
| `year % 400 == 0` | Checks **400**          | Allows special century years to be leap years |
| `and`             | Checks both conditions  | Both rules must be true                       |
| `or`              | Checks either condition | Either leap-year rule can make it a leap year |'''
