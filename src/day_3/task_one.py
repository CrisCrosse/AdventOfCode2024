import re

def main():
    input_data = get_input_from_txt_file()
    print(input_data)
    result = get_matching_pairs_and_multiplication_sums(input_data)
    print(result)


def get_input_from_txt_file():
    with open('/Users/chris.rossell/projects/AdventOfCode2024/AdventOfCode2024/src/day_3/input.txt', 'r') as file:
        return file.read()


def get_matching_pairs_and_multiplication_sums(input_data: str) -> int:
    number_pairs = match_only_numbers_from_string(input_data)
    return multiply_tuples_and_return_sum(number_pairs)


def match_mul_and_numbers_from_string(program_input: str) -> [str]:
    return re.findall(r'mul\(\d{1,3},\d{1,3}\)', program_input)


def match_only_numbers_from_string(program_input: str) -> [(int, int)]:
    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', program_input)
    return [(int(x), int(y)) for x, y in matches]


def multiply_tuples_and_return_sum(tuple_list: [(int, int)]) -> int:
    return sum([x * y for x, y in tuple_list])


if __name__ == '__main__':
    main()

# 85545273
# 174336360