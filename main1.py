# program using random module
import random
playing=True
num=random.randint(10,20)
while playing:
    guess=int(input("enter your guess between 10 and 20"))
    if num==guess:
        print("you win the game ")
        print("my number was",num)
        break
    else:
        print("too bad try agian for the first or 500th time")
