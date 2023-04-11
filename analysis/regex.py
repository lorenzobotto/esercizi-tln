import re
import shelve
from analysis.Frame import Frame


def create_db():
    with shelve.open("regex") as regex_db:
        # regex_db = regQuestion1 | regQuestion2 | regQuestion3 | regQuestion4 | regQuestion5 | \
        #                 regQuestion6 | regQuestion7 | regQuestion8 | regQuestion9 | regQuestion10
        # print(regex_db)
        regex_db["coruscant"] = tuple([({q1PosPattern1, q1PosPattern2, q1PosPattern3, q1PosPattern4, q1PosPattern5}),
                                    ({q1NegPattern1, q1NegPattern2, q1NegPattern3, q1NegPattern4, q1NegPattern5,
                                      q1NegPattern6})])
        regex_db["children"] = tuple([({q2PosPattern1, q2PosPattern2, q2PosPattern3, q2PosPattern4, q2PosPattern5,
                                     q2PosPattern6, q2PosPattern7, q2PosPattern8}),
                                   ({q2NegPattern1, q2NegPattern2, q2NegPattern3, q2NegPattern4, q2NegPattern5,
                                     q2NegPattern6, q2NegPattern7})])
        regex_db["force"] =  tuple([({q3PosPattern1_1, }),
                                  ({q3NegPattern1_1, })])
        regex_db["knowledge"] = tuple([({q3PosPattern1_2}),
                                       ({q3NegPattern1_2})])
        regex_db["self discipline"] = tuple([({q3PosPattern1_3}),
                                             ({q3NegPattern1_3})])
        regex_db["kyber"] = tuple([({q4PosPattern1, q4PosPattern3}),
                                   ({q4NegPattern2, q4NegPattern3, q4NegPattern4})])
        regex_db["order"] = tuple([({q5PosPattern1, q5PosPattern2, q5PosPattern3, q5PosPattern4, q5PosPattern5}),
                                   ({q5NegPattern1, q5NegPattern2, q5NegPattern3, q5NegPattern4, q5NegPattern5,
                                     q5NegPattern6})])
        regex_db["yoda"] = tuple([({q6PosPattern1}),
                                  ({q6NegPattern1, q6NegPattern2, q6NegPattern3, q6NegPattern4})])
        regex_db["color"] = tuple([({q7PosPattern1, q7PosPattern2}),
                                   ({q7NegPattern1, q7NegPattern2, q7NegPattern3, q7NegPattern4})])
        regex_db["dagobah"] = tuple([({q9PosPattern1}),
                                     ({q9NegPattern1, q9NegPattern2, q9NegPattern3, q9NegPattern4})])
        regex_db["master"] = tuple([({q8PosPattern1, q8PosPattern2, q8PosPattern3}),
                                    ({q8NegPattern1, q8NegPattern2, q8NegPattern3, q8NegPattern4})])
        regex_db["anakin"] = tuple([({q10PosPattern1, q10PosPattern2, q10PosPattern3,q10PosPattern4}),
                                  ({q10NegPattern1, q10NegPattern2, q10NegPattern3, q10NegPattern4})])
        regex_db["commander"] = tuple([({q11PosPattern1_2, q11PosPattern2_2, q11PosPattern3_2, q11PosPattern4_2}),
                                       ({q11NegPattern2_2, q11NegPattern3_2, q11NegPattern4_2})])
        regex_db["general"] = tuple([({q11PosPattern1_1, q11PosPattern2_1, q11PosPattern3_1, q11PosPattern4_1}),
                                     ({q11NegPattern2_1, q11NegPattern3_1, q11NegPattern4_1})])
        regex_db["guardian"] = tuple([({q12PosPattern1_1, q12PosPattern2_1, q12PosPattern3_1}),
                                      ({q12NegPattern1_1, q12NegPattern2_1, q12NegPattern3_1})])
        regex_db["sentinel"] = tuple([({q12PosPattern1_2, q12PosPattern2_2, q12PosPattern3_2}),
                                      ({q12NegPattern1_2, q12NegPattern2_2, q12NegPattern3_2})])
        regex_db["consular"] = tuple([({q12PosPattern1_3, q12PosPattern2_3, q12PosPattern3_3}),
                                      ({q12NegPattern1_2, q12NegPattern2_2})])


