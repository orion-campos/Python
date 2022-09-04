#import random
#namesString = input("Give me everybody's names, separated by a comma. ")
#names = namesString.split(", ")
#quantPeople = len(names)
#choosen = random.randint(0, quantPeople - 1)
#print((names[choosen]) + " is going to buy the meal today!")

import random
namesString = input("Give me everybody's names, separated by a comma. ")
names = namesString.split(", ")
choosen = random.choice(names)
print(choosen + " is going to buy the meal today!")
