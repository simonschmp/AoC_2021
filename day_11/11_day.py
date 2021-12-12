from typing import List
from copy import deepcopy

INPUT_FILE = "input_1.txt"


def read_in_field(input_field: str) -> List[List[int]]:
    lines: List[str] = input_field.splitlines()
    field: List[List[int]] = []
    for line in lines:
        chars: List[str] = [char for char in line]
        field.append(list(map(int, chars)))
    return field


def increment_field(field: List[List[int]]) -> List[List[int]]:
    for row in range(len(field)):
        for col in range(len(field[0])):
            field[row][col] += 1
    return field


def calculate_part_one(field: List[List[int]], rounds: int) -> int:
    lightning_counter: int = 0
    max_row: int = (len(field)-1)
    max_col: int = (len(field[0])-1)
    for _ in range(rounds):
        round_finished: bool = False
        field = increment_field(field)
        while not round_finished:
            round_finished = True
            for row in range(len(field)):
                for col in range(len(field[0])):
                    if field[row][col] > 9:
                        lightning_counter += 1
                        field[row][col] = 0
                        round_finished = False
                        if row > 0 and col > 0:
                            if field[row-1][col-1] > 0:
                                field[row-1][col-1] += 1
                        if row > 0:
                            if field[row-1][col] > 0:
                                field[row-1][col] += 1
                        if row > 0 and col < max_col:
                            if field[row-1][col+1] > 0:
                                field[row-1][col+1] += 1
                        if col > 0:
                            if field[row][col-1] > 0:
                                field[row][col-1] += 1
                        if col < max_col:
                            if field[row][col+1] > 0:
                                field[row][col+1] += 1
                        if row < max_row and col > 0:
                            if field[row+1][col-1] > 0:
                                field[row+1][col-1] += 1
                        if row < max_row:
                            if field[row+1][col] > 0:
                                field[row+1][col] += 1
                        if row < max_row and col < max_col:
                            if field[row+1][col+1] > 0:
                                field[row+1][col+1] += 1
    return lightning_counter


def calculate_part_two(field: List[List[int]]) -> int:
    round_counter: int = 0
    max_row: int = (len(field)-1)
    max_col: int = (len(field[0])-1)
    all_flashed: bool = False
    while not all_flashed:
        round_counter += 1
        field = increment_field(field)
        round_finished = False
        while not round_finished:
            round_finished = True
            for row in range(len(field)):
                for col in range(len(field[0])):
                    if field[row][col] > 9:
                        field[row][col] = 0
                        round_finished = False
                        if row > 0 and col > 0:
                            if field[row-1][col-1] > 0:
                                field[row-1][col-1] += 1
                        if row > 0:
                            if field[row-1][col] > 0:
                                field[row-1][col] += 1
                        if row > 0 and col < max_col:
                            if field[row-1][col+1] > 0:
                                field[row-1][col+1] += 1
                        if col > 0:
                            if field[row][col-1] > 0:
                                field[row][col-1] += 1
                        if col < max_col:
                            if field[row][col+1] > 0:
                                field[row][col+1] += 1
                        if row < max_row and col > 0:
                            if field[row+1][col-1] > 0:
                                field[row+1][col-1] += 1
                        if row < max_row:
                            if field[row+1][col] > 0:
                                field[row+1][col] += 1
                        if row < max_row and col < max_col:
                            if field[row+1][col+1] > 0:
                                field[row+1][col+1] += 1
        all_flashed = True
        for row in range(len(field)):
            for col in range(len(field[0])):
                if field[row][col] != 0:
                    all_flashed = False
    return round_counter


with open(INPUT_FILE) as f:
    field_part_one: List[List[int]] = read_in_field(f.read())
    field_part_two: List[List[int]] = deepcopy(field_part_one)
    print(f"part one: {calculate_part_one(field_part_one, 100)}")
    print(f"part two: {calculate_part_two(field_part_two)}")


####### Tests #################################################################


def test_calculate_part_one():
    # arrange
    input_lines = [[1, 1, 1, 1, 1],
                   [1, 9, 9, 9, 1],
                   [1, 9, 1, 9, 1],
                   [1, 9, 9, 9, 1],
                   [1, 1, 1, 1, 1]]
    rounds = 1
    expected_output = 9

    # act
    result = calculate_part_one(input_lines, rounds)

    # assert
    assert result == expected_output


def test_calculate_part_one_long():
    # arrange
    input_lines = [[5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
                   [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
                   [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
                   [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
                   [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
                   [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
                   [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
                   [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
                   [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
                   [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]]
    rounds = 100
    expected_output = 1656

    # act
    result = calculate_part_one(input_lines, rounds)

    # assert
    assert result == expected_output


def test_calculate_part_two():
    # arrange
    input_lines = [[5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
                   [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
                   [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
                   [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
                   [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
                   [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
                   [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
                   [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
                   [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
                   [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]]
    expected_output = 195

    # act
    result = calculate_part_two(input_lines)

    # assert
    assert result == expected_output
