import tkinter as tk
from tkinter import filedialog, messagebox, Text
from tkinter.ttk import Combobox
from transformers import pipeline
from gtts import gTTS
from playsound import playsound
import pyperclip
import os
import time
import random
import string
import json
import pytesseract
from PIL import Image
import PyPDF2 as pdf
from googletrans import Translator
from tkinter import Tk, Text, Button #Combobox 
from mypackage.upload_file import upload,upload_and_update_button
from mypackage.translate_text import trans,trans_and_update_button
from mypackage.summarize_textpt import Summarize,summarize_and_update_button
from mypackage.CPnCL import clear_text, copy_to_clipboard
from mypackage.speak_text import Uploadspeak, Translatespeak, Summaryspeak
from mypackage.Save_txt import custom_save_dialog




# Load language data
with open('languages.json') as json_file:
    data = json.load(json_file)
List_key = list(data.keys())

# Initialize Tkinter root window
root = tk.Tk()
root.title("Text to Speech")
root.geometry("900x600+200+200")
root.resizable(False, False)
root.configure(bg="#00e0ff")

# Background and Heading border of Tkinter
bg = tk.PhotoImage(file="assets/image4.png")
canvas1 = tk.Canvas(root, width=900, height=600)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")

image_icon = tk.PhotoImage(file="assets/speaker logo.png")
root.iconphoto(False, image_icon)

# Top Frame
Top_frame = tk.Frame(root, bg="white", width=1100, height=70)
Top_frame.place(x=0, y=0)
Logo = tk.PhotoImage(file="assets/speak.png")
tk.Label(Top_frame, image=Logo, bg="white").place(x=10, y=5)
tk.Label(Top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="white", fg="black").place(x=80, y=15)

# Text Box and Scroll Bar
scrol_bar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrol_bar.pack(side=tk.RIGHT, fill=tk.Y)

# First text area
text_area = tk.Text(root, font="roboto 20", bg="white", relief=tk.GROOVE, wrap=tk.WORD)
text_area.place(x=10, y=150, width=450, height=150)

# Buttons for the first text area:
copy_button1 = tk.Button(root, text="Copy", command=lambda: copy_to_clipboard(root, text_area, copy_button1))
copy_button1.place(x=420, y=123)

image = tk.PhotoImage(file="assets/Speakericon.png")
speakicon1 = image.subsample(9, 9)
Speak1 = tk.Button(root, text="Speak", image=speakicon1, compound=tk.LEFT, command=lambda: Uploadspeak(text_area, lang_combobox))
Speak1.place(x=10, y=305)

Clear_1 = tk.Button(root, text="Clear", command=lambda: clear_text(text_area))
Clear_1.place(x=80, y=305)

# Second text area
text_area1 = tk.Text(root, font="roboto 20", bg="white", relief=tk.GROOVE, wrap=tk.WORD)
text_area1.place(x=10, y=400, width=450, height=150)

# Buttons for the second text area:

copy_button2 = tk.Button(root, text="Copy", command=lambda: copy_to_clipboard(root, text_area1, copy_button2))
copy_button2.place(x=420, y=373)

image = tk.PhotoImage(file="assets/Speakericon.png")
speakicon2 = image.subsample(9, 9)
Speak2 = tk.Button(root, text="Speak", compound=tk.LEFT, image=speakicon2, command=lambda: Translatespeak(text_area1, lang_combobox))
Speak2.place(x=10, y=555)

Clear_2 = tk.Button(root, text="Clear", command=lambda: clear_text(text_area1))
Clear_2.place(x=80, y=555)

# Summary Button:
image = tk.PhotoImage(file="assets/summary.png")
sum1 = image.subsample(20, 20)
summarize_Button = tk.Button(root, text="Summarize", compound=tk.LEFT, width=190, image=sum1, bg="#AEC6CF", font="arial 14 bold", command=lambda: summarize_and_update_button(root, text_area, text_area1, text_area3, summarize_Button))
summarize_Button.place(x=500, y=80)

text_area3 = tk.Text(root, font="roboto 20", bg="white", relief=tk.GROOVE, wrap=tk.WORD)
text_area3.place(x=500, y=150, width=370, height=150)

# Buttons for the third text area:

copy_button3 = tk.Button(root, text="Copy", command=lambda: copy_to_clipboard(root, text_area3, copy_button3))
copy_button3.place(x=828, y=123)

image = tk.PhotoImage(file="assets/Speakericon.png")
speakicon3 = image.subsample(9, 9)
Speak3 = tk.Button(root, compound=tk.LEFT, text="Speak", image=speakicon3, command=lambda: Uploadspeak(text_area3, lang_combobox))
Speak3.place(x=500, y=305)

Clear_3 = tk.Button(root, text="Clear", command=lambda: clear_text(text_area3))
Clear_3.place(x=570, y=305)

# Translate Combobox and Button:
imageicon4 = tk.PhotoImage(file="assets/translate.png")
tr = tk.Button(root, text="Translate", compound=tk.LEFT, image=imageicon4, width=170, bg="#AEC6CF", font="arial 14 bold", command=lambda: trans_and_update_button(root, text_area, text_area1, text_area3, lang_combobox, List_key, tr)) #command=lambda:trans(text_area, text_area1, text_area3, lang_combobox, List_key))
tr.place(x=10, y=335)
lang_combobox = Combobox(root, values=List_key, font="arial 14", state='r', width=5)
lang_combobox.place(x=200, y=345)
lang_combobox.set('hi')

# # Speak Button
# imageicon = tk.PhotoImage(file="assets/speak.png")
# btn = tk.Button(root, text="Speak", compound=tk.LEFT, image=imageicon, width=130, font="arial 14 bold", command=lambda: translatedVoice())
# btn.place(x=500, y=335)

# Save Button:
image = tk.PhotoImage(file="assets/savetext.png")
save1 = image.subsample(20, 20)
save = tk.Button(root, text="Save", compound=tk.LEFT, image=save1, width=130, bg="#E5E4E2", font="arial 14 bold", command=lambda: custom_save_dialog(root, text_area, text_area1, text_area3))
save.place(x=712, y=320)

# Upload Button:
imageicon3 = tk.PhotoImage(file="assets/Upload.png")
upload_btn = tk.Button(root, text="Upload", compound=tk.LEFT, image=imageicon3, width=160, bg="#AEC6CF", font="arial 14 bold", command=lambda: upload_and_update_button(root, text_area, upload_btn)) #command=lambda:upload(text_area))
upload_btn.place(x=10, y=82)

# Start the Tkinter event loop:
root.mainloop()
