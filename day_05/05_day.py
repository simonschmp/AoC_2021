from typing import List

INPUT_FILE = "input_1.txt"


def parse_lines(lines_to_parse):
    lines_to_parse = lines_to_parse.split('\n')
    output_list = []
    for line in lines_to_parse:
        if line != '':
            line = line.split(" -> ")
            list_of_coordinates = []
            for coordinates in line:
                list_of_coordinates.append(list(map(int, coordinates.split(","))))
            output_list.append(list_of_coordinates)
    return output_list


def get_grid_size(lines):
    max_x = 0
    max_y = 0
    for line in lines:
        if line[0][1] > max_x:
            max_x = line[0][1]
        if line[1][1] > max_x:
            max_x = line[1][1]
        if line[0][0] > max_y:
            max_y = line[0][0]
        if line[1][0] > max_y:
            max_y = line[1][0]
    return max_x+1, max_y+1


def generate_grid(lines):
    x, y = get_grid_size(lines)
    grid = []
    for i in range(x):
        grid_y = []
        for j in range(y):
            grid_y.append(0)
        grid.append(grid_y)
    return grid


def print_grid(grid):
    print("Grid:")
    for line in grid:
        for num in line:
            if num == 0:
                print(".", end='')
            else:
                print(num, end='')
        print("\n")
    print("\n")


def fill_grid_straight_lines(lines, grid):
    for line in lines:
        if line[0][0] == line[1][0]:
            given_range = abs(line[0][1]-line[1][1])+1
            starting_number = min(line[0][1], line[1][1])
            for x in range(given_range):
                grid[x+starting_number][line[0][0]] += 1
        elif line[0][1] == line[1][1]:
            given_range = abs(line[0][0]-line[1][0])+1
            starting_number = min(line[0][0], line[1][0])
            for x in range(given_range):
                grid[line[0][1]][x+starting_number] += 1
    return grid


def fill_grid_diagonal_lines(lines, grid):
    for line in lines:
        if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
            first_direction = 1
            second_direction = 1
            if line[0][0] > line[1][0]:
                first_direction = -1
            if line[0][1] > line[1][1]:
                second_direction = -1
            given_range = abs(line[0][0]-line[1][0])+1
            for x in range(given_range):
                grid[line[0][1]+(second_direction*x)][line[0][0]+(first_direction*x)] += 1
    return grid


def count_larger_two_in_grid(grid):
    counter = 0
    for lines in grid:
        for value in lines:
            if value > 1:
                counter += 1
    return counter


def calculate_part_one(input_data):
    grid = generate_grid(input_data)
    grid = fill_grid_straight_lines(lines, grid)
    # print_grid(grid)
    return count_larger_two_in_grid(grid)


def calculate_part_two(input_data):
    grid = generate_grid(input_data)
    grid = fill_grid_straight_lines(lines, grid)
    grid = fill_grid_diagonal_lines(lines, grid)
    # print_grid(grid)
    return count_larger_two_in_grid(grid)


with open(INPUT_FILE) as f:
    input_data = f.read()
    lines = parse_lines(input_data)
    print(f"part one: {calculate_part_one(lines)}")
    print(f"part two: {calculate_part_two(lines)}")


####### Tests #################################################################


def test_parse_lines():
    # arrange
    lines_to_parse = "0,10 -> 5,10\n8,0 -> 0,8\n9,4 -> 3,4"
    expected_output = [[[0, 10], [5, 10]],
                       [[8, 0], [0, 8]],
                       [[9, 4], [3, 4]]]

    # act
    result = parse_lines(lines_to_parse)

    # assert
    assert result == expected_output


def test_get_grid_size():
    # arrange
    lines = [[[0, 8], [5, 8]],
             [[8, 0], [8, 4]],
             [[9, 4], [3, 4]]]
    expected_x = 9
    expected_y = 10

    # act
    result_x, result_y = get_grid_size(lines)

    # assert
    assert result_x == expected_x
    assert result_y == expected_y


def test_get_grid_size_2():
    # arrange
    lines = [[[0, 3], [1, 3]],
             [[4, 0], [4, 2]],
             [[1, 3], [2, 3]]]
    expected_x = 4
    expected_y = 5

    # act
    result_x, result_y = get_grid_size(lines)

    # assert
    assert result_x == expected_x
    assert result_y == expected_y


def test_generate_grid():
    # arrange
    lines = [[[0, 3], [1, 3]],
             [[4, 0], [4, 2]],
             [[1, 3], [2, 3]]]
    expected_grid = [[0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0]]

    # act
    result = generate_grid(lines)

    # assert
    assert result == expected_grid


def test_fill_grid():
    # arrange
    lines = [[[0, 3], [1, 3]],
             [[4, 0], [4, 2]],
             [[1, 3], [2, 3]]]

    grid = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

    expected_grid = [[0, 0, 0, 0, 1],
                     [0, 0, 0, 0, 1],
                     [0, 0, 0, 0, 1],
                     [1, 2, 1, 0, 0]]

    # act
    result = fill_grid_straight_lines(lines, grid)

    # assert
    assert result == expected_grid


def test_fill_grid_with_diagonals():
    # arrange
    lines = [[[0, 3], [1, 3]],
             [[4, 0], [4, 2]],
             [[1, 1], [3, 3]],
             [[3, 1], [1, 3]],
             [[0, 2], [2, 0]],
             [[0, 3], [3, 0]],
             [[1, 3], [2, 3]]]

    grid = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

    expected_grid = [[0, 0, 1, 1, 1],
                     [0, 2, 1, 1, 1],
                     [1, 1, 2, 0, 1],
                     [2, 3, 1, 1, 0]]

    # act
    result_a = fill_grid_straight_lines(lines, grid)
    result_b = fill_grid_diagonal_lines(lines, result_a)

    # assert
    assert result_b == expected_grid


def test_count_larger_two_in_grid():
    # arrange
    grid = [[0, 0, 0, 1],
            [0, 0, 0, 2],
            [1, 2, 0, 1],
            [0, 0, 0, 0],
            [1, 2, 1, 0]]
    expected_result = 3

    # act
    result = count_larger_two_in_grid(grid)

    # assert
    assert result == expected_result
