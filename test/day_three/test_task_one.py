from day_three.task_one import get_input_from_txt_file, match_mul_and_numbers_from_string, \
    match_only_numbers_from_string, multiply_tuples_and_return_sum, main, get_matching_pairs_and_multiplication_sums


def test_input_read_from_txt_file():
    actual = get_input_from_txt_file()

    assert isinstance(actual, str)
    assert actual[-8:] == "from()'*"


def test_return_mul_and_numbers():
    input_string = "mul(1,2)"

    actual = match_mul_and_numbers_from_string(input_string)
    expected = ['mul(1,2)']
    assert actual == expected

def test_return_mul_and_three_digit_numbers():
    input_string = "mul(123,234)"

    actual = match_mul_and_numbers_from_string(input_string)
    expected = ['mul(123,234)']
    assert actual == expected


def test_return_mul_and_number_match_multiple():
    input_string = "mul(1,2)////123!@£$£mul(3,4)"

    actual = match_mul_and_numbers_from_string(input_string)
    expected = ["mul(1,2)", "mul(3,4)"]
    assert actual == expected


def test_return_mul_and_number_match_on_real_string_frag():
    input_string = "from()why()?mul(603,692)({select()}] )]"

    actual = match_mul_and_numbers_from_string(input_string)
    expected = ["mul(603,692)"]
    assert actual == expected

# test the below function more thoroughly as it is the production function

def test_return_numbers_match():
    input_string = "mul(1,2)"

    actual = match_only_numbers_from_string(input_string)
    expected = [(1, 2)]
    assert actual == expected


def test_return_three_digit_numbers_match():
    input_string = "mul(123,234)"

    actual = match_only_numbers_from_string(input_string)
    expected = [(123, 234)]
    assert actual == expected

def test_does_not_return_four_digit_numbers_match():
    input_string = "mul(1234,2345)"

    actual = match_only_numbers_from_string(input_string)
    expected = []
    assert actual == expected

def test_does_not_return_no_numbers_match():
    input_string = "mul(,)"

    actual = match_only_numbers_from_string(input_string)
    expected = []
    assert actual == expected


def test_return_three_digit_numbers_match_multiple():
    input_string = "mul(1,2)////123!@£$£mul(3,4)"

    actual = match_only_numbers_from_string(input_string)
    expected = [(1, 2), (3, 4)]
    assert actual == expected

def test_return_numbers_match_on_separate_lines():
    input_string = "mul(1,2)\n123\nmul(3,4)"

    actual = match_only_numbers_from_string(input_string)
    expected = [(1, 2), (3, 4)]
    assert actual == expected

def test_return_numbers_match_on_real_string_frag():
    input_string = "from()why()?mul(603,692)({select()}] )]"

    actual = match_only_numbers_from_string(input_string)
    expected = [(603, 692)]
    assert actual == expected


def test_multiply_tuples_and_sum_results():
    input_string = [(1, 2), (3, 4)]

    actual = multiply_tuples_and_return_sum(input_string)
    expected = 14
    assert actual == expected

def test_test_match_numbers_from_string_and_return_multiplied_pair_sum():
    input_string = "mul(1,2)////123!@£$£mul(3,4)"

    actual = get_matching_pairs_and_multiplication_sums(input_string)
    expected = 14
    assert actual == expected

