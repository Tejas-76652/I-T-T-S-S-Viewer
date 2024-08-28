import time
import random
import string
# from distutils.command.upload import upload
# #from operator import indexOf
from tkinter import Tk
import tkinter as tk
# from token import LEFTSHIFT
from playsound import playsound
from gtts import gTTS
import pyperclip
from tkinter import *
from tkinter import filedialog,messagebox,Text

from transformers import pipeline
from tkinter.ttk import Combobox
import pyttsx3
import os
#from PIL import Image, ImageTk
import pytesseract
from PIL import Image
import PyPDF2 as pdf
# from mypackage.upload_file import upload
# from distutils.filelist import translate_pattern
from googletrans import Translator
import json



with open('languages.json') as json_file:
    data = json.load(json_file)
    # print("data is =>",data)
Key = data.keys()
List_key = list(Key)
Value = data.values()
List_val = list(Value)

'''print("key is =>",Key)
print("List of key is =>",List_key)
print("Value is =>",Value)
print("List of values is =>",Key)'''

root = Tk()
root.title("text to speech")
root.geometry("900x600+200+200")
root.resizable(True, True)
root.configure(bg="#00e0ff")


# Function to upload and process file:
def upload():
    f_types = [('All Files', '.*'), ('PNG Files', '.png'), ('JPG Files', '.jpg'), ('PDF Files', '.pdf'), 
               ('YAML Files', '.yaml'), ('JPEG Files', '.jpeg')]
    x = (".png", ".jpg", ".jpeg")
    y = (".pdf")
    filepath = filedialog.askopenfilename(multiple=False, filetypes=f_types)
    
    # Clear previous text in text_area
    text_area.delete(1.0, tk.END)
    
    if filepath.endswith(x):
        try:
            pytesseract.pytesseract.tesseract_cmd = r"C:\Users\tejas\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
            image = Image.open(filepath)
            image_to_text = pytesseract.image_to_string(image, lang='eng+spa+hin+jpn+mal')
            text_area.insert('end', image_to_text)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while processing the Image: {e}")

    elif filepath.endswith(y):
        try:
            print("PDF File")
            a = pdf.PdfReader(filepath)
            number_of_pages = len(a.pages)
            for num in range(number_of_pages):
                page = a.pages[num]
                text = page.extract_text()
                text_area.insert('end', text)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while processing the PDF: {e}")
    else:
        messagebox.showwarning("Unsupported File Type", "The selected file type is not supported. Please choose a PNG, JPG, or PDF file.")

# Function to translate text:
translater = Translator()

def trans():
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
        print(d)

        for i in range(len(List_key)):
            if langcombo == List_key[i]:
                out = translater.translate(text, dest=List_key[i])
                trtext = out.text
                pyperclip.copy(trtext)
                text_area1.insert('end', trtext + "\n")
    else:
        messagebox.showinfo("No Text", "There is no text to translate.")

# # Summary Function:

# summarizer = pipeline("summarization")

# def Summarize():
#     text_area3.delete(1.0, tk.END)  # Clear the summarizer box

#     if text_area1.get(1.0, tk.END).strip():  # Check if Translate box has text
#         text_to_summarize = text_area1.get(1.0, tk.END)
#     else:  # If Translate box is empty, check Upload box
#         text_to_summarize = text_area.get(1.0, tk.END)

#     if text_to_summarize.strip():  # Only summarize if there is text
#         try:
#             # Summarize the text
#             summary = summarizer(text_to_summarize, max_length=40, min_length=20, do_sample=False)
#             text_area3.insert('end', summary[0]['summary_text'])
#         except Exception as e:
#             messagebox.showerror("Summarization Error", f"An error occurred during summarization: {e}")
#     else:
#         messagebox.showinfo("No Text", "There is no text to summarize.")

# Initialize the summarization pipeline using PyTorch
summarizer = pipeline("summarization", framework="pt")

