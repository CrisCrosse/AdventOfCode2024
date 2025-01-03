from unittest.mock import patch

import pytest

from day_5.task_one import get_rule_input, get_input, get_update_input, update_passes_rule, find_middle_element, Printer


def test_get_input():
    actual = get_input()
    assert isinstance(actual, list)
    assert len(actual) > 0
    assert actual[0] == "32|75\n"
    assert actual[1] == "18|19\n"
    assert actual[-1] == "98,66,29,75,15,68,27,67,31,13,63,93,89,46,52,87,95,18,32,19,44,74,43"

def test_get_rule_input():
    actual = get_rule_input()
    assert isinstance(actual, list)
    assert len(actual) == 1176
    assert actual[0] == (32, 75)
    assert actual[-1] == (38, 62)

def test_get_update_input():
    actual = get_update_input()
    assert isinstance(actual, list)
    assert len(actual) == 185
    assert actual[0] == [52, 77, 83, 31, 94, 75, 34, 95, 29, 38, 82, 19, 41, 39, 27, 98, 84, 13, 55, 21, 66]
    assert actual [-1] == [98, 66, 29, 75, 15, 68, 27, 67, 31, 13, 63, 93, 89, 46, 52, 87, 95, 18, 32, 19, 44, 74, 43]


def test_update_passes_rule_happy_path():
    rule = (32, 75)
    update = [32, 75, 18, 19]
    expected = True
    actual = update_passes_rule(rule, update)
    assert actual == expected


def test_update_passes_rule_elements_not_adjacent():
    rule = (32, 75)
    update = [32, 18, 19, 75]
    expected = True
    actual = update_passes_rule(rule, update)
    assert actual == expected


def test_update_passes_rule_element_not_present():
    rule = (32, 85)
    update = [32, 75, 18, 19]
    expected = True
    actual = update_passes_rule(rule, update)
    assert actual == expected


def test_update_passes_rule_element_present_twice():
    rule = (32, 75)
    update = [32, 75, 18, 75]
    expected = True
    actual = update_passes_rule(rule, update)
    assert actual == expected


def test_update_passes_rule_element_present_twice_once_before():
    rule = (32, 75)
    update = [75, 32, 75]
    expected = False
    actual = update_passes_rule(rule, update)
    assert actual == expected

def test_find_middle_element_throws_error_where_even_number_of_elements():
    update = [32, 75, 18, 19, 13, 14, 16, 17]

    with pytest.raises(ValueError) as e:
        find_middle_element(update)
        assert e.value == "Middle index could not be found: even number of elements in [32, 75, 18, 19]"

def test_find_middle_element_happy_path():
    update = [32, 75, 18, 19, 44]
    expected = 18
    actual = find_middle_element(update)
    assert actual == expected

def test_find_middle_element_happy_path_more_elements():
    update = [32, 75, 18, 19, 44, 55, 66]
    expected = 19
    actual = find_middle_element(update)
    assert actual == expected

@pytest.fixture
@patch('day_5.task_one.py.get_update_input')
@patch('day_5.task_one.py.get_rule_input')
def printer(mock_rules, mock_updates):
    mock_rules.return_value = [(32, 75), (18, 19)]
    mock_updates.return_value = [[32, 75, 50, 18, 19]]
    return Printer()

def test_printer_update_passes_all_rules_happy_path(printer):
    update = [32, 75, 18, 19]
    expected = True
    actual = printer.update_passes_all_rules(update)
    assert actual == expected


def test_printer_update_passes_all_rules_unhappy_path(printer):
    update = [32, 75, 18]
    expected = False
    actual = printer.update_passes_all_rules(update)
    assert actual == expected


def test_count_updates_happy_path(printer):
    expected = 50
    actual = printer.count_updates_that_pass_all_rules()
    assert actual == expected


@patch('day_5.task_one.py.get_update_input')
@patch('day_5.task_one.py.get_rule_input')
def test_count_updates_does_not_count_invalid(mock_rules,
                                                                          mock_updates):
    mock_rules.return_value = [(32, 75), (18, 19)]
    mock_updates.return_value = [[32, 75, 50, 18, 19], [12, 13, 75, 32, 3]]
    printer = Printer()

    expected = 50
    actual = printer.count_updates_that_pass_all_rules()
    assert actual == expected