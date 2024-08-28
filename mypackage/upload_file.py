import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract
import PyPDF2 as pdf

def upload_and_update_button(root, text_area, button):
    # Change the button text to "Uploading..."
    button.config(text="Uploading...")

    # Perform the upload function
    upload(text_area)

    # Reset the button text back to "Upload" after 2 seconds
    root.after(2000, lambda: button.config(text="Upload"))

def upload(text_area):
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
            #print("PDF File")
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
