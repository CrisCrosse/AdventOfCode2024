from day_two.task_two import is_not_static_and_is_correct_magnitude_increment
from src.day_two.task_two import get_number_of_safe_reports_with_dampener, is_safe_report_with_dampener


def test_safe_report_when_increasing():
    report = [1, 3, 6, 7, 9]
    expected = True

    actual = is_safe_report_with_dampener(report)

    assert actual == expected


def test_safe_report_when_decreasing():
    report = [7, 6, 4, 2, 1]
    expected = True

    actual = is_safe_report_with_dampener(report)

    assert actual == expected


def test_unsafe_report_when_increasing():
    report = [1, 2, 7, 8, 9]
    expected = False

    actual = is_safe_report_with_dampener(report)

    assert actual == expected


def test_unsafe_report_decreasing():
    report = [9, 7, 6, 2, 1]
    expected = False

    actual = is_safe_report_with_dampener(report)

    assert actual == expected


def test_safe_report_when_increasing_and_need_to_remove():
    report = [1, 3, 2, 4, 5]
    expected = True

    actual = is_safe_report_with_dampener(report)

    assert actual == expected
    # in this case I want to remove 3 from the list as the increment changes to negative
    # then I need to assert that the first and new second value have a valid increment again
    # ie I need to start again? that would work

def test_unsafe_report_when_increasing_and_removing_value():
    report = [1, 3, 7]
    expected = False

    actual = is_safe_report_with_dampener(report)

    assert actual == expected


def test_safe_report_when_decreasing_and_need_to_remove():
    report = [8, 6, 4, 4, 1]
    expected = True

    actual = is_safe_report_with_dampener(report)

    assert actual == expected



# I think my logic is flawed --> at the time of recognising an increment which is not valid, it could be either the
# current value or the next value that is the problem value
# and I need to try and remove both of them
# write a test case to show this, where just removign the first element results i nan incrorect answer

# logically there wsa a single case where a report could fail;
# increment is not of correct magnitude + direction

# because we can now skip a value, there is now two extra cases
# increment is not of correct magnitude + direction and removing current value (increment[i-1:i+1]) is valid c--> continue with updated report (recursion --> it can  call the function from the first task which has no tolerance for removing values --> if it calls itself another problem value could be skipped similiarly)
# increment is not of correct magnitude + direction and removing next value (increment[i:i+2]) is valid --> continue with updated report
# increment is not of correct magnitude + direction and removing next value or current value is not valid --> fail


def test_safe_report_where_increasing_and_second_value_is_problem():
    # if the last 1 is removed then the report is valid
    report = [1, 2, 1, 4, 5]
    expected = True

    actual = is_safe_report_with_dampener(report)

    assert actual == expected

def test_safe_report_where_decreasing_and_second_value_is_problem():
    report = [8, 6, 5, 1, 4]
    expected = True

    actual = is_safe_report_with_dampener(report)

    assert actual == expected


# valid increment tests

def test_is_valid_increment_positive():
    difference = 3
    is_increasing_report = True
    expected = True

    actual = is_not_static_and_is_correct_magnitude_increment(difference, is_increasing_report)

    assert actual == expected

def test_is_valid_increment_negative():
    difference = -1
    is_increasing_report = False
    expected = True

    actual = is_not_static_and_is_correct_magnitude_increment(difference, is_increasing_report)

    assert actual == expected

def test_is_valid_increment_wrong_direction():
    difference = -1
    is_increasing_report = True
    expected = False

    actual = is_not_static_and_is_correct_magnitude_increment(difference, is_increasing_report)

    assert actual == expected


def test_is_valid_increment_zero():
    difference = 0
    is_increasing_report = True
    expected = False

    actual = is_not_static_and_is_correct_magnitude_increment(difference, is_increasing_report)

    assert actual == expected
