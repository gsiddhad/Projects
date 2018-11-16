# main.py / Idiom Corpus
# Gourav Siddhad
# 07-04-2018

import idiomcorpus
from mtranslate import translate
from tkinter import *

def perform_operation():
    object = idiomcorpus.Idiomcorpus()
    object.idiom_init(e1.get())
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

    try:
        object.check_idiom()
        object.idiom_convert()
        object.idiom_display()
        e2.insert(0, object.hidiom)
        e3.insert(0, object.eidiom)
        e4.insert(0, object.output)
    except:
        e2.insert(0, 'Not Found')
        e3.insert(0, 'Not Found')
        e4.insert(0, translate(e1.get(), 'en'))

master = Tk()
master.title("Hindi to English")
width, height = 800, 200
xcord = master.winfo_screenwidth()/2 - width/2
ycord = master.winfo_screenheight()/2 - height/2
master.geometry("%dx%d+%d+%d" % (width, height, xcord, ycord))

Label(master, text="Hindi").place(x=width/12, y=height/10, width=width/6, height=2*height/15)
Label(master, text="English").place(x=width/12, y=5*height/10, width=width/6, height=2*height/15)

e1 = Entry(master, justify='center')
e1.place(x=width/4, y=height/10, width=4*width/6, height=2*height/15)
e1.insert(END,"﻿भारत और पाकिस्तान के रिश्ते को देख कर लागता है की एक म्यान में दो तलवारें नहीं समातीं")

e2 = Entry(master, justify='center')
e2.place(x=width/20, y=3*height/10, width=5*width/12, height=2*height/15)
e3 = Entry(master, justify='center')
e3.place(x=10*width/20, y=3*height/10, width=5*width/12, height=2*height/15)

e4 = Entry(master, justify='center')
e4.place(x=width/4, y=5*height/10, width=4*width/6, height=2*height/15)

Button(master, text='Quit', command=master.quit).place(x=width/8, y=7*height/10, width=width/4, height=height/5)
Button(master, text='Convert', command=perform_operation).place(x=5*width/8, y=7*height/10, width=width/4, height=height/5)

mainloop()
