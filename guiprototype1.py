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
from matplotlib import pyplot as plt
from PIL import Image
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


def displayimage():
    
    txt=fpathentered.get()
    fpath=str(txt)
    img=imread(fpath)
    img_gray=color.rgb2gray(imgi)
    f = Figure()
    a = f.add_subplot(111)
    a.imshow(img_gray)
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
    canvas._tkcanvas.pack(side="top", fill="both", expand=1)
    
    '''label2= Label(root, text="The file path entered is " + txt + "\n")
    label2.pack()
    plt.imshow(img)
    plt.show()
    return (filepath)
    '''
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
    
    
#def deleteimage():
 #   c.delete("all")
    
def closewindow():
    root.destroy()
    exit()

    
label=Label(root, text="Skin Disease Classification System")
label.config(font=("Courier", 34))
label.pack()

label1=Label(root,text="Enter file path of image:", bg="white", fg="black", font="none 12 bold")
label1.pack()

#enter text in entry box
fpathentered=StringVar()
filepathentry=Entry(root,width=20, bg="white", textvariable=fpathentered)
filepathentry.pack()

button = Button(root, text="Show Entry", command=showfilepath)
button.pack()
 


button1=Button(root, text="Display Image", width=14, command=displayimage)
button1.pack()

button2=Button(root, text="Exit", width=14, command=closewindow)
button2.pack()

button3=Button(root, text="Diagnosis", width=15, command=diagnosis)
button3.pack()

filepathdisplay=Text(root, width=30, height =2, wrap=WORD)
filepathdisplay.pack()




#c=Canvas(root, width=500, height=500)
#c.pack()

root.mainloop()

