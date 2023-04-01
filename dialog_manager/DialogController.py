import shelve
import random
from enum import Enum
from dialog_manager.DContextModel import DContextModel
from generation.NaturalLanguageGenerator import NaturalLanguageGenerator
from speech.SpeechSynthesis import SpeechSynthesis


class Turn(Enum):
    INTRO = 0
    QUESTION = 1
    OUTRO = 2


class DialogController:
    def __init__(self, n_questions: int = 3):
        assert 3 <= n_questions <= 10, "invalid number of questions!"
        self.scenario = Turn.INTRO
        self.proceed = True
        self.nlg = NaturalLanguageGenerator()
        self.synth = SpeechSynthesis()
        self.context_model = DContextModel()
        self.n_questions = n_questions
        self.questions_dictionary = {}
        with shelve.open("databases/questions_db/questions") as questions_db:
            chosen_questions_keys = random.sample(list(questions_db), self.n_questions)  # n questions from the db
            self.questions_dictionary = {key: questions_db[key] for key in chosen_questions_keys}

        self.qst_generator = self._generate_questions()
        self.current_qst = None
        self.__questions_left = n_questions

    @property
    def questions_left(self):
        return self.n_questions - self.scenario.value

    def next_turn(self, idx=None):
        self.scenario = Turn(self.scenario.value + 1) if idx is None else Turn(idx)

    def _generate_questions(self):
        yield from self.questions_dictionary

    def output_text(self):
        match self.scenario:
            case Turn.INTRO:
                return self.nlg.greetings()
            case Turn.QUESTION:
                key = next(self.qst_generator)
                self.current_qst = (key, self.questions_dictionary[key])
                return self.nlg.ask_nth_question(self.current_qst[1])
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
            case Turn.QUESTION:
                response = self.context_model.decipher_response(user_input, self.current_qst[0])
                return self.nlg.generate_answer(response)
            case Turn.OUTRO:
                pass
            case _:
                pass
