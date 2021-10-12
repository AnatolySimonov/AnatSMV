import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

FILE_NAME = tkinter.NONE


def new_file():
    global FILE_NAME
    FILE_NAME = 'Безымянный'
    text.delete('1.0', END)


def save_file():
    data = text.get('1.0', END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()


def save_as():
    out = asksaveasfilename(filetypes=(
     ("TXT files", ".txt"),
     ("HTML files", ".html;.htm"),
     ("All files", ".*")))
    out_file = open(out, 'w')
    data = text.get('1.0', END)
    out_file.write(data)


def open_file():
    global FILE_NAME
    inp = askopenfilename()
    if inp is None:
        return
    a = open(inp, 'r', encoding="utf-8")
    data = a.read()
    text.delete('1.0', END)
    text.insert('1.0', data)


root = tkinter.Tk()
root.title('Блокнот')

root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)

text = tkinter.Text(root, width=400, height=400, wrap='word')
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side='right', fill='y')
text.configure(yscrollcommand=scrollb.set)

text.pack()
menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label='Создать', command=new_file)
fileMenu.add_command(label='Открыть', command=open_file)
fileMenu.add_command(label='Сохранить', command=save_file)
fileMenu.add_command(label='Сохранить как', command=save_as)

menuBar.add_cascade(label='Файл', menu=fileMenu)

root.config(menu=menuBar)
root.mainloop()
