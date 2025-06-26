weight = float(input("Enter your weight "))
height = float(input("Enter your height "))

bmi = weight / (height ** 2)

# Write your code below 👇
if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")

'''
weight = 85
height = 1.85
 
bmi = weight / (height ** 2)
 
if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")
'''