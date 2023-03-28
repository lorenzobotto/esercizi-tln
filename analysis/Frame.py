from regex import regex_q1


class Frame:
    def __init__(self,question,domain,intent,regex_set: set = None, **kwargs):
        self.question = question
        self.slot = dict(domain=domain,intent=intent) | kwargs
        self.regex = regex_set


        

    def modify_slot(self,edit):#edit = dict
        self.slot|edit #modify the value of the slot
    
    def resolve(self,string):
        pass







