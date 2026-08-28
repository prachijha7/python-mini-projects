print("Welcome to the Tip Calculator!")
bill = float(input("What was your Total Bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip_value = bill * tip/100
total_bill = bill + tip_value
bill_per_person = round(total_bill/people, 2)
print(f"Each person should pay: {bill_per_person}$")