def summarize_text(text):
    summary = summarizer(text, max_length=50, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def Summarize():
    text_area3.delete(1.0, tk.END)
    
    # Prioritize text in translate box
    text_to_summarize = text_area1.get(1.0, tk.END).strip()
    
    if not text_to_summarize:
        # If translate box is empty, check upload box
        text_to_summarize = text_area.get(1.0, tk.END).strip()
    
    if text_to_summarize:
        summary = summarize_text(text_to_summarize)
        text_area3.insert('end', summary)

# #Upload Fuction:

# def upload():
#     # f_types = [('png', '.png'), ('jpg', '.jpg'), ('pdf', '.pdf'),('yaml', '.yaml')]
#     f_types=[('All Files', '.*'), ('PNG Files', '.png'), ('JPG Files', '.jpg'), ('PDF Files', '.pdf'), ('YAML Files', '.yaml'), ('JPEG Files', '.jpeg')]

#     x = (".png",".jpg",".jpeg")
#     y = (".pdf")
#     filepath = filedialog.askopenfilename(multiple=False, filetypes=f_types)
#     if filepath.endswith(x):
#         try:
#             pytesseract.pytesseract.tesseract_cmd = r"C:\Users\tejas\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
#             image = Image.open(filepath)
#             image_to_text = pytesseract.image_to_string(image, lang='eng+spa+hin+jpn+mal')
#             pyperclip.copy(image_to_text)
#             print(image_to_text)
#             pyperclip.copy(image_to_text)
#             s2 = pyperclip.paste()
#             text_area.insert('end', s2)
#         except Exception as e:
#                 messagebox.showerror("Error", f"An error occurred while processing the Image: {e}")

#     elif filepath.endswith(y):
#             try:
#                 print("PDF File")
#                 a = pdf.PdfReader(filepath)
#                 number_of_pages = len(a.pages)
#                 print(f"Number of pages in PDF: {number_of_pages}")
#                 for num in range(number_of_pages):
#                     page = a.pages[num]
#                     text = page.extract_text()
#                     print(text)
#                     pyperclip.copy(text)
#                     s3 = pyperclip.paste()
#                     text_area.insert('end', s3)
#             except Exception as e:
#                 messagebox.showerror("Error", f"An error occurred while processing the PDF: {e}")
        
#     else:
#         messagebox.showwarning("Unsupported File Type", "The selected file type is not supported. Please choose a PNG, JPG, or PDF file.")
#         print("Unsupported File Type")

# Copy to Clipboard function:
def copy_to_clipboard(text_widget, button):
    # Copy the text to the clipboard
    root.clipboard_clear()
    root.clipboard_append(text_widget.get("1.0", tk.END))
    
    # Change the button text to "Copied":
    button.config(text="Copied")

       # Select all text in the text widget (This Shows the selected Text):
    # text_widget.tag_add("sel", "1.0", tk.END)
    
    # Scroll to the beginning of the text (Copy from the Begining) : 
    # text_widget.mark_set(tk.INSERT, "1.0")
    # text_widget.see(tk.INSERT)
    
    
    # Reset the button text back to "Copy" after 2 seconds
    root.after(2000, lambda: button.config(text="Copy"))


# #Translation Function:

# translater = Translator()

# def trans():
#     # Clear the existing text in text_area1
#     text_area1.delete(1.0, tk.END)
#     langcombo = lang_combobox.get()
#     text = text_area.get(1.0, tk.END)
#     detect = translater.detect(text)
#     # print("detect ", detect)
#     d = detect.lang
#     print(d)

#     for i in range(len(List_key)):
#         if langcombo == List_key[i]:
#             out = translater.translate(text, dest=List_key[i])
#             trtext = out.text
#             pyperclip.copy(trtext)
#             s4 = pyperclip.paste()
#             text_area1.insert('end', s4 + "\n")

# Voice of Upload:

engine = pyttsx3.init()


def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
            setvoice()
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
            setvoice()
            engine.runAndWait()
        else:
            engine.setProperty('rate', 60)
            setvoice()
            engine.runAndWait()

# Voice of Translate by Pyttxs(take Voice from Local OS):

def speaknow2():
    text = text_area1.get(1.0, END)
    print("Speak 2 text -"+text)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')
    detect = translater.detect(text).lang
    print("detected :"+detect)
    
    def setvoice():
        if gender == 'Male':
            print("voice id:"+voices[0].id)
            engine.setProperty('voice', voices[0].id)
            print(voices)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
            setvoice()
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
            setvoice()
            engine.runAndWait()
        else:
            engine.setProperty('rate', 60)
            setvoice()
            engine.runAndWait()

# Voice of Translate by gtts:

def speaknow3():
    # string=remove(str)
    # s=r(string)
    # print(s)
    t = time.time()
    ml = int(t * 1000)
    langcombo = lang_combobox.get()
    text = text_area1.get(1.0, END)
    print(text)
    
    # If Want to save Voice:

    filename = "tts"+langcombo+str(ml)+".mp3"
    tts = gTTS(text, lang=langcombo)
    tts.save(filename)
    playsound(filename)
# Remove this If want to Save Sound:
    os.remove(filename)


def translatedVoice():
    #langcombo = lang_combobox.get()
    # print("Text in translated text area  :"+langcombo)
    text = text_area1.get(1.0, END).strip()
    if not text:
        speaknow()
    else:
        speaknow3()

# .txt file save Fuction:

def generate_random_filename(extension=".txt"):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return f"{random_string}{extension}"

def save_file(text_widget):
    default_filename = generate_random_filename()
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             initialfile=default_filename,
                                             filetypes=[("Text files", ".txt"), ("All files", ".*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_widget.get("1.0", tk.END))

# Save Button:

def custom_save_dialog():
    dialog = tk.Toplevel(root)
    dialog.title("Save")
    dialog.geometry("300x150")
    
    label = tk.Label(dialog, text="What do you want to download?", font="Arial 12 bold")
    label.pack(pady=10)

    upload_button = tk.Button(dialog, text="Upload Text", command=lambda: [save_file(text_area), dialog.destroy()])
    upload_button.pack(pady=5)

    translate_button = tk.Button(dialog, text="Translate Text", command=lambda: [save_file(text_area1), dialog.destroy()])
    translate_button.pack(pady=5)

# Background and Heading border of Tkinter:

bg = PhotoImage(file="assets/BG1.png")


canvas1 = Canvas(root, width=900,
                 height=600)

canvas1.pack(fill="both", expand=True)

canvas1.create_image(0, 0, image=bg,
                     anchor="nw")

image_icon = PhotoImage(file="assets/speaker logo.png")
root.iconphoto(False, image_icon)

# Top Frame
Top_frame = Frame(root, bg="white", width=1100, height=70)
Top_frame.place(x=0, y=0)

Logo = PhotoImage(file="assets/speak.png")
Label(Top_frame, image=Logo, bg="white").place(x=10, y=5)
Label(Top_frame, text="TEXT TO SPEECH", font="arial 20 bold",
      bg="white", fg="black").place(x=80, y=15)

# Text Box and Scroll Bar:

scrol_bar = Scrollbar(root, orient=VERTICAL)
scrol_bar.pack(side=RIGHT, fill=Y)
# First text area
text_area = tk.Text(root, font="roboto 20", bg="white",
                    relief=tk.GROOVE, wrap=tk.WORD)
text_area.place(x=10, y=150, width=450, height=150)

# Copy button for the first text area
copy_button1 = tk.Button(root, text="Copy", command=lambda: copy_to_clipboard(text_area, copy_button1))
copy_button1.place(x=415, y=150)

# Second text area
text_area1 = tk.Text(root, font="roboto 20", bg="white",
                     relief=tk.GROOVE, wrap=tk.WORD)
text_area1.place(x=10, y=400, width=450, height=150)

# Copy button for the second text area
copy_button2 = tk.Button(root, text="Copy", command=lambda: copy_to_clipboard(text_area1, copy_button2))
copy_button2.place(x=415, y=400)

scrol_bar.config(command=text_area1.yview)

# # Voice and Text button:

# Label(root, text="VOICE", font="arial 15 bold",
#       bg="#305065", fg="white").place(x=580, y=160)
# Label(root, text="SPEED", font="arial 15 bold",
#       bg="#305065", fg="white").place(x=760, y=160)


# # combo box
# gender_combobox = Combobox(
#     root, values=['Male', 'Female'], font="arial 14", state='r', width=10)
# gender_combobox.place(x=550, y=200)
# gender_combobox.set('Male')

# # speed combobox
# speed_combobox = Combobox(
#     root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='r', width=10)
# speed_combobox.place(x=730, y=200)
# speed_combobox.set('Normal')

#Summary
summarize_Button = Button(root, text="Summarize", compound=LEFT, width=20, bg="#39c790", font="arial 14 bold",
                       command=Summarize)
summarize_Button.place(x=500, y=100)

# 3rd Text area:

text_area3 = tk.Text(root, font="roboto 20", bg="white",
                    relief=tk.GROOVE, wrap=tk.WORD)
text_area3.place(x=500, y=150, width=370, height=150)

# Copy button for the 3rd text area:
copy_button3 = tk.Button(root, text="Copy", command=lambda: copy_to_clipboard(text_area3, copy_button3))
copy_button3.place(x=820, y=150)


# translate combobox
imageicon4 = PhotoImage(file="assets/translate.png")

tr = Button(root, text="Translate", compound=LEFT, image=imageicon4, width=150, bg="#39c790", font="arial 14 bold",
            command=trans)
tr.place(x=10, y=335)

lang_combobox = Combobox(
    root, values=(List_key), font="arial 14", state='r', width=5)
lang_combobox.place(x=180, y=345)
lang_combobox.set('hi')

imageicon = PhotoImage(file="assets/speak.png")
btn = Button(root, text="Speak", compound=LEFT, image=imageicon,
             width=130, font="arial 14 bold",command=translatedVoice)
btn.place(x=500, y=335)

imageicon2 = PhotoImage(file="assets/download.png")
save = Button(root, text="Save", compound=LEFT, image=imageicon2, width=130, bg="#39c790", font="arial 14 bold",
              command=custom_save_dialog)
save.place(x=680, y=335)

imageicon3 = PhotoImage(file="assets/Upload 1.png")
save = Button(root, text="Upload", compound=LEFT, image=imageicon3, width=150, bg="#39c790", font="arial 14 bold",
             command=upload)
save.place(x=10, y=82)





# Start the Tkinter event loop
root.mainloop()