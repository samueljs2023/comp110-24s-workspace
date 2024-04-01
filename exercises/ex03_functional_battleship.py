"""EX03 Functional Battleship."""

__author__ = "730712233"

import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(grid_size: int, grid_dimension: str) -> int:
    """Initializes an input guess from the player."""
    assert grid_dimension == "row" or grid_dimension == "column"
    guess: str = input(f"Guess a {grid_dimension}: ")
    while int(guess) > grid_size or int(guess) < 1:
        guess = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    return int(guess)


def print_grid(grid_size: int, row_guess: int, column_guess: int, accuracy: bool) -> None:
    """Prints grid of colored boxes."""
    row_counter: int = 1
    column_counter: int = 1
    guess_line: str = ""
    while row_counter <= grid_size:
        if row_counter != row_guess:
            print(BLUE_BOX * grid_size)
            row_counter += 1
        elif row_counter == row_guess:
            while column_counter <= grid_size:
                if column_counter != column_guess:
                    guess_line += BLUE_BOX
                    column_counter += 1
                elif column_counter == column_guess:
                    if accuracy:
                        guess_line += RED_BOX
                    elif not accuracy:
                        guess_line += WHITE_BOX
                    column_counter += 1
            row_counter += 1 
            print(guess_line)


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Verifies if the location guess matches the secret guess."""
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Runs full battleship game."""
    turn_counter: int = 1
    player_accuracy: bool = False
    while turn_counter <= 5 and not player_accuracy:
        print(f"=== Turn {turn_counter}/5 ===")
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int = input_guess(grid_size, "column")
        player_accuracy = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, player_accuracy)
        if player_accuracy:
            print("Hit!")
            print(f"You won in {turn_counter}/5 turns!")
        else:
            print("Miss!")
            if turn_counter == 5 and not player_accuracy:
                print("X/5 - Better luck next time!")
        turn_counter += 1


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))