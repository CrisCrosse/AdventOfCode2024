from day_2.task_one import is_safe_report


def test_is_safe_report():
    report = [7, 6, 4, 2, 1]
    assert is_safe_report(report) == True
#
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9