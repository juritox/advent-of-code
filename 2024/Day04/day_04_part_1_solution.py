"""Solution to Advent of Code 4th December 2024 part 1."""

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


def count_xmas(line: str) -> int:
    """
    Count the number of "XMAS" occurrences in a given line.

    Args:
        line (str): The input string to search for "XMAS".

    Returns:
        int: The total count of "XMAS" in the line.
    """
    num_of_xmas = line.count("XMAS")

    return num_of_xmas


def count_samx(line: str) -> int:
    """
    Count the number of "SAMX" (XMAS backwards) occurrences in a given line.

    Args:
        line (str): The input string to search for "SAMX".

    Returns:
        int: The total count of "SAMX" in the line.
    """
    num_of_samx = line.count("SAMX")

    return num_of_samx


def get_all_horizontal_lines(puzzle: str) -> list[str]:
    """
    Split the puzzle input into horizontal lines.

    Args:
        puzzle (str): The complete puzzle input as a string.

    Returns:
        list[str]: A list of strings, each representing a horizontal line in the puzzle.
    """
    return puzzle.splitlines()


def get_all_vertical_lines(puzzle: str) -> list[str]:
    """
    Extract all vertical lines from the puzzle input.

    Args:
        puzzle (str): The complete puzzle input as a string.

    Returns:
        list[str]: A list of strings, each representing a vertical line in the puzzle.
    """
    rows = get_all_horizontal_lines(puzzle)
    transposed = zip(*rows)
    return ["".join(column) for column in transposed]


def get_all_primary_diagonal_lines(puzzle: str) -> list[str]:
    """
    Extract all primary (top-left to bottom-right) diagonal lines from the puzzle input.

    Args:
        puzzle (str): The complete puzzle input as a string.

    Returns:
        list[str]: A list of strings, each representing a primary diagonal line in the puzzle.
    """
    rows = get_all_horizontal_lines(puzzle)

    num_rows = len(rows)
    num_cols = len(rows[0])
    primary_diagonals = []

    # Traverse diagonals starting from the first column of each row
    for start_row in range(num_rows):
        diagonal = []
        row, col = start_row, 0
        while row < num_rows and col < num_cols:
            diagonal.append(rows[row][col])
            row += 1
            col += 1
        primary_diagonals.append("".join(diagonal))

    # Traverse diagonals starting from the first row of each column (except the first column)
    for start_col in range(1, num_cols):
        diagonal = []
        row, col = 0, start_col
        while row < num_rows and col < num_cols:
            diagonal.append(rows[row][col])
            row += 1
            col += 1
        primary_diagonals.append("".join(diagonal))

    return primary_diagonals


def get_all_secondary_diagonal_lines(puzzle: str) -> list[str]:
    """
    Extract all secondary (top-right to bottom-left) diagonal lines from the puzzle input.

    Args:
        puzzle (str): The complete puzzle input as a string.

    Returns:
        list[str]: A list of strings, each representing a secondary diagonal line in the puzzle.
    """
    rows = get_all_horizontal_lines(puzzle)

    num_rows = len(rows)
    num_cols = len(rows[0])
    secondary_diagonals = []

    # Traverse diagonals starting from the first column of each row
    for start_row in range(num_rows):
        diagonal = []
        row, col = start_row, num_cols - 1
        while row < num_rows and col >= 0:
            diagonal.append(rows[row][col])
            row += 1
            col -= 1
        secondary_diagonals.append("".join(diagonal))

    # Traverse diagonals starting from the last column of each row (except the first row)
    for start_col in range(num_cols - 2, -1, -1):
        diagonal = []
        row, col = 0, start_col
        while row < num_rows and col >= 0:
            diagonal.append(rows[row][col])
            row += 1
            col -= 1
        secondary_diagonals.append("".join(diagonal))

    return secondary_diagonals


def solve(input_file: Path = INPUT_FILE) -> int:
    """
    Solve the Advent of Code challenge for the given input file.

    This function calculates the total number of "XMAS" and "SAMX" occurrences
    in horizontal, vertical, primary diagonal, and secondary diagonal lines.
    The "SAMX" is XMAS backwards so it calculates it for both directions.

    Args:
        input_file (Path, optional): Path to the input file. Defaults to INPUT_FILE.

    Returns:
        int: The total sum of XMAS in a puzzle.
    """
    input_content = read_input(input_file)
    xmas_total = 0
    xmas_total += sum(map(count_xmas, get_all_horizontal_lines(input_content)))
    xmas_total += sum(map(count_samx, get_all_horizontal_lines(input_content)))
    xmas_total += sum(map(count_xmas, get_all_vertical_lines(input_content)))
    xmas_total += sum(map(count_samx, get_all_vertical_lines(input_content)))
    xmas_total += sum(map(count_xmas, get_all_primary_diagonal_lines(input_content)))
    xmas_total += sum(map(count_samx, get_all_primary_diagonal_lines(input_content)))
    xmas_total += sum(map(count_xmas, get_all_secondary_diagonal_lines(input_content)))
    xmas_total += sum(map(count_samx, get_all_secondary_diagonal_lines(input_content)))

    return xmas_total


if __name__ == "__main__":
    print(solve())
