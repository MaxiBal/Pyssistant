from gtts import gTTS
from playsound import playsound
from random import randint
from time import sleep

def tellAJoke():
    jokeStartList = ["Why can't you play games in the jungle", "How do oceans communicate",
                     "What do you call cheese that is not yours", "Why are ghosts bad liars?",
                     "Why should you never trust atoms", "Why do bees have sticky hair?"]
    jokeEndList = ["There's always gunna be a cheetah", "They Wave", "Nacho Cheese", "You can see right through them",
                   "They make up everything", "Cuz they use honey combs"]
    x = randint(0, len(jokeStartList) - 1)
    singleJokeStart = str(jokeStartList[x])
    singleJokeEnd = str(jokeEndList[x])
    audioFile = gTTS(text=singleJokeStart, lang="en")
    audioFile.save("intro.mp3")
    audioFile2 = gTTS(text=singleJokeEnd, lang="en")
    audioFile2.save("exit.mp3")
    zingo = gTTS(text="zingo", lang="en")
    zingo.save("zingo.mp3")
    
    playsound("intro.mp3")
    sleep(1)
    playsound("exit.mp3")
    sleep(1)
    playsound("zingo.mp3")

