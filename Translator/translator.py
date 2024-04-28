#The following packages have to be installed
# pip install SpeechRecognition
# pip install googletrans==4.0.0-rc1  
# pip install gTTS
# pip install playsound



import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import playsound

def speech_to_text(language="en-US"):
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        print(f" speak now (in {language})")
        audio = recognizer.listen(source, timeout=None)
    try:
        text = recognizer.recognize_google(audio, language=language)
        print(f"You said: {text}")
        return text
    except sr.RequestError:
        print("API unavailable. Check your internet connection.")
        return None
    except sr.UnknownValueError:
        print("Unable to recognize speech. Please try again.")
        return None

def translate_text(text, src_language, dest_language):
    translator = Translator()
    try:
        translated = translator.translate(text, src=src_language, dest=dest_language)
        return translated.text
    except Exception as e:
        print(f"Error during translation: {str(e)}")
        return None

def text_to_speech(text, language="en"):
    try:
        tts = gTTS(text=text, lang=language)
        filename = "temp.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    except Exception as e:
        print(f"Error in text-to-speech conversion: {str(e)}")

def main():
    language_options = {'1': ('en', 'ur'), '2': ('ur', 'en')}
    print("Select the language you will speak in :")
    print("1: English to Urdu")
    print("2: Urdu to English")
    choice = input("Enter your choice (1 or 2): ")

    if choice not in language_options:
        print("Invalid choice. Exiting.")
        return
    
    src_language, dest_language = language_options[choice]
    src_language_code = 'en-US' if src_language == 'en' else 'ur-PK'
    dest_language_code = dest_language

    spoken_text = speech_to_text(src_language_code)
    if spoken_text:
        translated_text = translate_text(spoken_text, src_language, dest_language_code)
        if translated_text:
            print(f"Translated Text: {translated_text}")
            text_to_speech(translated_text, dest_language_code)
        else:
            print("Failed to translate text.")
    else:
        print("Failed to recognize speech.")

if __name__ == "__main__":
    main()




