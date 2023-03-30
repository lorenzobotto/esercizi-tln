from generation.NaturalLanguageGenerator import NaturalLanguageGenerator
from speech.SpeechSynthesis import SpeechSynthesis
from enum import Enum


class Turn(Enum):
    INTRO = 0
    FIRST_QST = 1
    SECOND_QST = 2
    THIRD_QST = 3
    FOURTH_QST = 4
    FIFTH_QST = 5
    OUTRO = 6


class DialogController:
    def __init__(self):
        self.last_output = ""
        self.scenario = Turn.INTRO
        self.proceed = True
        self.nlg = NaturalLanguageGenerator()
        self.synth = SpeechSynthesis()

    def next_turn(self):
        self.scenario = Turn(self.scenario.value + 1)

    def output_text(self):
        match self.scenario:
            case Turn.INTRO:
                self.last_output = self.nlg.greetings()
                return self.last_output
                ##check for input?
            case Turn.FIRST_QST:
                # first question
                pass
            case Turn.SECOND_QST:
                # second string
                pass
            case Turn.THIRD_QST:
                # third question
                pass
            case Turn.FOURTH_QST:
                pass
            case Turn.FIFTH_QST:
                pass
            case Turn.OUTRO:
                pass
            case _:
                pass
