'''This Python file contains all audio functions'''

from gtts import gTTS
import pygame
import os
import pyttsx3
import speech_recognition as sr
from internetCheck import internet_available


def TextToSpeechGoogle(text):
    tts = gTTS(text,lang="en")
    tts.save("output.mp3")


#This Function plays audio using pygame
def playAudio():
    #Checks if output.mp3 exists if it does then play that else play output.wav
    file = "output.mp3" if os.path.exists("output.mp3") else "output.wav"
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    # Wait for the audio to finish playing before removing the file
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    os.remove(file)

#This Function is used to convert from text to speech using pyttsx3 - Used if the device is not connected to the Internet
def TextToSpeechOffline(text): 
    engine = pyttsx3.init()
    engine.save_to_file(text,"output.wav")
    engine.runAndWait()
    engine.stop()

def SpeechToText():
    r = sr.Recognizer()
    mic = sr.Microphone()
    
    print("Listening for your command...")
    
    with mic as source:
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("No speech detected (timeout)")
            speech = "No Command Received"
            if internet_available():
                TextToSpeechGoogle(speech)
            else:
                TextToSpeechOffline(speech)
            playAudio()
            return ""

    try:
        if internet_available():
            print("Recognizing using Google...")
            text = r.recognize_google(audio)
            if text == "":
                raise Exception("Empty recognition result")
            print(f"You said: {text}")
            return text
        else:
            print("Recognizing using Sphinx (offline)...")
            text = r.recognize_sphinx(audio)
            if text == "":
                raise Exception("Empty recognition result")
            print(f"You said: {text}")
            return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        speech = "Sorry, I didn't catch that"
        if internet_available():
            TextToSpeechGoogle(speech)
        else:
            TextToSpeechOffline(speech)
        playAudio()
        return ""
    except sr.RequestError as e:
        print(f"Recognition service error: {e}")
        speech = "Recognition service unavailable"
        if internet_available():
            TextToSpeechGoogle(speech)
        else:
            TextToSpeechOffline(speech)
        playAudio()
        return ""
    except Exception as e:
        print(f"Error: {e}")
        speech = "No Command Received"
        if internet_available():
            TextToSpeechGoogle(speech)
        else:
            TextToSpeechOffline(speech)
        playAudio()
        return ""