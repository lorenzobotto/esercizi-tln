# mazzei-chatbot



Questo chatbot permette di interrogare l'utente sulla conoscenza della cultura Jedi  
per decidere se quest'ultimo può diventare o meno un Padawan.

PIPELINE:  
- SPEECH RECOGNITION: L'utente potrà comunicare verbalmente con il chatbot per rispondere alle domande.
- LANGUAGE UNDERSTANDING: Convertito l'informazione verbale in testo, elaboriamo a livello semantico il contenuto delle frasi.
- DIALOG MANAGER: Vengono persistite le informazioni estratte durante la conversazione e vengono minate informazioni implicite (es. Sesso, Nome...). Il DM è composto dal DIALOG CONTROL e DIALOG CONTEXT MODEL.
- RESPONSE GENERATION: Come chatbot, voglio generare risposte attraverso le informazioni ottenute.
- TTS SYSTHESIS: self-explanatory.  

Librerie: 
- `spaCy`
- `speech_recognition`
- `simpleNLG`

