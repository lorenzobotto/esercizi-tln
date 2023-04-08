import speech_recognition


class SpeechRecognitionHandler:
    def __init__(self):
        self.handler = speech_recognition.Recognizer()

    def speak(self):
        can_continue = True
        while can_continue:
            with speech_recognition.Microphone() as audio_src:
                print("\nI'm listening...")
                audio = self.handler.listen(audio_src)
            try:
                print(self.handler.recognize_google(audio))
            except speech_recognition.UnknownValueError:
                print("Quite not catched that. Can you repeat?")
        except speech_recognition.RequestError:
            print("ERROR: Speech Recognition API is not currently working")

