from typing import List, Dict

INPUT_FILE = "input_1.txt"

Pairs = Dict[str, str]
CounterDict = Dict[str, int]


def parse_pairs(lines: List[str]) -> Pairs:
    pairs: Pairs = {}
    for line in lines:
        if "->" in line:
            a, b = line.split(" -> ")
            pairs[a] = a[0] + b + ">" + b + a[1]
    return pairs


def do_iterations(pairs: Pairs, input_str: str, iterations: int) -> CounterDict:
    letter_count: CounterDict = {}
    pairs_count: CounterDict = {}

    for key in pairs:
        pairs_count[key] = 0
        letter_count[pairs[key][1]] = 0

    empty_pairs_count: CounterDict = pairs_count.copy()

    for i in range(len(input_str)-1):
        pairs_count[input_str[i:i+2]] = 1

    for char in input_str:
        letter_count[char] += 1

    for _ in range(iterations):
        new_pairs_count: CounterDict = empty_pairs_count.copy()
        for key in pairs_count:
            new_pairs_count[pairs[key][:2]] += pairs_count[key]
            new_pairs_count[pairs[key][3:]] += pairs_count[key]
            letter_count[pairs[key][1]] += pairs_count[key]
        pairs_count = new_pairs_count.copy()

    return letter_count


def calculate_part_one(pairs: Pairs, input_str: str) -> int:
    letter_count: CounterDict = do_iterations(pairs, input_str, 10)
    return max(letter_count.values()) - min(letter_count.values())


def calculate_part_two(pairs: Pairs, input_str: str) -> int:
    letter_count: CounterDict = do_iterations(pairs, input_str, 40)
    return max(letter_count.values()) - min(letter_count.values())


with open(INPUT_FILE) as f:
    input_data: List[str] = [value.strip() for value in f.readlines()]
    input_str: str = input_data[0]
    pairs: Pairs = parse_pairs(input_data)
    print(f"part one: {calculate_part_one(pairs, input_str)}")
    print(f"part two: {calculate_part_two(pairs, input_str)}")


####### Tests #################################################################


def test_insert_pairs():
    # arrange
    input = "NNCB"
    pairs = {"CH": "CB>BH",
             "HH": "HN>NH",
             "CB": "CH>HB",
             "NH": "NC>CH",
             "HB": "HC>CB",
             "HC": "HB>BC",
             "HN": "HC>CN",
             "NN": "NC>CN",
             "BH": "BH>HH",
             "NC": "NB>BC",
             "NB": "NB>BB",
             "BN": "BB>BN",
             "BB": "BN>NB",
             "BC": "BB>BC",
             "CC": "CN>NC",
             "CN": "CC>CN"}
    expected_output = 1588

    # act
    result = calculate_part_one(pairs, input)

    # assert
    assert result == expected_output
