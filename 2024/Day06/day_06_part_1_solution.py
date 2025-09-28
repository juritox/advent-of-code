"""Solution to Advent of Code 6th December 2024 part 1."""

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


def create_map(data: str) -> list[list[str]]:
    """
    Convert the input string into a 2D grid representation of the room map.

    Args:
        data (str): The raw input data containing the room layout with newlines
                   separating rows.

    Returns:
        list[list[str]]: A 2D list where each inner list represents a row of
                        characters from the input map.
    """
    room_map = []
    rows = data.splitlines()
    for row in rows:
        columns = list(row)
        room_map.append(columns)
    return room_map


def get_map_dimensions(room_map: list[list[str]]) -> tuple[int, int]:
    """
    Get the dimensions of the room map.

    Args:
        room_map (list[list[str]]): A 2D list representing the room layout.

    Returns:
        tuple[int, int]: A tuple containing (number_of_rows, number_of_columns).
    """
    return len(room_map), len(room_map[0])


def find_guard_start_position(room_map: list[list[str]]) -> tuple[int, int, str]:
    """
    Locate the guard's initial position and direction in the room map.

    The guard is represented by directional characters:
    - '^' for facing up
    - 'v' for facing down
    - '<' for facing left
    - '>' for facing right

    Args:
        room_map (list[list[str]]): A 2D list representing the room layout.

    Returns:
        tuple[int, int, str]: A tuple containing (row_index, column_index, direction)
                             where direction is one of "up", "down", "left", "right".

    Raises:
        RuntimeError: If no guard character is found in the map.
    """
    for row in room_map:
        for column in row:
            if column == "^":
                return room_map.index(row), row.index(column), "up"
            elif column == "v":
                return room_map.index(row), row.index(column), "down"
            elif column == "<":
                return room_map.index(row), row.index(column), "left"
            elif column == ">":
                return room_map.index(row), row.index(column), "right"

    raise RuntimeError("The guard was not found")


def move_guard(
    room_map: list[list[str]], room_dimensions: tuple[int, int], guard_position: tuple[int, int, str]
) -> tuple[int, int, str]:
    """
    Move the guard according to the movement rules and mark visited positions.

    The guard moves forward in her current direction. If she encounters an obstacle ('#'),
    she turns right (90 degrees clockwise). If she would move outside the map bounds,
    her direction becomes "out". The current position is marked with 'X' before moving.

    Movement rules:
    - Up: Move to row-1, turn right if obstacle
    - Down: Move to row+1, turn left if obstacle
    - Left: Move to column-1, turn up if obstacle
    - Right: Move to column+1, turn down if obstacle

    Args:
        room_map (list[list[str]]): The 2D room map that will be modified to mark visited positions.
        room_dimensions (tuple[int, int]): The (rows, columns) dimensions of the room.
        guard_position (tuple[int, int, str]): Current (row, column, direction) of the guard.

    Returns:
        tuple[int, int, str]: New (row, column, direction) after the move.
                             Direction becomes "out" if the guard exits the map bounds.

    Raises:
        ValueError: If the guard direction is not one of "up", "down", "left", "right".
    """
    # Mark current position as visited
    room_map[guard_position[0]][guard_position[1]] = "X"
    guard_direction = guard_position[2]

    # Moving UP (decreasing row index)
    if guard_direction == "up":
        if guard_position[0] - 1 < 0:  # Would exit top boundary
            return guard_position[0], guard_position[1], "out"
        elif room_map[guard_position[0] - 1][guard_position[1]] == "#":  # Hit obstacle
            return guard_position[0], guard_position[1], "right"  # Turn right: up -> right
        else:  # Clear path
            return guard_position[0] - 1, guard_position[1], "up"  # Move up one row

    # Moving DOWN (increasing row index)
    elif guard_direction == "down":
        if guard_position[0] + 1 >= room_dimensions[0]:  # Would exit bottom boundary
            return guard_position[0], guard_position[1], "out"
        elif room_map[guard_position[0] + 1][guard_position[1]] == "#":  # Hit obstacle
            return guard_position[0], guard_position[1], "left"  # Turn right: down -> left
        else:  # Clear path
            return guard_position[0] + 1, guard_position[1], "down"  # Move down one row

    # Moving LEFT (decreasing column index)
    elif guard_direction == "left":
        if guard_position[1] - 1 < 0:  # Would exit left boundary
            return guard_position[0], guard_position[1], "out"
        elif room_map[guard_position[0]][guard_position[1] - 1] == "#":  # Hit obstacle
            return guard_position[0], guard_position[1], "up"  # Turn right: left -> up
        else:  # Clear path
            return guard_position[0], guard_position[1] - 1, "left"  # Move left one column

    # Moving RIGHT (increasing column index)
    elif guard_direction == "right":
        if guard_position[1] + 1 >= room_dimensions[1]:  # Would exit right boundary
            return guard_position[0], guard_position[1], "out"
        elif room_map[guard_position[0]][guard_position[1] + 1] == "#":  # Hit obstacle
            return guard_position[0], guard_position[1], "down"  # Turn right: right -> down
        else:  # Clear path
            return guard_position[0], guard_position[1] + 1, "right"  # Move right one column

    else:
        raise ValueError(f"Invalid guard direction: {guard_direction}")


def count_x(room_map: list[list[str]]) -> int:
    """
    Count the total number of 'X' characters in the room map.

    'X' characters represent positions that have been visited by the guard
    during her patrol route.

    Args:
        room_map (list[list[str]]): The 2D room map containing the guard's path.

    Returns:
        int: The total count of 'X' characters across all rows in the map.
    """
    return sum(row.count("X") for row in room_map)


def solve(input_file: Path = INPUT_FILE) -> int:
    """
    Solve the Advent of Code challenge by simulating guard movement and counting visited positions.

    Args:
        input_file (Path, optional): Path to the input file containing the room layout. Defaults to INPUT_FILE.

    Returns:
        int: The number of distinct positions visited by the guard before she exits the map.
    """
    input_content = read_input(input_file)
    room_map = create_map(input_content)
    room_dimensions = get_map_dimensions(room_map)
    guard_position = find_guard_start_position(room_map)
    while guard_position[2] != "out":
        guard_position = move_guard(room_map, room_dimensions, guard_position)

    return count_x(room_map)


if __name__ == "__main__":
    print(solve())
