from day_3.task_one import get_input_from_txt_file, get_matching_pairs_and_multiplication_sums
import re


def main():
    input_data = get_input_from_txt_file()
    valid_muls = get_valid_muls(input_data)
    result = get_pair_products_and_total(valid_muls)
    print(result)




def get_valid_muls(input_data: str) -> [str]:
    data_split_by_do = input_data.split('do()')
    strings_to_get_mul_from = []

    for data in data_split_by_do:
        if contains_dont(data):
            valid_data = re.findall(r"(.*?)don't\(\)", data)
            strings_to_get_mul_from.append(valid_data[0])
        else:
            # this will add any strings between two do(), or beginning and end where there are do()
            strings_to_get_mul_from.append(data)

    return strings_to_get_mul_from


# returns true if it contains dont
def contains_dont(item: str) -> bool:
    matched = re.search(r"don't\(\)", item)
    return True if matched else False


def get_pair_products_and_total(valid_muls: [str]) -> int:
    multiplied_results = [get_matching_pairs_and_multiplication_sums(split_mul) for split_mul in valid_muls]
    return sum(multiplied_results)



# same problem of multiplying tuples as last task

# but I also need to regex for do() and don't()
# and only count the numbers if they are preceded by a do
# do()....mul()...don't()
# do() mul() do()
# are there any other valid combinations?

# the start and end may not have opening and closing ones respectively
# so need to just parse the beginning until find a do or dont
# and then the last may not have a closing set
# eg do/dont ....
# do/dont .... mul() mul()
# how can i match for the beginning and end cases without matching everything in between

# split everything by dos and donts
# start: only muls, or muls + donts
# middle: muls bounded by dos or donts
# end: muls preceded by a do or dont or nothing after a do or dont
# then can pass the split bits into the previous tasks func

if __name__ == '__main__':
    main()
# 85545273 answer too low
# so I am missing some valid muls
# edge cases?