def resolve(sentence, frame: Frame):
    lwr_sentence = sentence.lower()
    response = [False, False]
    temp_slot = {}
    with shelve.open("databases/regex_db/regex") as reg_questions:
        for slot in frame.slots:
            if slot not in ["domain", "intent"]:
                reg_set = reg_questions[slot]  # prendiamo la chiave dello slots e cerchiamo fra le regex
                for neg_pattern in reg_set[1]:
                    if re.search(neg_pattern, lwr_sentence):
                        response[1] = True
                        break
                for pos_pattern in reg_set[0]:
                    pos_match = re.search(pos_pattern, lwr_sentence)
                    if pos_match:
                        response[0] = True
                        if not response[1]:
                            temp_slot[slot] = pos_match
                            frame.modify_slot(temp_slot)
                        break
    return response


# Domanda: Where is the headquarters of the Jedi Order located?---------------------------------------------------------------------------------------------------------------------------------
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

# pattern per frasi positive
q1PosPattern1 = "coruscant"  # funziona se ce la parola
q1PosPattern2 = "cor[a-z]{1,3}ant"  # funziona se ce la parola ma con qualche errore
# in caso di frasi più composte
q1PosPattern3 = "(located|situated) on cor[a-z]{1,3}ant"
q1PosPattern4 = "cor[a-z]{1,3}ant is the base"
q1PosPattern5 = "the base is on cor[a-z]{1,3}ant"

# pattern per frasi con negazione
q1NegPattern1 = "(is not|isn't|not|it's|didn't|did not|don't|do not) on cor[a-z]{1,3}ant"
q1NegPattern2 = "(is not|isn't|not|it's|didn't|did not|don't|do not) (located|situated) on cor[a-z]{1,3}ant"
q1NegPattern3 = "(is not|isn't|not|it's|didn't|did not|don't|do not) (located|situated) on (any planet|a planet)"
q1NegPattern4 = "(is not|isn't|not|it's|didn't|did not|don't|do not) cor[a-z]{1,3}ant"
q1NegPattern5 = "(located|situated) on ((?!cor[a-z]{1,3}ant).)*$"  # dico che il centro di comando e situato su un altro pianeta
q1NegPattern6 = "^((?!cor[a-z]{1,3}ant).)*$"  # dico il nome di un altra citta

regQuestion1 = {"coruscant": tuple([({q1PosPattern1, q1PosPattern2, q1PosPattern3, q1PosPattern4, q1PosPattern5}),
                                    ({q1NegPattern1, q1NegPattern2, q1NegPattern3, q1NegPattern4, q1NegPattern5,
                                      q1NegPattern6})])}

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
q2NegPattern7 = "^((?!zero).)*$"
q2NegPattern8 = "[1-9][0-9]"

regQuestion2 = {"children": tuple([({q2PosPattern1, q2PosPattern2, q2PosPattern3, q2PosPattern4, q2PosPattern5,
                                     q2PosPattern6, q2PosPattern7, q2PosPattern8}),
                                   ({q2NegPattern1, q2NegPattern2, q2NegPattern3, q2NegPattern4, q2NegPattern5,
                                     q2NegPattern6, q2NegPattern7})])}

# Domanda: What are the three pillars of Jedi culture?---------------------------------------------------------------------------------------------------------------------------------
# this question is divided into 3 slots
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

# pattern per frasi positive prmo slots
q3PosPattern1_1 = "(the force|force)"

# pattern per frasi con negazione primo slots
q3NegPattern1_1 = "(is not|isn't|not|it's|didn't|did not|don't|do not) (the force|force)"
q3NegPattern2_1 = "enforce"

regQuestion3_1 = {"force": tuple([({q3PosPattern1_1, }),
                                  ({q3NegPattern1_1, })])}
# pattern per frasi positive secondo slots
q3PosPattern1_2 = "(knowledge|the knowledge)"

# pattern per frasi con negazione secondo slots
q3NegPattern1_2 = "(is not|isn't|not|it's|didn't|did not|don't|do not) (knowledge|the knowledge)"

regQuestion3_2 = {"knowledge": tuple([({q3PosPattern1_2}),
                                      ({q3NegPattern1_2})])}
# pattern per frasi positive terzo slots
q3PosPattern1_3 = "(self discipline|self-discipline|the self discipline|the self-discipline)"

# pattern per frasi con negazione terzo slots
q3NegPattern1_3 = "(is not|isn't|not|it's|didn't|did not|don't|do not) (self discipline|self-discipline|the self discipline|the self-discipline)"

regQuestion3_3 = {"self discipline": tuple([({q3PosPattern1_3}),
                                            ({q3NegPattern1_3})])}

