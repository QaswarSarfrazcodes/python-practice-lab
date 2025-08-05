# Voice Command Language Translator
# Process: Record → Recognize → Translate → Speak

import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Speech Recognizer
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print(" Recognizing...")
    return recognizer, audio

#  Convert Audio to Text
def convert_audio_to_text(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio)
        print(f" You have  said: {text}")
        return text
    except sr.UnknownValueError:
        print(" Speech not understood.")
        return None
    except sr.RequestError as e:
        print(f"  error: {e}")
        return None

#  Translate Text Using Googletrans
def translate_text(text, target_language):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_language)
        translated_text = translation.text
        print(f"Translation in {target_language}: {translated_text}")
        return translated_text
    except Exception as e:
        print(f" Translation error: {e}")
        return None

#  Convert Translated Text to Speech
def speak_translation(translated_text, target_language):
    try:
        tts = gTTS(text=translated_text, lang=target_language)
        tts.save("translation.mp3")
        os.system("start translation.mp3")  
    except Exception as e:
        print(f" Speech conversion error: {e}")

#  Main 
def main():
    target_language = input("------------ Enter target language code (e.g., 'en','ur'):------------- ").strip()
    recognizer, audio = recognize_speech()
    text = convert_audio_to_text(recognizer, audio)
    if text:
        translated_text = translate_text(text, target_language)
        if translated_text:
            speak_translation(translated_text, target_language)

if __name__ == "__main__":
    main()
