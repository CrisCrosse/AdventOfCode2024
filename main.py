import pandas

def main():
    list_1, list_2 = get_sorted_lists_from_input()
    diff = get_difference_between_lists(list_1, list_2)
    print(diff)

def get_sorted_lists_from_input():
    # was getting an answer too high (?) because the first set of values in the text file were registered
    # as the column names, so I had to add the column names manually, the sep was also wrong at 2 spaces
    # not 3 as it was in the txt file
    id_dataframe = pandas.read_csv('input.txt', sep='   ', engine='python')

    print(id_dataframe)
    id_dataframe.columns = ['Column1', 'Column2']

    list_1 = id_dataframe['Column1'].tolist()
    list_2 = id_dataframe['Column2'].tolist()

    list_1_sorted = sorted(list_1)
    list_2_sorted = sorted(list_2)
    return list_1_sorted, list_2_sorted


def get_difference_between_lists(list_1, list_2):
    cumulative_difference = 0

    if len(list_1) == len(list_2):
        print("The lists are of the same length")
        print(len(list_1))
        for i in range(len(list_1)):
            if list_1[i] == list_2[i]:
                pass
            else:
                difference = abs(list_1[i] - list_2[i])
                print(f" the difference between {list_1[i]} and {list_2[i]} is {difference}")
                cumulative_difference += difference

    return cumulative_difference

if __name__ == '__main__':
    main()
