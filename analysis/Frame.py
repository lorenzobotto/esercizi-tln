class Frame:
    def __init(self, id, question, **kwargs):
        self.id = id
        self.question = question
        self.slots = dict(intent=None, domain=None) | kwargs

        self.slots["intent"] = kwargs["intent"]

    def modify_slot(self, slot: str):
        self.slots[slot] = "Nuovo Valore"




