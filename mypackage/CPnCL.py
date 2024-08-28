import tkinter as tk

def clear_text(text_widget):
    """Clear the text in the specified text widget."""
    text_widget.delete("1.0", tk.END)

def copy_to_clipboard(root, text_widget, button):
    """Copy the text from the specified text widget to the clipboard and update the button text."""
    # Copy the text to the clipboard
    root.clipboard_clear()
    root.clipboard_append(text_widget.get("1.0", tk.END))
    
    # Change the button text to "Copied"
    button.config(text="Copied")

    # Reset the button text back to "Copy" after 2 seconds
    root.after(2000, lambda: button.config(text="Copy"))
