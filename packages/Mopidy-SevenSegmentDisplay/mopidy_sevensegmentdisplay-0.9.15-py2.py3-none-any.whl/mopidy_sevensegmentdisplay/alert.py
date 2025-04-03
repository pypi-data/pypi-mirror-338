import random
import time
import logging
import json
from subprocess import call
from .max7219 import Symbols


class Alert:
    A = Symbols.A
    L = Symbols.L
    E = Symbols.E
    R = Symbols.R
    T1 = Symbols.T1
    T2 = Symbols.T2

    ANIMATION_ALERT = {
        "length": 1,
        "repeat": 1,
        "sleep": 0.05,
        "buffer": [
            [0, 0, 0, 0, 0, 0, 0, A],
            [0, 0, 0, 0, 0, 0, A, 0],
            [0, 0, 0, 0, 0, A, 0, 0],
            [0, 0, 0, 0, A, 0, 0, 0],
            [0, 0, 0, A, 0, 0, 0, 0],
            [0, 0, A, 0, 0, 0, 0, 0],
            [0, A, 0, 0, 0, 0, 0, L],
            [0, A, 0, 0, 0, 0, L, 0],
            [0, A, 0, 0, 0, L, 0, 0],
            [0, A, 0, 0, L, 0, 0, 0],
            [0, A, 0, L, 0, 0, 0, 0],
            [0, A, L, 0, 0, 0, 0, E],
            [0, A, L, 0, 0, 0, E, 0],
            [0, A, L, 0, 0, E, 0, 0],
            [0, A, L, 0, E, 0, 0, 0],
            [0, A, L, E, 0, 0, 0, R],
            [0, A, L, E, 0, 0, R, 0],
            [0, A, L, E, 0, R, 0, 0],
            [0, A, L, E, R, 0, 0, T1],
            [0, A, L, E, R, 0, T1, T2],
            [0, A, L, E, R, T1, T2, 0],
            [0, A, L, E, R, T1, T2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, A, L, E, R, T1, T2, 0],
            [0, A, L, E, R, T1, T2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, A, L, E, R, T1, T2, 0],
            [0, A, L, E, R, T1, T2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, A, L, E, R, T1, T2, 0]
        ]
    }

    def __init__(self, music, ir_sender, files):
        self._music = music
        self._ir_sender = ir_sender
        self._files = json.loads(files)

    def run(self, index):
        try:
            if (index is not None and 0 <= index < len(self._files)):
                if (not self._files[index]["enabled"]):
                    return
                file = self._files[index]
            else:
                file = random.choice([x for x in self._files if x["enabled"]])

            is_playing = self._music.is_playing()

            if (is_playing):
                self._music.pause()
            else:
                self._ir_sender.power(True)
                time.sleep(10 if "ir_send" in file else 2)

            if ("ir_send" in file):
                if ("bass" in file["ir_send"]):
                    self._ir_sender.bass(file["ir_send"]["bass"])
                if ("volume" in file["ir_send"]):
                    self._ir_sender.volume(file["ir_send"]["volume"])

            self._play_file(file["name"], file["volume"], file["repeat"])

            if ("ir_send" in file):
                if ("bass" in file["ir_send"]):
                    self._ir_sender.bass(- file["ir_send"]["bass"])
                if ("volume" in file["ir_send"]):
                    self._ir_sender.volume(- file["ir_send"]["volume"])

            if (is_playing):
                self._music.play(None)
            else:
                time.sleep(5 if "ir_send" in file else 1)
                self._ir_sender.power(False)
        except Exception as inst:
            logging.error(inst)

    def is_enabled(self):
        return len(self._files) > 0

    def get_files(self):
        return self._files

    def get_draw_alert_animation(self):
        return self.ANIMATION_ALERT

    def _play_file(self, file, volume=32768, repeat=1, sleep=0.5):
        for i in range(repeat):
            call(["mpg123", "-f", str(volume), "-q", file])
            time.sleep(sleep)
