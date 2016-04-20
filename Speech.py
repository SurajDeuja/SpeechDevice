import subprocess


class Speech:
    def __init__(self):
        pass

    def speak(self, text):
        proc = subprocess.Popen(["espeak", text])
        proc.communicate()

if __name__ == "__main__":
    speech = Speech()
    speech.speak("hello")