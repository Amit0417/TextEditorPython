from tkinter import *
from tkinter import filedialog


def new_file():
    text.delete(0.0, END)


def open_file():
    file1 = filedialog.askopenfile(mode='r')
    data = file1.read()
    text.delete(0.0, END)
    text.insert(0.0, data)


def save_file():
    filename = 'Untitled.txt'
    data = text.get(0.0, END)
    file1 = open(filename, 'w')
    file1.write(data)


def save_as():
    file1 = filedialog.asksaveasfile(mode='w')
    data = text.get(0.0, END)
    file1.write(data)


gui = Tk()
gui.title('Text Editor')
gui.geometry("600x500")
text = Text(gui)
text.pack()
mymenu = Menu()
list1 = Menu()
list2 = Menu()
list1.add_command(label='New File', command=new_file)
list1.add_command(label='Open File', command=open_file)
list2.add_command(label='Save As',  command=save_as)
mymenu.add_cascade(label='File', menu=list1)
mymenu.add_cascade(label='Save', menu=list2)
mymenu.add_cascade(label='Exit', command=gui.quit)
gui.config(menu=mymenu)
gui.mainloop()
