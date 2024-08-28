import tkinter as tk
from tkinter import filedialog
import random
import string

def generate_random_filename(extension=".txt"):
    """Generate a random filename with the given extension."""
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return f"{random_string}{extension}"

def save_file(text_widget):
    """Save the text from the text widget to a file."""
    default_filename = generate_random_filename()
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             initialfile=default_filename,
                                             filetypes=[("Text files", ".txt"), ("All files", ".*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_widget.get("1.0", tk.END))

def custom_save_dialog(root, text_area, text_area1, text_area3):
    """Display a dialog for saving text from different text areas."""
    dialog = tk.Toplevel(root)
    dialog.title("Save")
    dialog.geometry("300x150")
    
    label = tk.Label(dialog, text="What do you want to download?", font="Arial 12 bold")
    label.pack(pady=10)

    upload_button = tk.Button(dialog, text="Upload Text", command=lambda: [save_file(text_area), dialog.destroy()])
    upload_button.pack(pady=5)

    translate_button = tk.Button(dialog, text="Translate Text", command=lambda: [save_file(text_area1), dialog.destroy()])
    translate_button.pack(pady=5)
   
    summary_button = tk.Button(dialog, text="Summary Text", command=lambda: [save_file(text_area3), dialog.destroy()])
    summary_button.pack(pady=5)
