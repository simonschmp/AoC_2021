from typing import List
import pytest

INPUT_FILE = "input_1.txt"


def get_common_bit_of_index(values: List[str], index: int) -> str:
    bit_count: int = 0
    for value in values:
        if value[index] == "1":
            bit_count += 1
        else:
            bit_count -= 1
    if bit_count > 0:
        return "1"
    elif bit_count < 0:
        return "0"
    else:
        return "None"


def get_gamma_rate(values: List[str]) -> str:
    gamma_rate_bin: str = ""
    for index in range(len(values[0])):
        gamma_rate_bin = gamma_rate_bin + get_common_bit_of_index(values, index)
    return gamma_rate_bin


def get_power_consumption(values: List[str]) -> int:
    gamma_rate: str = get_gamma_rate(values)
    epsilon_rate: str = "".join('1' if x == '0' else '0' for x in gamma_rate)
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def get_oxygen_generator_rating(values: List[str]) -> str:
    for index in range(len(values[0])):
        common_bit: str = get_common_bit_of_index(values, index)
        if common_bit == "None":
            common_bit = "1"
        values = [value for value in values if not value[index] != common_bit]
        if len(values) == 1:
            break
    return values[0]


def get_co2_scrubber_rating(values: List[str]) -> str:
    for index in range(len(values[0])):
        common_bit: str = get_common_bit_of_index(values, index)
        if common_bit == "None" or common_bit == "1":
            common_bit = "0"
        else:
            common_bit = "1"
        values = [value for value in values if not value[index] != common_bit]
        if len(values) == 1:
            break
    return values[0]


def get_life_support_rating(values: List[str]) -> int:
    return int(get_oxygen_generator_rating(values), 2) * int(get_co2_scrubber_rating(values), 2)


with open(INPUT_FILE) as f:
    input_data: List[str] = [value for value in f.read().splitlines()]
    print(f"Part one: {get_power_consumption(input_data)}")
    print(f"Part two: {get_life_support_rating(input_data)}")


####### Tests #################################################################


def test_get_gamma_rate():
    # arrange
    test_values = ["00100", "11110", "10110", "10111", "10101",
                   "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    expected_result = "10110"

    # act
    result = get_gamma_rate(test_values)

    # assert
    assert result == expected_result


def test_get_power_consumption():
    # arrange
    test_values = ["00100", "11110", "10110", "10111", "10101",
                   "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    expected_result = 198

    # act
    result = get_power_consumption(test_values)

    # assert
    assert result == expected_result


def test_get_oxygen_generator_rating():
    # arrange
    test_values = ["00100", "11110", "10110", "10111", "10101",
                   "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    expected_result = "10111"

    # act
    result = get_oxygen_generator_rating(test_values)

    # assert
    assert result == expected_result


def test_get_co2_scrubber_rating():
    # arrange
    test_values = ["00100", "11110", "10110", "10111", "10101",
                   "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    expected_result = "01010"

    # act
    result = get_co2_scrubber_rating(test_values)

    # assert
    assert result == expected_result


def test_get_life_support_rating():
    # arrange
    test_values = ["00100", "11110", "10110", "10111", "10101",
                   "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    expected_result = 230

    # act
    result = get_life_support_rating(test_values)

    # assert
    assert result == expected_result
