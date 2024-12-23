import pandas

from day_4.task_one_checkers import check_forward, check_backward, check_up, check_down, check_up_left, check_up_right, \
    check_down_left, check_down_right


def test_check_forward() -> None:
    table = pandas.DataFrame([['X', 'M', 'A', 'S'],
                              ['S', 'X', 'S', 'M']]
                             )
    expected = True
    row_number = 0
    x_index = 0

    actual = check_forward(table, row_number, x_index)

    assert actual == expected


def test_check_forward_where_not_4_indices_left() -> None:
    table = pandas.DataFrame([['S', 'X', 'S', 'M'],
                              ['S', 'X', 'S', 'M']]
                             )
    expected = False
    row_number = 0
    x_index = 1

    actual = check_forward(table, row_number, x_index)

    assert actual == expected


def test_check_backward() -> None:
    table = pandas.DataFrame([['S', 'A', 'M', 'X'],
                              ['S', 'X', 'S', 'M']]
                             )
    expected = True
    row_number = 0
    x_index = 3

    actual = check_backward(table, row_number, x_index)

    assert actual == expected


def test_check_backward_where_not_4_indices_left() -> None:
    table = pandas.DataFrame([['S', 'X', 'S', 'M'],
                              ['S', 'X', 'S', 'M']]
                             )
    expected = False
    row_number = 0
    x_index = 1

    actual = check_backward(table, row_number, x_index)

    assert actual == expected


def test_check_up() -> None:
    table = pandas.DataFrame([['Q', 'S', 'Y', 'U'],
                              ['Z', 'A', 'H', 'I'],
                              ['W', 'M', 'J', 'P'],
                              ['C', 'X', 'N', 'L']]
                             )
    expected = True
    row_number = 3
    x_index = 1

    actual = check_up(table, row_number, x_index)

    assert actual == expected


def test_check_up_where_not_4_indices_above() -> None:
    table = pandas.DataFrame([
        ['Z', 'A', 'H', 'I'],
        ['W', 'M', 'J', 'P'],
        ['C', 'X', 'N', 'L'],
        ['Q', 'S', 'Y', 'U']
    ])
    expected = False
    row_number = 2
    x_index = 1

    actual = check_up(table, row_number, x_index)

    assert actual == expected


def test_check_down() -> None:
    table = pandas.DataFrame([
        ['C', 'X', 'N', 'L'],
        ['W', 'M', 'J', 'P'],
        ['Z', 'A', 'H', 'I'],
        ['Q', 'S', 'Y', 'U']
    ])
    expected = True
    row_number = 0
    x_index = 1

    actual = check_down(table, row_number, x_index)

    assert actual == expected

def test_check_down_where_not_4_indices_below() -> None:
    table = pandas.DataFrame([
        ['Q', 'S', 'Y', 'U'],
        ['C', 'X', 'N', 'L'],
        ['W', 'M', 'J', 'P'],
        ['Z', 'A', 'H', 'I']

    ])
    expected = False
    row_number = 1
    x_index = 1

    actual = check_down(table, row_number, x_index)

    assert actual == expected

def test_check_up_left() -> None:
    table = pandas.DataFrame([
        ['S', 'X', 'N', 'L'],
        ['W', 'A', 'J', 'P'],
        ['Z', 'A', 'M', 'I'],
        ['Q', 'S', 'Y', 'X']
    ])
    expected = True
    row_number = 3
    x_index = 3

    actual = check_up_left(table, row_number, x_index)

    assert actual == expected

def test_check_up_left_where_not_4_left() -> None:
    table = pandas.DataFrame([
        ['A', 'X', 'N', 'L'],
        ['W', 'M', 'J', 'P'],
        ['Z', 'A', 'X', 'I'],
        ['Q', 'S', 'Y', 'S']
    ])
    expected = False
    row_number = 2
    x_index = 2

    actual = check_up_left(table, row_number, x_index)

    assert actual == expected


def test_check_up_right() -> None:
    table = pandas.DataFrame([
        ['S', 'X', 'N', 'S'],
        ['W', 'A', 'A', 'P'],
        ['Z', 'M', 'M', 'I'],
        ['X', 'S', 'Y', 'X']
    ])
    expected = True
    row_number = 3
    x_index = 0

    actual = check_up_right(table, row_number, x_index)

    assert actual == expected


def test_check_up_right_where_not_4_left_row() -> None:
    table = pandas.DataFrame([
        ['S', 'X', 'A', 'A'],
        ['W', 'M', 'M', 'P'],
        ['X', 'X', 'M', 'I'],
        ['S', 'S', 'Y', 'X']
    ])
    expected = False
    row_number = 2
    x_index = 0

    actual = check_up_right(table, row_number, x_index)

    assert actual == expected


def test_check_up_right_where_not_4_left_x() -> None:
    table = pandas.DataFrame([
        ['S', 'X', 'A', 'A'],
        ['W', 'M', 'M', 'A'],
        ['X', 'X', 'M', 'I'],
        ['S', 'X', 'Y', 'X']
    ])
    expected = False
    row_number = 3
    x_index = 1

    actual = check_up_right(table, row_number, x_index)

    assert actual == expected


def test_check_down_left() -> None:
    table = pandas.DataFrame([
        ['S', 'X', 'N', 'X'],
        ['W', 'A', 'M', 'P'],
        ['Z', 'A', 'M', 'I'],
        ['S', 'S', 'Y', 'X']
    ])
    expected = True
    row_number = 0
    x_index = 3

    actual = check_down_left(table, row_number, x_index)

    assert actual == expected


def test_check_down_left_where_not_4_left_row() -> None:
    table = pandas.DataFrame([
        ['S', 'X', 'N', 'X'],
        ['W', 'A', 'M', 'X'],
        ['Z', 'A', 'M', 'I'],
        ['S', 'A', 'Y', 'X']
    ])
    expected = False
    row_number = 1
    x_index = 3

    actual = check_down_left(table, row_number, x_index)

    assert actual == expected

def test_check_down_left_where_not_4_left_x() -> None:
    table = pandas.DataFrame([
        ['S', 'X', 'X', 'X'],
        ['W', 'M', 'M', 'X'],
        ['A', 'A', 'M', 'I'],
        ['S', 'A', 'Y', 'X']
    ])
    expected = False
    row_number = 0
    x_index = 2

    actual = check_down_left(table, row_number, x_index)

    assert actual == expected


def test_check_down_right() -> None:
    table = pandas.DataFrame([
        ['X', 'X', 'N', 'X'],
        ['W', 'M', 'M', 'P'],
        ['Z', 'A', 'A', 'I'],
        ['S', 'S', 'Y', 'S']
    ])
    expected = True
    row_number = 0
    x_index = 0

    actual = check_down_right(table, row_number, x_index)

    assert actual == expected


def test_check_down_right_where_not_4_left_row() -> None:
    table = pandas.DataFrame([
        ['S', 'X', 'N', 'X'],
        ['X', 'A', 'M', 'X'],
        ['Z', 'M', 'M', 'I'],
        ['S', 'A', 'A', 'X']
    ])
    expected = False
    row_number = 1
    x_index = 0

    actual = check_down_right(table, row_number, x_index)

    assert actual == expected

def test_check_down_right_where_not_4_left_x() -> None:
    table = pandas.DataFrame([
        ['S', 'X', 'X', 'X'],
        ['W', 'M', 'M', 'X'],
        ['A', 'A', 'M', 'A'],
        ['S', 'A', 'Y', 'X']
    ])
    expected = False
    row_number = 0
    x_index = 1

    actual = check_down_right(table, row_number, x_index)

    assert actual == expected



