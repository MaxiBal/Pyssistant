import wikipedia as wk
from gtts import gTTS
from playsound import playsound
import os
language = "en" #Change if you want in a different language.
def search(x):
    wk.set_lang(language)
    x = str(x)
    wiki = wk.summary(x)
    print(wiki)
    audioFile = gTTS(text=wiki, lang=language)
    audioFile.save("wiki.mp3")
    playsound("wiki.mp3")
    os.remove("wiki.mp3")
