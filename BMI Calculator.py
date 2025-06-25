weight = float(input("Enter the weight\n"))
height = float(input("Enter the height\n"))
#bmi formula
bmi = weight / height ** 2
print(bmi)
#print(round(bmi))
#round 2 decimal places
print(round(bmi, 2))