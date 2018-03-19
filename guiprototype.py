#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 15:22:17 2018

@author: ahmedosman
"""

from tkinter import *
import tkinter as tk
from skimage.io import imread
from skimage.transform import resize
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.figure import Figure
import matplotlib.cm as cm

 
root=Tk()
root.title("GUI")
root.geometry("1000x500")


def displayimage():
    txt=filepathentry.get()
    img=imread(txt)
    f = Figure()
    a = f.add_subplot(111)
    a.imshow(img)
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
    canvas._tkcanvas.pack(side="top", fill="both", expand=1)
    '''label2= Label(root, text="The file path entered is " + txt + "\n")
    label2.pack()
    img=imread(txt)
    plt.imshow(img)
    plt.show()
    return (filepath)
    '''
def showfilepath():
    s=filepathentry.get()
    filepath=str(s)
    #label2= Label(root, text="The file path entered is " + txt + "\n")
    #label2.pack()
    filepathdisplay.insert(0.0, "The file path entered is " + filepath + "\n")
    
def closewindow():
    root.destroy()
    exit()
    
#def showImage():
    
    
    
label=Label(root, text="Skin Disease Classification System")
label.config(font=("Courier", 34))
label.pack()

label1=Label(root,text="Enter file path of image:", bg="white", fg="black", font="none 12 bold")
label1.pack()

#enter text in entry box
filepathentry=Entry(root,width=20, bg="white")
filepathentry.pack()

button = Button(root, text="Show Entry", command=showfilepath)
button.pack()
 
#r=showtext()
#print("the file path is", r)

button1=Button(root, text="Display Image", width=14, command=displayimage)
button1.pack()

button1=Button(root, text="Exit", width=14, command=closewindow)
button1.pack()

filepathdisplay=Text(root, width=30, height =2, wrap=WORD)
filepathdisplay.pack()

#canvas=Canvas(root, width=500, height=500)
#canvas.pack()

#etext=textentry.get()

    
#def savetext (self):
        #self.enteredtext=textentry.get()
        #print ("the entered text is" )
        #output.delete(0.0, END)
        #filepath=input('textentry')

#def printtext(self):
        
        #label=self.Label(root, text=textentry)
        #self.label.pack()
    
       # print ("the entered text is", textentry )

 
#image= "/Users/User/Desktop/Year4/WINTER2018/BME800/image10.png"

#button1 = Button(root, text="Upload Image", command=name)
#button1.pack()

#def displaytext():
 #   label2=Label(root, text="hello")
  #  label2.config(font="none 12")
   # label2.pack()
    

 


#button3 = Button(root, text="Print text", command=self.printtext)
#button3.pack()



#canvas= Canvas(root, width=300,height=300)
#canvas.bind("<Button>", printName)
#canvas.pack()

root.mainloop()

