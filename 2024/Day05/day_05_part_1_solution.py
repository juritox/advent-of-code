"""Solution to Advent of Code 5th December 2024 part 1."""

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
    ordering_rules = []
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
    updates = []
    for line in lines[start_index:]:
        updates.append(line)
    return updates


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
    checked_pages = []
    for page in pages:
        for rule in rules:
            rule_parts = rule.split("|")
            if rule_parts[0] == page:
                if rule_parts[1] in pages:
                    if rule_parts[1] in checked_pages:
                        return False
        checked_pages.append(page)
    return True


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
    validates the updates against the rules, and calculates the sum of middle
    page numbers from valid updates.

    Args:
        input_file (Path, optional): Path to the input file. Defaults to INPUT_FILE.

    Returns:
        int: The sum of middle page numbers from all valid updates.
    """
    input_content = read_input(input_file)
    ordering_rules, updates_start_index = read_ordering_rules(input_content)
    updates = read_updates(input_content, updates_start_index)
    printed_updates = []
    for update in updates:
        if check_rules(update, ordering_rules):
            printed_updates.append(update)
    middle_page_numbers = []
    for printed_update in printed_updates:
        middle_page_numbers.append(extract_middle_number(printed_update))

    return sum(middle_page_numbers)


if __name__ == "__main__":
    print(solve())
