from unittest.mock import patch

import pandas

from day_4.task_two import iterate_through_lines_and_count_mas_in_x_shape
from src.day_4.task_one import get_table_from_input, find_all_x_in_line, \
    iterate_through_lines_and_count_xmas


def test_get_table_from_input() -> None:
    actual = get_table_from_input()

    assert isinstance(actual, pandas.DataFrame)
    assert actual.shape == (140, 140)
    first_row = actual.iloc[0]
    first_nine_items_from_first_row = list(first_row[:9])
    assert first_nine_items_from_first_row == ['M', 'S', 'S', 'M', 'M', 'S', 'X', 'S', 'M']


def test_dataframe_creation() -> None:
    single_characters_into_lists = [['M', 'S', 'S'], ['M', 'S', 'S'], ['M', 'S', 'S']]
    actual = pandas.DataFrame(single_characters_into_lists)

    assert actual.shape == (3, 3)
    assert actual.iloc[0, 0] == 'M'
    assert actual.iloc[1, 1] == 'S'
    assert actual.iloc[2, 2] == 'S'


# test find all x

def test_find_all_x() -> None:
    line = pandas.Series(['M', 'S', 'X', 'S', 'M', 'X'])
    actual = find_all_x_in_line(line)

    assert actual == [2, 5]


def test_find_all_x_no_x() -> None:
    line = pandas.Series(['M', 'S', 'S', 'M'])
    actual = find_all_x_in_line(line)

    assert actual == []


# test iterate through lines

@patch('src.day_4.task_one.get_number_of_xmas_at_position')
@patch('src.day_4.task_one.find_all_x_in_line')
def test_iterate_through_lines_calls_correct_functions(find_x_mock,
                                                       get_number_xmas_mock
                                                       ) -> None:
    find_x_mock.return_value = [2]
    get_number_xmas_mock.return_value = 1

    table = pandas.DataFrame([['M', 'S', 'S', 'M', 'M', 'S', 'X', 'S', 'M'],
                              ['M', 'S', 'S', 'M', 'M', 'S', 'X', 'S', 'M']]
                             )
    actual = iterate_through_lines_and_count_xmas(table)

    assert actual == 2
    assert find_x_mock.call_count == 2
    assert get_number_xmas_mock.call_count == 2


@patch('src.day_4.task_one.get_number_of_xmas_at_position')
@patch('src.day_4.task_one.find_all_x_in_line')
def test_iterate_through_lines_calls_correct_functions_multiple_x_per_line(find_x_mock,
                                                                           get_number_xmas_mock
                                                                           ) -> None:
    find_x_mock.return_value = [2, 3, 4]
    get_number_xmas_mock.return_value = 1

    table = pandas.DataFrame([['M', 'S', 'S', 'M', 'M', 'S', 'X', 'S', 'M'],
                              ['M', 'S', 'S', 'M', 'M', 'S', 'X', 'S', 'M']]
                             )
    actual = iterate_through_lines_and_count_xmas(table)

    assert actual == 6
    assert find_x_mock.call_count == 2
    assert get_number_xmas_mock.call_count == 6