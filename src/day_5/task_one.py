def main():
    print("Hello World!")

def get_rule_input() -> list[tuple[int, int]]:
    input = get_input()
    rules = input[:1176]
    list_of_list_of_str_numbers = [rule.split('|') for rule in rules]
    return [(int(rule[0]), int(rule[1])) for rule in list_of_list_of_str_numbers]


def get_input() -> list[str]:
    with open("/Users/chris.rossell/projects/AdventOfCode2024/AdventOfCode2024/src/day_5/input.txt") as file:
        return file.readlines()


def get_update_input():
    pass

if __name__ == "__main__":
    main()