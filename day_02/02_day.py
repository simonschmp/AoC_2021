from typing import List

INPUT_FILE = "02_day_input_1.txt"


def get_position(values: List[str]) -> int:
    horizontal_position = 0
    depth_position = 0

    for value in values:
        number: int = int(''.join(filter(str.isdigit, value)))
        if "forward" in value:
            horizontal_position += number
        if "down" in value:
            depth_position += number
        if "up" in value:
            depth_position -= number

    return horizontal_position * depth_position


def get_position_with_aim(values: List[str]) -> int:
    horizontal_position: int = 0
    depth_position: int = 0
    aim: int = 0

    for value in values:
        number: int = int(''.join(filter(str.isdigit, value)))
        if "forward" in value:
            horizontal_position += number
            depth_position += (number * aim)
        if "down" in value:
            aim += number
        if "up" in value:
            aim -= number

    return horizontal_position * depth_position


with open(INPUT_FILE) as f:
    input_data: List[str] = [value for value in f.read().splitlines()]
    print(f"Part one: {get_position(input_data)}")
    print(f"Part two: {get_position_with_aim(input_data)}")


####### Tests #################################################################


def test_get_position():
    # arrange
    test_values = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    expected_result = 150

    # act
    result = get_position(test_values)

    # assert
    assert result == expected_result


def test_get_position_with_aim():
    # arrange
    test_values = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    expected_result = 900

    # act
    result = get_position_with_aim(test_values)

    # assert
    assert result == expected_result
