import shelve
import random
from dialog_manager.DContextModel import DContextModel
from generation.NaturalLanguageGenerator import NaturalLanguageGenerator
from speech.SpeechSynthesis import SpeechSynthesis
from utils.enumerators import Turn, Response


class DialogController:
    def __init__(self, n_questions: int = 3):
        assert 3 <= n_questions <= 10, "invalid number of questions!"
        self.scenario = Turn.INTRO
        self.last_response = None
        self.attempts = 0
        self.proceed = True
        self.nlg = NaturalLanguageGenerator()
        self.synth = SpeechSynthesis()
        self.context_model = DContextModel()
        self.n_questions_to_ask = n_questions
        self.questions_dictionary = {}
        with shelve.open("databases/questions_db/questions") as questions_db:
            chosen_questions_keys = random.sample(list(questions_db), self.n_questions_to_ask)  # n questions from db
            self.questions_dictionary = {key: questions_db[key] for key in chosen_questions_keys}

        self.qst_generator = self._generate_questions()
        self.current_qst = None

    def next_turn(self, idx=None):
        self.scenario = Turn(self.scenario.value + 1) if idx is None else Turn(idx)

    def _generate_questions(self):
        yield from self.questions_dictionary

    def _backup_strategy(self):
        pass

    def output_text(self):
        match self.scenario:
            case Turn.INTRO:
                return self.nlg.greetings()
            case Turn.QUESTION:
                if self.last_response != Response.CORRECT:
                    # implement a logic for when we are reacting to a new
                    pass
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
                self.last_response = self.context_model.decipher_response(user_input, self.current_qst[0])
                if self.last_response == Response.CORRECT:
                    self.proceed = True
                    self.n_questions_to_ask -= 1
                else:
                    self.proceed = False
                    self.attempts += 1
                return self.nlg.generate_answer(self.last_response)
            case Turn.OUTRO:
                pass
            case _:
                pass
