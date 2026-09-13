#Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.



#formula--> Distance=(x2​−x1​)2+(y2​−y1​)2
#import math library
import math
#take first coordinates from the user as input.
x1=float(input("Enter the first coordinate of first point: "))
y1=float(input("Enter the first coordinate of second point: "))

#take Second coordinates from the user as input.
x2=float(input("Enter the second coordinate of first point: "))
y2=float(input("Enter the second coordinate of second point: "))

#find the euclidean distance between two coordinates
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)

#print the distance
print("euclidean distance between two coordinates: ",distance)
