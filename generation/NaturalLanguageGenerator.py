from simplenlg.framework import *
from simplenlg.realiser.english import *
from simplenlg.phrasespec import *
from simplenlg.features import *
import random

# import sys
# sys.path.append('C:\\Users\\lores\\Desktop\\mazzei-chatbot')

from utils.enumerators import Response
from utils.enumerators import Turn


class NaturalLanguageGenerator:

    def __init__(self):
        lexicon = Lexicon.getDefaultLexicon()
        self.nlg_factory = NLGFactory(lexicon)
        self.realiser = Realiser(lexicon)
        self.affirmative_answers = {}
        self.negative_answers = {}
        self.uncertain_answers = {}
        self.retry_answers = {}
        self._generate_affirmative_answers()
        self._generate_negative_answers()
        self._generate_uncertain_answers()
        self._generate_retry_answers()

    def _greetings(self) -> str:
        # Create a sentence with the form "Hello, I am Obi-1 and I will question you about Jedi culture. What is your name?"
        s_0 = self.nlg_factory.createClause("Hello")

        # Create a sentence with the form "I am Obi-1"
        subj_1 = self.nlg_factory.createNounPhrase("I")
        verb_1 = self.nlg_factory.createVerbPhrase("be")
        obj_1 = self.nlg_factory.createNounPhrase("Obi-1")
        s_1 = self.nlg_factory.createClause(subj_1, verb_1, obj_1)

        # Create a sentence with the form "I will question you"
        subj_2 = self.nlg_factory.createNounPhrase("I")
        verb_2 = self.nlg_factory.createVerbPhrase("question")
        verb_2.setFeature(Feature.TENSE, Tense.FUTURE)
        obj_2 = self.nlg_factory.createNounPhrase("you")
        s_2 = self.nlg_factory.createClause(subj_2, verb_2, obj_2)

        # Create a preposition phrase with the form "about Jedi culture"
        p_1 = self.nlg_factory.createPrepositionPhrase("about")
        p_1.addComplement("Jedi culture")

        # I add the preposition phrase to the sentence
        s_2.addComplement(p_1)

        # I tie the sentence 0 and sentence 1 together with a comma
        c_1 = self.nlg_factory.createCoordinatedPhrase()
        c_1.setConjunction(",")
        c_1.addCoordinate(s_0)
        c_1.addCoordinate(s_1)

        # I tie the sentence generated in the previous step and sentence 2 together with the word "and"
        c_2 = self.nlg_factory.createCoordinatedPhrase()
        c_2.setConjunction("and")
        c_2.addCoordinate(c_1)
        c_2.addCoordinate(s_2)

        # Create a sentence with the form "What is your name?"
        subj_3 = self.nlg_factory.createNounPhrase("name")
        verb_3 = self.nlg_factory.createVerbPhrase("be")
        pron_3 = self.nlg_factory.createWord("you", LexicalCategory.PRONOUN)
        pron_3.setFeature(Feature.POSSESSIVE, True)
        subj_3.setDeterminer(pron_3)
        s_3 = self.nlg_factory.createClause(subj_3, verb_3)
        s_3.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.WHAT_OBJECT)

        # I tie the three sentences together with a new line
        return f"{self.realiser.realiseSentence(c_2)}\n{self.realiser.realiseSentence(s_3)}"

    def _greets_user(self, name: str) -> str:
        # Create a sentence with the form "Hello, name!" if the name is not None, otherwise "Hello, aspiring Padawan!"
        s_0 = self.nlg_factory.createClause("Hello")
        if name:
            subj_1 = self.nlg_factory.createNounPhrase(name)
            s_1 = self.nlg_factory.createClause(subj_1)
            c_1 = self.nlg_factory.createCoordinatedPhrase()
            c_1.setConjunction(",")
            c_1.addCoordinate(s_0)
            c_1.addCoordinate(s_1)
        else:
            subj_1 = self.nlg_factory.createNounPhrase("Padawan")
            subj_1.setDeterminer("aspiring")
            s_1 = self.nlg_factory.createClause(subj_1)
            c_1 = self.nlg_factory.createCoordinatedPhrase()
            c_1.setConjunction(",")
            c_1.addCoordinate(s_0)
            c_1.addCoordinate(s_1)

        # Create a sentence with the form "We can start the interview"
        subj_1 = self.nlg_factory.createNounPhrase("we")
        verb_1 = self.nlg_factory.createVerbPhrase("start")
        obj_1 = self.nlg_factory.createNounPhrase("the", "interview")
        s_1 = self.nlg_factory.createClause(subj_1, verb_1, obj_1)
        s_1.setFeature(Feature.MODAL, "can")

        # Create a preposition phrase with the form "with the first question"
        prep_2 = self.nlg_factory.createPrepositionPhrase("with")
        subj_2 = self.nlg_factory.createNounPhrase("the", "question")
        subj_2.addModifier("first")
        prep_2.addComplement(subj_2)
        s_1.addPostModifier(prep_2)
        return f"{self.realiser.realiseSentence(c_1)}\n{self.realiser.realiseSentence(s_1)}"

    def _ask_nth_question(self, question) -> str:
        # Create a sentence with for the question extracted from a PD
        s_1 = self.nlg_factory.createSentence(question)
        return self.realiser.realiseSentence(s_1)

    def _generate_affirmative_answers(self):
        # 1. Create a sentence with the form "Yes, that is correct."
        s_0 = self.nlg_factory.createClause("Yes")
        adv_1 = self.nlg_factory.createWord("that", LexicalCategory.ADVERB)
        verb_1 = self.nlg_factory.createVerbPhrase("be")
        verb_1.addModifier(adv_1)
        obj_1 = self.nlg_factory.createNounPhrase("correct")
        s_1 = self.nlg_factory.createClause(verb_1, obj_1)

        # I tie the two sentences together with a comma
        c_1 = self.nlg_factory.createCoordinatedPhrase()
        c_1.setConjunction(",")
        c_1.addCoordinate(s_0)
        c_1.addCoordinate(s_1)
        rs_c1 = self.realiser.realiseSentence(c_1)
        self.affirmative_answers.update({
            rs_c1: 1
        })

        # 2. Create a sentence with the form "That is exactly right!"
        adv_2 = self.nlg_factory.createWord("that", LexicalCategory.ADVERB)
        verb_2 = self.nlg_factory.createVerbPhrase("be")
        verb_2.addModifier(adv_2)
        obj_2 = self.nlg_factory.createNounPhrase("right")
        adv_2 = self.nlg_factory.createWord("exactly", LexicalCategory.ADVERB)
        obj_2.addPreModifier(adv_2)
        s_2 = self.nlg_factory.createClause(verb_2, obj_2)
        rs_s2 = self.realiser.realiseSentence(s_2)
        self.affirmative_answers.update({
            rs_s2: 1
        })

        # 3. Create a sentence with the form "You are absolutely correct! You have a great understanding of the topic at hand."
        # Create a sentence with the form "You are absolutely correct!"
        subj_3 = self.nlg_factory.createNounPhrase("you")
        verb_3 = self.nlg_factory.createVerbPhrase("be")
        obj_3 = self.nlg_factory.createNounPhrase("correct!")
        adv_1 = self.nlg_factory.createWord("absolutely", LexicalCategory.ADVERB)
        obj_3.addPreModifier(adv_1)
        s_3 = self.nlg_factory.createClause(subj_3, verb_3, obj_3)

        # Create a sentence with the form "You have a great understanding"
        subj_4 = self.nlg_factory.createNounPhrase("you")
        verb_4 = self.nlg_factory.createVerbPhrase("have")
        obj_4 = self.nlg_factory.createNounPhrase("understanding")
        adj_4 = self.nlg_factory.createWord("a great", LexicalCategory.ADJECTIVE)
        obj_4.addModifier(adj_4)
        s_4 = self.nlg_factory.createClause(subj_4, verb_4, obj_4)

        # Create a preposition phrase with the form "of the topic at hand"
        prep_5 = self.nlg_factory.createPrepositionPhrase("of")
        subj_5 = self.nlg_factory.createNounPhrase("the", "topic")
        subj_5.addModifier("at hand")

        # I tie the preposition phrase to the previous sentence
        prep_5.addComplement(subj_5)
        s_4.addPostModifier(prep_5)

        # I tie the two sentences together with a space
        self.affirmative_answers.update({
            f"{self.realiser.realiseSentence(s_3)[:-1]} {self.realiser.realiseSentence(s_4)}": 1
        })

        # 4. Create a sentence with the form "You are spot on! Your answer perfectly aligns with the correct solution."
        # Create a sentence with the form "You are spot on!"
        subj_6 = self.nlg_factory.createNounPhrase("you")
        verb_6 = self.nlg_factory.createVerbPhrase("be")
        obj_6 = self.nlg_factory.createNounPhrase("spot")
        obj_6.addPostModifier("on!")
        s_6 = self.nlg_factory.createClause(subj_6, verb_6, obj_6)

        # Create a sentence with the form "Your answer perfectly aligns with the correct solution."
        # Create a sentence with the form "Your answer perfectly aligns"
        subj_7 = self.nlg_factory.createNounPhrase("answer")
        pron_7 = self.nlg_factory.createWord("you", LexicalCategory.PRONOUN)
        pron_7.setFeature(Feature.POSSESSIVE, True)
        subj_7.setSpecifier(pron_7)
        verb_7 = self.nlg_factory.createVerbPhrase("align")
        adv_7 = self.nlg_factory.createWord("perfectly", LexicalCategory.ADVERB)
        verb_7.addModifier(adv_7)
        s_7 = self.nlg_factory.createClause(subj_7, verb_7)

        # Create a preposition phrase with the form "with the correct solution"
        prep_2 = self.nlg_factory.createPrepositionPhrase("with")
        subj_8 = self.nlg_factory.createNounPhrase("the", "solution")
        subj_8.addModifier("correct")
        prep_2.addComplement(subj_8)
        s_7.addPostModifier(prep_2)

        # I tie the two sentences together with a space
        self.affirmative_answers.update({
            f"{self.realiser.realiseSentence(s_6)[:-1]} {self.realiser.realiseSentence(s_7)}": 1
        })

        # 5. Create a sentence with the form "Bingo! You got it right. Your response is completely accurate."
        # Create a sentence with the form "Bingo!"
        s_8 = self.nlg_factory.createClause("Bingo!")

        # Create a sentence with the form "You got it right."
        subj_9 = self.nlg_factory.createNounPhrase("you")
        verb_9 = self.nlg_factory.createVerbPhrase("get")
        verb_9.setFeature(Feature.TENSE, Tense.PAST)
        obj_9 = self.nlg_factory.createNounPhrase("right")
        pron_9 = self.nlg_factory.createWord("it", LexicalCategory.PRONOUN)
        obj_9.addPreModifier(pron_9)
        s_9 = self.nlg_factory.createClause(subj_9, verb_9, obj_9)

        # Create a sentence with the form "Your response is completely accurate."
        subj_10 = self.nlg_factory.createNounPhrase("response")
        pron_10 = self.nlg_factory.createWord("you", LexicalCategory.PRONOUN)
        pron_10.setFeature(Feature.POSSESSIVE, True)
        subj_10.setSpecifier(pron_10)
        verb_10 = self.nlg_factory.createVerbPhrase("be")
        obj_10 = self.nlg_factory.createNounPhrase("accurate")
        adv_10 = self.nlg_factory.createWord("completely", LexicalCategory.ADVERB)
        obj_10.addPreModifier(adv_10)
        s_10 = self.nlg_factory.createClause(subj_10, verb_10, obj_10)

        self.affirmative_answers.update({
            f"{self.realiser.realiseSentence(s_8)[:-1]} {self.realiser.realiseSentence(s_9)} {self.realiser.realiseSentence(s_10)}": 1
        })

    def _generate_negative_answers(self):
        # 1. Create a sentence with the form "I am sorry, but that is false."
        # Create a sentence with the form "I am sorry."
        subj_1 = self.nlg_factory.createNounPhrase("I")
        verb_1 = self.nlg_factory.createVerbPhrase("be")
        obj_1 = self.nlg_factory.createNounPhrase("sorry")
        s_1 = self.nlg_factory.createClause(subj_1, verb_1, obj_1)

        # Create a sentence with the form "but that is false."
        prep_2 = self.nlg_factory.createPrepositionPhrase("but")
        subj_2 = self.nlg_factory.createNounPhrase("that")
        verb_2 = self.nlg_factory.createVerbPhrase("be")
        obj_2 = self.nlg_factory.createNounPhrase("false")
        subj_2.addPreModifier(prep_2)
        s_2 = self.nlg_factory.createClause(subj_2, verb_2, obj_2)

        # I tie the two sentences together with a comma
        c_1 = self.nlg_factory.createCoordinatedPhrase()
        c_1.setConjunction(",")
        c_1.addCoordinate(s_1)
        c_1.addCoordinate(s_2)

        # I add the sentence to the dictionary
        self.negative_answers.update({
            self.realiser.realiseSentence(c_1): 1
        })

        # 2. Create a sentence with the form "It doesn't match with my prior knowledge."
        # Create a sentence with the form "It doesn't match"
        pron_3 = self.nlg_factory.createWord("it", LexicalCategory.PRONOUN)
        verb_3 = self.nlg_factory.createVerbPhrase("do match")
        verb_3.setFeature(Feature.NEGATED, True)
        s_3 = self.nlg_factory.createClause(pron_3, verb_3)

        # Create a sentence with the form "with my prior knowledge."
        prep_4 = self.nlg_factory.createPrepositionPhrase("with")
        subj_4 = self.nlg_factory.createNounPhrase("knowledge")
        adj_4 = self.nlg_factory.createAdjectivePhrase("prior")
        subj_4.addModifier(adj_4)
        pron_4 = self.nlg_factory.createWord("I", LexicalCategory.PRONOUN)
        pron_4.setFeature(Feature.POSSESSIVE, True)
        subj_4.setDeterminer(pron_4)
        prep_4.addComplement(subj_4)
        s_4 = self.nlg_factory.createClause(prep_4)

        # I tie the two sentences together without conjunction
        c_1 = self.nlg_factory.createCoordinatedPhrase()
        c_1.setConjunction("")
        c_1.addCoordinate(s_3)
        c_1.addCoordinate(s_4)

        # I add the sentence to the dictionary
        self.negative_answers.update({
            self.realiser.realiseSentence(c_1): 1
        })

        # 3. Create a sentence with the form "That is not the answer that i expected."
        # Create a sentence with the form "That is not the answer"
        subj_5 = self.nlg_factory.createNounPhrase("that")
        verb_5 = self.nlg_factory.createVerbPhrase("be")
        verb_5.setFeature(Feature.NEGATED, True)
        obj_5 = self.nlg_factory.createNounPhrase("the", "answer")
        s_5 = self.nlg_factory.createClause(subj_5, verb_5, obj_5)

        # Create a sentence with the form "that i expected."
        subj_6 = self.nlg_factory.createNounPhrase("I")
        verb_6 = self.nlg_factory.createVerbPhrase("expect")
        verb_6.setFeature(Feature.TENSE, Tense.PAST)
        s_6 = self.nlg_factory.createClause(subj_6, verb_6)
        s_5.addComplement(s_6)

        # I add the sentence to the dictionary
        self.negative_answers.update({
            self.realiser.realiseSentence(s_5): 1
        })

        # 4. Create a sentence with the form "I don't really think so."
        subj_7 = self.nlg_factory.createNounPhrase("I")
        verb_7 = self.nlg_factory.createVerbPhrase("think")
        verb_7.setFeature(Feature.NEGATED, True)
        adv_7 = self.nlg_factory.createAdverbPhrase("really")
        verb_7.addComplement(adv_7)
        adv_8 = self.nlg_factory.createAdverbPhrase("so")
        verb_7.addComplement(adv_8)
        s_7 = self.nlg_factory.createClause(subj_7, verb_7)

        # I add the sentence to the dictionary
        self.negative_answers.update({
            self.realiser.realiseSentence(s_7): 1
        })

        # 5. Create a sentence with the form "I am sorry, I doubt that is the correct answer."
        # Create a sentence with the form "I am sorry"
        subj_8 = self.nlg_factory.createNounPhrase("I")
        verb_8 = self.nlg_factory.createVerbPhrase("be")
        obj_8 = self.nlg_factory.createNounPhrase("sorry")
        s_8 = self.nlg_factory.createClause(subj_8, verb_8, obj_8)

        # Create a sentence with the form "I doubt that is the correct answer."
        subj_9 = self.nlg_factory.createNounPhrase("I")
        verb_9 = self.nlg_factory.createVerbPhrase("doubt")
        s_9 = self.nlg_factory.createClause(subj_9, verb_9)

        # I tie the two sentences together with a comma
        c_9 = self.nlg_factory.createCoordinatedPhrase()
        c_9.setConjunction(",")
        c_9.addCoordinate(s_8)
        c_9.addCoordinate(s_9)

        # Create a sentence with the form "that is the correct answer."
        subj_10 = self.nlg_factory.createNounPhrase("that")
        verb_10 = self.nlg_factory.createVerbPhrase("be")
        obj_10 = self.nlg_factory.createNounPhrase("the", "answer")
        adj_10 = self.nlg_factory.createAdjectivePhrase("correct")
        obj_10.addModifier(adj_10)
        s_10 = self.nlg_factory.createClause(subj_10, verb_10, obj_10)

        c_10 = self.nlg_factory.createCoordinatedPhrase()
        c_10.setConjunction("")
        c_10.addCoordinate(c_9)
        c_10.addCoordinate(s_10)

        # I add the sentence to the dictionary
        self.negative_answers.update({
            self.realiser.realiseSentence(c_10): 1
        })

    def _generate_uncertain_answers(self):
        # 1. Create a sentence with the form "Sorry, I didn't catch that."
        # Create a sentence with the form "Sorry"
        s_0 = self.nlg_factory.createClause("Sorry")

        # Create a sentence with the form "I didn't catch that."
        subj_1 = self.nlg_factory.createNounPhrase("I")
        verb_1 = self.nlg_factory.createVerbPhrase("catch")
        verb_1.setFeature(Feature.NEGATED, True)
        verb_1.setFeature(Feature.TENSE, Tense.PAST)
        obj_1 = self.nlg_factory.createNounPhrase("that")
        s_1 = self.nlg_factory.createClause(subj_1, verb_1, obj_1)

        # I tie the two sentences together with a comma
        c_1 = self.nlg_factory.createCoordinatedPhrase()
        c_1.setConjunction(",")
        c_1.addCoordinate(s_0)
        c_1.addCoordinate(s_1)

        # I add the sentence to the dictionary
        self.uncertain_answers.update({
            self.realiser.realiseSentence(c_1): 1
        })

        # 2. Create a sentence with the form "I am sorry, I didn't quite understand what you said."
        # Create a sentence with the form "I am sorry"
        subj_2 = self.nlg_factory.createNounPhrase("I")
        verb_2 = self.nlg_factory.createVerbPhrase("be")
        obj_2 = self.nlg_factory.createNounPhrase("sorry")
        s_2 = self.nlg_factory.createClause(subj_2, verb_2, obj_2)

        # Create a sentence with the form "I didn't quite understand"
        subj_3 = self.nlg_factory.createNounPhrase("I")
        verb_3 = self.nlg_factory.createVerbPhrase("understand")
        verb_3.setFeature(Feature.NEGATED, True)
        verb_3.setFeature(Feature.TENSE, Tense.PAST)
        adv_3 = self.nlg_factory.createWord("quite", LexicalCategory.ADVERB)
        verb_3.addModifier(adv_3)
        s_3 = self.nlg_factory.createClause(subj_3, verb_3)

        # Create a sentence with the form "what you said."
        p_4 = self.nlg_factory.createPrepositionPhrase("what")
        subj_4 = self.nlg_factory.createNounPhrase("you")
        verb_4 = self.nlg_factory.createVerbPhrase("say")
        verb_4.setFeature(Feature.TENSE, Tense.PAST)
        subj_4.addPreModifier(p_4)
        s_4 = self.nlg_factory.createClause(subj_4, verb_4)

        # I tie the three sentences together with a space
        c_4 = self.nlg_factory.createCoordinatedPhrase()
        c_4.setConjunction("")
        c_4.addCoordinate(s_3)
        c_4.addCoordinate(s_4)

        # I tie the two sentences together with a comma
        c_5 = self.nlg_factory.createCoordinatedPhrase()
        c_5.setConjunction(",")
        c_5.addCoordinate(s_2)
        c_5.addCoordinate(c_4)

        # I add the sentence to the dictionary
        self.uncertain_answers.update({
            self.realiser.realiseSentence(c_5): 1
        })

        # 3. Create a sentence with the form "Sorry, I missed what you just said."
        # Create a sentence with the form "Sorry"
        s_6 = self.nlg_factory.createClause("Sorry")

        # Create a sentence with the form "I missed"
        subj_7 = self.nlg_factory.createNounPhrase("I")
        verb_7 = self.nlg_factory.createVerbPhrase("miss")
        verb_7.setFeature(Feature.TENSE, Tense.PAST)
        s_7 = self.nlg_factory.createClause(subj_7, verb_7)

        # I tie the two sentences together with a comma
        c_8 = self.nlg_factory.createCoordinatedPhrase()
        c_8.setConjunction(",")
        c_8.addCoordinate(s_6)
        c_8.addCoordinate(s_7)

        # Create a sentence with the form "what you just said."
        p_9 = self.nlg_factory.createPrepositionPhrase("what")
        subj_9 = self.nlg_factory.createNounPhrase("you")
        verb_9 = self.nlg_factory.createVerbPhrase("say")
        verb_9.setFeature(Feature.TENSE, Tense.PAST)
        adv_9 = self.nlg_factory.createWord("just", LexicalCategory.ADVERB)
        verb_9.addModifier(adv_9)
        subj_9.addPreModifier(p_9)
        s_9 = self.nlg_factory.createClause(subj_9, verb_9)

        # I tie the two sentences together with a space
        c_9 = self.nlg_factory.createCoordinatedPhrase()
        c_9.setConjunction("")
        c_9.addCoordinate(c_8)
        c_9.addCoordinate(s_9)

        # I add the sentence to the dictionary
        self.uncertain_answers.update({
            self.realiser.realiseSentence(c_9): 1
        })

        # 4. Create a sentence with the form "I did not get that."
        subj_10 = self.nlg_factory.createNounPhrase("I")
        verb_10 = self.nlg_factory.createVerbPhrase("get")
        obj_10 = self.nlg_factory.createNounPhrase("that")
        verb_10.setFeature(Feature.TENSE, Tense.PAST)
        verb_10.setFeature(Feature.NEGATED, True)
        s_10 = self.nlg_factory.createClause(subj_10, verb_10, obj_10)

        # I add the sentence to the dictionary
        self.uncertain_answers.update({
            self.realiser.realiseSentence(s_10): 1
        })

        # 5. Create a sentence with the form "I didn't entirely understand it."
        subj_11 = self.nlg_factory.createNounPhrase("I")
        verb_11 = self.nlg_factory.createVerbPhrase("understand")
        obj_11 = self.nlg_factory.createNounPhrase("it")
        adv_11 = self.nlg_factory.createWord("entirely", LexicalCategory.ADVERB)
        verb_11.addModifier(adv_11)
        verb_11.setFeature(Feature.TENSE, Tense.PAST)
        verb_11.setFeature(Feature.NEGATED, True)
        s_11 = self.nlg_factory.createClause(subj_11, verb_11, obj_11)

        # I add the sentence to the dictionary
        self.uncertain_answers.update({
            self.realiser.realiseSentence(s_11): 1
        })

    def _generate_retry_answers(self) -> str:
        # 1. Create a sentence with the form "Could you please repeat?"
        subj_1 = self.nlg_factory.createNounPhrase("you")
        verb_1 = self.nlg_factory.createVerbPhrase("repeat")
        verb_1.addModifier("please")
        s_1 = self.nlg_factory.createClause(subj_1, verb_1)
        s_1.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
        s_1.setFeature(Feature.MODAL, "could")

        # I add the sentence to the dictionary
        self.retry_answers.update({
            self.realiser.realiseSentence(s_1): 1
        })

        # 2. Create a sentence with the form "Can you say it again?"
        subj_2 = self.nlg_factory.createNounPhrase("you")
        verb_2 = self.nlg_factory.createVerbPhrase("say")
        obj_2 = self.nlg_factory.createNounPhrase("again")
        pron_2 = self.nlg_factory.createWord("it", LexicalCategory.PRONOUN)
        obj_2.addPreModifier(pron_2)
        s_2 = self.nlg_factory.createClause(subj_2, verb_2, obj_2)
        s_2.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
        s_2.setFeature(Feature.MODAL, "can")

        # I add the sentence to the dictionary
        self.retry_answers.update({
            self.realiser.realiseSentence(s_2): 1
        })

        # 3. Create a sentence with the form "Could you say that one more time"
        subj_3 = self.nlg_factory.createNounPhrase("you")
        verb_3 = self.nlg_factory.createVerbPhrase("say")
        s_3 = self.nlg_factory.createClause(subj_3, verb_3)
        s_3.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
        s_3.setFeature(Feature.MODAL, "could")

        noun_4 = self.nlg_factory.createClause("time")
        adv_4 = self.nlg_factory.createWord("one more", LexicalCategory.ADJECTIVE)
        noun_4.addFrontModifier(adv_4)

        s_3.addComplement(noun_4)

        # Create a sentence with the form "please?"
        s_4 = self.nlg_factory.createClause("please?")

        # I tie the two sentences together with a comma
        c_5 = self.nlg_factory.createCoordinatedPhrase()
        c_5.setConjunction(",")
        c_5.addCoordinate(s_3)
        c_5.addCoordinate(s_4)

        # I add the sentence to the dictionary
        self.retry_answers.update({
            self.realiser.realiseSentence(c_5): 1
        })

        # 4. Create a sentence with the form "Could you please reiterate your point?"
        subj_6 = self.nlg_factory.createNounPhrase("you")
        verb_6 = self.nlg_factory.createVerbPhrase("reiterate")
        adv_6 = self.nlg_factory.createWord("please", LexicalCategory.ADVERB)
        verb_6.addModifier(adv_6)
        obj_6 = self.nlg_factory.createNounPhrase("point")
        pron_6 = self.nlg_factory.createWord("you", LexicalCategory.PRONOUN)
        pron_6.setFeature(Feature.POSSESSIVE, True)
        obj_6.setDeterminer(pron_6)
        s_6 = self.nlg_factory.createClause(subj_6, verb_6, obj_6)
        s_6.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
        s_6.setFeature(Feature.MODAL, "could")

        # I add the sentence to the dictionary
        self.retry_answers.update({
            self.realiser.realiseSentence(s_6): 1
        })

        # 5. Create a sentence with the form "Could you kindly rephrase what you just said?"
        subj_7 = self.nlg_factory.createNounPhrase("you")
        verb_7 = self.nlg_factory.createVerbPhrase("rephrase")
        adj_7 = self.nlg_factory.createWord("kindly", LexicalCategory.ADVERB)
        verb_7.addModifier(adj_7)
        s_7 = self.nlg_factory.createClause(subj_7, verb_7)
        s_7.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
        s_7.setFeature(Feature.MODAL, "could")

        # Create a sentence with the form "what you just said."
        p_8 = self.nlg_factory.createPrepositionPhrase("what")
        subj_8 = self.nlg_factory.createNounPhrase("you")
        verb_8 = self.nlg_factory.createVerbPhrase("say")
        verb_8.setFeature(Feature.TENSE, Tense.PAST)
        adv_8 = self.nlg_factory.createWord("just", LexicalCategory.ADVERB)
        verb_8.addModifier(adv_8)
        subj_8.addPreModifier(p_8)
        s_8 = self.nlg_factory.createClause(subj_8, verb_8)

        # I tie the two sentences together with a space
        c_11 = self.nlg_factory.createCoordinatedPhrase()
        c_11.setConjunction("")
        c_11.addCoordinate(s_7)
        c_11.addCoordinate(s_8)

        # I add the sentence to the dictionary
        self.retry_answers.update({
            f"{self.realiser.realiseSentence(c_11)[:-1]}?": 1
        })

    def _generate_outro_answers(self, **kwargs) -> str:
        passed = kwargs["passed"]
        tot_qst = kwargs["tot_qst"]
        correct_qst = kwargs["correct_qst"]

        random_int = random.randint(1, 2)
        if random_int == 1:
            # 1. Create a sentence with the form "Congratulations, you passed the test with flying colors! You got two out of three questions correct, making you a Padawan!" if passed
            # or "Unfortunately, I have to inform that you did not pass the test. You got only 3 out of 3 questions correct, not making you a Padawan!" if not passed
            if passed:
                s_0 = self.nlg_factory.createClause("Congratulations")
            else:
                s_0 = self.nlg_factory.createClause("Unfortunately")

            if passed:
                # Create a sentence with the form "you passed the test"
                subj_1 = self.nlg_factory.createNounPhrase("you")
                verb_1 = self.nlg_factory.createVerbPhrase("pass")
                verb_1.setFeature(Feature.TENSE, Tense.PAST)
                obj_1 = self.nlg_factory.createNounPhrase("the", "test")
                s_1 = self.nlg_factory.createClause(subj_1, verb_1, obj_1)
            else:
                # Create a sentence with the form "I have to inform that you did not pass the test."
                subj_1 = self.nlg_factory.createNounPhrase("I")
                verb_1 = self.nlg_factory.createVerbPhrase("have to inform")
                s_1 = self.nlg_factory.createClause(subj_1, verb_1)

                # Create a sentence with the form "you did not pass the test"
                subj_2 = self.nlg_factory.createNounPhrase("you")
                verb_2 = self.nlg_factory.createVerbPhrase("pass")
                verb_2.setFeature(Feature.TENSE, Tense.PAST)
                verb_2.setFeature(Feature.NEGATED, True)
                obj_2 = self.nlg_factory.createNounPhrase("the", "test")
                s_2 = self.nlg_factory.createClause(subj_2, verb_2, obj_2)

                s_1.addComplement(s_2)


            # I tie the two sentences together with a comma
            c_1 = self.nlg_factory.createCoordinatedPhrase()
            c_1.setConjunction(",")
            c_1.addCoordinate(s_0)
            c_1.addCoordinate(s_1)

            if passed:
                # Create a sentence with the form "with flying colors!"
                prep_2 = self.nlg_factory.createPrepositionPhrase("with")
                adv_2 = self.nlg_factory.createWord("flying", LexicalCategory.ADJECTIVE)
                subj_1 = self.nlg_factory.createNounPhrase("color")
                subj_1.addModifier(adv_2)
                s_2 = self.nlg_factory.createClause(prep_2, subj_1)
                s_2.setPlural(True)
            
                # I tie the two sentences together without a space
                c_2 = self.nlg_factory.createCoordinatedPhrase()
                c_2.setConjunction("")
                c_2.addCoordinate(c_1)
                c_2.addCoordinate(s_2)

            # Create a sentence with the form "You got two out of three questions correct"
            subj_3 = self.nlg_factory.createNounPhrase("you")
            verb_3 = self.nlg_factory.createVerbPhrase("get")
            verb_3.setFeature(Feature.TENSE, Tense.PAST)
            obj_3 = self.nlg_factory.createNounPhrase(f"{correct_qst} out of {tot_qst} questions")
            obj_3.setPlural(True)
            adj_3 = self.nlg_factory.createWord("correct", LexicalCategory.ADJECTIVE)
            verb_3.addModifier(adj_3)
            if not passed:
                # I add the adverb "only" if the user did not pass the test for making the sentence: "You got only two out of three questions correct"
                adv_3 = self.nlg_factory.createWord("only", LexicalCategory.ADVERB)
                obj_3.addPreModifier(adv_3)
            s_3 = self.nlg_factory.createClause(subj_3, verb_3, obj_3)
            
            # Create a sentence with the form "making you a Padawan!"
            verb_4 = self.nlg_factory.createVerbPhrase("make")
            verb_4.setFeature(Feature.PROGRESSIVE, True)
            if not passed:
                # I negate the verb if the user did not pass the test for making the sentence: "not making you a Padawan!"
                verb_4.setFeature(Feature.NEGATED, True)
            pron_4 = self.nlg_factory.createWord("you", LexicalCategory.PRONOUN)
            verb_4.addModifier(pron_4)
            obj_4 = self.nlg_factory.createNounPhrase("a", "Padawan!")
            s_4 = self.nlg_factory.createClause(verb_4, obj_4)

            if passed:
                return f"{self.realiser.realiseSentence(c_2)[:-1]}! {self.realiser.realiseSentence(s_3)[:-1]}, {self.realiser.realiseSentence(s_4)[3:-1]}"
            else:
                return f"{self.realiser.realiseSentence(c_1)} {self.realiser.realiseSentence(s_3)[:-1]}, {self.realiser.realiseSentence(s_4)[3:-1]}"

        else:
            # 2. Create a sentence with the form "Well done! You successfully passed the test, answering two out of three questions correctly, proving that you are a Padawan!"
            if passed:
                # Create a sentence with the form "Well done!"
                s_0 = self.nlg_factory.createClause("Well done!")

                # Create a sentence with the form "you successfully passed the test"
                subj_1 = self.nlg_factory.createNounPhrase("you")
                verb_1 = self.nlg_factory.createVerbPhrase("pass")
                verb_1.setFeature(Feature.TENSE, Tense.PAST)
                adv_1 = self.nlg_factory.createWord("successfully", LexicalCategory.ADVERB)
                verb_1.addModifier(adv_1)
                obj_1 = self.nlg_factory.createNounPhrase("the", "test")
                s_1 = self.nlg_factory.createClause(subj_1, verb_1, obj_1)

            else:
                # Create a sentence with the form "Regrettably, you failed the test"
                s_0 = self.nlg_factory.createClause("Regrettably")

                # Create a sentence with the form "you failed the test"
                subj_1 = self.nlg_factory.createNounPhrase("you")
                verb_1 = self.nlg_factory.createVerbPhrase("fail")
                verb_1.setFeature(Feature.TENSE, Tense.PAST)
                obj_1 = self.nlg_factory.createNounPhrase("the", "test")
                s_1 = self.nlg_factory.createClause(subj_1, verb_1, obj_1)

                # I tie the two sentences together with a comma
                c_1 = self.nlg_factory.createCoordinatedPhrase()
                c_1.setConjunction(",")
                c_1.addCoordinate(s_0)
                c_1.addCoordinate(s_1)

            # Create a sentence with the form "answering two out of three questions correctly" if passed
            if passed:
                verb_2 = self.nlg_factory.createVerbPhrase("answer")
                verb_2.setFeature(Feature.PROGRESSIVE, True)
            else:
                # I change the verb if the user did not pass the test for making the sentence: "You answered only two out of three questions correctly"
                subj_2 = self.nlg_factory.createNounPhrase("you")
                verb_2 = self.nlg_factory.createVerbPhrase("answer")
                verb_2.setFeature(Feature.TENSE, Tense.PAST)
            obj_2 = self.nlg_factory.createNounPhrase(f"{correct_qst} out of {tot_qst} questions")
            adj_2 = self.nlg_factory.createWord("correctly", LexicalCategory.ADJECTIVE)
            obj_2.addPostModifier(adj_2)
            if not passed:
                # I add the adverb "only" if the user did not pass the test
                adv_2 = self.nlg_factory.createWord("only", LexicalCategory.ADVERB)
                obj_2.addPreModifier(adv_2)
            if passed:
                s_2 = self.nlg_factory.createClause(verb_2, obj_2)
            else:
                s_2 = self.nlg_factory.createClause(subj_2, verb_2, obj_2)

            # Create a sentence with the form "proving that you are a Padawan!"
            verb_3 = self.nlg_factory.createVerbPhrase("prove")
            verb_3.setFeature(Feature.PROGRESSIVE, True)
            s_3 = self.nlg_factory.createClause(verb_3)
            subj_4 = self.nlg_factory.createNounPhrase("you")
            verb_4 = self.nlg_factory.createVerbPhrase("be")
            if not passed:
                # I negate the verb if the user did not pass the test for making the sentence: "not proving that you are a Padawan!"
                verb_4.setFeature(Feature.NEGATED, True)
            obj_4 = self.nlg_factory.createNounPhrase("a", "Padawan!")
            s_4 = self.nlg_factory.createClause(subj_4, verb_4, obj_4)

            s_3.addComplement(s_4)
            
            if passed:
                return f"{self.realiser.realiseSentence(s_0)[:-1]} {self.realiser.realiseSentence(s_1)[:-1]}, {self.realiser.realiseSentence(s_2)[3:-1]}, {self.realiser.realiseSentence(s_3)[3:-1]}"
            else:
                return f"{self.realiser.realiseSentence(c_1)} {self.realiser.realiseSentence(s_2)[:-1]}, {self.realiser.realiseSentence(s_3)[3:-1]}"

    def _generate_answer(self, initiative_type: bool, response_type: Response, **kwargs) -> str:
        # Extract the negative or affirmative sentences that have yet to be used
        if not initiative_type:
            match response_type:
                case Response.CORRECT:
                    sentences = self.affirmative_answers
                case Response.INCORRECT:
                    sentences = self.negative_answers
                case Response.UNCERTAIN:
                    sentences = self.uncertain_answers
                case Response.INCOMPLETE:
                    return f"Non ho capito bene, hai {kwargs['total_slots']} slot, ma ne hai azzeccate solo {kwargs['complete_slots']} non sono stati ancora compilati."
        else:
            sentences = self.retry_answers
        returnable_sentences = [key for key, value in sentences.items() if value == 1]

        # I randomly select one of the sentences
        extracted_sentence = random.choice(returnable_sentences)

        # I update the dictionary to mark the sentence as used
        sentences[extracted_sentence] = 0

        # I reset the dictionary if all the sentences have been used
        if len(returnable_sentences) == 1:
            if not initiative_type:
                match response_type:
                    case Response.CORRECT:
                        self.affirmative_answers = self.affirmative_answers.fromkeys(self.affirmative_answers, 1)
                    case Response.INCORRECT:
                        self.negative_answers = self.negative_answers.fromkeys(self.negative_answers, 1)
                    case Response.UNCERTAIN:
                        self.uncertain_answers = self.uncertain_answers.fromkeys(self.uncertain_answers, 1)
            else:
                self.retry_answers = self.retry_answers.fromkeys(self.retry_answers, 1)

        return extracted_sentence 

    def response(self, turn: Turn, last_response: Response = None, **kwargs) -> str:
        match turn:
            case Turn.INTRO:
                # If the turn is the intro, I greet the user
                return self._greets_user(kwargs["name"])
            case Turn.QUESTION:
                # If the turn is the question, I generate the answer based on the last response
                return self._generate_answer(False, last_response, **kwargs)
        pass

    def initiative(self, turn: Turn, last_response: Response = None, **kwargs) -> str:
        match turn:
            case Turn.INTRO:
                # If the turn is the intro, it's the first time the user is talking to the bot, so I greet and i ask the name of the user
                return self._greetings()
            case Turn.QUESTION:
                match last_response:
                    case Response.CORRECT:
                        # If the turn is the question and the last response is correct, I ask the next question
                        return self._ask_nth_question(kwargs["question"])
                    case Response.UNCERTAIN | Response.INCOMPLETE | Response.INCORRECT:
                        # If the turn is the question and the last response is incorrect, I ask the user to repeat the answer
                        return self._generate_answer(True, last_response)
            case Turn.OUTRO:
                # If the turn is the outro, I say to the user if he passed or not the test for being a Padawan
                return self._generate_outro_answers(**kwargs)
                
                
if __name__ == "__main__":
    nlg = NaturalLanguageGenerator()
    # print(nlg.initiative(Turn.QUESTION, Response.CORRECT, question="Cosa è il 2+2?"))
    # print(nlg.response(Turn.INTRO, None, "Giovanni"))
    # print(nlg.initiative(Turn.QUESTION, Response.UNCERTAIN, total_slots=3, incomplete_slots=2))
    # print(nlg.initiative(Turn.QUESTION, Response.BACKUP))
    print(nlg.initiative(Turn.OUTRO, passed=False, tot_qst=3, correct_qst=3))