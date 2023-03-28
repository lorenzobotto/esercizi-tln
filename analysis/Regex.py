import re

#frasi semplici
test_string_phrase = "the headquarters of the jedi order is located on the planet coruscant" #riconosciuto da patter 1 
test_string_word = "coruscant" #riconosciuto da patter 1 
test_string_error_word = "coruskant"#funziona per pattern 3
test_string_error_word2 = "corusant"#funziona per pattern 2 e 3

#pattern 
pattern = "coruscant" #funziona se ce la parola
pattern2 = "cor[a-z]{1,3}ant" #funziona se ce la parola ma con qualche errore
#in caso di frasi più corrette
pattern3 = "is (located|situated) on cor[a-z]{1,3}ant" 
pattern4 = "cor[a-z]{1,3}ant is the base" 
pattern5 = "the base is on cor[a-z]{1,3}ant"


"""
frasi negative
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
#frasi con negazioni
negativephrase = "isn't coruscant"

#pattern per trocare le negazioni
patternNegative="(is not|isn't) on cor[a-z]{1,3}ant"
patternNegative2="(is not|isn't) (located|situated) on cor[a-z]{1,3}ant"
patternNegative3 = "(is not|isn't) (located|situated) on any planet"
patternNegative4 = "(is not|isn't) cor[a-z]{1,3}ant"

match = re.search(patternNegative4, negativephrase) 

if match:
  print(match.group())
  print("TRUE")
else:
  print("pattern not found")ù



regex_q1 = set(patternNegative, patternNegative2, patternNegative3)