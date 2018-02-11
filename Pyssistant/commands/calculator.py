from gtts import gTTS
from playsound import playsound
def calc(num1, operator, num2):
    if operator == "*":
        ans = str(num1 * num2)
        audioFile = gTTS(text=ans, lang="en")
        audioFile.save("Answer.mp3")
        playsound("Answer.mp3")
    elif operator == "/":
        ans = str(num1 / num2)
        audioFile = gTTS(text=ans, lang="en")
        audioFile.save("Answer.mp3")
        playsound("Answer.mp3")
    elif operator == "+":
        ans = str(num1 + num2)
        audioFile = gTTS(text=ans, lang="en")
        audioFile.save("Answer.mp3")
        playsound("Answer.mp3")
    elif operator == "-":
        ans = str(num1 - num2)
        audioFile = gTTS(text=ans, lang="en")
        audioFile.save("Answer.mp3")
        playsound("Answer.mp3")
    elif operator == "%":
        ans = str(num1 % num2)
        audioFile = gTTS(text=ans, lang="en")
        audioFile.save("Answer.mp3")
        playsound("Answer.mp3")
    elif operator == "**":
        ans = str(num1 ** num2)
        audioFile = gTTS(text=ans, lang="en")
        audioFile.save("Answer.mp3")
        playsound("Answer.mp3")
    
