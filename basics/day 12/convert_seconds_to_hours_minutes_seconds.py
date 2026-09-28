'''Write a Python program to convert a given number of seconds into hours, minutes, and seconds.'''

totl_sec = int(input("Enter a time in seconds: "))

# 1 minute = 60 seconds
# 1 hour = 60 * 60 = 3600 seconds
t = 60

# Converting seconds into hours
hrs = totl_sec // (t * t)

# Remaining seconds after hours
rem_sec = totl_sec % (t * t)

# Converting remaining seconds into minutes
mint = rem_sec // t

# Remaining seconds
sec = rem_sec % t

print("Total time taken:", hrs, "hours", mint, "minutes", sec, "seconds")


'''What I Learned — Logic
// → Used to get the quotient
% → Used to get the remainder
Hours: total_seconds // 3600
Remaining seconds: total_seconds % 3600
Minutes: remaining_seconds // 60
Seconds: remaining_seconds % 60
Main logic: First calculate hours, then use the remaining seconds to calculate minutes, and finally get the remaining seconds.'''
