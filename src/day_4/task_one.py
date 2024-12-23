.import pandas

XMAS_CHARACTERS = ['X', 'M', 'A', 'S']


def main() -> None:
    table = get_table_from_input()
    print(table)


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
            print(xmas_counter)

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
    if check_each_diagonal(table, row_number, x_index):
        number_of_xmas_at_position += 1
    if check_vertical(table, row_number, x_index):
        number_of_xmas_at_position += 1

    return number_of_xmas_at_position


def check_forward(table: pandas.DataFrame,
                  row_number: int,
                  x_index: int
                  ) -> bool:
    forward_slice = table.iloc[row_number, x_index:x_index + 4]
    return forward_slice.tolist() == XMAS_CHARACTERS


def check_backward(table: pandas.DataFrame,
                   row_number: int,
                   x_index: int
                   ) -> bool:
    backward_slice = table.iloc[row_number, x_index - 3: x_index+1]
    backward_slice_reversed = backward_slice.tolist()[::-1]
    return backward_slice_reversed == XMAS_CHARACTERS


def check_each_diagonal(table: pandas.DataFrame,
                        row_number: int,
                        x_index: int
                        ) -> int:
    xmas_counter = 0
    if check_up_left(table, row_number, x_index):
        xmas_counter += 1
    if check_up_right(table, row_number, x_index):
        xmas_counter += 1
    if check_down_left(table, row_number, x_index):
        xmas_counter += 1
    if check_down_right(table, row_number, x_index):
        xmas_counter += 1
    return xmas_counter


def check_vertical(table: pandas.DataFrame,
                   row_number: int,
                   x_index: int
                   ) -> bool:
    return True


if __name__ == '__main__':
    main()
