import re

#frasi semplici
test_string_phrase = "the headquarters of the jedi order is located on the planet coruscant" #riconosciuto da patter 1 
test_string_word = "coruscant" #riconosciuto da patter 1 
test_string_error_word = "coruskant"#funziona per pattern 3
test_string_error_word2 = "corusant"#funziona per pattern 2 e 3

#pattern 
pattern = "coruscant" #funziona in caso di frase corretta
pattern2 = "corusant" #funziona in caso di mancanza di una lettera (errore molto comune)
pattern3 = "cor[a-z]{1,3}ant" #funziona in caso di uno o più errori multipli al centro della
patter4 = "(located|situated) on cor[a-z]{1,3}ant"


"""
----------------------------------------------risolti
the headquarters is not on coruscant.
it is not coruscant
is not coruscant
isn't coruscant
The headquarters of the Jedi Order is not situated on coruscant.
The headquarters of the Jedi Order is not located on any planet.

----------------------------------------------si ignora e si dice che hai sbagliato
The Jedi Order does not exist in the Star Wars universe.
The Jedi Order does not have a headquarters. 

The headquarters of the Jedi Order is located on a planet other than coruscant.
The planet Coruscant does not exist in the Star Wars universe.

---------------------------------------------frasi stronze
The headquarters of the Sith Order is located on Coruscant instead of the Jedi Order. 
"""
#frasi con negazioni
negativephrase = ""

#pattern per trocare le negazioni
patternNegative="(is not|isn't) on cor[a-z]{1,3}ant"
patternNegative2="(is not|isn't) (located|situated) on cor[a-z]{1,3}ant"
patternNegative3 = "(is not|isn't) (located|situated) on any planet"

match = re.search(patternNegative3, negativephrase7) 

if match:
  print(match.group())
  print("TRUE")
else:
  print("pattern not found")