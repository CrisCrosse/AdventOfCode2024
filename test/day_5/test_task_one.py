from day_5.task_one import get_rule_input, get_input, get_update_input


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

