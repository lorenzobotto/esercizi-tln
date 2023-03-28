import re
#Domanda: Where is the headquarters of the Jedi Order located ?---------------------------------------------------------------------------------------------------------------------------------
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
#frase da testare
phrase = "isn't coruscant"

#pattern per frasi positive
q1PosPattern1 = "coruscant" #funziona se ce la parola
q1PosPattern2 = "cor[a-z]{1,3}ant" #funziona se ce la parola ma con qualche errore
#in caso di frasi più composte
q1PosPattern3 = "(located|situated) on cor[a-z]{1,3}ant" 
q1PosPattern4 = "cor[a-z]{1,3}ant is the base" 
q1PosPattern5 = "the base is on cor[a-z]{1,3}ant"

#pattern per frasi con negazione
q1NegPattern1="(is not|isn't) on cor[a-z]{1,3}ant"
q1NegPattern2="(is not|isn't) (located|situated) on cor[a-z]{1,3}ant"
q1NegPattern3 = "(is not|isn't) (located|situated) on (any planet|a planet)"
q1NegPattern4 = "(is not|isn't) cor[a-z]{1,3}ant"
q1NegPattern5 = "(located|situated) on ((?!cor[a-z]{1,3}ant).)*$" #dico che il centro di comando e situato su un altro pianeta
q1NegPattern6 = "((?!cor[a-z]{1,3}ant).)*$" #dico il nome di un altra citta


#testiamo se il pattern crea un match
match = re.search(q1NegPattern6, "banana") 

if match:
  print(match.group())
  print("TRUE")
else:
  print("pattern not found")

#Domanda: What are the three pillars of Jedi culture?---------------------------------------------------------------------------------------------------------------------------------
"""
POSITIVE

-------------------da risolvere------------------------------
the force, knowledge and self-discipline
the force
knowledge
self-discipline
self discipline
the tree pillars of jedi culture is The force, knowledge and self-discipline


NEGATIVE

"""
#frase da testare
phrase = ""

#pattern per frasi positive
q2PosPattern1 = "(the force|force)"
q2PosPattern2 = "knowledge"
q2PosPattern3 = "(self discipline|self-discipline)"

#pattern per frasi con negazione
q1NegPattern1="(is not|isn't) (the force|force)"
q1NegPattern2="(is not|isn't) knowledge"
q1NegPattern3="(is not|isn't) (self discipline|self-discipline)"


