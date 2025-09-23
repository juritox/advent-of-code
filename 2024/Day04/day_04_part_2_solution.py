"""Solution to Advent of Code 4th December 2024 part 2."""

from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


def read_input(file_path: Path) -> str:
    """
    Read the contents of a file and return them as a string.

    Args:
        file_path (Path): The path to the input file to be read.

    Returns:
        str: The contents of the file as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there's an issue reading the file.
    """
    try:
        return file_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    except IOError as e:
        raise IOError(f"Error reading file '{file_path}': {e}")


def get_all_horizontal_lines(puzzle: str) -> list[str]:
    """
    Split the puzzle input into horizontal lines.

    Args:
        puzzle (str): The complete puzzle input as a string.

    Returns:
        list[str]: A list of strings, each representing a horizontal line in the puzzle.
    """
    return puzzle.splitlines()


def find_all_As(puzzle: str) -> list[tuple[int, int]]:
    """
    Find the positions of all occurrences of the character "A" in the puzzle, excluding the border.

    Args:
        puzzle (str): The complete puzzle input as a string.

    Returns:
        list[tuple[int, int]]: A list of tuples, where each tuple contains the (row_index, col_index)
                               of an "A" found in the puzzle.
    """
    lines = get_all_horizontal_lines(puzzle)
    all_As = []
    for line_index, line in enumerate(lines[1:-1], start=1):  # Skip the first and last lines
        for char_index, char in enumerate(line[1:-1], start=1):  # Skip the first and last characters in each line
            if char == "A":
                all_As.append((line_index, char_index))
    return all_As


def get_upper_line_chars(puzzle: str, position: tuple[int, int]) -> str:
    """
    Get the characters to the left and right of a position in the line above the given position.

    Args:
        puzzle (str): The complete puzzle input as a string.
        position (tuple[int, int]): A tuple representing the (row_index, col_index) of the position.

    Returns:
        str: A string containing two characters from the line above the given position:
             the character to the left and the character to the right of the specified column.
    """
    lines = get_all_horizontal_lines(puzzle)
    row_index = position[0]
    col_index = position[1]
    upper_line = lines[row_index - 1]
    upper_line_left_char = upper_line[col_index - 1]
    upper_line_right_char = upper_line[col_index + 1]
    both_chars = upper_line_left_char + upper_line_right_char
    return both_chars


def get_lower_line_chars(puzzle: str, position: tuple[int, int]) -> str:
    """
    Get the characters to the left and right of a position in the line below the given position.

    Args:
        puzzle (str): The complete puzzle input as a string.
        position (tuple[int, int]): A tuple representing the (row_index, col_index) of the position.

    Returns:
        str: A string containing two characters from the line below the given position:
             the character to the left and the character to the right of the specified column.
    """
    lines = get_all_horizontal_lines(puzzle)
    row_index = position[0]
    col_index = position[1]
    lower_line = lines[row_index + 1]
    lower_line_left_char = lower_line[col_index - 1]
    lower_line_right_char = lower_line[col_index + 1]
    both_chars = lower_line_left_char + lower_line_right_char
    return both_chars


def check_x_mas(puzzle: str, position: tuple[int, int]) -> bool:
    """
    Check if a given position in the puzzle is part of an "X-MAS" pattern.

    The "X-MAS" pattern is defined as two "MAS" in the shape of an X.

    Args:
        puzzle (str): The complete puzzle input as a string.
        position (tuple[int, int]): A tuple representing the (row_index, col_index) of the position.

    Returns:
        bool: "True" if the position matches the "X-MAS" pattern, "False" otherwise.
    """
    upper_line_chars = get_upper_line_chars(puzzle, position)
    lower_line_chars = get_lower_line_chars(puzzle, position)
    if upper_line_chars == "MM" and lower_line_chars == "SS":
        return True
    elif upper_line_chars == "SS" and lower_line_chars == "MM":
        return True
    elif upper_line_chars == "MS" and lower_line_chars == "MS":
        return True
    elif upper_line_chars == "SM" and lower_line_chars == "SM":
        return True
    else:
        return False


def solve(input_file: Path = INPUT_FILE) -> int:
    """
    Solve the Advent of Code challenge for the given input file.

    This function finds all "A" characters in the puzzle (excluding borders) and checks if each "A"
    is the center of a valid "X-MAS" pattern. A valid "X-MAS" pattern consists of:
    - An "A" at the center
    - Two characters in the line above ("M", "S" in either order)
    - Two characters in the line below ("M", "S" in either order)
    arranged in one of these valid patterns:
    1. "MM" above and "SS" below
    2. "SS" above and "MM" below
    3. "MS" above and "MS" below
    4. "SM" above and "SM" below

    Args:
        input_file (Path, optional): Path to the input file. Defaults to INPUT_FILE.

    Returns:
        int: The total number of valid X-MAS patterns found in the puzzle.
    """
    input_content = read_input(input_file)
    all_As = find_all_As(input_content)
    xmas_total = 0
    for A in all_As:
        if check_x_mas(input_content, A):
            xmas_total += 1
    return xmas_total


if __name__ == "__main__":
    print(solve())
