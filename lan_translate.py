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
root.geometry("600x800")
root.config(bg="Orange")

lab_txt = Label(root,text="Translator", font=("Arial", 35 , "bold"),bg="white")
lab_txt.place(x=150,y=40,height=40,width=300,)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root,text="Enter Text", font=("Arial", 20 , "bold"),bg="white", fg="black")
lab_txt.place(x=170,y=100,height=40,width=250,)

sor_txt = Text(frame, font=("Arial", 20 , "bold"), wrap=WORD)
sor_txt.place(x=20, y=150, height=200,width=560)

list_text = list(LANGUAGES.values())
comb_sor = ttk.Combobox(frame, value=list_text)
comb_sor.place(x=20,y=370,height=40,width=180)
comb_sor.set("English")

button_change = Button(frame, text="Translate", font=("bold") ,relief=RAISED, command=data)
button_change.place(x=210,y=370,height=40,width=180)

comb_dest = ttk.Combobox(frame, value=list_text)
comb_dest.place(x=400,y=370,height=40,width=180)
comb_dest.set("English")

lab_txt = Label(root,text="Translation Text", font=("Arial", 20 , "bold"),bg="white", fg="black")
lab_txt.place(x=170,y=430,height=40,width=250,)

trans_txt = Text(frame, font=("Arial", 20 , "bold"), wrap=WORD)
trans_txt.place(x=20, y=500, height=200,width=560)

root.mainloop()