import random
def game():
    print("You are playing the game...")
    score = random.randint(1,60)
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
        if(hiscore == ""):
            hiscore = 0
        else:
            hiscore = int(hiscore)
    print(f"Your score is {score}")
    with open("hiscore.txt", "w") as f:
        if(score > hiscore):
            f.write(str(score))
    return score

game()