from simplenlg.framework import *
# from simplenlg.lexicon import *
from simplenlg.realiser.english import *
from simplenlg.phrasespec import *
from simplenlg.features import *
import random

from utils.enumerators import Response


class NaturalLanguageGenerator:

    def __init__(self):
        lexicon = Lexicon.getDefaultLexicon()
        self.nlg_factory = NLGFactory(lexicon)
        self.realiser = Realiser(lexicon)
        self.affirmative_answers = {}
        self.negative_answers = {}
        self.uncertain_answers = {}
        self._generate_affirmative_answers()
        self._generate_negative_answers()
        self._generate_uncertain_answers()

    def greetings(self) -> str:
        # Create a sentence with the form "Hello, I'm Obi-1 and I will question you about Jedi culture. We can start the interview now. What is your name?"
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

        # Create a sentence with the form "We can start the interview now"
        subj_3 = self.nlg_factory.createNounPhrase("we")
        verb_3 = self.nlg_factory.createVerbPhrase("start")
        adv_3 = self.nlg_factory.createAdverbPhrase("now")
        verb_3.setPostModifier(adv_3)
        obj_3 = self.nlg_factory.createNounPhrase("the", "interview")
        s_3 = self.nlg_factory.createClause(subj_3, verb_3, obj_3)
        s_3.setFeature(Feature.MODAL, "can")

        # Create a sentence with the form "What is your name?"
        subj_4 = self.nlg_factory.createNounPhrase("name")
        verb_4 = self.nlg_factory.createVerbPhrase("be")
        pron_4 = self.nlg_factory.createWord("you", LexicalCategory.PRONOUN)
        pron_4.setFeature(Feature.POSSESSIVE, True)
        subj_4.setDeterminer(pron_4)
        s_4 = self.nlg_factory.createClause(subj_4, verb_4)
        s_4.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.WHAT_OBJECT)

        # I tie the three sentences together with a new line
        return self.realiser.realiseSentence(c_2) + '\n' + self.realiser.realiseSentence(
            s_3) + '\n' + self.realiser.realiseSentence(s_4)

    def greets_user(self, name: str = None) -> str:
        # Create a sentence with the form "Hello, name!" if the name is not None, otherwise "Hello, aspiring Padawan!"
        s_0 = self.nlg_factory.createClause("Hello")
        if name:
            subj_1 = self.nlg_factory.createNounPhrase(name + "!")
            s_1 = self.nlg_factory.createClause(subj_1)
            c_1 = self.nlg_factory.createCoordinatedPhrase()
            c_1.setConjunction(",")
            c_1.addCoordinate(s_0)
            c_1.addCoordinate(s_1)
            return self.realiser.realiseSentence(c_1)
        subj_1 = self.nlg_factory.createNounPhrase("Padawan!")
        subj_1.setDeterminer("aspiring")
        s_1 = self.nlg_factory.createClause(subj_1)
        c_1 = self.nlg_factory.createCoordinatedPhrase()
        c_1.setConjunction(",")
        c_1.addCoordinate(s_0)
        c_1.addCoordinate(s_1)

        # Create a sentence with the form "Let's start"
        verb_1 = self.nlg_factory.createVerbPhrase("let's start")
        verb_1.setFeature(Feature.PERSON, Person.FIRST)
        s_2 = self.nlg_factory.createClause(verb=verb_1)

        # Create a preposition phrase with the form "with the first question"
        prep_1 = self.nlg_factory.createPrepositionPhrase("with")
        subj_1 = self.nlg_factory.createNounPhrase("the", "question")
        subj_1.addModifier("first")
        prep_1.addComplement(subj_1)
        s_2.addPostModifier(prep_1)
        return self.realiser.realiseSentence(c_1)[:-1] + '\n' + self.realiser.realiseSentence(s_2)

    def ask_nth_question(self, question) -> str:
        # Create a sentence with for the question extracted from a PD
        s_1 = self.nlg_factory.createSentence(question)
        return self.realiser.realiseSentence(s_1)

    def _generate_affirmative_answers(self):
        # 1. Create a sentence with the form "Yes, that's correct."
        s_0 = self.nlg_factory.createClause("Yes")
        verb_1 = self.nlg_factory.createVerbPhrase("that's")
        verb_1.setFeature(Feature.PERSON, Person.FIRST)
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

        # 2. Create a sentence with the form "That's exactly right!"
        verb_2 = self.nlg_factory.createVerbPhrase("that's")
        verb_2.setFeature(Feature.PERSON, Person.FIRST)
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
        # 1. Create a sentence with the form "I'm sorry, but that's false."
        # Create a sentence with the form "I'm sorry."
        subj_1 = self.nlg_factory.createNounPhrase("I")
        verb_1 = self.nlg_factory.createVerbPhrase("be")
        obj_1 = self.nlg_factory.createNounPhrase("sorry")
        s_1 = self.nlg_factory.createClause(subj_1, verb_1, obj_1)

        # Create a sentence with the form "but that's false."
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

        # 3. Create a sentence with the form "That's not the answer that i expected."
        # Create a sentence with the form "That's not the answer"
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

        # 5. Create a sentence with the form "I'm sorry, I doubt that's the correct answer."
        # Create a sentence with the form "I'm sorry"
        subj_8 = self.nlg_factory.createNounPhrase("I")
        verb_8 = self.nlg_factory.createVerbPhrase("be")
        obj_8 = self.nlg_factory.createNounPhrase("sorry")
        s_8 = self.nlg_factory.createClause(subj_8, verb_8, obj_8)

        # Create a sentence with the form "I doubt that's the correct answer."
        subj_9 = self.nlg_factory.createNounPhrase("I")
        verb_9 = self.nlg_factory.createVerbPhrase("doubt")
        s_9 = self.nlg_factory.createClause(subj_9, verb_9)

        # I tie the two sentences together with a comma
        c_9 = self.nlg_factory.createCoordinatedPhrase()
        c_9.setConjunction(",")
        c_9.addCoordinate(s_8)
        c_9.addCoordinate(s_9)

        # Create a sentence with the form "that's the correct answer."
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
        # 1. Create a sentence with the form "Sorry, I didn't catch that. Could you please repeat?"
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

        # Create a sentence with the form "Could you please repeat?"
        subj_2 = self.nlg_factory.createNounPhrase("you")
        verb_2 = self.nlg_factory.createVerbPhrase("repeat")
        verb_2.addModifier("please")
        s_2 = self.nlg_factory.createClause(subj_2, verb_2)
        s_2.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
        s_2.setFeature(Feature.MODAL, "could")

        # I add the sentence to the dictionary
        self.uncertain_answers.update({
            f"{self.realiser.realiseSentence(c_1)} {self.realiser.realiseSentence(s_2)}": 1
        })

        # 2. Create a sentence with the form "I'm sorry, I didn't quite understand what you said. Can you say it again?"
        # Create a sentence with the form "I'm sorry"
        subj_3 = self.nlg_factory.createNounPhrase("I")
        verb_3 = self.nlg_factory.createVerbPhrase("be")
        obj_3 = self.nlg_factory.createNounPhrase("sorry")
        s_3 = self.nlg_factory.createClause(subj_3, verb_3, obj_3)

        # Create a sentence with the form "I didn't quite understand"
        subj_4 = self.nlg_factory.createNounPhrase("I")
        verb_4 = self.nlg_factory.createVerbPhrase("understand")
        verb_4.setFeature(Feature.NEGATED, True)
        verb_4.setFeature(Feature.TENSE, Tense.PAST)
        adv_4 = self.nlg_factory.createWord("quite", LexicalCategory.ADVERB)
        verb_4.addModifier(adv_4)
        s_4 = self.nlg_factory.createClause(subj_4, verb_4)

        # Create a sentence with the form "what you said."
        p_5 = self.nlg_factory.createPrepositionPhrase("what")
        subj_5 = self.nlg_factory.createNounPhrase("you")
        verb_5 = self.nlg_factory.createVerbPhrase("say")
        verb_5.setFeature(Feature.TENSE, Tense.PAST)
        subj_5.addPreModifier(p_5)
        s_5 = self.nlg_factory.createClause(subj_5, verb_5)

        # I tie the three sentences together with a space
        c_5 = self.nlg_factory.createCoordinatedPhrase()
        c_5.setConjunction("")
        c_5.addCoordinate(s_4)
        c_5.addCoordinate(s_5)

        # I tie the two sentences together with a comma
        c_6 = self.nlg_factory.createCoordinatedPhrase()
        c_6.setConjunction(",")
        c_6.addCoordinate(s_3)
        c_6.addCoordinate(c_5)

        # Create a sentence with the form "Can you say it again?"
        subj_7 = self.nlg_factory.createNounPhrase("you")
        verb_7 = self.nlg_factory.createVerbPhrase("say")
        obj_7 = self.nlg_factory.createNounPhrase("again")
        pron_7 = self.nlg_factory.createWord("it", LexicalCategory.PRONOUN)
        obj_7.addPreModifier(pron_7)
        s_7 = self.nlg_factory.createClause(subj_7, verb_7, obj_7)
        s_7.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
        s_7.setFeature(Feature.MODAL, "can")

        # I add the sentence to the dictionary
        self.uncertain_answers.update({
            f"{self.realiser.realiseSentence(c_6)} {self.realiser.realiseSentence(s_7)}": 1
        })

        # 3. Create a sentence with the form "Sorry, I missed what you just said. Could you say that one more time, please?"
        # Create a sentence with the form "Sorry"
        s_8 = self.nlg_factory.createClause("Sorry")

        # Create a sentence with the form "I missed"
        subj_9 = self.nlg_factory.createNounPhrase("I")
        verb_9 = self.nlg_factory.createVerbPhrase("miss")
        verb_9.setFeature(Feature.TENSE, Tense.PAST)
        s_9 = self.nlg_factory.createClause(subj_9, verb_9)

        # I tie the two sentences together with a comma
        c_8 = self.nlg_factory.createCoordinatedPhrase()
        c_8.setConjunction(",")
        c_8.addCoordinate(s_8)
        c_8.addCoordinate(s_9)

        # Create a sentence with the form "what you just said."
        p_10 = self.nlg_factory.createPrepositionPhrase("what")
        subj_10 = self.nlg_factory.createNounPhrase("you")
        verb_10 = self.nlg_factory.createVerbPhrase("say")
        verb_10.setFeature(Feature.TENSE, Tense.PAST)
        adv_10 = self.nlg_factory.createWord("just", LexicalCategory.ADVERB)
        verb_10.addModifier(adv_10)
        subj_10.addPreModifier(p_10)
        s_10 = self.nlg_factory.createClause(subj_10, verb_10)

        # I tie the two sentences together with a space
        c_9 = self.nlg_factory.createCoordinatedPhrase()
        c_9.setConjunction("")
        c_9.addCoordinate(c_8)
        c_9.addCoordinate(s_10)

        # Create a sentence with the form "Could you say that one more time"
        subj_11 = self.nlg_factory.createNounPhrase("you")
        verb_11 = self.nlg_factory.createVerbPhrase("say")
        s_11 = self.nlg_factory.createClause(subj_11, verb_11)
        s_11.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
        s_11.setFeature(Feature.MODAL, "could")

        noun_12 = self.nlg_factory.createClause("time")
        adv_12 = self.nlg_factory.createWord("one more", LexicalCategory.ADJECTIVE)
        noun_12.addFrontModifier(adv_12)

        s_11.addComplement(noun_12)

        # Create a sentence with the form "please?"
        s_12 = self.nlg_factory.createClause("please?")

        # I tie the two sentences together with a comma
        c_10 = self.nlg_factory.createCoordinatedPhrase()
        c_10.setConjunction(",")
        c_10.addCoordinate(s_11)
        c_10.addCoordinate(s_12)

        # I add the sentence to the dictionary
        self.uncertain_answers.update({
            f"{self.realiser.realiseSentence(c_9)} {self.realiser.realiseSentence(c_10)}": 1
        })

        # 4. Create a sentence with the form "I didn't get that. Could you please reiterate your point?"
        # Create a sentence with the form "I didn't get that."
        subj_13 = self.nlg_factory.createNounPhrase("I")
        verb_13 = self.nlg_factory.createVerbPhrase("get")
        obj_13 = self.nlg_factory.createNounPhrase("that")
        verb_13.setFeature(Feature.TENSE, Tense.PAST)
        verb_13.setFeature(Feature.NEGATED, True)
        s_13 = self.nlg_factory.createClause(subj_13, verb_13, obj_13)

        # Create a sentence with the form "Could you please reiterate your point?"
        subj_14 = self.nlg_factory.createNounPhrase("you")
        verb_14 = self.nlg_factory.createVerbPhrase("reiterate")
        adv_14 = self.nlg_factory.createWord("please", LexicalCategory.ADVERB)
        verb_14.addModifier(adv_14)
        obj_14 = self.nlg_factory.createNounPhrase("point")
        pron_14 = self.nlg_factory.createWord("you", LexicalCategory.PRONOUN)
        pron_14.setFeature(Feature.POSSESSIVE, True)
        obj_14.setDeterminer(pron_14)
        s_14 = self.nlg_factory.createClause(subj_14, verb_14, obj_14)
        s_14.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
        s_14.setFeature(Feature.MODAL, "could")

        # I add the sentence to the dictionary
        self.uncertain_answers.update({
            f"{self.realiser.realiseSentence(s_13)} {self.realiser.realiseSentence(s_14)}": 1
        })

        # 5. Create a sentence with the form "Could you kindly rephrase what you just said? I didn't quite understand it."
        # Create a sentence with the form "Could you kindly rephrase what you just said?"
        subj_15 = self.nlg_factory.createNounPhrase("you")
        verb_15 = self.nlg_factory.createVerbPhrase("rephrase")
        adj_15 = self.nlg_factory.createWord("kindly", LexicalCategory.ADVERB)
        verb_15.addModifier(adj_15)
        s_15 = self.nlg_factory.createClause(subj_15, verb_15)
        s_15.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
        s_15.setFeature(Feature.MODAL, "could")

        # Create a sentence with the form "what you just said."
        p_15 = self.nlg_factory.createPrepositionPhrase("what")
        subj_16 = self.nlg_factory.createNounPhrase("you")
        verb_16 = self.nlg_factory.createVerbPhrase("say")
        verb_16.setFeature(Feature.TENSE, Tense.PAST)
        adv_16 = self.nlg_factory.createWord("just", LexicalCategory.ADVERB)
        verb_16.addModifier(adv_16)
        subj_16.addPreModifier(p_15)
        s_16 = self.nlg_factory.createClause(subj_16, verb_16)

        # I tie the two sentences together with a space
        c_11 = self.nlg_factory.createCoordinatedPhrase()
        c_11.setConjunction("")
        c_11.addCoordinate(s_15)
        c_11.addCoordinate(s_16)

        # Create a sentence with the form "I didn't entirely understand it."
        subj_17 = self.nlg_factory.createNounPhrase("I")
        verb_17 = self.nlg_factory.createVerbPhrase("understand")
        obj_17 = self.nlg_factory.createNounPhrase("it")
        adv_17 = self.nlg_factory.createWord("entirely", LexicalCategory.ADVERB)
        verb_17.addModifier(adv_17)
        verb_17.setFeature(Feature.TENSE, Tense.PAST)
        verb_17.setFeature(Feature.NEGATED, True)
        s_17 = self.nlg_factory.createClause(subj_17, verb_17, obj_17)

        # I add the sentence to the dictionary
        self.uncertain_answers.update({
            f"{self.realiser.realiseSentence(c_11)[:-1]}? {self.realiser.realiseSentence(s_17)}": 1
        })

    def generate_answer(self, response_type: Response) -> str:
        # Extract the negative or affirmative sentences that have yet to be used
        match response_type:
            case Response.CORRECT:
                sentences = self.affirmative_answers
            case Response.INCORRECT:
                sentences = self.negative_answers
            case Response.UNCERTAIN:
                sentences = self.uncertain_answers
            case _:
                sentences = {"a": "vuoto"}
        returnable_sentences = [key for key, value in sentences.items() if value == 1]

        # I randomly select one of the sentences
        extracted_sentence = random.choice(returnable_sentences)

        # I update the dictionary to mark the sentence as used
        sentences[extracted_sentence] = 0

        # I reset the dictionary if all the sentences have been used
        if len(returnable_sentences) == 1:
            match response_type:
                case Response.CORRECT:
                    self.affirmative_answers = self.affirmative_answers.fromkeys(self.affirmative_answers, 1)
                case Response.INCORRECT:
                    self.negative_answers = self.negative_answers.fromkeys(self.negative_answers, 1)
                case Response.UNCERTAIN:
                    self.uncertain_answers = self.uncertain_answers.fromkeys(self.uncertain_answers, 1)

        return extracted_sentence


if __name__ == "__main__":
    nlg = NaturalLanguageGenerator()
    nlg.greetings()
    nlg.greets_user()
    nlg.ask_nth_question("How many children can a Jedi have?")
    nlg.generate_answer(Response.CORRECT)
    nlg.generate_answer(Response.INCORRECT)
    nlg.generate_answer(Response.UNCERTAIN)
