from generation.NaturalLanguageGenerator import NaturalLanguageGenerator
from speech.SpeechSynthesis import SpeechSynthesis


class DialogController:
    def __init__(self):
        self.output = "ciccino"
        self.scenario = 0
        self.proceed = True
        self.nlg = NaturalLanguageGenerator
        self.synth = SpeechSynthesis

    def output_text(self):

        match self.scenario:
            case 0:

                pass
            case 1:
                # first question
                pass
            case 2:
                # second string
                pass
            case 3:
                # third question
                pass
            case 9:
                pass
            case 10:
                pass
            case _:
                output = ""
