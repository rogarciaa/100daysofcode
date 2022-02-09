print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
number_of_people = input("How many people to split the bill? ")

bill_and_tip = (int(tip) / 100 + 1) * float(total_bill)
bill_splitted = round(bill_and_tip / int(number_of_people), 2)
print(f"Each person should pay: ${bill_splitted}")