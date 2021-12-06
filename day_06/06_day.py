from typing import List

INPUT_FILE = "input_1.txt"


def get_fish_groups(fishes: List[int]) -> List[int]:
    fishes_cumulated: List[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in fishes:
        fishes_cumulated[fish] += 1
    return fishes_cumulated


def calculate_number_of_fishes(fishes: List[int], days: int) -> int:
    fish_groups: List[int] = get_fish_groups(fishes)
    for _ in range(days):
        fish_groups = fish_groups[1:] + fish_groups[:1]
        fish_groups[6] += fish_groups[8]
    return sum(fish_groups)


with open(INPUT_FILE) as f:
    input_data: str = f.readline()
    fish_list: List[int] = list(map(int, input_data.split(',')))
    print(f"part one: {calculate_number_of_fishes(fish_list, 80)}")
    print(f"part two: {calculate_number_of_fishes(fish_list, 256)}")


####### Tests #################################################################


def test_calculate_number_of_fishes_80_days():
    # arrange
    fishes = [3, 4, 3, 1, 2]
    days = 80
    expected_output = 5934

    # act
    result = calculate_number_of_fishes(fishes, days)

    # assert
    assert result == expected_output


def test_calculate_number_of_fishes_256_days():
    # arrange
    fishes = [3, 4, 3, 1, 2]
    days = 256
    expected_output = 26984457539

    # act
    result = calculate_number_of_fishes(fishes, days)

    # assert
    assert result == expected_output
