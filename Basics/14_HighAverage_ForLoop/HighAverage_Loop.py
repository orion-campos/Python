#without sum() len() max() or min()
numbers = input("Input a list of numbers ").split()
for n in range(0, len(numbers)):
 numbers[n] = int(numbers[n])

highestNumber = 0
for number in numbers:
 if highestNumber < number:
  highestNumber = number
print(f"The highest number is: {highestNumber}")

totalNumber = 0
numberQuantity = 0
for number in numbers:
 totalNumber += number
 numberQuantity += 1
average = round(totalNumber / numberQuantity)
print(f"The average is: {average}")
