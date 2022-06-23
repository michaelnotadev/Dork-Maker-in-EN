# Originally Coded By MuhammedTr768 - hackersmtt@gmail.com
# Tranlated to English by: Slow one
# michaelnotadev
# Created 2022-06-10
# Custom Dork Maker


from tkinter import *
from tkinter import messagebox

pen = Tk()
pen.title('M Dork Maker')
pen.geometry('500x400')

def control():
    sonuc["text"] = "site:" + entry.get(), "filetype:" + entry2.get(), "intitle:" + entry3.get(), "intext:" + entry4.get(), "inurl:" + entry5.get()
    filecreat = open("mdork.txt", "w")
    filecreat.write(sonuc["text"])
    filecreat.close()
girbt = Button(pen, text="GO", command=control)
girbt.pack()

sad = Label(pen, text="Enter Site Name and Extension:")
sad.pack()

entry = Entry(pen, width=15)
entry.pack()

dtip = Label(pen, text="Select File Type")
dtip.pack()

entry2 = Entry(pen, width=15)
entry2.pack()

sbas = Label(pen, text="Select Site Title")
sbas.pack()

entry3 = Entry(pen, width=15)
entry3.pack()

sicerik = Label(pen, text="Enter What You Want To Write Inside The Site:") 
sicerik.pack()

entry4 = Entry(pen, width=15)
entry4.pack()

urlicer = Label(pen, text="Enter What You Want To Write In The URL:") 
urlicer.pack()

entry5 = Entry(pen, width=15)
entry5.pack()

sonuc = Label(pen, text="")
sonuc.pack()


pen.mainloop()
