from day_two.task_one import get_reports_from_input, is_static_increment, is_increasing_increment, is_valid_increment

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


def is_safe_report_with_dampener(report):

        # get if the list is increasing or decreasing to compare each increment against
        # this will break if report does not have two elements
        has_skipped_an_index = False
        last_index = len(report) - 1

        first_diff = report[1] - report[0]
        if is_static_increment(first_diff):



            if has_skipped_an_index:
                return False
            else:
                has_skipped_an_index = True
                report.pop(0)
                last_index -= 1
        if not is_valid_increment(abs(first_diff)):
            if has_skipped_an_index:
                return False
            else:
                has_skipped_an_index = True
                report.pop(0)
                last_index -= 1
        is_increasing_report = is_increasing_increment(first_diff)


        index = 1
        # iterate through the list, checking the magnitude of the difference and the direction
        while index < last_index:
            level = report[index]

            if index < last_index:
                next_level = report[index + 1]
                difference_to_next_level = (next_level - level)

                if is_static_increment(difference_to_next_level):
                    if has_skipped_an_index:
                        return False
                    else:
                        has_skipped_an_index = True
                        report.pop(index)
                        last_index -= 1
                        index = -1
                elif is_increasing_increment(difference_to_next_level) != is_increasing_report:
                    if has_skipped_an_index:
                        return False
                    else:
                        has_skipped_an_index = True
                        report.pop(index)
                        last_index -= 1
                        index = -1
                elif not is_valid_increment(abs(difference_to_next_level)):
                    if has_skipped_an_index:
                        return False
                    else:
                        has_skipped_an_index = True
                        report.pop(index)
                        last_index -= 1
                        index = -1
            index += 1
        return True

# this function will return the report without the current value or the next value if either
def handle_invalid_increment(report, index, last_index):
    report_without_current_value = report.pop(index)
    if index < last_index:
        report_without_next_value = report.pop(index)
        return is_safe_report_with_dampener(report_without_current_value) | is_safe_report_with_dampener(report_without_next_value)
    else:
        return is_safe_report_with_dampener(report_without_current_value)


def is_not_static_and_is_correct_magnitude_increment(difference, is_increasing_report):
    if is_increasing_report:
        return 3 >= difference > 0
    else:
        return 0 > difference >= -3

if __name__ == '__main__':
    main()


