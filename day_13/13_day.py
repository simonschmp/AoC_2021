from typing import List, Tuple

INPUT_FILE = "input_1.txt"

Points = List[Tuple[int, int]]
Folds = List[Tuple[str, int]]
Field = List[List[str]]


def parse_points(lines: List[str]) -> Points:
    points: Points = []
    for line in lines:
        if "," in line:
            a, b = line.split(",")
            points.append((int(a), int(b)))
    return points


def parse_folds(lines: List[str]) -> Folds:
    folds = []
    for line in lines:
        if "=" in line:
            relevant_text = line.split("along ", 1)[1]
            a, b = relevant_text.split("=")
            folds.append((a, int(b)))
    return folds


def calculate_field_size(points: Points) -> Tuple[int, int]:
    max_x: int = 0
    max_y: int = 0
    for point in points:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
    return (max_x, max_y)


def create_field(points: Points) -> Field:
    field_size: Tuple[int, int] = calculate_field_size(points)
    field: Field = []
    for _ in range(field_size[1]+1):
        row: List[str] = []
        field.append(row)
        for _ in range(field_size[0]+1):
            row.append(".")
    return field


def print_field(field: Field):
    for row in field:
        string_to_print: str = ''
        for col in row:
            string_to_print += col
        print(string_to_print)


def populate_field(field: Field, points: Points) -> Field:
    for point in points:
        field[point[1]][point[0]] = "#"
    return field


def count_hashes(field: Field) -> int:
    counter: int = 0
    for row in field:
        for col in row:
            if col == "#":
                counter += 1
    return counter


def fold_y(field: Field, fold_line: int) -> Field:
    fold_index: int = fold_line
    for row in field[fold_line:]:
        for col_index, col in enumerate(row):
            if col == "#":
                field[fold_index][col_index] = "#"
        fold_index -= 1
    return field[:fold_line]


def fold_x(field: Field, fold_line: int) -> Field:
    for row_index, row in enumerate(field):
        fold_index = fold_line
        for col in row[fold_line:]:
            if col == "#":
                field[row_index][fold_index] = "#"
            fold_index -= 1
    new_field: Field = []
    for row in field:
        new_field.append(row[:fold_line])
    return new_field


def fold(field: Field, fold: Tuple[str, int]) -> Field:
    fold_direction: str = fold[0]
    fold_line: int = fold[1]
    if fold_direction == "y":
        field = fold_y(field, fold_line)
    else:
        field = fold_x(field, fold_line)
    return field


def calculate_part_one(points: Points, folds: Folds) -> int:
    field: Field = create_field(points)
    field = populate_field(field, points)
    field = fold(field, folds[0])
    return count_hashes(field)


def calculate_part_two(points: Points, folds: Folds) -> int:
    field: Field = create_field(points)
    field = populate_field(field, points)
    for fold_line in folds:
        field = fold(field, fold_line)
    # this prints the solution
    print_field(field)
    return count_hashes(field)


with open(INPUT_FILE) as f:
    input_data: List[str] = [value.strip() for value in f.readlines()]
    points = parse_points(input_data)
    folds = parse_folds(input_data)
    print(f"part one: {calculate_part_one(points, folds)}")
    print(f"part two: {calculate_part_two(points, folds)}")


####### Tests #################################################################


def test_calculate_part_one():
    # arrange
    points = [[6, 10],
              [0, 14],
              [9, 10],
              [0, 3],
              [10, 4],
              [4, 11],
              [6, 0],
              [6, 12],
              [4, 1],
              [0, 13],
              [10, 12],
              [3, 4],
              [3, 0],
              [8, 4],
              [1, 10],
              [2, 14],
              [8, 10],
              [9, 0]]
    folds = [["y", 7], ["x", 5]]
    expected_output = 17

    # act
    result = calculate_part_one(points, folds)

    # assert
    assert result == expected_output
