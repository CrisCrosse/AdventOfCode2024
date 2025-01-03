def main():
    printer = Printer()
    print(printer.count_updates_that_pass_all_rules())

class Printer:
    rules: list[tuple[int, int]]
    updates: list[list[int]]

    def __init__(self):
        self.rules = get_rule_input()
        self.updates = get_update_input()

    def update_passes_all_rules(self, update: list[int]) -> bool:
        for rule in self.rules:
            if update_does_not_pass_rule(rule, update):
                return False
        return True

    def count_updates_that_pass_all_rules(self) -> int:
        count = 0
        for update in self.updates:
            if self.update_passes_all_rules(update):
                count += find_middle_element(update)
        return count


def get_rule_input() -> list[tuple[int, int]]:
    task_input = get_input()
    string_rules = task_input[:1176]
    list_of_numbers_in_rules = [rule.split('|') for rule in string_rules]
    return [(int(rule[0]), int(rule[1])) for rule in list_of_numbers_in_rules]


def get_update_input() -> list[list[int]]:
    task_input = get_input()
    string_updates = task_input[1177:]
    split_updates = [update.split(',') for update in string_updates]
    updates = []
    for update in split_updates:
        updates.append([int(update_element) for update_element in update])
    return updates


def get_input() -> list[str]:
    with open("/Users/chris.rossell/projects/AdventOfCode2024/AdventOfCode2024/src/day_5/input.txt") as file:
        return file.readlines()

def update_does_not_pass_rule(rule: tuple[int, int], update: list[int]) -> bool:
    return not update_passes_rule(rule, update)

def update_passes_rule(rule: tuple[int, int], update: list[int]) -> bool:
    first_number, second_number = rule
    if first_number not in update or second_number not in update:
        return True
    first_number_index = update.index(first_number)
    second_number_index = update.index(second_number)
    return first_number_index < second_number_index


def find_middle_element(update: list[int]) -> int:
    max_index = len(update) - 1
    middle_index = max_index / 2
    if max_index % 2 == 0:
        return update[int(middle_index)]
    else:
        raise ValueError(f"Middle index could not be found: even number of elements in {update}")

if __name__ == "__main__":
    main()