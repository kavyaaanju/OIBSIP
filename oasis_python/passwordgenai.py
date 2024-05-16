import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        messagebox.showerror("Error", "No character set selected.")
        return None
    
    password = ''
    while 'ai' in password:  # Ensure 'ai' sequence is not present
        password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def generate_button_clicked():
    length = int(length_entry.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        password_output.config(state=tk.NORMAL)
        password_output.delete(0, tk.END)
        password_output.insert(0, password)
        password_output.config(state=tk.DISABLED)

def copy_to_clipboard():
    generated_password = password_output.get()
    root.clipboard_clear()
    root.clipboard_append(generated_password)
    root.update()

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

letters_var = tk.BooleanVar()
letters_checkbox = tk.Checkbutton(root, text="Include Letters", variable=letters_var)
letters_checkbox.pack()

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_checkbox.pack()

symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_checkbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_button_clicked)
generate_button.pack()

password_output = tk.Entry(root, state=tk.DISABLED)
password_output.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

root.mainloop()
