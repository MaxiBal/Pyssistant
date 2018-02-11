from googletrans import Translator
from gtts import gTTS
from playsound import playsound

def translate(translationText, language):
    if language == "afrikaans":
        language = "af"
    elif language == "albanian":
        language = "sq"
    elif language == "arabic":
        language = "ar"
    elif language == "armenian":
        language = "hy"
    elif language == "bengali":
        language = "bn"
    elif language == "catalan":
        language = "ca"
    elif language == "chinese":
        language = "zh"
    elif language == "mandarin chinese":
        language = "zh-cn"
    elif language == "mandarin taiwan":
        langauge = "zh-tw"
    elif language == "cantonese":
        language = "zh-yue"
    elif language == "croatian":
        language = "hr"
    elif language == "czech":
        language = "cs"
    elif language == "danish":
        language = "da"
    elif language == "dutch":
        language = "nl"
    elif language == "english":
        language = "en"
    elif language == "english australia":
        language = "en-au"
    elif language == "english united kingdom":
        language = "en-uk"
    elif language == "english united states":
        language = "en-us"
    elif language == "esperanto":
        language = "eo"
    elif language == "finnish":
        language = "fi"
    elif language == "french":
        language = "fr"
    elif language == "german":
        language = "de"
    elif language == "greek":
        language = "el"
    elif language == "hindi":
        language = "hi"
    elif language == "hungarian":
        language = "hu"
    elif language == "icelandic":
        language = "is"
    elif language == "indonesion":
        language = "id"
    elif language == "italian":
        language = "it"
    elif language == "japanese":
        language = "ja"
    elif language == "cambodian":
        language = "km"
    elif language == "korean":
        language = "ko"
    elif language == "latin":
        language = "la"
    elif language == "latvian":
        language = "lv"
    elif language == "macedonian":
        language = "mk"
    elif language == "norwegian":
        language = "no"
    elif language == "polish":
        language = "pl"
    elif language == "portuguese":
        language = "pt"
    elif language == "romanian":
        language = "ro"
    elif language == "russian":
        language = "ru"
    elif language == "serbian":
        language = "sr"
    elif language == "sinhala":
        language = "si"
    elif language == "slovak":
        language = "sk"
    elif language == "spanish":
        language = "es"
    elif language == "spainish spain":
        language = "es-es"
    elif language == "spanish united states":
        language = "es-us"
    elif language == "swahili":
        language = "sw"
    elif language == "swedish":
        language = "sv"
    elif language == "tamil":
        language = "ta"
    elif language == "thai":
        language = "th"
    elif language == "turkish":
        language = "tr"
    elif language == "ukranian":
        language = "uk"
    elif language == "vietnamese":
        language = "vi"
    elif language == "welsh":
        language = "cy"
    translator = Translator()
    finalTrans = str(translator.translate(translationText, dest=language)).strip("Translated(src=en").strip(")").replace(", pronunciation=", "")
    finalTrans = finalTrans.replace(finalTrans[:1], "").replace(" dest=", "")
    finalTrans = finalTrans.replace(finalTrans[:3], "").replace("text=", "").replace("None", "")
    print(finalTrans)
    audioFile = gTTS(text=finalTrans, lang=language)
    audioFile.save("translatedFile.mp3")
    playsound("translatedFile.mp3")
