from typing import List

INPUT_FILE = "input_1.txt"


def get_fish_list(fishes):
    fishes_cumulated = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in fishes:
        fishes_cumulated[fish] += 1
    return fishes_cumulated


def calculate_number_of_fishes(fishes, days):
    fishes_list = get_fish_list(fishes)
    for _ in range(days):
        fake_list = []
        fake_list.append(fishes_list[1])
        fake_list.append(fishes_list[2])
        fake_list.append(fishes_list[3])
        fake_list.append(fishes_list[4])
        fake_list.append(fishes_list[5])
        fake_list.append(fishes_list[6])
        fake_list.append(fishes_list[7]+fishes_list[0])
        fake_list.append(fishes_list[8])
        fake_list.append(fishes_list[0])
        fishes_list = fake_list
    return sum(fishes_list)


with open(INPUT_FILE) as f:
    input_data = f.readline()
    fish_list = list(map(int, input_data.split(',')))
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
