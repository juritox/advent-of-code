"""
Solution to Advent of Code 2nd December 2024 part 1.
"""

import os

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
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        return content


def differerence_is_valid(line: str) -> bool:
    """
    Check if the absolute difference between adjacent numbers in a line is valid.

    The difference between any two adjacent numbers must be at most 3.

    Args:
        line (str): A string containing space-separated integers.

    Returns:
        bool: True if all adjacent differences are at least 3, False otherwise.
    """
    numbers = list(map(int, line.split()))
    previous_number = numbers[0]
    for number in numbers[1:]:
        if abs(previous_number - number) > 3:
            return False
        previous_number = number
    return True


def is_decreasing(line: str) -> bool:
    """
    Check if the numbers in a line are strictly decreasing.

    Args:
        line (str): A string containing space-separated integers.

    Returns:
        bool: True if the numbers are strictly decreasing, False otherwise.
    """
    numbers = list(map(int, line.split()))
    previous_number = numbers[0]
    for number in numbers[1:]:
        if number >= previous_number:
            return False
        previous_number = number
    return True


def is_increasing(line: str) -> bool:
    """
    Check if the numbers in a line are strictly increasing.

    Args:
        line (str): A string containing space-separated integers.

    Returns:
        bool: True if the numbers are strictly increasing, False otherwise.
    """
    numbers = list(map(int, line.split()))
    previous_number = numbers[0]
    for number in numbers[1:]:
        if number <= previous_number:
            return False
        previous_number = number
    return True


def is_safe(line: str) -> bool:
    """
    Determine if a line is considered "safe".

    A line is considered "safe" if:
    - The numbers are either strictly increasing or strictly decreasing.
    - Any two adjacent numbers differ by at least 1 and at most 3.

    Args:
        line (str): A string containing space-separated integers.

    Returns:
        bool: True if the line is safe, False otherwise.
    """
    return differerence_is_valid(line) and (is_decreasing(line) or is_increasing(line))


def solve(input_file: str = INPUT_FILE) -> int:
    """
    Solve the Advent of Code challenge for the given input file.

    This function reads the input file, evaluates each line to determine
    if it is "safe", and counts the total number of safe lines.
    
    A line is considered "safe" if:
    - The numbers are either strictly increasing or strictly decreasing.
    - Any two adjacent numbers differ by at least 1 and at most 3.

    Args:
        input_file (str, optional): Path to the input file.
        Defaults to INPUT_FILE.

    Returns:
        int: The total count of safe lines in the input file.
    """
    safe_reports = 0
    lines = read_input(input_file).splitlines()
    for line in lines:
        if is_safe(line):
            safe_reports += 1
    return safe_reports


if __name__ == "__main__":
    print(solve())
