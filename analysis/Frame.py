class Frame:

    def __init__(self, domain, intent, **kwargs):
        self.slots = {"domain": domain, "intent": intent} | kwargs
        self._complete = False
        self.__incomplete_slots = len(self.slots) - 2
        # self.regex = regex_set

    def modify_slot(self, edit):  # edit = dict
        self.slots |= edit  # adds a new slots or modifies the value of an existing one

    @property
    def complete(self):
        return len([res for res in self.slots.items() if not res[1]]) == 0

    # @property
    # def total_slot_number(self):
    #     return len(self.slots) - 2
    @property
    def incomplete_slots(self):
        return list(self.slots.values()).count(None) - 2
