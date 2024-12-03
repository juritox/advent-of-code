"""
Solution to Advent of Code 1st December 2024 part 1.
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


def sort_lists(lists: str) -> tuple[list[int], list[int]]:
    """
    Split and sort the input string into two separate lists.

    Args:
        lists (str): A string of space-separated numbers.

    Returns:
        tuple[list[int], list[int]]: A tuple containing two sorted lists of integers.
    """
    list_1 = []
    list_2 = []
    for index, number in enumerate(lists.split()):
        if index % 2 == 0:
            list_1.append(int(number))
        else:
            list_2.append(int(number))

    return sorted(list_1), sorted(list_2)


def calculate_difference(lists: tuple[list[int], list[int]]) -> int:
    """
    Calculate the total absolute difference between two lists of equal length.

    This function takes two sorted lists and calculates the sum of absolute
    differences between corresponding elements.

    Args:
        lists (tuple[list[int], list[int]]): A tuple containing two lists of integers.

    Returns:
        int: The total absolute difference between corresponding elements.
    """
    list_1, list_2 = lists

    total_difference = sum(
        abs(number_1 - number_2) for number_1, number_2 in zip(list_1, list_2)
    )

    return total_difference


def solve(input_file: str = INPUT_FILE) -> int:
    """
    Solve the Advent of Code challenge by reading input, sorting lists,
    and calculating the difference.

    Args:
        input_file (str, optional): Path to the input file.
        Defaults to INPUT_FILE.

    Returns:
        int: The solution to the challenge.
    """

    input_content = read_input(input_file)
    sorted_lists = sort_lists(input_content)
    return calculate_difference(sorted_lists)


if __name__ == "__main__":
    print(solve())
