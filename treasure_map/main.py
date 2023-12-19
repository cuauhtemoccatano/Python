line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
grid = [line1, line2, line3]
play = True
while play:
    print("Hide your treasure! \n"
          "X marks the spot.")
    position1 = input("Where do you want to put the treasure? \n"
                      "Choose a letter from A to C. \n")
    letter = position1.lower()
    abc = ["a", "b", "c"]
    letter_index = abc.index(letter)
    position2 = input("Where do you want to put the treasure? \n"
                      "Choose a number from row 1 to 3. \n")
    number_index = int(position2) - 1
    grid[number_index][letter_index] = "X"
    print(f"{line1}\n{line2}\n{line3}")

    play_again = input("Do you want to play again? Type 'Y' or 'N'.\n")
    if play_again == "N":
        play = False
        print("Thanks for playing!")
    else:
        play = True
