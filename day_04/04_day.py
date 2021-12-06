from typing import List
from copy import deepcopy

INPUT_FILE = "input_1.txt"
FIELD_SIZE = 5


def read_in_field(input_field):
    lines = input_field.splitlines()
    field = []
    for line in lines:
        field.append(list(map(int, line.split())))
    return field


def check_bingo(draw_order, field):
    num_of_iterations = 0
    for num in draw_order:
        for i in range(FIELD_SIZE):
            for j in range(FIELD_SIZE):
                if field[i][j] == num:
                    field[i][j] = None
        num_of_iterations += 1
        if num_of_iterations > 4:
            for row in field:
                row_count = sum(x is None for x in row)
                if row_count == 5:
                    return num_of_iterations, num, field
            for i in range(FIELD_SIZE):
                if field[0][i] == field[1][i] == field[2][i] == field[3][i] == field[4][i] == None:
                    return num_of_iterations, num, field
    return num_of_iterations, None, field


def determine_fastest_win(draw_order, fields):
    results = []
    for field in fields:
        result, a, b = check_bingo(draw_order, field)
        results.append(result)
    return results.index(min(results))


def determine_slowest_win(draw_order, fields):
    results = []
    for field in fields:
        result, a, b = check_bingo(draw_order, field)
        results.append(result)
    return results.index(max(results))


def calculate_final_result(draw_order, field):
    _, winning_number, final_field = check_bingo(draw_order, field)
    total_of_available_numbers = 0
    for i in range(FIELD_SIZE):
        for j in range(FIELD_SIZE):
            if final_field[i][j] != None:
                total_of_available_numbers += final_field[i][j]
    return total_of_available_numbers * winning_number


def calculate_part_one(draw_order, fields_1):
    copy_fields = deepcopy(fields_1)
    fields = deepcopy(fields_1)
    winning_field = determine_fastest_win(draw_order, fields)
    print(copy_fields[winning_field])
    print(fields[winning_field])
    return calculate_final_result(draw_order, copy_fields[winning_field])


def calculate_part_two(draw_order, fields_1):
    copy_fields = deepcopy(fields_1)
    fields = deepcopy(fields_1)
    winning_field = determine_slowest_win(draw_order, fields)
    print(copy_fields[winning_field])
    print(fields[winning_field])
    return calculate_final_result(draw_order, copy_fields[winning_field])


with open(INPUT_FILE) as f:
    input_data = f.read()
    first_row = input_data.splitlines()[0]
    draw_order = list(map(int, first_row.split(',')))
    input_data = input_data[input_data.find("\n\n")+2:]
    input_data = input_data.split("\n\n")
    fields = []
    for field in input_data:
        fields.append(read_in_field(field))
    print(f"part one: {calculate_part_one(draw_order, fields)}")
    print(f"part two: {calculate_part_two(draw_order, fields)}")


####### Tests #################################################################


def test_read_in_field():
    # arrange
    input_field = "22 13 17 11  0\n8  2 23  4 24\n21  9 14 16  7\n6 10  3 18  5\n1 12 20 15 19"
    expected_field = [[22, 13, 17, 11, 0, ],
                      [8, 2, 23, 4, 24, ],
                      [21, 9, 14, 16, 7, ],
                      [6, 10, 3, 18, 5, ],
                      [1, 12, 20, 15, 19]]

    # act
    result = read_in_field(input_field)

    # assert
    assert result == expected_field


def test_check_bingo_row():
    # arrange
    test_input = [8, 2, 23, 4, 0, 24, 7]
    test_field = [[22, 13, 17, 11, 0],
                  [8, 2, 23, 4, 24],
                  [21, 9, 14, 16, 7],
                  [6, 10, 3, 18, 5],
                  [1, 12, 20, 15, 19]]
    expected_num_of_iterations = 6
    expected_winning_num = 24

    # act
    num_of_iterations, winning_num, field = check_bingo(test_input, test_field)

    # assert
    assert num_of_iterations == expected_num_of_iterations
    assert expected_winning_num == winning_num


def test_check_bingo_column():
    # arrange
    test_input = [13, 2, 9, 10, 99, 12, 98]
    test_field = [[22, 13, 17, 11, 0],
                  [8, 2, 23, 4, 24],
                  [21, 9, 14, 16, 7],
                  [6, 10, 3, 18, 5],
                  [1, 12, 20, 15, 19]]
    expected_num_of_iterations = 6
    expected_winning_num = 12

    # act
    num_of_iterations, winning_num, field = check_bingo(test_input, test_field)

    # assert
    assert num_of_iterations == expected_num_of_iterations
    assert expected_winning_num == winning_num


