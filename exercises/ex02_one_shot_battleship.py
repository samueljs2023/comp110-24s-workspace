"""EX02 One Shot Battleship."""

__author__ = "730712233"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


grid_size: int = 9
secret_row: int = 6
secret_column: int = 6

guess_line: str = ""
blank_line: str = f"{BLUE_BOX}" * grid_size
row_counter: int = 1
column_counter: int = 1


row_guess: str = input("Guess a row: ")
while int(row_guess) > grid_size or int(row_guess) < 1:
    row_guess = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")

column_guess: str = input("Guess a column: ")
while int(column_guess) > grid_size or int(column_guess) < 1:
    column_guess = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")

while row_counter <= grid_size:
    if row_counter != int(row_guess):
        print(BLUE_BOX * grid_size)
        row_counter += 1
    elif row_counter == int(row_guess):
        while column_counter <= grid_size:
            if column_counter != int(column_guess):
                guess_line += BLUE_BOX
                column_counter += 1
            elif column_counter == int(column_guess):
                if int(column_guess) == secret_column and int(row_guess) == secret_row:
                    guess_line += RED_BOX
                elif int(column_guess) != secret_column or int(row_guess) != secret_row:
                    guess_line += WHITE_BOX
                column_counter += 1
        row_counter += 1 
        print(guess_line)

if int(row_guess) == secret_row and int(column_guess) == secret_column:
    print("Hit!")
elif int(row_guess) == secret_row and int(column_guess) != secret_column:
    print("Close! Correct row, wrong column.")
elif int(row_guess) != secret_row and int(column_guess) == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")