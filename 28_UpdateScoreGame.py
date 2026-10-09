print(''' The game function in a program lets a user play a game and returns the score as an integer.
 You need to read a file "highscore.txt" which is either blank or contains the privious highscore.
 you need to write a program to update the high score whenever the game function breaks the high score. ''')

import random 

def game():
    print("Yor are playing game..")
    score = random.randint(1,10000)
    with open("28.1_highscore.txt") as f:
        highscore = f.read()
        if(highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0

    print("your score", score)
    if(score > highscore):
        with open("28.1_highscore.txt", "w") as f:
            f.write(highscore)
    
    return score

game()