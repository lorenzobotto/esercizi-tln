# part_3
Esercizi per la Terza Parte del corso di TLN (Tecnologie del Linguaggio Naturale) - Unito 2023

## Come eseguire
Crearsi un environment ed installare i requirements necessari:

```pip install -r requirements.txt```

Una volta installati, si possono eseguire tutti i Jupyter.

**N.B.**: Per eseguire l'ex6, è richiesto scaricare gli embeddings di Glove (glove.6B.100d.txt) ed inserirli nel path: ex6/data/glove.6B.100d.txt.

## ex1
Misurazione dell’overlap lessicale tra una serie di definizioni per concetti generici/specifici e concreti/astratti.

## ex2
I comuni dizionari a cui siamo abituati partono dalle parole, ovvero dalla forma, per arrivare al contenuto. Esistono alcuni tipi
di dizionario chiamati dizionari analogici che funzionano ”al
contrario”, ovvero non si ricerca per parola ma per definizione.
Questo tipo di ricerca viene chiamata ricerca onomasiologica,
ovvero si parte dal contenuto per arrivare alla forma. Su questo principio si basa l'ex2.

## ex3
Implementazione della teoria sulle valenze di Patrick Hanks. In particolare, partendo da un corpus e uno specifico verbo, l’idea è di costruire dei possibili
cluster semantici, con relativa frequenza. Ad es., dato il verbo
"to see" con valenza v = 2, e usando un parser sintattico (ad
es. Spacy), si possono collezionare eventuali fillers per i ruoli
di subj e obj del verbo, per poi convertirli in semantic types.
Su questo principio si basa l'ex3.

## ex4
Implementazione di un sistema di text segmentation, prendendo ispirazione da TextTiling. In particolare, partendo da un corpus composto da 3 sezioni su tematiche molto diverse il sistema deve individuare le giuste linee di taglio (o quasi).

## ex5
Implementazione del Topic Modeling, utilizzando librerie open (come ad es. GenSim2
). Testing di algoritmi (ad esempio LDA) con più valori di k (num. di
topics) e valutazione della coerenza dei risultati.

## ex6
Classificazione basic/advanced. Uso del dataset su basicness per fare classificazione binaria automatica (basic/advanced) su nuovi termini e/o synset presi in esame.