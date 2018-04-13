#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 15:22:17 2018

@author: ahmedosman
"""
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg 
from matplotlib.figure import Figure
#from matplotlib import pyplot as plt
#import matplotlib.backend_bases
#from PIL import Image
import matplotlib.image as mpimg
#import matplotlib.cm as cm
from tkinter import *
#import tkinter as tk
import skimage.io
from skimage.io import imread
from skimage import io, color

 
root=Tk()
root.title("GUI")
root.geometry("1000x500")
fpathentered=StringVar()

def displayimage():
    
        def clear(): 
                canvas.get_tk_widget().destroy()
            
        txt=fpathentered.get()
        fpath=str(txt)
        img=imread(fpath)
        img_gray=color.rgb2gray(img)
        f = Figure()
        a = f.add_subplot(111)
        a.imshow(img_gray)
        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.show()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
        canvas._tkcanvas.pack(side="top", fill="both", expand=1)
        
        button3=Button(root, text="Delete", width=15, command=clear)
        button3.grid(row=20)
        
def showfilepath():
    s=fpathentered.get()
    filepath=str(s)
    #label2= Label(root, text="The file path entered is " + txt + "\n")
    #label2.pack()
    filepathdisplay.insert(0.0, "The file path entered is " + filepath + "\n")
 
def diagnosis():
    p=fpathentered.get()   
    ipath=str(p)
    print("the file path is ", p)
    return p

def displaystring():
    
    q=fpathentered.get()
    i=str(q)
    filepathdisplay1.insert(0.0, "The skin lesion is " + i + "\n")

def closewindow():
    root.destroy()
    exit()
       
label=Label(root, text="Skin Disease Classification System")
label.config(font=("Courier", 20))
label.grid(row=0)

label1=Label(root,text="Enter file path of image:", bg="white", fg="black", font="none 12 bold")
label1.grid(row=1)

#enter text in entry box

filepathentry=Entry(root,width=20, bg="white", textvariable=fpathentered)
filepathentry.grid(row=2)

button = Button(root, text="Show Entry", command=showfilepath)
button.grid(row=3)
 
button1=Button(root, text="Display Image", width=14, command=displayimage)
button1.grid(row=4 )

button2=Button(root, text="Exit", width=14, command=closewindow)
button2.grid(row=5)

#button3=Button(root, text="Delete", width=15, command=clear)
#button3.pack()

filepathdisplay=Text(root, width=30, height =2, wrap=WORD)
filepathdisplay.grid(row=6)

filepathdisplay1=Text(root, width=30, height =2, wrap=WORD)
filepathdisplay1.grid(row=7)



root.mainloop()

