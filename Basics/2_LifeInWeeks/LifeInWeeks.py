age = input("What is your current age?")
leftAge = 90 - int(age)
months = leftAge * 12
weeks = leftAge * 52
days = leftAge * 365 
print(f"You have {days} days, {weeks} weeks, and {months} months left.")