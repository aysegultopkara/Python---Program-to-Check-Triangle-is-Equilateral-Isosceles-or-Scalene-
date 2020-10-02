A = int(input("Enter side A :"))
B = int(input("Enter side B :"))
C = int(input("Enter side c :"))
if A == B == C:
    print("This is an equilateral triangle.")
elif A == B or B == C or A == C:
    print("This is an isosceles triangle..")
else:
    print("his is a scalene triangle.")
