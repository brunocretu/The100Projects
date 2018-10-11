#Text Editor
#Notepad style application that can open, edit, and save text documents. Add syntax highlighting and other features.
#Most of the code was taken from: https://www.youtube.com/watch?v=xqDonHEYPgA by Zach King
#Zach's Github: https://github.com/zcking

from tkinter import *
from tkinter import filedialog

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)

    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)

    try:
        f.write(t.rstrip())
    except:
        showerror(title='Oops!', message='Unable to save file...')

def openFile():
    f.askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

def main():
    root = Tk()
    root.title('Text Editor')
    root.minsize(width=400, height=400)
    root.maxsize(width=400, height=400)

    text = Text(root, width=400, height=400)
    text.pack()

    menubar = Menu(root)
    filemenu = Menu(menubar)
    filemenu.add_command(label='New', command=newFile)
    filemenu.add_command(label='Open', command=openFile)
    filemenu.add_command(label='Save', command=saveFile)
    filemenu.add_command(label='Save as...', command=saveAs)
    filemenu.add_separator()
    filemenu.add_command(label='Quit', command=root.quit())
    menubar.add_cascade(label='File', menu=filemenu)

    root.config(menu=menubar)

    root.mainloop()

if __name__ == '__main__':
    main()
