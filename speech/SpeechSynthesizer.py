import os
import io
import contextlib
import pydub.playback
from TTS.api import TTS
from threading import Thread
from pydub import AudioSegment
from utils.io_utilities import thread_dots


class SpeechSynthesizer:
    def __init__(self):
        stop = False
        self.file_path = "speech/wav_dir/output.wav"
        thread = Thread(target=thread_dots, args=(lambda: stop, "Downloading",))
        thread.start()
        with contextlib.redirect_stdout(io.StringIO()):
            self.model = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts",
                             progress_bar=False, gpu=False)
        stop = True
        thread.join()
        print("\nDone.\n")

    def play(self, text_to_reproduce):
        digit_dict = {0:"zero",1: "one",2: "two",3:"three",
                      4:"four",5:"five",6:"six",7:"seven",
                      8: "eight",9 :"nine", 10: "ten", 11:"eleven", 12:"twelve"}
        new_text_to_reproduce = ""
        for word in text_to_reproduce.split(" "):
            if word == "Obi-1":
                new_text_to_reproduce += "Obi one "
            elif word.isnumeric() and int(word) in digit_dict:
                new_text_to_reproduce += f"{digit_dict[int(word)]} "
            else:
                new_text_to_reproduce += word + " "
        self._clean_dir()
        try:
            kwargs = {
                "text": new_text_to_reproduce,
                "speaker_wav": "speech/wav_dir/obi-wan-kenobi.wav",
                "language": "en",
                "file_path": self.file_path}
            with contextlib.redirect_stdout(io.StringIO()):
                self.model.tts_to_file(**kwargs)
            speech_response = AudioSegment.from_wav(self.file_path)
            pydub.playback.play(speech_response)
        finally:
            self._clean_dir()
            del speech_response

    def _clean_dir(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

