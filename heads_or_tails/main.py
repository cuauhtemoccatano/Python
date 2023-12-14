
import random
repeat = True
while repeat:
    print("Welcome to the coin toss program")
    print("I will flip a coin.")
    coin_toss = random.randint(0, 1)

    if coin_toss == 0:
        print("The coin toss is: Tails")
    else:
        print("The coin toss is: Heads")

    other_toss = input("Would you like to toss again? (Y/N): ").upper()
    if other_toss == "Y":
        repeat = True
    else:
        print("See you on the next toss")
        repeat = False
