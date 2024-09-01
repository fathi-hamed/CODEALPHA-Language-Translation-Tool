from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


root= Tk()
root.geometry('1100x500')
root.resizable(0,0)
root['bg']='thistle'
root.title('Language Translator')
Label(root, text='Language Translator', font= 'Arial 20 bold').pack()

Label(root, text='Enter Text', font='Arial 13 bold', bg='white smoke').place(x=165,y=90)
input_text = Entry(root, width= 70)
input_text.place(x=30, y=130)
input_text.get()

# input_text = Text(root, width= 50, height=11)
# input_text.place(x=30, y=130)

Label(root, text='Output', font='Arial 13 bold', bg='white smoke').place(x=780,y=90)
output_text = Text(root, font = 'Arial 10', height = 11, wrap = WORD, padx = 5, pady=5, width = 60)
output_text.place(x=600, y=130)


language = list(LANGUAGES.values())
dest_lang = ttk.Combobox(root, values= language, width=22)
dest_lang.place(x=30, y=200)
dest_lang.set('Choose Language')

def Translate():
    translator = Translator()
    translated = translator.translate(text = input_text.get(), dest= dest_lang.get())
    output_text.delete(1.0,END)
    output_text.insert(END, translated.text)

trans_btn = Button(root, text= 'Translate', font='Arial 12 bold', pady=5, command = Translate, bg='mediumorchid', activebackground= 'violet')
trans_btn.place(x=30, y=250)

root.mainloop()