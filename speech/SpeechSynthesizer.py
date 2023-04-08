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
        self._clean_dir()
        try:
            kwargs = {
                "text": text_to_reproduce,
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

