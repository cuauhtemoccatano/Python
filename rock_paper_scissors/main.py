import random
import figures

play = True  # variable for while loop

while play:  # while loop for playing again

    game_images = [figures.rock, figures.paper, figures.scissors]  # list of images for rock, paper, scissors

    print("Let's play Rock, Paper, Scissors!" + "\n")
    print("What's your move?")
    user_move = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

    if user_move >= 3 or user_move < 0:  # check number is between list ranges
        print("invalid number, you lose" + "\n" + "(Choose a number between 0 and 2)" + "\n")

    else:
        print(game_images[user_move])

        computer_move = random.randint(0, 2)  # Chooses between 0,1,2
        print("Computer chose: ")
        print(game_images[computer_move])  # prints computer's move

        if user_move == computer_move:
            print("It's a tie!")
        elif user_move == 0 and computer_move == 1:  # rock and paper
            print("You lose!")
        elif user_move == 0 and computer_move == 2:  # rock and scissors
            print("You win!")
        elif user_move == 1 and computer_move == 0:  # paper and rock
            print("You win!")
        elif user_move == 1 and computer_move == 2:  # paper and scissors
            print("You lose!")
        elif user_move == 2 and computer_move == 0:  # scissors and rock
            print("You lose!")
        elif user_move == 2 and computer_move == 1:  # scissors and paper
            print("You win!")

        play_again = input("Do you want to play again? Type Y for Yes or N for No.").upper()
        # break or repeat while loop
        if play_again == "Y":
            play = True
        else:
            print("Thanks for playing!")
            play = False
