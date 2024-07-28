# part_2
Esercizi per la Seconda Parte del corso di TLN (Tecnologie del Linguaggio Naturale) - Unito 2023

## Come eseguire
Crearsi un environment ed installare i requirements necessari:

```pip install -r requirements.txt```

Una volta installati, si possono eseguire tutti i Jupyter.

## ex1
Implementazione della conceptual similartity, che consiste nel fornire un punteggio numerico di similarità di due termini, che ne indichi la vicinzanza semantica.

L’input per questa esercitazione è costituito da coppie di termini a cui è attribuito un valore numerico [0, 10] che rappresenta la similarità fra gli elementi della coppia.

L'esercizio consiste nell'implementare tre misure di similarità basate su WordNet:
- WU & Palmer similarity
- Shortest Path similarity
- Leacock & Chodorow similarity

Per ciascuna di tali misure di similarità, vengono calcolati gli indici di
correlazione di Spearman e gli indici di correlazione di Pearson fra i risultati ottenuti e quelli ‘target’ presenti nel file annotato.

## ex2
Mapping di Frame in WN Synsets.

Come prima cosa, si individuano un insieme di Frame di riferimento scelti casualmente (FrameSet).
Per ogni frame nel FrameSet è necessario assegnare un WN synset ai seguenti elementi:
- Frame name: nel caso si tratti di una multiword expression, come per esempio
'Religious_belief', disambiguare il termine principale, che in generale è il sostantivo se l'espressione è composta da NOUN+ADJ, e il verbo se l'espressione è composta da VERB+NOUN; in generale l'elemento fondamentale è individuato come il reggente dell'espressione.
- Frame Elements (FEs) del frame;
- Lexical Units (LUs).

I contesti di disambiguazione possono essere creati utilizzando le definizioni disponibili dei Frame, FEs e LUs, mentre per il contesto dei sensi presenti in WN si selezionano glosse ed esempi d'uso.

L'algoritmo di mapping utilizzando è il bag of words e scelta del senso che permette di massimizzare l'intersezione fra i contesti, utilizzando e riscrivendo (from scratch) l'algoritmo di Lesk per ottenere il miglior synset.

Per la fase di valutazione, sono stati annotati i vari frames e si calcola l'accuratezza tra i synset annotati rispetto all'algoritmo Lesk.

## ex3
Dato il Trump Twitter Archive (~290 tweet attribuiti all'ex Presidente US):
- SI acquisiscono due language models (uno a bi-grammi e uno a trigrammi) su questo set di testi;
- Si utilizzano questi due modelli per generare nuovi tweet. In pratica, si costruisce una matrice delle probabilità condizionate che, data una parola, indica la probabilità che un'altra parola segua (per i bigrammi, e in modo analogo per i trigrammi). In questo modo, si crea una frase in cui le parole si susseguono secondo le probabilità più alte.

## ex4
Il principio su cui si basa questo ex4, è l'utilizzo del metodo di Rocchio per la classificazione di documenti.
- Dati due set di documenti (italiano vs. inglese; 20 docs x 10 classi, vs.
20 docs x 20 classi) con caratteristiche diverse, se ne sceglie uno e si divide in train/test.
- Utilizzando una rappresentazione vettoriale (CountVectorizer e TfidfVectorizer) si devono costruire i profili (Rocchio) relativi alle classi cui
appartengono i documenti.
- Si classifica i nuovi documenti (utilizzando come metrica di distanza la
cosine similarity o una delle metriche derivate) in una delle classi date.