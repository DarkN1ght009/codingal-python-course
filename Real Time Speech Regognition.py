import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) # Speed of speech

    # Fetch the voices list from the engine
    voices = engine.getProperty('voices')

    if language == "en":
        # Default English voice
        engine.setProperty('voice', voices[0].id) 
    else:
        # Fallback to another voice if available
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id) 
        else:
            engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("???? Please speak now in English...")

    try:
       print("???? Recognizing speech...")
       text = recognizer.recognize_google(audio, language="en-US") # Uses Google Web Speech API
       print(f"✅ You said: {text}")
       return text

    except sr.UnknownValueError:
      print("❌ Could not understand audio")

    except sr.RequestError as e:
       print(f"❌ API Error: {e}")

    return ""

def translate_text(text, target_language="es"): # Default target language is Spanish (es)

    translator = Translator()

    translation = translator.translate(text, dest=target_language)

    print(f"Translated text: {translation.text}")

    return translation.text

def display_language_options():
    print("\n🌐 Available translation languages: ")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")

    choice = input("Please select the language number (1-8): ")

    language_dict = {
        "1": "hi",
        "2": "ta",
        "3": "te",
        "4": "bn",
        "5": "mr",
        "6": "gu",
        "7": "ml",
        "8": "pa"
    }
    return language_dict.get(choice, "es") # Default to Spanish if invalid input

def main():
    # Step 1: Get target language from user
    target_language = display_language_options()

    # Step 2: Convert Speech to Text
    original_text = speech_to_text()

    if original_text:
        # Step 3: Translate to selected target language
        translated_text = translate_text(original_text, target_lang=target_language)

        if translated_text:
            # Step 4: Text-to-Speech (Speak the translated output)
            # Note: pyttsx3 uses the voices installed on your system. 
            # If your OS doesn't have the target language pack installed, it will fallback to English.
            speak(translated_text, language=target_language)  
            print("✅ Translation spoken out!")

if __name__ == "__main__":
    main()