"""Solution to Advent of Code 3rd December 2024 part 2."""

from pathlib import Path
import re
from operator import mul

# Prevents "unused import" warning - mul is used by eval()
_ = mul

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


def find_all_expressions(data: str) -> list[str]:
    """
    Find all relevant expressions in the input data.

    This function uses a regular expression to find all instances
    of mul(x,y) in the input string, with additional validation.
    It also find all "do()" and "don't" instructions.

    Args:
        data (str): The input string to search for multiplication expressions.

    Returns:
        list[str]: A list of all found relevant expressions.
    """
    pattern = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"
    matches = re.findall(pattern, data)

    validated_matches = [
        match
        for match in matches
        if (match.startswith("mul(") and match.endswith(")")) or match == "do()" or match == "don't()"
    ]
    return validated_matches


def filter_all_enabled_muls(expressions: list[str]) -> list[str]:
    """
    Filter multiplication expressions based on enable/disable instructions.

    This function processes a list of expressions, tracking whether
    multiplication operations are currently enabled. It returns a list of
    multiplication expressions that are active when encountered.

    Args:
        expressions (list[str]): A list of expressions including
            multiplication operations, "do()", and "don't()" instructions.

    Returns:
        list[str]: A list of multiplication expressions that were
        enabled at the time of their occurrence.

    Notes:
        - "do()" enables multiplication operations
        - "don't()" disables multiplication operations
        - Only multiplication expressions encountered while enabled
          are included in the result
    """
    enabled_muls = []
    muls_enabled = True
    for expression in expressions:
        if muls_enabled and "mul" in expression:
            enabled_muls.append(expression)
        elif expression == "do()":
            muls_enabled = True
        elif expression == "don't()":
            muls_enabled = False

    return enabled_muls


def solve(input_file: Path = INPUT_FILE) -> int:
    """
    Solve the Advent of Code challenge for the given input file.

    This function reads the input file, finds all enabled multiplication
    expressions, evaluates them, and returns their total sum.

    Args:
        input_file (Path, optional): Path to the input file. Defaults to INPUT_FILE.

    Returns:
        int: The total sum of all multiplications.
    """
    input_content = read_input(input_file)
    all_expressions = find_all_expressions(input_content)
    all_muls = filter_all_enabled_muls(all_expressions)
    all_muls_evaluated = list(map(eval, all_muls))
    multiplications_total = sum(all_muls_evaluated)

    return multiplications_total


if __name__ == "__main__":
    print(solve())