# Domanda: What powers the lightsabers ?-------------------------------------------------------------------------------------------------------
"""
POSITIVE
--------------------------------------------------
kyber crystal
kyber
lightsabers are powered by a kiber crystal

NEGATIVE
(altra parola)
cristal (non kyber)
not kyber crystal
kyber
are not powered by anything
"""

# pattern per frasi positive
q4PosPattern1 = "(kyber crystal|kyber cristal)"
q4PosPattern3 = "powered by a (kyber crystal|kyber cristal)"

# pattern per frasi con negazioneù
q4NegPattern2 = "((?!(kyber crystal|kyber cristal)).)*$ "
q4NegPattern3 = "(is not|isn't|not|it's|didn't|did not|don't|do not) (kyber crystal|kyber cristal)"
q4NegPattern4 = "(is not|isn't|not|it's|didn't|did not|don't|do not) (powered|power)"

regQuestion4 = {"kyber": tuple([({q4PosPattern1, q4PosPattern3}),
                                ({q4NegPattern2, q4NegPattern3, q4NegPattern4})])}

# Domanda: What order did Emperor Palpatine issue ? -------------------------------------------------------------------------------------------------------
"""
POSITIVE
--------------------------------------------------
order 66
66
sixty-six
the order sixty-six
he gave the order 66
he issued the order 66

NEGATIVE
(qualunque altro numero)
not sixty-six
the order (altro numero)
"""

# pattern per frasi positive
q5PosPattern1 = "(66|sixty-six|sixty six)"
q5PosPattern2 = "order (66|sixty-six|sixty six)"
q5PosPattern3 = "(gave|issued) the order (66|sixty-six|sixty six)"
q5PosPattern4 = "to (gave|issue) order (66|sixty-six|sixty six)"
q5PosPattern5 = "it is order (66|sixty-six|sixty six)"

# pattern per frasi con negazione
q5NegPattern1 = "^((?!(66|sixty-six|sixty six)).)*$"
q5NegPattern2 = "order ((?!(66|sixty-six|sixty six)).)*$"
q5NegPattern3 = "(is not|isn't|not|it's|didn't|did not|don't|do not) (66|sixty-six|sixty six)"
q5NegPattern4 = "(is not|isn't|not|it's|didn't|did not|don't|do not) order (66|sixty-six|sixty six)"
q5NegPattern5 = "(is not|isn't|not|it's|didn't|did not|don't|do not) to (gave|issue) order (66|sixty-six|sixty six)"
q5NegPattern6 = "(is not|isn't|not|it's|didn't|did not|don't|do not) (think|belive|suppose|assume|repute|opine) it's order (66|sixty-six|sixty six)"

regQuestion5 = {"order": tuple([({q5PosPattern1, q5PosPattern2, q5PosPattern3, q5PosPattern4, q5PosPattern5}),
                                ({q5NegPattern1, q5NegPattern2, q5NegPattern3, q5NegPattern4, q5NegPattern5,
                                  q5NegPattern6})])}

# Domanda: Who is the grand master of the jedi council ?------------------------------------------------------------------------------------------------------------------
"""
POSITIVE
--------------------------------
yoda
the grand master of the jedi council is yoda
yoda is the grandmaster of the council

NEGATIVE
--------------------------------
the grand master of the jedi council is anakin
anakin
"""
# pattern per frasi positive
q6PosPattern1 = "yoda"

# pattern per frasi con negazioneSW
q6NegPattern1 = "is ((?!yoda).)*$"
q6NegPattern2 = "^((?!yoda).)*$"
q6NegPattern3 = "grand master of the jedi council is ((?!yoda).)*$"  # se formula la classica risposta ma con un altro nome
q6NegPattern4 = "(is not|isn't|not|it's|didn't|did not|don't|do not) yoda"

regQuestion6 = {"yoda": tuple([({q6PosPattern1}),
                               ({q6NegPattern1, q6NegPattern2, q6NegPattern3, q6NegPattern4})])}

# Domanda: What color are the lightsabers of the sith ?-------------------------------------------------------------------------------------------------------------------
"""
POSITIVE
--------------------------------
Red
is red
the color of the lightsaber of the sith is red

NEGATIVE
--------------------------------
the color of the lightsaber of the sith is red (altro colore)
(altro colore)

"""
# pattern per frasi positive
q7PosPattern1 = "red"
q7PosPattern2 = "is red"

# pattern per frasi con negazioneSW
q7NegPattern1 = "is ((?!red).)*$"
q7NegPattern2 = "^((?!red).)*$"
q7NegPattern3 = "(is not|isn't|not|it's|didn't|did not|don't|do not) red"
q7NegPattern4 = "(don't have|have no) color"

