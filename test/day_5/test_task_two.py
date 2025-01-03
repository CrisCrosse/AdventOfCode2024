from unittest.mock import patch

import pytest

from day_5.task_two import IncorrectPrinter


@pytest.fixture
@patch('day_5.task_one.get_update_input')
@patch('day_5.task_one.get_rule_input')
def printer(mock_rules, mock_updates):
    mock_rules.return_value = [(32, 75), (18, 19), (19, 25)]
    mock_updates.return_value = [[75, 32, 75, 18, 19]]
    return IncorrectPrinter()


@patch('day_5.task_two.IncorrectPrinter.reorder_update')
def test_count_updates_that_do_not_pass_all_rules_happy_path(reorder_mock, printer):
    reorder_mock.return_value = [32, 75, 50, 18, 19]
    expected = 50
    actual = printer.count_updates_that_do_not_pass_all_rules()
    assert actual == expected


def test_reorder_update_happy_path_one_rule_to_reorder(printer):
    update = [75, 32, 30, 18, 19]
    expected = [32, 75, 30, 18, 19]
    actual = printer.reorder_update(update)
    assert actual == expected


def test_reorder_update_happy_path_two_rules_to_reorder(printer):
    update = [75, 32, 30, 19, 18]
    expected = [32, 75, 30, 18, 19]
    actual = printer.reorder_update(update)
    assert actual == expected


def test_reorder_update_happy_path_two_overwriting_rules_to_reorder(printer):
    update = [75, 32, 25, 19, 18]
    # [75, 32, 25, 19, 18] -> [32, 75, 25, 19, 18] -> [32, 75, 25, 18, 19] -> [32, 75, 18, 19, 25]
    expected = [32, 75, 18, 19, 25]
    actual = printer.reorder_update(update)
    assert actual == expected


@patch('day_5.task_one.get_update_input')
@patch('day_5.task_one.get_rule_input')
def test_reorder_update_example_from_guide(mock_rules,
                                           mock_updates):
        mock_rules.return_value = [
            (97, 13), (97, 47), (75, 29), (29, 13), (97, 29), (47, 13), (75, 47),
            (97, 75), (47, 29), (75, 13)
        ]
        mock_updates.return_value = [[97, 13, 75, 29, 47]]
        # first incorrect rule is 29, 13 -> [97, 75, 29, 13, 47]
        # the second incorrect rule is 47, 13 -> [97, 75, 29, 47, 13]
        # the third incorrect rule is 47, 29 -> [97, 75, 47, 29, 13]
        expected = [97, 75, 47, 29, 13]
        actual = IncorrectPrinter().reorder_update([97, 13, 75, 29, 47])
        assert actual == expected

