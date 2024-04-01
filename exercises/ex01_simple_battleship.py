"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730712233"
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
boat_location: str = input("Pick a secret boat location between 1 and 4: ")
if int(boat_location) > 4:
    print("Error! " + str(boat_location) + " too high!")
    exit()
elif int(boat_location) < 1:
    print("Error! " + str(boat_location) + " too low!")
    exit()
else:
    boat_guess: str = input("Guess a number between 1 and 4: ")
    if int(boat_guess) > 4:
        print("Error! " + str(boat_guess) + " too high!")
        exit()
    elif int(boat_guess) < 1:
        print("Error! " + str(boat_guess) + " too low!")
        exit()
    else:
        if int(boat_guess) != int(boat_location):
            if int(boat_guess) == 1:
                print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
                print("Incorrect! You missed the ship.")
            elif int(boat_guess) == 2:
                print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
                print("Incorrect! You missed the ship.")
            elif int(boat_guess) == 3:
                print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
                print("Incorrect! You missed the ship.")
            elif int(boat_guess) == 4:
                print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)
                print("Incorrect! You missed the ship.")
        else:
            if int(boat_location) == 1:
                print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
                print("Correct! You hit the ship.")
            elif int(boat_location) == 2:
                print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
                print("Correct! You hit the ship.")
            elif int(boat_location) == 3:
                print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
                print("Correct! You hit the ship.")
            elif int(boat_location) == 4:
                print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
                print("Correct! You hit the ship.")