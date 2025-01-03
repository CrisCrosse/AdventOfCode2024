def main():
    print("Hello World!")

def get_rule_input() -> list[tuple[int, int]]:
    task_input = get_input()
    string_rules = task_input[:1176]
    list_of_numbers_in_rules = [rule.split('|') for rule in string_rules]
    return [(int(rule[0]), int(rule[1])) for rule in list_of_numbers_in_rules]


def get_input() -> list[str]:
    with open("/Users/chris.rossell/projects/AdventOfCode2024/AdventOfCode2024/src/day_5/input.txt") as file:
        return file.readlines()


def get_update_input() -> list[list[int]]:
    task_input = get_input()
    string_updates = task_input[1177:]
    split_updates = [update.split(',') for update in string_updates]
    updates = []
    for update in split_updates:
        updates.append([int(update_element) for update_element in update])
    return updates


if __name__ == "__main__":
    main()