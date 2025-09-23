"""Solution to Advent of Code 5th December 2024 part 2."""

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


def read_ordering_rules(puzzle: str) -> tuple[list[str], int]:
    """
    Extract ordering rules from the puzzle input and determine where updates begin.

    Args:
        puzzle (str): The complete puzzle input as a string.

    Returns:
        tuple[list[str], int]: A tuple containing:
            - list[str]: List of ordering rules
            - int: Index where the updates section begins
    """
    lines = puzzle.splitlines()
    ordering_rules: list[str] = []
    for line in lines:
        if "|" not in line:
            rules_end_index = lines.index(line)
            break
        else:
            ordering_rules.append(line)
    update_start_index = rules_end_index + 1
    return ordering_rules, update_start_index


def read_updates(puzzle: str, start_index: int) -> list[str]:
    """
    Extract the list of updates from the puzzle input starting at a specific index.

    Args:
        puzzle (str): The complete puzzle input as a string.
        start_index (int): The line index where updates begin.

    Returns:
        list[str]: List of update strings from the puzzle input.
    """
    lines = puzzle.splitlines()
    return lines[start_index:]


def check_rules(update: str, rules: list[str]) -> bool:
    """
    Verify if an update follows all the ordering rules.

    Args:
        update (str): A single update string containing comma-separated pages.
        rules (list[str]): List of ordering rules to check against.

    Returns:
        bool: True if the update follows all rules, False otherwise.
    """
    pages = update.split(",")
    checked_pages: list[str] = []
    for page in pages:
        for rule in rules:
            rule_parts = rule.split("|")
            if rule_parts[0] == page:
                if rule_parts[1] in pages:
                    if rule_parts[1] in checked_pages:
                        return False
        checked_pages.append(page)
    return True


def update_string_to_list(update: str) -> list[int]:
    """
    Convert a comma-separated string of page numbers to a list of integers.

    Args:
        update (str): A comma-separated string of page numbers.

    Returns:
        list[int]: A list of integers representing the page numbers.
    """
    return list(map(int, update.split(",")))


def update_list_to_string(update: list[int]) -> str:
    """
    Convert a list of integers to a comma-separated string.

    Args:
        update (list[int]): A list of integers representing page numbers.

    Returns:
        str: A comma-separated string representation.
    """
    return ",".join(map(str, update))


def find_rule_violation(update: str, rules: list[str]) -> tuple[int, int]:
    """
    Find the first rule violation in an update and return the indices involved.

    Args:
        update (str): A single update string containing comma-separated pages.
        rules (list[str]): List of ordering rules to check against.

    Returns:
        tuple[int, int]: A tuple containing:
            - int: Index of the page that violates the rule
            - int: Index of the page that should come after but appears before

    Raises:
        RuntimeError: If no rule violation is found.
    """
    pages = update.split(",")
    checked_pages: list[str] = []
    for page in pages:
        for rule in rules:
            rule_parts = rule.split("|")
            if rule_parts[0] == page:
                if rule_parts[1] in pages:
                    if rule_parts[1] in checked_pages:
                        index_of_violated_page = checked_pages.index(rule_parts[1])
                        return pages.index(page), index_of_violated_page
        checked_pages.append(page)

    raise RuntimeError("No rule violation found")


def move_page_number_left(update: list[int], index_of_origin: int, index_to_move: int) -> list[int]:
    """
    Move a page number from one position to another in the update list.

    Args:
        update (list[int]): List of page numbers to modify.
        index_of_origin (int): The current index of the page to move.
        index_to_move (int): The target index where the page should be moved.

    Returns:
        list[int]: The modified list with the page number moved to the new position.
    """
    page_number = update.pop(index_of_origin)
    update.insert(index_to_move, page_number)
    return update


def extract_middle_number(update: str) -> int:
    """
    Extract the middle number from a comma-separated string of pages.

    Args:
        update (str): A string of comma-separated page numbers.

    Returns:
        int: The middle number from the update string.
    """
    pages = update.split(",")
    middle_index = len(pages) // 2
    return int(pages[middle_index])


def solve(input_file: Path = INPUT_FILE) -> int:
    """
    Solve the Advent of Code challenge for the given input file.

    This function processes a puzzle input containing ordering rules and updates,
    identifies updates that violate the ordering rules, corrects them by
    repeatedly moving pages to fix rule violations, and calculates the sum of
    middle page numbers from the corrected updates.

    The correction process works by:
    1. Finding incorrectly ordered updates
    2. For each incorrect update, iteratively finding rule violations
    3. Moving the violating page to the correct position
    4. Repeating until all rules are satisfied

    Args:
        input_file (Path, optional): Path to the input file. Defaults to INPUT_FILE.

    Returns:
        int: The sum of middle page numbers from all corrected updates.
    """
    input_content = read_input(input_file)
    ordering_rules, updates_start_index = read_ordering_rules(input_content)
    updates = read_updates(input_content, updates_start_index)
    incorrect_updates: list[str] = []
    for update in updates:
        if not check_rules(update, ordering_rules):
            incorrect_updates.append(update)
    corrected_updates: list[str] = []
    for incorrect_update in incorrect_updates:
        while not check_rules(incorrect_update, ordering_rules):
            page_index, index_of_violated_page = find_rule_violation(incorrect_update, ordering_rules)
            update_as_list = update_string_to_list(incorrect_update)
            incorrect_update = update_list_to_string(
                move_page_number_left(update_as_list, page_index, index_of_violated_page)
            )
        corrected_updates.append(incorrect_update)
    middle_page_numbers: list[int] = []
    for corrected_update in corrected_updates:
        middle_page_numbers.append(extract_middle_number(corrected_update))

    return sum(middle_page_numbers)


if __name__ == "__main__":
    print(solve())
