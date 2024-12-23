import pandas

XMAS_CHARACTERS = ['X', 'M', 'A', 'S']

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


def check_up(table: pandas.DataFrame,
                   row_number: int,
                   x_index: int
                   ) -> bool:
    upward_slice = table.iloc[row_number - 3:row_number + 1, x_index]
    upward_slice_reversed = upward_slice.tolist()[::-1]
    return upward_slice_reversed == XMAS_CHARACTERS

def check_down(table: pandas.DataFrame,
                   row_number: int,
                   x_index: int
                   ) -> bool:
    downward_slice = table.iloc[row_number:row_number + 4, x_index]
    return downward_slice.tolist() == XMAS_CHARACTERS


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


def check_up_left(table: pandas.DataFrame,
                   row_number: int,
                   x_index: int
                   ) -> bool:
    upwards_left_slice = []
    for i in range(4):
        if row_number - i < 0 or x_index - i < 0:
            return False
        upwards_left_slice.append(table.iloc[row_number - i, x_index - i])
    return upwards_left_slice == XMAS_CHARACTERS


def check_up_right(table: pandas.DataFrame,
                   row_number: int,
                   x_index: int
                   ) -> bool:
    upwards_right_slice = []
    upper_x_bound = table.shape[1] - 1
    for i in range(4):
        if row_number - i < 0 or x_index + i > upper_x_bound:
            return False
        upwards_right_slice.append(table.iloc[row_number - i, x_index + i])
    return upwards_right_slice == XMAS_CHARACTERS


def check_down_left(table: pandas.DataFrame,
                   row_number: int,
                   x_index: int
                   ) -> bool:
    downwards_left_slice = []
    upper_row_bound = table.shape[0] - 1
    for i in range(4):

        next_row_number = row_number + i
        next_x_index = x_index - i
        if next_row_number > upper_row_bound or next_x_index < 0:
            return False
        downwards_left_slice.append(table.iloc[next_row_number, next_x_index])
    return downwards_left_slice == XMAS_CHARACTERS


def check_down_right(table: pandas.DataFrame,
                     row_number: int,
                     x_index: int
                     ) -> bool:
    downwards_right_slice = []
    upper_row_bound = table.shape[0] - 1
    upper_x_bound = table.shape[1] - 1
    for i in range(4):

        next_row_number = row_number + i
        next_x_index = x_index + i
        if next_row_number > upper_row_bound or next_x_index > upper_x_bound:
            return False
        downwards_right_slice.append(table.iloc[next_row_number, next_x_index])
    return downwards_right_slice == XMAS_CHARACTERS
