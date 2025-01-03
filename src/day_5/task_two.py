from day_5.task_one import Printer, find_middle_element, update_does_not_pass_rule


class IncorrectPrinter(Printer):
    def update_does_not_pass_all_rules(self, update: list[int]) -> bool:
        return not self.update_passes_all_rules(update)

    def count_updates_that_do_not_pass_all_rules(self) -> int:
        count = 0
        for update in self.updates:
            if self.update_does_not_pass_all_rules(update):
                count += find_middle_element(self.reorder_update(update))

        return count

    def reorder_update(self, update: list[int]) -> list[int]:
        # this moves the second element in the rule directly after the first
        # it could move the first element directly before the second
        for rule in self.rules:
            if update_does_not_pass_rule(rule, update):
                first_number, second_number = rule
                first_number_index = update.index(first_number)
                second_number_index = update.index(second_number)
                update.insert(first_number_index, update.pop(second_number_index))
                return self.reorder_update(update)
        return update


def main():
    printer = IncorrectPrinter()
    print(printer.count_updates_that_do_not_pass_all_rules())


if __name__ == "__main__":
    main()