"""EX02 One Shot Battleship"""

__author__ = "730712233"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

the_grid: str = ""
the_grid2: str = ""
emoji_string: str = f"{BLUE_BOX}" * grid_size
row_counter: int = 1
column_counter: int = 1


row_guess: int = input("Guess a row: ")
while int(row_guess) > grid_size or int(row_guess) < 1:
    row_guess = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")

column_guess: int = input("Guess a column: ")
while int(column_guess) > grid_size or int(column_guess) < 1:
    column_guess = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")

if int(row_guess) == secret_row and int(column_guess) == secret_column:
    print("Hit!")
else:
    print("Miss!")

while row_counter <= grid_size:
    if row_counter != secret_row:
        print(BLUE_BOX * grid_size)
        row_counter += 1
    else:
        while column_counter != int(column_guess) and column_counter <= grid_size:
            the_grid += BLUE_BOX
            column_counter += 1
        if column_counter == int(column_guess):
            if int(column_guess) == secret_column and int(row_guess) == secret_row:
                the_grid += RED_BOX
            else:
                the_grid += WHITE_BOX
            column_counter += 1
        
        print(the_grid)
        row_counter += 1


exit()