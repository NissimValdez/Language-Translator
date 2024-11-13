from tkinter import *
import googletrans
from googletrans import Translator, constants
from tkinter import ttk, messagebox

root = Tk()
root.title('Language Translator')
root.geometry("1200x570")
root.config(bg="#2C3E50")

tl = Translator()

def translate():
    translated_text.delete(1.0, END)
    try:
        for key, value in languages.items():
            try: 
                from_language_key = key
            except ('Detect Language' == original_combo.get()):
                detect = tl.detect(original_text.get(1.0, END))
                from_language_key = detect.lang

        for key, value in languages.items():
            if (value.capitalize() == translated_combo.get()):
                to_language_key = key

        txt = original_text.get(1.0, END)
        translation = tl.translate(txt, src=from_language_key, dest=to_language_key)

        translated_text.insert(1.0, translation.text)

    except Exception as e:
        messagebox.showerror("Translator", e)

def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

def detect():
    detect = tl.detect(original_text.get(1.0, END))
    language = constants.LANGUAGES[detect.lang]
    lC = language.capitalize()
    my_label = Label(root, text=f"Entered language is {lC}", font=("Microsoft YaHei UI", 12), bg="#2C3E50", fg="white")
    my_label.grid(row=4, column=1, pady=12)

languages = googletrans.LANGUAGES

lower_language_list = list(languages.values())
language_list = list(map(lambda x: x.capitalize(), lower_language_list))
language_list.append('Detect Language')
language_abbreviation_list = list(languages.keys())

original_text = Text(root, height=10, width=40, font=("Microsoft YaHei UI", 14), bg="#ECF0F1", fg="#2C3E50")
original_text.grid(row=0, column=0, padx=20, pady=20)

translated_text = Text(root, height=10, width=40, font=("Microsoft YaHei UI", 14), bg="#ECF0F1", fg="#2C3E50")
translated_text.grid(row=0, column=2, padx=20, pady=20)

original_combo = ttk.Combobox(root, width=30, value=language_list, font=("Microsoft YaHei UI", 12))
original_combo.current(107)
original_combo.grid(row=1, column=0, padx=20, pady=10)

translated_combo = ttk.Combobox(root, width=30, value=language_list, font=("Microsoft YaHei UI", 12))
translated_combo.current(93)
translated_combo.grid(row=1, column=2, padx=20, pady=10)

translate_button = Button(root, text='Translate', font=("Microsoft YaHei UI", 14), command=translate, bg="#3498DB", fg="white", padx=10, pady=5)
translate_button.grid(row=0, column=1, padx=10, pady=5)

clear_button = Button(root, text='Clear', font=("Microsoft YaHei UI", 12), command=clear, bg="#E74C3C", fg="white", padx=10, pady=5)
clear_button.grid(row=2, column=1, pady=5)

detect_button = Button(root, text='Detect Language', font=("Microsoft YaHei UI", 12), command=detect, bg="#1ABC9C", fg="white", padx=10, pady=5)
detect_button.grid(row=3, column=1, pady=20)

my_label = Label(root, text="", font=("Microsoft YaHei UI", 12), bg="#2C3E50", fg="white")
my_label.grid(row=4, column=1, pady=10)

root.mainloop()