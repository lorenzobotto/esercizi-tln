import io
import contextlib
import os
from TTS.api import TTS
from threading import Thread
from pydub import AudioSegment
from pydub.playback import play
from utils.io_utilities import thread_dots


class SpeechSynthesizer:
    def __init__(self):
        stop = False
        thread = Thread(target=thread_dots, args=(lambda: stop, "Downloading",))
        thread.start()
        with contextlib.redirect_stdout(io.StringIO()):
            self.model = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts",
                             progress_bar=False, gpu=False)
        stop = True
        thread.join()
        print("\nDone.\n")

    def play(self, text_to_reproduce):
        file_path = "speech/wav_dir/output.wav"
        kwargs = {
            "text": text_to_reproduce,
            "speaker_wav": "speech/wav_dir/obi-wan-kenobi.wav",
            "language": "en",
            "file_path": file_path}
        with contextlib.redirect_stdout(io.StringIO()):
            self.model.tts_to_file(**kwargs)
        song = AudioSegment.from_wav(file_path)
        play(song)
        del song
        os.remove(file_path)

