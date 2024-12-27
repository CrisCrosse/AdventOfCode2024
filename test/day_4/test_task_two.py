from unittest.mock import patch

import pandas

from day_4.task_two import iterate_through_lines_and_count_mas_in_x_shape, find_all_a_in_row, function_to_mock, \
    get_upper_left_to_lower_right_slice, upper_left_to_lower_right_mas, get_lower_left_to_upper_right_slice, \
    is_mas_in_x_shape_at_location


def test_iterate_nd_count_mas_in_x_shape_happy_path() -> None:
    table = pandas.DataFrame([
        ['M', 'S', 'S'],
        ['M', 'A', 'A'],
        ['M', 'S', 'S']
    ])
    expected = 1
    actual = iterate_through_lines_and_count_mas_in_x_shape(table)
    assert actual == expected


# @patch('src.day_4.task_two.find_all_a_in_row')
# def test_iterate_nd_count_mas_in_x_shape_calls_correct_function(
#                                                                    find_all_a_mock
#                                                                  ) -> None:
#
#     # is_mas_mock.return_value = True
#     find_all_a_mock.return_value = []
#     table = pandas.DataFrame([
#         ['M', 'S', 'S'],
#         ['M', 'A', 'A'],
#         ['M', 'S', 'S']
#     ])
#     actual = iterate_through_lines_and_count_mas_in_x_shape(table)
#
#     assert find_all_a_mock.call_count == 3
#     # assert is_mas_mock.call_count == 2
#
#
# @patch('src.day_4.task_two.function_to_mock')
# def test_function_to_mock(function_mock) -> None:
#     function_mock.return_value = True
#     actual = function_to_mock()
#     assert actual == True

def test_find_all_a_in_row_happy_path() -> None:
    row = pandas.Series(['M', 'S', 'A', 'S', 'A', 'M'])
    expected = [2, 4]
    actual = find_all_a_in_row(row)
    assert actual == expected

def test_find_all_a_in_row_unhappy_path() -> None:
    row = pandas.Series(['M', 'S', 'S', 'S', 'S', 'M'])
    expected = []
    actual = find_all_a_in_row(row)
    assert actual == expected


def test_get_upper_left_to_lower_right_slice() -> None:
    table = pandas.DataFrame([
        ['M', 'S', 'S'],
        ['M', 'A', 'A'],
        ['M', 'S', 'S']
    ])
    row_number = 1
    a_index = 1
    expected = ['M', 'A', 'S']
    actual = get_upper_left_to_lower_right_slice(table, row_number, a_index)
    assert actual == expected



def test_upper_left_to_lower_right_slice() -> None:
    table = pandas.DataFrame([
        ['M', 'Y', 'Q'],
        ['X', 'A', 'Z'],
        ['D', 'X', 'S']
    ])
    row_number = 1
    a_index = 1
    expected = True
    actual = upper_left_to_lower_right_mas(table, row_number, a_index)
    assert actual == expected


def test_get_lower_left_to_upper_right_slice() -> None:
    table = pandas.DataFrame([
        ['Q', 'Y', 'S'],
        ['X', 'A', 'Z'],
        ['M', 'X', 'L']
    ])
    row_number = 1
    a_index = 1
    expected = ['M', 'A', 'S']
    actual = get_lower_left_to_upper_right_slice(table, row_number, a_index)
    assert actual == expected


def test_is_mas_in_x_shape_at_location_one_limb_wrong() -> None:
    table = pandas.DataFrame([
        ['M', 'S', 'D'],
        ['M', 'A', 'A'],
        ['M', 'S', 'S']
    ])
    row_number = 1
    a_index = 1
    expected = False
    actual = is_mas_in_x_shape_at_location(table, row_number, a_index)
    assert actual == expected

def test_is_mas_in_x_shape_at_location() -> None:
    table = pandas.DataFrame([
        ['M', 'S', 'S'],
        ['M', 'A', 'A'],
        ['M', 'S', 'S']
    ])
    row_number = 1
    a_index = 1
    expected = True
    actual = is_mas_in_x_shape_at_location(table, row_number, a_index)
    assert actual == expected
