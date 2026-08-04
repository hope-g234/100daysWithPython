print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = float(input("How much percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip/100 * total_bill + total_bill
split_with_people = bill_with_tip / people
print(f"Each person should pay: ${split_with_people:.2f}")

