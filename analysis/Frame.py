import re


class Frame:
    def __init(self, question, domain, intent, **kwargs):
        self.question = question
        self.intent = intent
        self.domain = domain
        self.slots = {"intent": intent, "domain": domain} | kwargs

    def modify_slot(self, slot_seq: dict):
        self.slots |= slot_seq
