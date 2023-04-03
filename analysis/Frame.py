class Frame:

    def __init__(self, domain, intent, **kwargs):
        self.slot = {"domain": domain, "intent": intent} | kwargs
        self.__complete = False
        # self.regex = regex_set

    def modify_slot(self, edit):  # edit = dict
        self.slot |= edit  # adds a new slot or modifies the value of an existing one

    @property
    def complete(self):
        return len([res for res in self.slot.items() if not res[1]]) == 0
    
    @property
    def total_slot_number(self):
        return (len(self.slot)-2)
    
    @property
    def missing_slot_number(self):
        return (len(self.slot)-2)-(len([res for res in self.slot.items() if res[1]])-2)

# {slot1: tuple(set(regexPositive),set(regexNegative))
# slot2: tuple(set(regexPositive),set(regexNegative)}
# if __name__ == "__main__":
#     f1 = Frame("headquarters", "headquarters", coruscant=None,banana="banana",lorenzo="")
#     print(f1.slot)
#     print(f1.total_slot_number)
#     print(f1.missing_slot_number)
#     #f1.resolve("The headquarters of the Jedi Order is situated on corusant")
#     #Vprint(f1.slot)
#     pass
