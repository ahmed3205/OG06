#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 01:06:13 2018

@author: ahmedosman
"""

from tkinter import *
import matplotlib 
from matplotlib import pyplot
from skimage import io

class gui:
    
    def __init__(self,master):
        
        frame=Frame(master)
        frame.pack()
        #self.frame.geometry("1000x500")
        
        self.label=Label(frame, text="Skin Disease Classification System")
        self.label.config(font=("Courier", 34))
        self.label.pack()

        self.label1=Label(frame,text="Enter file path of image:", bg="white", fg="black", font="none 12 bold")
        self.label1.pack()

        #enter text in entry box
        self.textentry=Entry(frame,width=20, bg="white")
        self.textentry.pack()
    
        self.button2 = Button(frame, text="Save File Path", command=self.savetext)
        self.button2.pack()

        self.button3 = Button(frame, text="Print text", command=self.printtext)
        self.button3.pack()
        
        #self.photo=PhotoImage(file="image1.jpg")
        #self.canvas()
        
        #self.label2=Label(frame, text=self.enteredtext)
        #self.label2.pack()
               
    def savetext (self):
         self.enteredtext=self.textentry.get()
         s=self.enteredtext
         return s  
     
    def printtext(self):
        print ("The entered file path is", self.enteredtext)
        self.label=Label(frame, text="hello") 
    
   # def closewindow(self):
    #    self.frame.destroy()
     #   exit()
root=Tk()
a=gui(root)
root.mainloop()

    