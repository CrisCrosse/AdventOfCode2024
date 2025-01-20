from day_6.online_solution import main_part_1, main_part_2


def test_main_part_1():
    expected = 5312
    actual = main_part_1()

    assert actual == expected


def test_main_part_2():
    expected = 1748
    actual = main_part_2()

    assert actual == expected