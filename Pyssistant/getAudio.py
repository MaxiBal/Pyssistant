#talking and VUI
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
#import commands
#see commands folder for more information on what each does
from commands.wikiSearch import search
import commands.weather as we
from commands.calculator import calc
from commands.trans import translate
from favorites.jokes import tellAJoke
import pyowm

r = sr.Recognizer()
#def to start listening for the commands
def startListening():
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
    try:
        recognizedString = r.recognize_google(audio)
        print(recognizedString)
        if "wiki" in recognizedString.lower():
            finalString = recognizedString.lower().replace("wiki ", "")
            search(finalString)
        if "weather" in recognizedString.lower():
            finalString = recognizedString.strip("weather ")
            if "in" in finalString.lower():
                finalString = finalString.strip("in")
            #if weather location is not found
            try:
                we.getWeather(finalString)
            except pyowm.exceptions.not_found_error.NotFoundError:
                we.notFound()
        elif "*" in recognizedString.lower() or "multiplied by" in recognizedString.lower():
            string = recognizedString.lower().replace("* ", "").split(" ")
            firstnum = int(string[0])
            secondnum = int(string[1])
            calc(firstnum, "*", secondnum)
        elif "+" in recognizedString.lower():
            string = recognizedString.lower().replace("+ ", "").split(" ")
            firstnum = int(string[0])
            secondnum = int(string[1])
            calc(firstnum, "+", secondnum)
        elif "-" in recognizedString.lower():
            string = recognizedString.lower().replace("- ", "").split(" ")
            firstnum = int(string[0])
            secondnum = int(string[1])
            calc(firstnum, "-", secondnum)
        elif "/" in recognizedString.lower():
            string = recognizedString.lower().replace("/ ", "").split(" ")
            firstnum = int(string[0])
            secondnum = int(string[1])
            calc(firstnum, "/", secondnum)
        elif "^" in recognizedString.lower():
            string = recognizedString.lower().replace("^ ", "").split(" ")
            firstnum = int(string[0])
            secondnum = int(string[1])
            calc(firstnum, "**", secondnum)
        elif "remainder" in recognizedString.lower():
            string = recognizedString.lower().replace("remainder of ", "").replace("and ", "").split(" ")
            firstnum = int(string[0])
            secondnum = int(string[1])
            calc(firstnum, "%", secondnum)
        elif "translate" in recognizedString.lower():
            string = recognizedString.lower().replace("translate ", "").replace(" to", "").split(" ")
            language = str(string[int(len(string) - 1)])
            del string[-1]
            "".join(string)
            textToTranslate = str(string[0])
            translate(textToTranslate, language)
        elif "joke" in recognizedString.lower():
            tellAJoke()
        elif "thanks" in recognizedString.lower():
            return None
    except PermissionError:
        audioFile = gTTS(text="Sorry, I've burned out of this command, use it again later.")
        audioFile.save("commandFinish.mp3")
        playsound("commandFinish.mp3")
    except sr.UnknownValueError:
        audioFile = gTTS(text="Sorry, I couldn't understand you.")
        audioFile.save("Sorry.mp3")
        playsound("Sorry.mp3")

while True:
    startListening()
