
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

LANGUAGES = {
    "Dwarvish": "Dwarvish.json",
    "Elvish": "Elvish.json",
    "Draconic": "Draconic.json",
    "Infernal": "Infernal.json"
}

def load_alphabet(language):
    filename = LANGUAGES.get(language)
    if not filename:
        raise ValueError(f"Lingua non supportata: {language}")
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def translate(text, language):
    alphabet = load_alphabet(language)
    result = []
    for char in text:
        upper_char = char.upper()
        if upper_char in alphabet:
            translated = alphabet[upper_char]
            if char.islower():
                translated = translated.lower()
            result.append(translated)
        else:
            result.append(char)
    return ''.join(result)

def run_gui():
    root = tk.Tk()
    root.title("D&D Translator")
    root.geometry("420x320")
    root.resizable(False, False)

    style = ttk.Style()
    style.theme_use('clam')

    title = ttk.Label(root, text="D&D Translator", font=("Segoe UI", 18, "bold"))
    title.pack(pady=10)

    frame = ttk.Frame(root)
    frame.pack(pady=5)

    lang_label = ttk.Label(frame, text="Lingua:", font=("Segoe UI", 12))
    lang_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    lang_var = tk.StringVar(value=list(LANGUAGES.keys())[0])
    lang_menu = ttk.Combobox(frame, textvariable=lang_var, values=list(LANGUAGES.keys()), state="readonly", font=("Segoe UI", 12))
    lang_menu.grid(row=0, column=1, padx=5, pady=5)

    input_label = ttk.Label(root, text="Testo da tradurre:", font=("Segoe UI", 12))
    input_label.pack(pady=(10,0))
    input_text = tk.Text(root, height=4, width=40, font=("Segoe UI", 11))
    input_text.pack(pady=5)

    output_label = ttk.Label(root, text="Traduzione:", font=("Segoe UI", 12))
    output_label.pack(pady=(10,0))
    output_text = tk.Text(root, height=4, width=40, font=("Segoe UI", 11), state="disabled", bg="#f4f4f4")
    output_text.pack(pady=5)

    def do_translate():
        lang = lang_var.get()
        text = input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showinfo("Info", "Inserisci del testo da tradurre.")
            return
        try:
            translated = translate(text, lang)
            output_text.config(state="normal")
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, translated)
            output_text.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

    translate_btn = ttk.Button(root, text="Traduci", command=do_translate)
    translate_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_gui()


