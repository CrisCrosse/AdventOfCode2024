from day_2.task_one import get_reports_from_input, is_safe_report, is_increasing_increment

def main():
    report_values = get_reports_from_input()
    no_safe_reports = get_number_of_safe_reports_with_dampener(report_values)
    print(no_safe_reports)


def get_number_of_safe_reports_with_dampener(list_of_reports):
    no_safe_reports = 0
    for current_report in list_of_reports:
        cleaned_report = [x for x in current_report if str(x) != 'nan']

        if is_safe_report_with_dampener(cleaned_report):
            no_safe_reports += 1

    return no_safe_reports

def is_invalid_increment(difference, is_increasing_report):
    return not is_valid_increment(difference, is_increasing_report)

def is_valid_increment(difference, is_increasing_report):
    if is_increasing_report:
        return 3 >= difference > 0
    else:
        return 0 > difference >= -3

def is_safe_report_with_dampener(report):
    # the first difference is a unique case because you need to set an increasing or decreasing flag
    # for each subsequent difference to be compared against
    first_diff = report[1] - report[0]
    is_increasing = is_increasing_increment(first_diff)

    if is_invalid_increment(first_diff, is_increasing):
        return is_valid_report_with_first_or_current_or_next_value_removed(report, 0)

    last_index = len(report) - 1
    for index, level in enumerate(report):
        if index == last_index:
            break
        next_level = report[index + 1]
        difference_to_next_level = (next_level - level)
        if is_invalid_increment(difference_to_next_level, is_increasing):
            return is_valid_report_with_first_or_current_or_next_value_removed(report, index)

    return True

# this function cannot get called on the last index as all the diffs have been checked by then
def is_valid_report_with_first_or_current_or_next_value_removed(report, current_index):
    report_with_current_removed = report.copy()
    report_with_current_removed.pop(current_index)

    report_with_next_removed = report.copy()
    report_with_next_removed.pop(current_index + 1)

    report_with_first_removed = report.copy()
    report_with_first_removed.pop(0)
    return (
            is_safe_report(report_with_current_removed) |
            is_safe_report(report_with_next_removed) |
            is_safe_report(report_with_first_removed)
    )

if __name__ == '__main__':
    main()


