#Rock, paper , scissor game using python
import random
for i in range(100):
 computer = random.choice(["rock","paper","scissor"])
 player = input("Enter your choice (rock,paper,scissor):")

 if computer ==  player :
    print(f"Computer choosed {computer} and you choosed {player}")
    print("draw")
 elif computer == "rock" and player =="scissor":
    print(f"Computer choosed {computer} and you choosed {player}")
    print("computer win")
 elif computer == "scissor" and player =="rock":
    print(f"Computer choosed {computer} and you choosed {player}")
    print("you win")
 elif computer == "paper" and player =="rock":
    print(f"Computer choosed {computer} and you choosed {player}")
    print("computer win")
 elif computer == "rock" and player =="paper":
    print(f"Computer choosed {computer} and you choosed {player}")
    print("you win")
 elif computer == "scissor" and player =="paper":
    print(f"Computer choosed {computer} and you choosed {player}")
    print("computer win")
 elif computer == "paper" and player =="scissor":
    print(f"Computer choosed {computer} and you choosed {player}")
    print("you win")
