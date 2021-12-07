from typing import List
import pytest

INPUT_FILE = "input_1.txt"


def calculate_best_position_part_one(crap_positions: List[int]) -> int:
    min_sum: int = 0
    for index in range(max(crap_positions)):
        sum_to_check: int = 0
        for position in crap_positions:
            sum_to_check += abs(position-index)
        if sum_to_check < min_sum or index == 0:
            min_sum = sum_to_check
    return min_sum


def get_fuel(position, index):
    diff: int = abs(position-index)
    return diff*(diff+1)/2


def calculate_best_position_part_two(crap_positions: List[int]) -> int:
    min_sum: int = 0
    for index in range(max(crap_positions)):
        sum_to_check: int = 0
        for position in crap_positions:
            sum_to_check += get_fuel(position, index)
        if sum_to_check < min_sum or index == 0:
            min_sum = sum_to_check
    return min_sum


with open(INPUT_FILE) as f:
    input_data: str = f.readline()
    crap_positions: List[int] = list(map(int, input_data.split(',')))
    print(f"part one: {calculate_best_position_part_one(crap_positions)}")
    print(f"part two: {calculate_best_position_part_two(crap_positions)}")


####### Tests #################################################################


def test_calculate_best_position_part_one():
    # arrange
    crap_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    expected_output_sum = 37

    # act
    result_sum = calculate_best_position_part_one(crap_positions)

    # assert
    assert result_sum == expected_output_sum


def test_calculate_best_position_part_two():
    # arrange
    crap_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    expected_output_sum = 168

    # act
    result_sum = calculate_best_position_part_two(crap_positions)

    # assert
    assert result_sum == expected_output_sum


@pytest.mark.parametrize("position, index, expected", [(1, 4, 6), (1, 5, 10), (16, 5, 66)])
def test_get_fuel(position, index, expected):
    # act
    result = get_fuel(position, index)

    # assert
    assert result == expected
