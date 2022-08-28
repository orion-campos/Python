print("Welcome to the Tip Calculator")
billTotal = float(input("What was the total bill value? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? ")) / 100 + 1
numPeople = int(input("How many people are going to split the bill? "))
#billPerson = round(((billTotal / numPeople) * tip),2)
billPerson = "{:.2f}".format((billTotal / numPeople) * tip)
#print(f"Each person should pay: ${billPerson}")
print("Each person should pay: $" + billPerson)