def test_determine_fastest_win():
    # arrange
    draw_order = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24,
                  10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    test_fields = [[[22, 13, 17, 11, 0],
                   [8, 2, 23, 4, 24],
                   [21, 9, 14, 16, 7],
                   [6, 10, 3, 18, 5],
                   [1, 12, 20, 15, 19]],

                   [[3, 15, 0, 2, 22],
                   [9, 18, 13, 17, 5],
                   [19, 8, 7, 25, 23],
                   [20, 11, 10, 24, 4],
                   [14, 21, 16, 12, 6]],

                   [[14, 21, 17, 24, 4],
                   [10, 16, 15, 9, 19],
                   [18, 8, 23, 26, 20],
                   [22, 11, 13, 6, 5],
                   [2, 0, 12, 3, 7]]]
    expected_result = 2

    # act
    field_with_fastest_win = determine_fastest_win(draw_order, test_fields)

    # assert
    assert field_with_fastest_win == expected_result


def test_calculate_final_result():
    # arrange
    draw_order = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24,
                  10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    test_field = [[14, 21, 17, 24, 4],
                  [10, 16, 15, 9, 19],
                  [18, 8, 23, 26, 20],
                  [22, 11, 13, 6, 5],
                  [2, 0, 12, 3, 7]]
    expected_result = 4512

    # act
    result = calculate_final_result(draw_order, test_field)

    # assert
    assert result == expected_result


def test_calculate_part_one():
    # arrange
    draw_order = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24,
                  10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    test_fields = [[[22, 13, 17, 11, 0],
                   [8, 2, 23, 4, 24],
                   [21, 9, 14, 16, 7],
                   [6, 10, 3, 18, 5],
                   [1, 12, 20, 15, 19]],

                   [[3, 15, 0, 2, 22],
                   [9, 18, 13, 17, 5],
                   [19, 8, 7, 25, 23],
                   [20, 11, 10, 24, 4],
                   [14, 21, 16, 12, 6]],

                   [[14, 21, 17, 24, 4],
                   [10, 16, 15, 9, 19],
                   [18, 8, 23, 26, 20],
                   [22, 11, 13, 6, 5],
                   [2, 0, 12, 3, 7]]]
    expected_result = 4512

    # act
    result = calculate_part_one(draw_order, test_fields)

    # assert
    assert result == expected_result


def test_determine_slowest_win():
    # arrange
    draw_order = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24,
                  10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    test_fields = [[[22, 13, 17, 11, 0],
                   [8, 2, 23, 4, 24],
                   [21, 9, 14, 16, 7],
                   [6, 10, 3, 18, 5],
                   [1, 12, 20, 15, 19]],

                   [[3, 15, 0, 2, 22],
                   [9, 18, 13, 17, 5],
                   [19, 8, 7, 25, 23],
                   [20, 11, 10, 24, 4],
                   [14, 21, 16, 12, 6]],

                   [[14, 21, 17, 24, 4],
                   [10, 16, 15, 9, 19],
                   [18, 8, 23, 26, 20],
                   [22, 11, 13, 6, 5],
                   [2, 0, 12, 3, 7]]]
    expected_result = 1

    # act
    field_with_fastest_win = determine_slowest_win(draw_order, test_fields)

    # assert
    assert field_with_fastest_win == expected_result


def test_calculate_part_two():
    # arrange
    draw_order = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24,
                  10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    test_fields = [[[22, 13, 17, 11, 0],
                   [8, 2, 23, 4, 24],
                   [21, 9, 14, 16, 7],
                   [6, 10, 3, 18, 5],
                   [1, 12, 20, 15, 19]],

                   [[3, 15, 0, 2, 22],
                   [9, 18, 13, 17, 5],
                   [19, 8, 7, 25, 23],
                   [20, 11, 10, 24, 4],
                   [14, 21, 16, 12, 6]],

                   [[14, 21, 17, 24, 4],
                   [10, 16, 15, 9, 19],
                   [18, 8, 23, 26, 20],
                   [22, 11, 13, 6, 5],
                   [2, 0, 12, 3, 7]]]
    expected_result = 1924

    # act
    result = calculate_part_two(draw_order, test_fields)

    # assert
    assert result == expected_result
