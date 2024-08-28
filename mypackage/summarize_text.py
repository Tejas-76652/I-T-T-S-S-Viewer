import tkinter as tk
from tkinter import messagebox
from transformers import pipeline

summarizer = pipeline("summarization")


# Initialize the summarization pipeline using PyTorch
summarizer = pipeline("summarization", model="google/pegasus-xsum", framework="pt")

def summarize_and_update_button(root, text_area, text_area1, text_area3, button):
    # Change the button text to "Summarizing..."
    button.config(text="Summarizing...")

    # Perform the summarization
    Summarize(text_area, text_area1, text_area3)

    # Reset the button text back to "Summarize" after 2 seconds
    root.after(2000, lambda: button.config(text="Summarize"))


def Summarize(text_area, text_area1, text_area3):
    text_area3.delete(1.0, tk.END)  # Clear the summarizer box

    if text_area1.get(1.0, tk.END).strip():  # Check if Translate box has text
        text_to_summarize = text_area1.get(1.0, tk.END)
    else:  # If Translate box is empty, check Upload box
        text_to_summarize = text_area.get(1.0, tk.END)

    if text_to_summarize.strip():  # Only summarize if there is text
        try:
            # Summarize the text
            summary = summarizer(text_to_summarize, max_length=50, min_length=30, do_sample=False)
            text_area3.insert('end', summary[0]['summary_text'])
        except Exception as e:
            messagebox.showerror("Summarization Error", f"An error occurred during summarization: {e}")
    else:
        messagebox.showinfo("No Text", "There is no text to summarize.")
