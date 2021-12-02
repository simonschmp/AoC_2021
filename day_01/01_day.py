INPUT_FILE = "01_day_input_1.txt"

def count_increases(values):
    number_of_increases = 0
    previous_value = None
    for value in values:
        if previous_value != None and previous_value < value:
            number_of_increases += 1
        previous_value = value
    return number_of_increases


def count_sum_of_tripples(values):
    commulated_data = []
    for idx in range(len(values)-2):
        commulated_number = values[idx] + values[idx+1] + values[idx+2]
        commulated_data.append(commulated_number)
    return count_increases(commulated_data)


with open(INPUT_FILE) as f:
    input_data = [int(value) for value in f.read().splitlines()]
    print(count_increases(input_data))
    print(count_sum_of_tripples(input_data))


####### Tests #################################################################

def test_count_increases():
    # arrange
    test_values = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected_result = 7

    # act
    result  = count_increases(test_values)

    # assert
    assert result == expected_result


def test_count_sum_of_tripples():
    # arrange
    test_values = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected_result = 5

    # act
    result = count_sum_of_tripples(test_values)

    # assert
    assert result == expected_result
