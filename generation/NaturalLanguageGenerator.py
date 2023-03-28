from simplenlg.framework import *
from simplenlg.lexicon import *
from simplenlg.realiser.english import *
from simplenlg.phrasespec import *
from simplenlg.features import *

class NaturalLanguageGenerator: 
    
    def __init__(self):
        lexicon = Lexicon.getDefaultLexicon()
        self.ngl_factory = NLGFactory(lexicon)
        self.realiser = Realiser(lexicon)

    def greetings(self) -> str:
        # Create a sentence with the form "Hello, I'm Obi1 and I will question you about Jedi culture. We can start the interview now. What is your name?"
        s_0 = self.ngl_factory.createClause("Hello")
        
        # Create a sentence with the form "I am Obi1"
        subj_1 = self.ngl_factory.createNounPhrase("I")
        verb_1 = self.ngl_factory.createVerbPhrase("be")
        obj_1 = self.ngl_factory.createNounPhrase("Obi1")
        s_1 = self.ngl_factory.createClause(subj_1, verb_1, obj_1)

        # Create a sentence with the form "I will question you"
        subj_2 = self.ngl_factory.createNounPhrase("I")
        verb_2 = self.ngl_factory.createVerbPhrase("question")
        verb_2.setFeature(Feature.TENSE, Tense.FUTURE)
        obj_2 = self.ngl_factory.createNounPhrase("you")
        s_2 = self.ngl_factory.createClause(subj_2, verb_2, obj_2)

        # Create a preposition phrase with the form "about Jedi culture"
        p_1 = self.ngl_factory.createPrepositionPhrase("about")
        p_1.addComplement("Jedi culture")

        # I add the preposition phrase to the sentence
        s_2.addComplement(p_1)

        # I tie the sentence 0 and sentence 1 together with a comma
        c_1 = self.ngl_factory.createCoordinatedPhrase()
        c_1.setConjunction(",")
        c_1.addCoordinate(s_0)
        c_1.addCoordinate(s_1)

        # I tie the sentence generated in the previous step and sentence 2 together with the word "and"
        c_2 = self.ngl_factory.createCoordinatedPhrase()
        c_2.setConjunction("and")
        c_2.addCoordinate(c_1)
        c_2.addCoordinate(s_2)

        # Create a sentence with the form "We can start the interview now"
        subj_3 = self.ngl_factory.createNounPhrase("we")
        verb_3 = self.ngl_factory.createVerbPhrase("start")
        adv_3 = self.ngl_factory.createAdverbPhrase("now")
        verb_3.setPostModifier(adv_3)
        obj_3 = self.ngl_factory.createNounPhrase("interview")
        obj_3.setDeterminer("the")
        s_3 = self.ngl_factory.createClause(subj_3, verb_3, obj_3)
        s_3.setFeature(Feature.MODAL, "can")
        
        # Create a sentence with the form "What is your name?"
        subj_4 = self.ngl_factory.createNounPhrase("name")
        verb_4 = self.ngl_factory.createVerbPhrase("be")
        pron_4 = self.ngl_factory.createWord("you", LexicalCategory.PRONOUN)
        pron_4.setFeature(Feature.POSSESSIVE, True)
        subj_4.setDeterminer(pron_4)
        s_4 = self.ngl_factory.createClause(subj_4, verb_4)
        s_4.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.WHAT_OBJECT)

        # I tie the three sentences together with a new line
        return self.realiser.realiseSentence(c_2) + '\n' + self.realiser.realiseSentence(s_3) + '\n' + self.realiser.realiseSentence(s_4)

    def greets_user(self, name: str = None) -> str:
        # Create a sentence with the form "Hello, name"
        s_0 = self.ngl_factory.createClause("Hello")
        if name:
            subj_1 = self.ngl_factory.createNounPhrase(name)
            s_1 = self.ngl_factory.createClause(subj_1)
            c_1 = self.ngl_factory.createCoordinatedPhrase()
            c_1.setConjunction(",")
            c_1.addCoordinate(s_0)
            c_1.addCoordinate(s_1)
            return self.realiser.realiseSentence(c_1)
        return self.realiser.realiseSentence(s_0)

        # TODO: implement Hello, bro! or other things if the name is not known

    def ask_first_question(self, question) -> str:
        # Create a sentence with the form "Let's start"
        verb_1 = self.ngl_factory.createVerbPhrase("let's start")
        verb_1.setFeature(Feature.PERSON, Person.FIRST)
        s_1 = self.ngl_factory.createClause(verb=verb_1)

        # Create a preposition phrase with the form "with the first question"
        prep = self.ngl_factory.createPrepositionPhrase("with")
        noun = self.ngl_factory.createNounPhrase("question")
        noun.setDeterminer("the")
        noun.addModifier("first")
        prep.addComplement(noun)
        s_1.addPostModifier(prep)
        return self.realiser.realiseSentence(s_1)

        # TODO: implement the question
    
    
if __name__ == "__main__":
    nlg = NaturalLanguageGenerator()
    nlg.greetings()
    nlg.greets_user("John")
    nlg.ask_first_question("Come stai?")