regQuestion7 = {"color": tuple([({q7PosPattern1, q7PosPattern2}),
                                ({q7NegPattern1, q7NegPattern2, q7NegPattern3, q7NegPattern4})])}

# Domanda: Where is Master Yoda hiding after escaping from Order 66?-------------------------------------------------------------------------------------------------------------------
"""
POSITIVE
--------------------------------
dagobah
dagoba
is dagobah
the planet where he hid is dagobah

NEGATIVE
--------------------------------
(non dagobah)
not

"""
q9PosPattern1 = "dagobah"

# pattern per frasi con negazioneSW
q9NegPattern1 = "is ((?!dagobah).)*$"
q9NegPattern2 = "^((?!dagobah).)*$"
q9NegPattern3 = "the planet where he hid is ((?!yoda).)*$"
q9NegPattern4 = "(is not|isn't|not|it's|didn't|did not|don't|do not) dagobah"

regQuestion9 = {"dagobah": tuple([({q9PosPattern1}),
                                  ({q9NegPattern1, q9NegPattern2, q9NegPattern3, q9NegPattern4})])}

# Domanda: What is the most important role a jedi can play ?-------------------------------------------------------------------------------------------------------------------
"""
POSITIVE
--------------------------------
master
jedi master
The role of jedi master/teacher
the most important role a jedi can play is master
the most important role a jedi can play is that of master

NEGATIVE
--------------------------------
(non maestro)
the most important role a jedi can play is not that of master

"""
q8PosPattern1 = "master"
q8PosPattern2 = "jedi (master|teacher)"
q8PosPattern3 = "role of (master|teacher)"

# pattern per frasi con negazioneSW
q8NegPattern1 = "^((?!master).)*$"
q8NegPattern2 = "is ((?!master).)*$"
q8NegPattern3 = "role of ((?!master).)*$"
q8NegPattern4 = "(is not|isn't|not|it's|didn't|did not|don't|do not) dagobah"

regQuestion8 = {"master": tuple([({q8PosPattern1, q8PosPattern2, q8PosPattern3}),
                                 ({q8NegPattern1, q8NegPattern2, q8NegPattern3, q8NegPattern4})])}

# Domanda: Is anakin Skywalker a jedi master ?-------------------------------------------------------------------------------------------------------------------
"""
POSITIVE
--------------------------------
no
no anakin has never received/recognized the rank of master
It was not granted to him
he didn't receive it

NEGATIVE
--------------------------------
yes
yes he received it
yes they recognized him
he was granted/allowed

"""
q10PosPattern1 = "^no$"
q10PosPattern2 = "(has|have|was) never (received|granted|recognized|allowed)"
q10PosPattern3 = "(is not|isn't|not|it's|didn't|did not|don't|do not) (received|granted|recognized|allowed|think)"
q10PosPattern4 = "(is not|isn't|not|it's|didn't|did not|don't|do not) (received|granted|recognized|allowed|think)"

# pattern per frasi con negazioneSW
q10NegPattern1 = "^yes$"
q10NegPattern2 = "(received|granted|recognized) (it|him)"
q10NegPattern3 = "was (received|granted|recognized|allowed)"
q10NegPattern4 = "^((?!no).)*$"

regQuestion10 = {"anakin": tuple([({q10PosPattern1, q10PosPattern2, q10PosPattern3,q10PosPattern4}),
                                  ({q10NegPattern1, q10NegPattern2, q10NegPattern3, q10NegPattern4})])}

# Domanda: What are the two roles that a Jedi can assume in the military hierarchy ? -------------------------------------------------------------------------------------------------------------------
"""
POSITIVE slots 1
--------------------------------
general
role of general
the general


NEGATIVE slots 1
--------------------------------
not the role of general
not general

POSITIVE slots 2
--------------------------------
commander
the role of commander
the commander

NEGATIVE slots 2
--------------------------------
not the role of commander
not the position of commander
not commander

"""
q11PosPattern1_1 = "(general|generals)"
q11PosPattern2_1 = "role of (general|generals)"
q11PosPattern3_1 = "the (general|generals)"
q11PosPattern4_1 = "can be (general|generals)"

q11NegPattern2_1 = "(is not|isn't|not|it's|didn't|did not|don't|do not) (general|generals)"
q11NegPattern3_1 = "(is not|isn't|not|it's|didn't|did not|don't|do not) the (position|role) of (general|generals)"
q11NegPattern4_1 = "(can't|can not) be (general|generals)"

