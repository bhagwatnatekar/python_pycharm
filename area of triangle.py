#This code will calculate the area of the triangle
#formula
# area = (1/2) * base * height

def area_of_triangle():
    base = float(input("Enter the base of triangle: "))
    height = float(input("Enter the height of triangle: "))
    area = (1 / 2) * base * height
    print(f"Area of triangle is: {area}")

area_of_triangle()