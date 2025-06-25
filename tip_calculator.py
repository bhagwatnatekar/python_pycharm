print("Welcom to the tip calculator!")
bill = float(input("What was the total bill?\n"))
tip = float(input("How much tip would you like to give? 10, 20, 12, 15\n"))
people = int(input("How many people to split the bill?\n"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
split_bill = total_bill / people
final_bill = round(split_bill, 2)
print(f"Each person should pay: ${final_bill}")
