"""
Solution to Advent of Code 1st December 2024 part 2.
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


def split_lists(lists: str) -> tuple[list[int], list[int]]:
    """
    Split the input string into two separate lists.

    Args:
        lists (str): A string of space-separated numbers.

    Returns:
        tuple[list[int], list[int]]: A tuple containing two lists of integers.
    """
    list_1 = []
    list_2 = []
    for index, number in enumerate(lists.split()):
        if index % 2 == 0:
            list_1.append(int(number))
        else:
            list_2.append(int(number))

    return list_1, list_2


def calculate_similarity_score(lists: tuple[list[int], list[int]]) -> int:
    """
    Calculate the total similarity score between two lists of equal length.

    Similarity score is calculated by adding up each number in the first list
    after multiplying it by the number of times that number appears in second list.

    Args:
        lists (tuple[list[int], list[int]]): A tuple containing two lists of integers.

    Returns:
        int: The total similarity score between both lists.
    """
    list_1, list_2 = lists

    # Create a list of unique numbers from list_1 to avoid counting duplicates multiple times
    list_1_unique = list(set(list_1))

    similarity_score = 0

    for number in list_1_unique:
        if number in list_2:
            similarity_score += number * list_2.count(number)

    return similarity_score


def solve(input_file: str = INPUT_FILE) -> int:
    """
    Solve the Advent of Code challenge by reading input, splitting lists,
    and calculating the similarity score.

    Args:
        input_file (str, optional): Path to the input file.
        Defaults to INPUT_FILE.

    Returns:
        int: The solution to the challenge.
    """

    input_content = read_input(input_file)
    splited_lists = split_lists(input_content)
    return calculate_similarity_score(splited_lists)


if __name__ == "__main__":
    print(solve())
