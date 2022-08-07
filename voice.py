from gtts import gTTS
import os


def voice():
    text1 = "hello ashwanth"
    lang1 = 'en'

    voice = gTTS(text=text1, lang=lang1, slow=True)

    voice.save("test1.mp3")
    os.system(" start test1.mp3")


voice()
