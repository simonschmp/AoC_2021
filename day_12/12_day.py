INPUT_FILE = "input_1.txt"


def parse_ways(input):
    ways = {}
    for line in input:
        a, b = line.split("-")
        if a in ways:
            ways[a].append(b)
        else:
            ways[a] = [b]
        if b in ways:
            ways[b].append(a)
        else:
            ways[b] = [a]
    return ways


def walk_ways(ways, current_points):
    cave_ways = []
    if current_points[-1] != 'end':
        for point in ways[current_points[-1]]:
            if point.isupper() or point not in current_points:
                cave_ways.extend(walk_ways(ways, current_points + [point]))
    else:
        return [current_points]
    return cave_ways


def walk_ways_2(ways, current_points):
    cave_ways = []
    if current_points[-1] != 'end':
        for point in ways[current_points[-1]]:
            if point.isupper() or point not in current_points:
                cave_ways.extend(walk_ways_2(ways, current_points + [point]))
            elif point.islower() and point in current_points and point != "start" and point != "end":
                small_value_already_twice = False
                for value in current_points:
                    if value.islower():
                        if current_points.count(value) > 1:
                            small_value_already_twice = True
                if not small_value_already_twice:
                    cave_ways.extend(walk_ways_2(ways, current_points + [point]))
    else:
        return [current_points]
    return cave_ways


def calculate_part_one(input_data):
    ways = parse_ways(input_data)
    paths = walk_ways(ways, ['start'])
    return len(paths)


def calculate_part_two(input_data):
    ways = parse_ways(input_data)
    paths = walk_ways_2(ways, ['start'])
    return len(paths)


with open(INPUT_FILE) as f:
    input_data = [value.strip() for value in f.readlines()]
    print(f"part one: {calculate_part_one(input_data)}")
    print(f"part two: {calculate_part_two(input_data)}")


####### Tests #################################################################


def test_calculate_part_one_1():
    # arrange
    input_lines = ["start-A",
                   "start-b",
                   "A-c",
                   "A-b",
                   "b-d",
                   "A-end",
                   "b-end"]
    expected_output = 10

    # act
    result = calculate_part_one(input_lines)

    # assert
    assert result == expected_output


def test_calculate_part_one_2():
    # arrange
    input_lines = ["dc-end",
                   "HN-start",
                   "start-kj",
                   "dc-start",
                   "dc-HN",
                   "LN-dc",
                   "HN-end",
                   "kj-sa",
                   "kj-HN",
                   "kj-dc"]
    expected_output = 19

    # act
    result = calculate_part_one(input_lines)

    # assert
    assert result == expected_output


def test_calculate_part_two():
    # arrange
    input_lines = ["dc-end",
                   "HN-start",
                   "start-kj",
                   "dc-start",
                   "dc-HN",
                   "LN-dc",
                   "HN-end",
                   "kj-sa",
                   "kj-HN",
                   "kj-dc"]
    expected_output = 103

    # act
    result = calculate_part_two(input_lines)

    # assert
    assert result == expected_output
