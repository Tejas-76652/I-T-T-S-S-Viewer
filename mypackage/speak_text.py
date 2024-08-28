import os
import time
from gtts import gTTS
from playsound import playsound
import tkinter as tk

def speak(text_widget, langcombo):
    """Convert text from a widget to speech using gTTS and play it."""
    # Generate a unique filename using the current time in milliseconds
    t = time.time()
    ml = int(t * 1000)
    text = text_widget.get(1.0, tk.END).strip()

    if not text:
        print("No text to speak.")
        return
    
    filename = f"tts_{langcombo}_{ml}.mp3"
    tts = gTTS(text, lang=langcombo)
    tts.save(filename)
    playsound(filename)

    # Remove the audio file after playing
    os.remove(filename)

def Uploadspeak(text_area, lang_combobox):
    """Speak the text from the upload area."""
    langcombo = lang_combobox.get()
    speak(text_area, langcombo)

def Translatespeak(text_area1, lang_combobox):
    """Speak the text from the translate area."""
    langcombo = lang_combobox.get()
    speak(text_area1, langcombo)

def Summaryspeak(text_area3, lang_combobox):
    """Speak the text from the summary area."""
    langcombo = lang_combobox.get()
    speak(text_area3, langcombo)
