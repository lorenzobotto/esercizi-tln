import re
class Frame:
    def __init__(self,question,domain,intent,regex_set: dict = None, **kwargs):
        self.question = question
        self.slot = dict(domain=domain,intent=intent) | kwargs
        self.regex = regex_set


        

    def modify_slot(self,edit):#edit = dict
        self.slot|edit #modify the value of the slot
    
    def resolve(self,sentence):
        #pre processing
        #lower case
        sentence = sentence.lower()
        
        #self.regex[x][0] tuple positive
        #self.regex[x][1] tuple negative
        for x in self.regex:
            for pattern in self.regex[x][1]:
                match = re.search(pattern, sentence) 
                if match:
                    print(match.group())
                    print("Abbiamo frase negativa --> errore")
                    return("male")
            for pattern in self.regex[x][1]:
                match = re.search(pattern, sentence) 
                if match:
                    print(match.group())
                    print("Abbiamo frase giusta --> ok")
                    #self.slot[x] = match.group()#scrivo nello slot
                    return("buono")
            return("ripeti o backup")



#{slot1: tuple(set(regexPositive),set(regexNegative)) 
# slot2: tuple(set(regexPositive),set(regexNegative)}
if __name__ == "__main__":
    reg = {"coruscant": tuple([set({"coruscant", "cor[a-z]{1,3}ant", "(located|situated) on cor[a-z]{1,3}ant"}),
                          set({"(is not|isn't) on cor[a-z]{1,3}ant", "(is not|isn't) (located|situated) on cor[a-z]{1,3}ant","(located|situated) on ((?!cor[a-z]{1,3}ant).)*$"})])}
    f1 = Frame("headquarters","headquarters","banana",reg,coruscant="")
    print(f1.slot)
    f1.resolve("The headquarters of the Jedi Order is not situated on banana.")
    print(f1.slot)
    pass


