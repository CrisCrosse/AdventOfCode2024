import pandas

def main():
    report_values = get_reports_from_input()
    no_safe_reports = get_number_of_safe_reports(report_values)
    print(no_safe_reports)


def get_reports_from_input():

    report_dataframe = pandas.read_csv('input.txt', sep=' ', engine='python')

    list_of_reports = report_dataframe.values.tolist()
    print(list_of_reports)

    return list_of_reports


def get_number_of_safe_reports(list_of_reports):
    no_safe_reports = 0
    for current_report in list_of_reports:
        cleaned_report = [x for x in current_report if str(x) != 'nan']

        if is_safe_report(cleaned_report):
            no_safe_reports += 1

    return no_safe_reports



def is_static_increment(difference):
    if difference == 0:
        return True
    else:
        return False


def is_increasing_increment(difference):
    if difference > 0:
        return True
    else:
        return False

def is_valid_increment(difference):
    if 3 >= difference > 0:
        return True
    else:
        return False



def is_safe_report(report):
    last_index_in_report = len(report) - 1
    has_skipped_an_index = False

    # get if the list is increasing or decreasing to compare each increment against
    first_diff = report[1] - report[0]
    if is_static_increment(first_diff):
        return False
    is_increasing_report = is_increasing_increment(first_diff)


    # iterate through the list, checking the magnitude of the difference and the direction
    for index, level in enumerate(report):
        print("value: ", level)
        print("index: ", index)

        # removal cases for dampener;
        # the difference between item a and item b


        if index < last_index_in_report:
            next_level = report[index + 1]
            difference = (next_level - level)

            if is_static_increment(difference):
                return False
            is_current_increment_increasing = is_increasing_increment(difference)
            if is_current_increment_increasing != is_increasing_report:
                return False

            if not is_valid_increment(abs(difference)):
                    return False
    return True


if __name__ == '__main__':
    main()