#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:48:38 2018
@author: aruranvijayaratnam
"""

"""
Created on Wed Mar 21 13:48:38 2018
@author: aruranvijayaratnam
"""

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg 
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from PIL import Image
import matplotlib.image as img
from tkinter import filedialog
from tkinter import *
import skimage.io
from skimage.io import imread
from skimage import io, color
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Conv2D 
from keras.layers import MaxPooling2D 
from keras.layers import Flatten 
from keras.layers import Dense 
from keras.layers import Activation
from IPython.display import display
import numpy as np
from keras.preprocessing import image
from os import path
 
from tkinter import Menu


def build_model():
    model = Sequential()
    #first layer
    model.add(Conv2D(32, (3, 3), input_shape = (256, 256, 3), activation = 'relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    #second layer
    model.add(Conv2D(32, (3, 3), activation = 'relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    #third layer
    model.add(Conv2D(32,(3,3),activation='relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    #fourth layer
    model.add(Conv2D(32,(3,3),activation='relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    #Fifth layer
    model.add(Conv2D(32,(3,3),activation='relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    model.add(Flatten())
    model.add(Dense(units = 128, activation = 'relu'))
    model.add(Dense(units = 1, activation = 'sigmoid'))
    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    return model

model2 = build_model()
model2.load_weights('final_model_weights.h5')
classifier=model2

class ImageClassify:


    def testimage(img):
        test_img=image.load_img(img,target_size = (256, 256))
        test_img=image.img_to_array(test_img)
        test_image = np.expand_dims(test_img, axis = 0)
        result_1 = classifier.predict(test_image)
        if result_1[0][0] == 1:
            prediction = 'Benign'
        else:
            prediction = 'Melanoma'
        return prediction 

    def displayimage():
        
        
        file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
        fpath=str(file)
        img=imread(fpath)
        f = Figure()
        a = f.add_subplot(111) 
        a.axis("off")
        a.imshow(img)
        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.get_tk_widget().place(relx=0.5, rely=0.66, anchor="center")
        canvas._tkcanvas.place(relx=0.5, rely=0.66, anchor="center")
        
        
        prediction1=ImageClassify.testimage(fpath)
            #filepathdisplay.insert(0.0, "The image appears to be " + prediction1 + "\n\n")
       
    
        def clear(): 
                canvas.get_tk_widget().destroy()
                canvas._tkcanvas.destroy()
        
        button4=Button(root, text="Delete", width=14, command=clear)
        button4.place(relx=0.5, rely=0.26, anchor="center")
        
        return prediction1
    
    
    def diagnosis():
        file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
        ipath=str(file)
        prediction1=ImageClassify.testimage(ipath)
        filepathdisplay.insert(0.0, "The image appears to be " + prediction1 + "\n\n")
        return prediction1
    
root=Tk()
root.title("GUI")
root.geometry("500x530")

def closewindow():
    root.destroy()
    exit()

    
label=Label(root, text="Skin Lesion Classification System")
label.config(font=("Courier", 20))
label.place(relx=0.5, rely=0.02, anchor="center")

button1=Button(root, text="Select Image", width=14, command=ImageClassify.displayimage)
button1.place(relx=0.5, rely=0.08, anchor="center")

button2=Button(root, text="Diagnosis", width=14, command=ImageClassify.diagnosis)
button2.place(relx=0.5, rely=0.14, anchor="center")

button3=Button(root, text="Exit", width=14, command=closewindow)
button3.place(relx=0.5, rely=0.2, anchor="center")

filepathdisplay=Text(root, width=30, height =2, wrap=WORD)
filepathdisplay.place(relx=0.5, rely=0.36, anchor="center")



#filepathdisplay1=Text(root, width=30, height =2, wrap=WORD)
#filepathdisplay1.grid(row=5)



root.mainloop()