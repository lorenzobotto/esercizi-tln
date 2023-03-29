import re

# Domanda: Where is the headquarters of the Jedi Order located ? ---------------------------------------------------------------------------------------------------------------------------------
"""
POSITIVE
----------------------------------------------risolti
the headquarters of the jedi order is located on the planet coruscant
coruscant
coruskant
corusant

NEGATIVE
----------------------------------------------da risolvere 
The headquarters of the Jedi Order is located on a planet other than coruscant.

----------------------------------------------risolti
the headquarters is not on coruscant.
it is not coruscant
isn't coruscant
The headquarters of the Jedi Order is not situated on coruscant.
The headquarters of the Jedi Order is not located on any planet.

----------------------------------------------si ignora e si dice che hai sbagliato
The Jedi Order does not exist in the Star Wars universe.
The Jedi Order does not have a headquarters. 
The planet Coruscant does not exist in the Star Wars universe.

---------------------------------------------frasi stronze
The headquarters of the Sith Order is located on Coruscant instead of the Jedi Order. 
"""
# frase da testare
phrase = "isn't coruscant"

# pattern per frasi positive
q1PosPattern1 = "coruscant"  # funziona se ce la parola
q1PosPattern2 = "cor[a-z]{1,3}ant"  # funziona se ce la parola ma con qualche errore
# in caso di frasi più composte
q1PosPattern3 = "(located|situated) on cor[a-z]{1,3}ant"
q1PosPattern4 = "cor[a-z]{1,3}ant is the base"
q1PosPattern5 = "the base is on cor[a-z]{1,3}ant"

# pattern per frasi con negazione
q1NegPattern1 = "(is not|isn't) on cor[a-z]{1,3}ant"
q1NegPattern2 = "(is not|isn't) (located|situated) on cor[a-z]{1,3}ant"
q1NegPattern3 = "(is not|isn't) (located|situated) on (any planet|a planet)"
q1NegPattern4 = "(is not|isn't) cor[a-z]{1,3}ant"
q1NegPattern5 = "(located|situated) on ((?!cor[a-z]{1,3}ant).)*$"  # dico che il centro di comando e situato su un altro pianeta
q1NegPattern6 = "((?!cor[a-z]{1,3}ant).)*$"  # dico il nome di un altra citta

regQuestion1 = {"coruscant": tuple([{q1PosPattern1, q1PosPattern2, q1PosPattern3, q1PosPattern4, q1PosPattern5},
                                    {q1NegPattern1, q1NegPattern2, q1NegPattern3, q1NegPattern4, q1NegPattern5,
                                     q1NegPattern6}])}

# Domanda: How many children can a Jedi have?---------------------------------------------------------------------------------------------------------------------------------
"""
POSITIVE
--------------------------------
0
zero
A jedi cannot have children
no son
Jedi are forbidden from having any children

NEGATIVE
--------------------------------
[1-9]
many children
some children
can have many children
"""
q2PosPattern1 = "(0|zero)"
q2PosPattern2 = "(cannot|can not|can't) have (children|child|daughter|son|baby)"
q2PosPattern3 = "(forbidden|prohibited)"
q2PosPattern4 = "(forbidden|prohibited) having any (children|child|daughter|son|baby)"
q2PosPattern5 = "have no (children|child|daughter|son|baby)"
q2PosPattern6 = "(cannot|can not|can't) even have a (children|child|daughter|son|baby)"
q2PosPattern7 = "(cannot|can not|can't) have"
q2PosPattern8 = "(doesn't|dont|don't|do not) have"

q2NegPattern1 = "[1-9]"
q2NegPattern2 = "many"
q2NegPattern3 = "some"
q2NegPattern4 = "(can|may) have"  # da chidere a nicola
q2NegPattern5 = "(can|may) have (children|child|daughter|son|baby)"
q2NegPattern6 = "(can|may) have (some|many) (children|child|daughter|son|baby)"

regQuestion2 = {"children": tuple([{q2PosPattern1, q2PosPattern2, q2PosPattern3, q2PosPattern4, q2PosPattern5,
                                    q2PosPattern6, q2PosPattern7, q2PosPattern8},
                                   {q2NegPattern1, q2NegPattern2, q2NegPattern3, q2NegPattern4, q2NegPattern5,
                                    q2NegPattern6}])}

# Domanda: What are the three pillars of Jedi culture?---------------------------------------------------------------------------------------------------------------------------------
"""
POSITIVE
--------------------------------------------------
the force, knowledge and self-discipline
the force
knowledge
self-discipline
self discipline
the tree pillars of jedi culture is The force, knowledge and self-discipline


NEGATIVE

"""
# frase da testare
phrase = ""

# pattern per frasi positive
q3PosPattern1 = "(the force|force)"
q3PosPattern2 = "knowledge"
q3PosPattern3 = "(self discipline|self-discipline)"

# pattern per frasi con negazione
q3NegPattern1 = "(is not|isn't) (the force|force)"
q3NegPattern2 = "(is not|isn't) knowledge"
q3NegPattern3 = "(is not|isn't) (self discipline|self-discipline)"

regQuestion3 = {"pillars": tuple([{q3PosPattern1, q3PosPattern2, q3PosPattern3},
                                  {q3NegPattern1, q3NegPattern2, q3NegPattern3}])}

# Domanda: Who is the grand master of the jedi council ?---------------------------------------------------------------------------------------------------------------------------------
"""
POSITIVE
--------------------------------
yoda
the grand master of the jedi council is yoda
yoda is the grandmaster of the council

NEGATIVE
--------------------------------


"""

# testiamo se il pattern crea un match
match = re.search(q2NegPattern4, "It can have 0")

if match:
    print(match.group())
    print("TRUE")
else:
    print("pattern not found")
