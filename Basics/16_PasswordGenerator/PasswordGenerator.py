import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nrLetters= int(input("How many letters would you like in your password?\n")) 
nrNumbers = int(input(f"How many numbers would you like?\n"))
nrSymbols = int(input(f"How many symbols would you like?\n"))

password = ""

for i in range(1, nrLetters + 1):
 password += random.choice(letters)

for i in range(1, nrNumbers + 1):
 password += random.choice(numbers)

for i in range(1, nrSymbols + 1):
 password += random.choice(symbols)

l = list(password)
random.shuffle(l)
password = ''.join(l)
print(password)