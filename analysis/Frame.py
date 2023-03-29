import re
from regex import regQuestion1


class Frame:
    def __init__(self, question, domain, intent, regex_set: dict = None, **kwargs):
        self.question = question
        self.slot = {"domain":domain, "intent":intent} | kwargs
        self.regex = regex_set
        self.__complete = False

    def modify_slot(self, edit):  # edit = dict
        self.slot |= edit  # modify the value of the slot

    @property
    def complete(self):
        return True if len([res for res in self.slot.items() if not res[1]]) == 0 else False




# {slot1: tuple(set(regexPositive),set(regexNegative))
# slot2: tuple(set(regexPositive),set(regexNegative)}
if __name__ == "__main__":
    f1 = Frame("headquarters", "headquarters", "banana", regQuestion1, coruscant="")
    print(f1.slot)
    f1.resolve("The headquarters of the Jedi Order is situated on corusant")
    print(f1.slot)
    pass
