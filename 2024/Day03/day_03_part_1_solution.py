"""
Solution to Advent of Code 3rd December 2024 part 1.
"""

import os
import re
from operator import mul

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")


def read_input(file_path: str) -> str:
    """
    Read the contents of a file and return them as a string.

    Args:
        file_path (str): The path to the input file to be read.

    Returns:
        str: The contents of the file as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there's an issue reading the file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    except IOError as e:
        raise IOError(f"Error reading file '{file_path}': {e}")


def find_all_muls(data: str) -> list[str]:
    """
    Find all multiplication expressions in the input data.

    This function uses a regular expression to find all instances
    of mul(x,y) in the input string, with additional validation.

    Args:
        data (str): The input string to search for multiplication expressions.

    Returns:
        List[str]: A list of all found multiplication expressions.
    """
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, data)

    validated_matches = [
        match for match in matches if match.startswith("mul(") and match.endswith(")")
    ]
    return validated_matches


def solve(input_file: str = INPUT_FILE) -> int:
    """
    Solve the Advent of Code challenge for the given input file.

    This function reads the input file, finds all multiplication
    expressions, evaluates them, and returns their total sum.

    Args:
        input_file (str, optional): Path to the input file.
        Defaults to INPUT_FILE.

    Returns:
        int: The total sum of all multiplications.
    """

    input_content = read_input(input_file)
    all_muls = find_all_muls(input_content)
    all_muls_evaluated = list(map(eval, all_muls))
    multiplications_total = sum(all_muls_evaluated)

    return multiplications_total


if __name__ == "__main__":
    print(solve())
