'''This Python file contains all audio functions'''

from gtts import gTTS
import pygame
import os
import pyttsx3



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
    os.remove(file)

#This Function is used to convert from text to speech using pyttsx3 - Used if the device is not connected to the Internet
def TextToSpeechOffline(text): 
    engine = pyttsx3.init()
    engine.save_to_file(text,"output.wav")
    engine.runAndWait()
    engine.stop()