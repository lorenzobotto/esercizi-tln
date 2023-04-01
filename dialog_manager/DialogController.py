import shelve
import random
from enum import Enum
from dialog_manager.DContextModel import DContextModel
from generation.NaturalLanguageGenerator import NaturalLanguageGenerator
from speech.SpeechSynthesis import SpeechSynthesis


class Turn(Enum):
    INTRO = 0
    FIRST_QST = 1
    SECOND_QST = 2
    THIRD_QST = 3
    FOURTH_QST = 4
    FIFTH_QST = 5
    SIXTH_QST = 6
    SEVENTH_QST = 7
    EIGHTH_QST = 8
    NINTH_QST = 9
    TENTH_QST = 10
    OUTRO = 11


class DialogController:
    def __init__(self, n_questions: int = 3):
        assert 3 <= n_questions <= 10, "invalid number of questions!"
        self.scenario = Turn.INTRO
        self.proceed = True
        self.nlg = NaturalLanguageGenerator()
        self.synth = SpeechSynthesis()
        self.context_model = DContextModel()
        self.questions_generator = self._generate_questions(n_questions)
        # self.

    def next_turn(self, idx=None):
        self.scenario = Turn(self.scenario.value + 1) if idx is None else Turn(idx)

    def _generate_questions(self, n_questions):
        self.dictionary = {}
        with shelve.open("databases/questions_db/questions") as questions_db:
            chosen_questions_keys = random.sample(list(questions_db), n_questions)  # 3 random questions from the db
            self.dictionary = {key: questions_db[key] for key in chosen_questions_keys}
        yield from self.dictionary

    def output_text(self):
        match self.scenario:
            case Turn.INTRO:
                return self.nlg.greetings()
            case Turn.FIRST_QST:
                # question = self.nlg.ask_nth_question()
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
            case Turn.SIXTH_QST:
                pass
            case Turn.SEVENTH_QST:
                pass
            case Turn.EIGHTH_QST:
                pass
            case Turn.NINTH_QST:
                pass
            case Turn.TENTH_QST:
                pass
            case Turn.OUTRO:
                pass
            case _:
                pass

    def elaborate_user_input(self, user_input: str):
        match self.scenario:
            case Turn.INTRO:
                self.context_model.find_name(user_input)
                self.next_turn()
                return self.nlg.greets_user(self.context_model.user_name)
            case Turn.FIRST_QST:
                pass
            case Turn.SECOND_QST:
                pass
            case Turn.THIRD_QST:
                pass
            case Turn.FOURTH_QST:
                pass
            case Turn.FIFTH_QST:
                pass
            case Turn.SIXTH_QST:
                pass
            case Turn.SEVENTH_QST:
                pass
            case Turn.EIGHTH_QST:
                pass
            case Turn.NINTH_QST:
                pass
            case Turn.TENTH_QST:
                pass
            case Turn.OUTRO:
                pass
            case _:
                pass
