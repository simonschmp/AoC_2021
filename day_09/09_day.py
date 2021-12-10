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


def get_low_points(field: List[List[int]]) -> List[List[int]]:
    min_numbers: List[List[int]] = []
    smallest: bool = True
    for row in range(len(field)):
        for col in range(len(field[0])):
            if row < (len(field)-1):
                if field[row][col] >= field[row+1][col]:
                    smallest = False
            if row > 0:
                if field[row][col] >= field[row-1][col]:
                    smallest = False
            if col < (len(field[0])-1):
                if field[row][col] >= field[row][col+1]:
                    smallest = False
            if col > 0:
                if field[row][col] >= field[row][col-1]:
                    smallest = False
            if smallest:
                min_numbers.append([row, col])
            smallest = True
    return min_numbers


def calculate_part_one(field: List[List[int]]) -> int:
    min_numbers_points: List[List[int]] = get_low_points(field)
    points: int = 0
    for row_col in min_numbers_points:
        points += (field[row_col[0]][row_col[1]] + 1)
    return points


def get_next_points(field: List[List[int]], position: List[int], shadow_field: List[List[int]]) -> List[List[int]]:
    next_points: List[List[int]] = []
    row: int = position[0]
    col: int = position[1]
    if row < (len(field)-1):
        if field[row][col] < field[row+1][col] and field[row+1][col] != 9 and shadow_field[row+1][col] != 9:
            next_points.append([row+1, col])
            shadow_field[row+1][col] = 9
    if row > 0:
        if field[row][col] < field[row-1][col] and field[row-1][col] != 9 and shadow_field[row-1][col] != 9:
            next_points.append([row-1, col])
            shadow_field[row-1][col] = 9
    if col < (len(field[0])-1):
        if field[row][col] < field[row][col+1] and field[row][col+1] != 9 and shadow_field[row][col+1] != 9:
            next_points.append([row, col+1])
            shadow_field[row][col+1] = 9
    if col > 0:
        if field[row][col] < field[row][col-1] and field[row][col-1] != 9 and shadow_field[row][col-1] != 9:
            next_points.append([row, col-1])
            shadow_field[row][col-1] = 9
    return next_points


def calculate_part_two(field: List[List[int]]):
    shadow_field: List[List[int]] = deepcopy(field)
    low_points: List[List[int]] = get_low_points(field)
    value_list: List[int] = []
    for low_point in low_points:
        shadow_field[low_point[0]][low_point[1]] = 9
        count: int = 0
        list_to_check: List[List[int]] = []
        list_to_check.append(low_point)
        while len(list_to_check) > 0:
            list_to_check.extend(get_next_points(field, list_to_check[0], shadow_field))
            list_to_check.pop(0)
            count += 1
        value_list.append(count)
    value_list = sorted(value_list, reverse=True)
    return value_list[0] * value_list[1] * value_list[2]


with open(INPUT_FILE) as f:
    field = read_in_field(f.read())
    print(f"part one: {calculate_part_one(field)}")
    print(f"part two: {calculate_part_two(field)}")


####### Tests #################################################################


def test_calculate_part_one():
    # arrange
    input = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
             [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
             [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
             [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
             [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]
    expected_output = 15

    # act
    result = calculate_part_one(input)

    # assert
    assert result == expected_output


def test_calculate_part_two():
    # arrange
    input = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
             [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
             [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
             [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
             [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]
    expected_output = 1134

    # act
    result = calculate_part_two(input)

    # assert
    assert result == expected_output
