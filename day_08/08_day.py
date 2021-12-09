from typing import List, Dict

INPUT_FILE = "input_1.txt"


def get_inputs(line: str) -> List[str]:
    return line[:line.find("|")].strip().split(" ")


def get_outputs(line: str) -> List[str]:
    return line[line.find("|")+1:].strip().split(" ")


def calculate_part_one(input_data: List[str]) -> int:
    counter: int = 0
    line: str
    output: str
    for line in input_data:
        outputs: List[str] = get_outputs(line)
        for output in outputs:
            if len(output) < 5 or len(output) > 6:
                counter += 1
    return counter


def get_decoded_numbers(line) -> Dict[str, List[str]]:
    letter_dict: Dict[str, List[str]] = {}
    inputs: List[str] = get_inputs(line)
    inp: str
    for inp in inputs:
        sorted_inp: List[str] = sorted(inp)
        if len(inp) == 2:
            letter_dict["1"] = sorted_inp
        if len(inp) == 3:
            letter_dict["7"] = sorted_inp
        if len(inp) == 4:
            letter_dict["4"] = sorted_inp
        if len(inp) == 7:
            letter_dict["8"] = sorted_inp

    # figure out 6
    for inp in inputs:
        if len(inp) == 6:
            sorted_inp = sorted(inp)
            if not set(letter_dict["1"]).issubset(sorted_inp):
                letter_dict["6"] = sorted_inp

    # figure out 0,9,2,3,5
    for inp in inputs:
        sorted_inp = sorted(inp)
        if len(inp) == 6:
            if set(letter_dict["4"]).issubset(sorted_inp):
                letter_dict["9"] = sorted_inp
            elif letter_dict["6"] != sorted_inp:
                letter_dict["0"] = sorted_inp
        if len(inp) == 5:
            if set(letter_dict["1"]).issubset(sorted_inp):
                letter_dict["3"] = sorted_inp
            elif set(sorted_inp).issubset(letter_dict["6"]):
                letter_dict["5"] = sorted_inp
            else:
                letter_dict["2"] = sorted_inp
    return letter_dict


def decode_line(letter_dict: Dict[str, List[str]], line: str) -> int:
    outputs: List[str] = get_outputs(line)
    number: str = ''
    output: str
    for output in outputs:
        for key in letter_dict:
            if sorted(output) == letter_dict[key]:
                number += key
    return int(number)


def calculate_part_two(input_data: List[str]) -> int:
    result: int = 0
    for line in input_data:
        decoded_numbers: Dict[str, List[str]] = get_decoded_numbers(line)
        result += decode_line(decoded_numbers, line)
    return result


with open(INPUT_FILE) as f:
    input_data: List[str] = [x.strip() for x in f.readlines()]
    print(f"part one: {calculate_part_one(input_data)}")
    print(f"part two: {calculate_part_two(input_data)}")


####### Tests #################################################################


def test_get_inputs():
    # arrange
    input_str = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"
    expected_input = ["be", "cfbegad", "cbdgef", "fgaecd",
                      "cgeb", "fdcge", "agebfd", "fecdb", "fabcd", "edb"]

    # act
    inputs = get_inputs(input_str)

    # assert
    assert inputs == expected_input


def test_get_outputs():
    # arrange
    input_str = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"
    expected_output = ["fdgacbe", "cefdb", "cefbgd", "gcbe"]

    # act
    outputs = get_outputs(input_str)

    # assert
    assert outputs == expected_output


def test_calculate_part_one():
    # arrange
    input = ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
             "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
             "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
             "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
             "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
             "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
             "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
             "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
             "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
             "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"]
    expected_result = 26

    # act
    result = calculate_part_one(input)

    # assert
    assert result == expected_result


def test_get_decoded_numbers():
    # arrange
    input = "dbcfeag cgaed fe bfgad aefcdb efa efgda gcef dcaebg dfeagc | fae cfge fae baefdc"
    expected_result = {'0': ['a', 'b', 'c', 'd', 'e', 'f'],
                       '1': ['e', 'f'],
                       '2': ['a', 'b', 'd', 'f', 'g'],
                       '3': ['a', 'd', 'e', 'f', 'g'],
                       '4': ['c', 'e', 'f', 'g'],
                       '5': ['a', 'c', 'd', 'e', 'g'],
                       '6': ['a', 'b', 'c', 'd', 'e', 'g'],
                       '7': ['a', 'e', 'f'],
                       '8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                       '9': ['a', 'c', 'd', 'e', 'f', 'g']}

    # act
    result = get_decoded_numbers(input)

    # assert
    assert result == expected_result


def test_decoded_line():
    # arrange
    input_line = "unimportant part | dbcfeag cgaed fe bfgad aefcdb efa efgda gcef dcaebg dfeagc"
    input_dict = {'0': ['a', 'b', 'c', 'd', 'e', 'f'],
                  '1': ['e', 'f'],
                  '2': ['a', 'b', 'd', 'f', 'g'],
                  '3': ['a', 'd', 'e', 'f', 'g'],
                  '4': ['c', 'e', 'f', 'g'],
                  '5': ['a', 'c', 'd', 'e', 'g'],
                  '6': ['a', 'b', 'c', 'd', 'e', 'g'],
                  '7': ['a', 'e', 'f'],
                  '8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                  '9': ['a', 'c', 'd', 'e', 'f', 'g']}
    expected_result = 8512073469

    # act
    result = decode_line(input_dict, input_line)

    # assert
    assert result == expected_result


def test_calculate_part_two():
    # arrange
    input = ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
             "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
             "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
             "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
             "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
             "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
             "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
             "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
             "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
             "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"]
    expected_result = 61229

    # act
    result = calculate_part_two(input)

    # assert
    assert result == expected_result
