import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# Initialize text-to-speech engine

def speak(text, language="en"):
    engine = pyttsx3.init()
    
    engine.setProperty('rate', 150) # Speed of speech

    # FIX: Fetch the voices list from the engine so the variable exists
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

#Speech-to-Text: Recognize spoken language (English)

def speech_to_text():
   
   recognizer = sr.Recognizer()

   with sr.Microphone() as source:
      print("???? Please speak now in English...")

      audio = recognizer.listen(source)

   # FIX: Added the mandatory except blocks for the try statement
   try:
        print("Recognizing speech...")
        
        # Use English for speech recognition
        text = recognizer.recognize_google(audio, language="en-US")
        
        print(f"✅ You said: {text}")
        return text
   except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
        return None
   except sr.RequestError:
        print("❌ Could not request results from the service.")
        return None
   
def translate_text(text, target_lang="es"):
    # Default target language is Spanish (es)
    
    translator = Translator()
    
    translation = translator.translate(text, dest=target_lang)
    
    print(f"Translated text: {translation.text}")
    
    return translation.text

def display_language_options():
    print("???? Available translation languages: ")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")

    choice = input("Please select the language number (1-8): ")

    language_dict = {
    "1": "hi",
    "2": "ta",
    "3": "te",
    "4": "bn",
    "5":"mr",
    "6": "gu",
    "7": "ml",
    "8": "pa"
    
}
    return language_dict.get(choice, "es") # Default to Spanish if invalid input

# Main function to combine all steps
def main():

    # Step 1: Display language options and get user's choice
    target_language = display_language_options()

    # Step 2: Speech-to-Text (recognizing English speech)
    original_text = speech_to_text()

    if original_text:
       




