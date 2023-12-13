import figure
play = True  # variable for while loop

while play:

    print(figure.chest)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    first_road = input("Which road would you take? \n Left or Right? \n ").lower()
    if first_road == "left":
        second_road = input("You get to the end of the road and find a lake. "
                            "\n Would you swim or wait for a boat? \n ¿Swim or wait?\n ").lower()

        if second_road == "wait":
            third_road = input("You walk through a cave and find 3 doors "
                               "\n ¿Which on are you choosing? \n Red, Blue Or Yellow?\n ").lower()
            if third_road == "yellow":
                print("You found a treasure chest and decide to open it. "
                      "\n It´s full of gold, you're rich")
            elif third_road == "red":
                print("You encounter a vast cave and decide to walk, "
                      "\n the door locks behind you and you're trapped forever. "
                      "\n Good luck")
            elif third_road == "blue":
                print("You find a bunch of bloodsucking bats. "
                      "\n Game over.")
            else:
                print("You fell into a hole and died.")
        else:
            print("You face a group of alligators and died.")
    else:
        print("You fell into a hole and died.")

        play_again = input("Do you want to play again? Type Y for Yes or N for No.").upper()
        # Question to break or repeat while loop
        if play_again == "Y":
            play = True
        else:
            print("Thanks for playing!")
            play = False
