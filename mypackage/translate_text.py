import tkinter as tk
from tkinter import messagebox
import pyperclip
from googletrans import Translator

translater = Translator()

def trans_and_update_button(root, text_area, text_area1, text_area3, lang_combobox, List_key, button):
    # Change the button text to "Translating..."
    button.config(text="Translating...")

    # Perform the translation
    trans(text_area, text_area1, text_area3, lang_combobox, List_key)

    # Reset the button text back to "Translate" after 2 seconds
    root.after(2000, lambda: button.config(text="Translate"))

def trans(text_area, text_area1, text_area3, lang_combobox, List_key):
    # Clear the existing text in text_area1
    text_area1.delete(1.0, tk.END)
    langcombo = lang_combobox.get()

    # Prioritize text_area3 (summarizer box) if it has text:
    if text_area3.get(1.0, tk.END).strip():
        text = text_area3.get(1.0, tk.END)
    else:
        text = text_area.get(1.0, tk.END)

    if text.strip():  # Only proceed if there is text to translate
        detect = translater.detect(text)
        d = detect.lang
        print("upload lang: ",d)

        for i in range(len(List_key)):
            if langcombo == List_key[i]:
                out = translater.translate(text, dest=List_key[i])
                trtext = out.text
                print("translated lang: ",translater.detect(trtext).lang)
                #pyperclip.copy(trtext)
                text_area1.insert('end', trtext + "\n")
    else:
        messagebox.showinfo("No Text", "There is no text to translate.")
