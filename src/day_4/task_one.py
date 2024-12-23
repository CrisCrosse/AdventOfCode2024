from day_4.task_one_checkers import check_forward, check_backward, check_each_diagonal, check_down, \
    check_up
import pandas


def main() -> None:
    table = get_table_from_input()
    print(table)
    xmas_counter = iterate_through_lines_and_count_xmas(table)
    print(xmas_counter)


def get_table_from_input() -> pandas.DataFrame:
    with open('/Users/chris.rossell/projects/AdventOfCode2024/AdventOfCode2024/src/day_4/input.txt') as f:
        lines = f.readlines()
    lines_split_by_char = [list(line.strip()) for line in lines]
    return pandas.DataFrame(lines_split_by_char)


def iterate_through_lines_and_count_xmas(table: pandas.DataFrame) -> int:
    xmas_counter = 0
    for row_number, row in table.iterrows():
        x_indices = find_all_x_in_line(row)

        for x_index in x_indices:
            number_of_xmas_at_position = get_number_of_xmas_at_position(table, row_number, x_index)
            xmas_counter += number_of_xmas_at_position

    return xmas_counter


def find_all_x_in_line(line: pandas.Series) -> list:
    return [i for i, x in enumerate(line) if x == 'X']


def get_number_of_xmas_at_position(table: pandas.DataFrame,
                                   row_number: int,
                                   x_index: int
                                   ) -> int:

    number_of_xmas_at_position = 0
    if check_forward(table, row_number, x_index):
        number_of_xmas_at_position += 1
    if check_backward(table, row_number, x_index):
        number_of_xmas_at_position += 1

    if check_up(table, row_number, x_index):
        number_of_xmas_at_position += 1
    if check_down(table, row_number, x_index):
        number_of_xmas_at_position += 1

    number_of_xmas_at_position += check_each_diagonal(table, row_number, x_index)


    return number_of_xmas_at_position


if __name__ == '__main__':
    main()
