# main.py / Stemmer
# Gourav Siddhad
# 07-04-2018

import stemmer
from tkinter import *

def perform_operation():
    object = stemmer.Stemmer()
    object.stem_init(e1.get())
    e2.delete(0, END)
    e3.delete(0, END)

    try:
        object.hstem()
        e2.insert(0, object.rem)
        e3.insert(0, object.output)
    except:
        e2.insert(0, 'Not Found')
        e3.insert(0, 'Not Found')

master = Tk()
master.title("Hindi Word Stemming")
width, height = 400, 200
xcord = master.winfo_screenwidth()/2 - width/2
ycord = master.winfo_screenheight()/2 - height/2
master.geometry("%dx%d+%d+%d" % (width, height, xcord, ycord))

Label(master, text="Hindi").place(x=width/12, y=height/10, width=width/6, height=2*height/15)
Label(master, text="Ending").place(x=width/12, y=3*height/10, width=width/6, height=2*height/15)
Label(master, text="Stemmed").place(x=width/12, y=5*height/10, width=width/6, height=2*height/15)

e1 = Entry(master, justify='center')
e1.place(x=width/4, y=height/10, width=4*width/6, height=2*height/15)
e1.insert(END,"दृष्टिकोण")

e2 = Entry(master, justify='center')
e2.place(x=width/4, y=3*height/10, width=4*width/6, height=2*height/15)

e3 = Entry(master, justify='center')
e3.place(x=width/4, y=5*height/10, width=4*width/6, height=2*height/15)

Button(master, text='Quit', command=master.quit).place(x=width/8, y=7*height/10, width=width/4, height=height/5)
Button(master, text='Stem', command=perform_operation).place(x=5*width/8, y=7*height/10, width=width/4, height=height/5)

mainloop()
