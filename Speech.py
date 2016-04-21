import subprocess
from threading import Thread

class Speech:
    def __init__(self):
        pass

    def run_cmd(self, text):
        try:
            proc = subprocess.Popen(["espeak", text])
            proc.communicate()
        except Exception:
            pass

    def speak(self, text):
        thread = Thread(target=self.run_cmd(text))
        thread.start()

if __name__ == "__main__":
    speech = Speech()
    speech.speak("hello")