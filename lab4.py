import math
sides = int(input("Input number of sides: "))  
length = float(input("Input the length of a side: "))  
polygon_area = (sides * length ** 2) / (4 * math.tan(math.pi / sides))  
print("The area of the polygon is:", polygon_area) 