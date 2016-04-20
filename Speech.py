import subprocess


class Speech:
    def __init__(self):
        pass

    def speak(self, text):
        try:
            proc = subprocess.Popen(["espeak", text])
            proc.communicate()
        except Exception:
            pass

if __name__ == "__main__":
    speech = Speech()
    speech.speak("hello")