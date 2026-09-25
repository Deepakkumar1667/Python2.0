import random

computer = random.choice([1,2,3])
yourchoice = input("Enter your choice: ").lower()
choice = {"rock" : 1,
          "paper": 2,
          "scissor": 3}

reversechoice = {1 : "rock", 
                 2 : "paper",
                 3 : "scissor"}

if yourchoice not in choice:
    print("Spelling mistake! choose:(rock, paper, scissor)")

else:
    you = choice[yourchoice]

    print("computer choice :",reversechoice[computer])
    print("your choice :",reversechoice[you])

    if(computer == you):
        print("It's draw!")
    elif(computer == 1 or you == 2):
        print("you win!")
    elif(computer == 2 or you == 3):
        print("you win!")
    elif(computer == 3 or you == 1):
        print("you win!")
    else:
        print("you lose!")

    