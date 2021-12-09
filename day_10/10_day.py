from typing import List, Optional, Dict
import pytest

INPUT_FILE = "input_1.txt"


def get_first_corrupted_char(line: str) -> Optional[str]:
    counterparts: Dict[str, str] = {"(": ")", "[": "]", "{": "}", "<": ">"}
    current_closing_chars: List[str] = []
    char: str
    for char in line:
        if char in counterparts.keys():
            current_closing_chars.append(counterparts[char])
        elif len(current_closing_chars) > 0:
            if char is current_closing_chars[-1]:
                if char in ")]}>":
                    current_closing_chars.pop()
            else:
                return char
    return None


def calculate_part_one(input_lines: List[str]) -> int:
    error_points: Dict[str, int] = {")": 3, "]": 57, "}": 1197, ">": 25137}
    result: int = 0
    line: str
    for line in input_lines:
        corrupted_char: Optional[str] = get_first_corrupted_char(line)
        if corrupted_char:
            result += error_points[corrupted_char]
    return result


def is_line_corrupted(line: str) -> bool:
    if get_first_corrupted_char(line):
        return True
    else:
        return False


def get_missing_chars(line: str) -> str:
    counterparts: Dict[str, str] = {"(": ")", "[": "]", "{": "}", "<": ">"}
    current_closing_chars: List[str] = []
    char: str
    for char in line:
        if char in counterparts.keys():
            current_closing_chars.append(counterparts[char])
        elif len(current_closing_chars) > 0:
            if char is current_closing_chars[-1]:
                if char in ")]}>":
                    current_closing_chars.pop()
    return "".join(current_closing_chars)[::-1]


def calculate_part_two(input_lines: List[str]) -> int:
    score_points: Dict[str, int] = {")": 1, "]": 2, "}": 3, ">": 4}
    solutions: List[int] = []
    line: str
    for line in input_lines:
        if not is_line_corrupted(line):
            solution_string: str = get_missing_chars(line)
            score: int = 0
            char: str
            for char in solution_string:
                score = score * 5
                score += score_points[char]
            solutions.append(score)
    solutions = sorted(solutions)
    mid_index: int = int((len(solutions) - 1)/2)
    return solutions[mid_index]


with open(INPUT_FILE) as f:
    input_lines: List[str] = [value.strip() for value in f.readlines()]
    print(f"part one: {calculate_part_one(input_lines)}")
    print(f"part two: {calculate_part_two(input_lines)}")


####### Tests #################################################################


@pytest.mark.parametrize("input, expected_output",
                         [("{([(<{}[<>[]}>{[]{[(<()>", "}"),
                          ("[[<[([]))<([[{}[[()]]]", ")"),
                          ("[{[{({}]{}}([{[{{{}}([]", "]"),
                          ("<{([([[(<>()){}]>(<<{{", ">")])
def test_get_first_corrupted_char(input, expected_output):
    # act
    result = get_first_corrupted_char(input)

    # assert
    assert result == expected_output


def test_calculate_part_one():
    # arrange
    input_lines = ["[({(<(())[]>[[{[]{<()<>>",
                   "[(()[<>])]({[<{<<[]>>(",
                   "{([(<{}[<>[]}>{[]{[(<()>",
                   "(((({<>}<{<{<>}{[]{[]{}",
                   "[[<[([]))<([[{}[[()]]]",
                   "[{[{({}]{}}([{[{{{}}([]",
                   "{<[[]]>}<{[{[{[]{()[[[]",
                   "[<(<(<(<{}))><([]([]()",
                   "<{([([[(<>()){}]>(<<{{",
                   "<{([{{}}[<[[[<>{}]]]>[]]"]
    expected_output = 26397

    # act
    result = calculate_part_one(input_lines)

    # assert
    assert result == expected_output


@pytest.mark.parametrize("input, expected_output",
                         [("[({(<(())[]>[[{[]{<()<>>", False),
                          ("[(()[<>])]({[<{<<[]>>(", False),
                          ("(((({<>}<{<{<>}{[]{[]{}", False),
                          ("[[<[([]))<([[{}[[()]]]", True),
                          ("[{[{({}]{}}([{[{{{}}([]", True),
                          ("<{([([[(<>()){}]>(<<{{", True),
                          ("{<[[]]>}<{[{[{[]{()[[[]", False)])
def test_is_line_corrupted(input, expected_output):
    # act
    result = is_line_corrupted(input)

    # assert
    assert result == expected_output


@pytest.mark.parametrize("input, expected_output",
                         [("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
                          ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
                          ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))"),
                          ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>")])
def test_get_missing_chars(input, expected_output):
    # act
    result = get_missing_chars(input)

    # assert
    assert result == expected_output


def test_calculate_part_two():
    # arrange
    input_lines = ["[({(<(())[]>[[{[]{<()<>>",
                   "[(()[<>])]({[<{<<[]>>(",
                   "{([(<{}[<>[]}>{[]{[(<()>",
                   "(((({<>}<{<{<>}{[]{[]{}",
                   "[[<[([]))<([[{}[[()]]]",
                   "[{[{({}]{}}([{[{{{}}([]",
                   "{<[[]]>}<{[{[{[]{()[[[]",
                   "[<(<(<(<{}))><([]([]()",
                   "<{([([[(<>()){}]>(<<{{",
                   "<{([{{}}[<[[[<>{}]]]>[]]"]
    expected_output = 288957

    # act
    result = calculate_part_two(input_lines)

    # assert
    assert result == expected_output
