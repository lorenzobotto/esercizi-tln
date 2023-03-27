class Frame:
    def __init__(self,question,domain,intent,**kwargs):
        self.question = question
        self.slot = dict(domain=domain,intent=intent) | kwargs

    def modify_slot(self,edit):#edit = dict
        self.slot|edit #modify the value of the slot








