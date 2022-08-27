height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = float(weight) / float(height) ** 2
bmiInt = int(bmi)
#bmiStr = str(bmiInt)
#print("Your BMI is: " + bmiStr)
print(f"Your BMI is: {bmiInt}")