## Inputs
# Total rent
# Electricity bill
# Food

## Output
# Total rent to pay

total_rent = int(input("Enter the room rent amount: \n"))
electric_unit = int(input("Total electric unit: \n"))
per_unit = int(input("Enter charge per unit \n"))
food_bill = int(input("Total food bill is: \n"))
peopel = int(input("Bill divide by: \n"))

total_rent = (electric_unit * per_unit) + food_bill + total_rent
print(f"Total bill is: {total_rent}")

split_bill = total_rent / peopel
print(f"Total bill per person: {split_bill}")