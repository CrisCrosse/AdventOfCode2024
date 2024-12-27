import pandas

from day_4.task_one import get_table_from_input

MAS_CHARACTERS = ['M', 'A', 'S']

def main():
    table_data = get_table_from_input()
    xmas_counter = iterate_through_lines_and_count_mas_in_x_shape(table_data)
    print(xmas_counter)


def iterate_through_lines_and_count_mas_in_x_shape(table: pandas.DataFrame) -> int:
    xmas_counter = 0
    for row_number, row in table.iterrows():
        a_indices = find_all_a_in_row(row)

        for a_index in a_indices:
            if is_mas_in_x_shape_at_location(table, row_number, a_index):
                xmas_counter += 1

    return xmas_counter

def find_all_a_in_row(row: pandas.Series) -> list:
    return [i for i, value in enumerate(row) if value == 'A']

def is_mas_in_x_shape_at_location(table: pandas.DataFrame, row_number: int, a_index: int) -> int:
    if (upper_left_to_lower_right_mas(table, row_number, a_index)
            and lower_left_to_upper_right_mas(table, row_number, a_index)):
        return True
    else:
        return False

def upper_left_to_lower_right_mas(table: pandas.DataFrame, row_number: int, a_index: int) -> bool:
    if this_slice_will_exceed_table_bounds(row_number, a_index, table):
        return False
    else:
        diagonal_slice = get_upper_left_to_lower_right_slice(table, row_number, a_index)
        return diagonal_slice == MAS_CHARACTERS or diagonal_slice[::-1] == MAS_CHARACTERS


def lower_left_to_upper_right_mas(table: pandas.DataFrame, row_number: int, a_index: int) -> bool:
    if this_slice_will_exceed_table_bounds(row_number, a_index, table):
        return False
    else:
        diagonal_slice = get_lower_left_to_upper_right_slice(table, row_number, a_index)
        return diagonal_slice == MAS_CHARACTERS or diagonal_slice[::-1] == MAS_CHARACTERS



def get_upper_left_to_lower_right_slice(table: pandas.DataFrame, row_number: int, a_index: int) -> list:
    diagonal_slice = []
    for i in range(-1, 2):
        diagonal_slice.append(table.iloc[row_number+i, a_index+i])
    return diagonal_slice

def get_lower_left_to_upper_right_slice(table: pandas.DataFrame, row_number: int, a_index: int) -> list:
    diagonal_slice = []
    for i in range(-1, 2):
        diagonal_slice.append(table.iloc[row_number-i, a_index+i])
    return diagonal_slice


def this_slice_will_exceed_table_bounds(row_number: int, a_index: int, table: pandas.DataFrame) -> bool:
    table_lower_bound = 0
    a_index_upper_bound = table.shape[1] - 1
    row_index_upper_bound = table.shape[0] - 1

    required_a_index_upper_bound = a_index + 1
    required_row_index_upper_bound = row_number + 1

    if (row_number <= table_lower_bound) or (a_index <= table_lower_bound):
        return True
    elif required_a_index_upper_bound > a_index_upper_bound or required_row_index_upper_bound > row_index_upper_bound:
        return True
    else:
        return False


def function_to_mock() -> bool:
    return False



if __name__ == '__main__':
    main()