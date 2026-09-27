'''Question

Write a Python program to convert a given number of days into months and remaining days, assuming 1 month = 30 days.

Example:
Input: 140
Output: 4 months 20 days'''

days = int(input("Enter total no days: "))
mon = 30


#flor using  get integer value and remove decimal value
months = days // mon
#Modulus is using to get remainder
days = days % mon

print(months, "months", days, "days")
