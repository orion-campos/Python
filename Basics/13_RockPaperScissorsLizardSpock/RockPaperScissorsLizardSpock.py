from operator import truediv
import random
spock = r"""
 _  _          _  _
/ \/ \        / \/ \
\  \  \      /  /  /
 \  \  \    /  /  /
 _\  \  \  /  /  /
/ \\  \  \/  /  /
|  |            |
|  |            |
\               /
 \             /
  \           /
   |         |
"""
scissors = r"""
 _          _
/ \        / \
\  \      /  /
 \  \    /  /
 _\  \  /  /  _
/ \\  \/  / \/ \
|  |      |  |  |
|  |      |  |  |
\         \_/\_/
 \             /
  \           /
   |         |
"""
paper = r"""
    _   _  _    
   / \ / \/ \ _
   |  |  |  |/ \ 
   |  |  |  |  |
 _ |  |  |  |  |
/ \|  |  |  |  |
|  |            |
|  |            |
\               /
 \             /
  \           /
   |         |
"""
rock = r"""
 _   _  _  _  _
/ \ / \/ \/ \/ \
|  |  |   |  |  |
|  |  |   |  |  |
\   \_/\_/\_/\_/
 \             /
  \           /
   |         |
"""
lizard = r"""
    _____________________
   /    ______________/_/
  /    /         --
 /     \     __/  /
/ |     \___/   _/
| |           _/
| |        __/
|       ___/
|      /
"""
gameImages = [spock, scissors, paper, rock, lizard]
player = input("Choose Rock, Paper, Scissors, Lizard, or Spock: ").lower()

if player == "spock":
  playerChoose = 0
  print(gameImages[0])
elif player == "scissors":
  playerChoose = 1
  print(gameImages[1])
elif player == "paper":
  playerChoose = 2
  print(gameImages[2])
elif player == "rock":
  playerChoose = 3
  print(gameImages[3])
elif player == "lizard":
  playerChoose = 4
  print(gameImages[4])
else:
  print("Enter a valid option.")
print("You picked " + player)

computerChoose = random.randint(0, 4)
if computerChoose == 0:
  print(gameImages[0])
  print("Computer picked spock")
elif computerChoose == 1:
  print(gameImages[1])
  print("Computer picked scissors")
elif computerChoose == 2:
  print(gameImages[2])
  print("Computer picked paper")
elif computerChoose == 3:
  print(gameImages[3])
  print("Computer picked rock")
else:
  print(gameImages[4])
  print("Computer picked lizard")

if playerChoose == computerChoose:
  print("It is a draw.")
elif playerChoose == 0 and (computerChoose == 1 or computerChoose == 3):
  print("Your logic wins!")
elif playerChoose == 1 and (computerChoose == 2 or computerChoose == 4):
  print("Your sharp scissors wins!")
elif playerChoose == 2 and (computerChoose == 3 or computerChoose == 0):
  print("Your well written article wins!")
elif playerChoose == 3 and (computerChoose == 4 or computerChoose == 1):
  print("Your brute force wins!")
elif playerChoose == 4 and (computerChoose == 0 or computerChoose == 2):
  print("Your cold blood wins!")
else:
  print("You lose.")