from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", trans="Urdu"):
    trans0 = Translator()
    translation = trans0.translate(text, src=src, dest=trans)
    return translation.text

def data():
    s = comb_sor.get()
    t = comb_dest.get()
    msg = sor_txt.get(1.0, END)
    textget = change(text=msg, src=s, trans=t)
    trans_txt.delete(1.0, END)
    trans_txt.insert(END, textget)

root = Tk()
root.title("Language Translator")
root.geometry("1200x800")  # Set a larger window size
root.config(bg="light grey")  # Light grey background similar to iOS apps

# Title label
lab_title = Label(root, text="MyTranslator", font=("Arial", 35, "bold"), bg="dark cyan", fg="white")
lab_title.grid(row=0, column=0, columnspan=4, pady=20)

# Source language combobox
lab_sor_lang = Label(root, text="Source Language:", font=("Arial", 14, "bold"), bg="light grey")
lab_sor_lang.grid(row=1, column=0, padx=10, pady=10, sticky=W)
comb_sor = ttk.Combobox(root, value=list(LANGUAGES.values()), font=("Arial", 12))
comb_sor.grid(row=1, column=1, padx=10, pady=10, sticky=W)
comb_sor.set("English")

# Destination language combobox
lab_dest_lang = Label(root, text="Destination Language:", font=("Arial", 14, "bold"), bg="light grey")
lab_dest_lang.grid(row=1, column=2, padx=10, pady=10, sticky=W)
comb_dest = ttk.Combobox(root, value=list(LANGUAGES.values()), font=("Arial", 12))
comb_dest.grid(row=1, column=3, padx=10, pady=10, sticky=W)
comb_dest.set("Urdu")

# Source text label
lab_sor_txt = Label(root, text="Enter Text", font=("Arial", 20, "bold"), bg="dark cyan", fg="white")
lab_sor_txt.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=W)

# Translation text label
lab_trans_txt = Label(root, text="Translation Text", font=("Arial", 20, "bold"), bg="dark cyan", fg="white")
lab_trans_txt.grid(row=2, column=2, columnspan=2, padx=10, pady=10, sticky=W)

# Source text box
sor_txt = Text(root, font=("Arial", 16), wrap=WORD, bd=2, relief=GROOVE)
sor_txt.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=N+S+E+W)

# Translation text box
trans_txt = Text(root, font=("Arial", 16), wrap=WORD, bd=2, relief=GROOVE)
trans_txt.grid(row=3, column=2, columnspan=2, padx=10, pady=10, sticky=N+S+E+W)

# Translate button
button_change = Button(root, text="Translate", font=("Arial", 14, "bold"), bg="dark cyan", fg="white", command=data)
button_change.grid(row=4, column=0, columnspan=4, pady=20)

# Configure grid weights to make text boxes expand with window
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(3, weight=1)

root.mainloop()