regQuestion11_1 = {"general": tuple([({q11PosPattern1_1, q11PosPattern2_1, q11PosPattern3_1, q11PosPattern4_1}),
                                     ({q11NegPattern2_1, q11NegPattern3_1, q11NegPattern4_1})])}

q11PosPattern1_2 = "(commander|commanders)"
q11PosPattern2_2 = "role of (commander|commanders)"
q11PosPattern3_2 = "the (commander|commanders)"
q11PosPattern4_2 = "can be (commander|commanders)"

q11NegPattern2_2 = "(is not|isn't|not|it's|didn't|did not|don't|do not) (commander|commanders)"
q11NegPattern3_2 = "(is not|isn't|not|it's|didn't|did not|don't|do not) the (position|role) of (commander|commanders)"
q11NegPattern4_2 = "(can't|can not) be (commander|commanders)"

regQuestion11_2 = {"commander": tuple([({q11PosPattern1_2, q11PosPattern2_2, q11PosPattern3_2, q11PosPattern4_2}),
                                       ({q11NegPattern2_2, q11NegPattern3_2, q11NegPattern4_2})])}

# Domanda: what are the three jedi orders ? -------------------------------------------------------------------------------------------------------------------
"""
POSITIVE slots 1
--------------------------------
guardian
the guardians
the order of the guardians

NEGATIVE slots 1
--------------------------------
not the guardian
not the order of the guardians

POSITIVE slots 2
--------------------------------
sentinel
the sentinels
the order of the sentinels

NEGATIVE slots 2
--------------------------------
not the order of the sentinels


POSITIVE slots 3
--------------------------------
consular
the consular
the order of the consular

NEGATIVE slots 3
--------------------------------
not the order of the consular

"""
q12PosPattern1_1 = "(guardian|guardians)"
q12PosPattern2_1 = "the (guardian|guardians)"
q12PosPattern3_1 = "the order of the (guardian|guardians)"

q12NegPattern1_1 = "(is not|isn't|not|it's|didn't|did not|don't|do not) the order of the (guardian|guardians)"
q12NegPattern2_1 = "(is not|isn't|not|it's|didn't|did not|don't|do not) the (guardian|guardians)"
q12NegPattern3_1 = "(is not|isn't|not|it's|didn't|did not|don't|do not) (guardian|guardians)"

regQuestion12_1 = {"guardian": tuple([({q12PosPattern1_1, q12PosPattern2_1, q12PosPattern3_1}),
                                      ({q12NegPattern1_1, q12NegPattern2_1, q12NegPattern3_1})])}

q12PosPattern1_2 = "(sentinel|sentinels)"
q12PosPattern2_2 = "the (sentinel|sentinels)"
q12PosPattern3_2 = "the order of the (sentinel|sentinels)"

q12NegPattern1_2 = "(is not|isn't|not|it's|didn't|did not|don't|do not) the order of the (sentinel|sentinels)"
q12NegPattern2_2 = "(is not|isn't|not|it's|didn't|did not|don't|do not) the (sentinel|sentinels)"
q12NegPattern3_2 = "(is not|isn't|not|it's|didn't|did not|don't|do not) (sentinel|sentinels)"

regQuestion12_2 = {"sentinel": tuple([({q12PosPattern1_2, q12PosPattern2_2, q12PosPattern3_2}),
                                      ({q12NegPattern1_2, q12NegPattern2_2, q12NegPattern3_2})])}

q12PosPattern1_3 = "consular"
q12PosPattern2_3 = "the consular"
q12PosPattern3_3 = "the order of the consular"

q12NegPattern1_2 = "(is not|isn't|not|it's|didn't|did not|don't|do not) the order of the consular"
q12NegPattern2_2 = "(is not|isn't|not|it's|didn't|did not|don't|do not) the consular"
q12NegPattern3_2 = "(is not|isn't|not|it's|didn't|did not|don't|do not) consular"

regQuestion12_3 = {"consular": tuple([({q12PosPattern1_3, q12PosPattern2_3, q12PosPattern3_3}),
                                      ({q12NegPattern1_2, q12NegPattern2_2, q12NegPattern3_2})])}

# # testiamo se il pattern crea un match
# match = re.search(q10PosPattern1, "i dont know")

# if match:
#     print(match.group())
#     print("TRUE")
# else:
#     print("pattern not found")


# if __name__ == "__main__":
#     # resolve()
#     create_db()
#     # with shelve.open("regex") as regexp_db:
#     #     for reg in regexp_db:
#     #         print(reg)
