# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:28:02 2020

@author: Chaitanya
"""

import os
from tkinter import Tk
from tkinter import Button
import tkinter as tk

tkWindow = Tk()  
tkWindow.geometry('600x450')  
tkWindow.title('Face Detection')


def camera():
    import camera

def faceDetection():  
    import faceDetection
    
def eyeDetection():
    import eyeDetection

def mask():
    import moneyHeistMask
    
def goggles():
    import thugGoggles

def close_window (): 
    tkWindow.destroy()
    
cameraButton = Button(tkWindow,
	text = 'Camera',
    font = " bold ",
	command = camera, 
    width = 25)  
cameraButton.pack(padx=15, pady=15)

fdButton = Button(tkWindow,
	text = 'Face Detection',
    font = " bold ",
	command = faceDetection, 
    width = 25)  
fdButton.pack(padx=15, pady=15)

edButton = Button(tkWindow,
	text = 'Eye Detection',
    font = " bold ",
	command = eyeDetection, 
    width = 25)  
edButton.pack(padx=15, pady=15) 

maskButton = Button(tkWindow,
	text = 'Money Heist Mask',
    font = " bold ",
	command = mask, 
    width = 25)  
maskButton.pack(padx=15, pady=15)  

goggleButton = Button(tkWindow,
	text = 'Thug Life Goggles',
    font = " bold ",
	command = goggles, 
    width = 25)  
goggleButton.pack(padx=15, pady=15) 

closeButton = Button(tkWindow,
                     text="Close",
                     fg="red",
                     font = " bold ",
                     command = close_window, 
                     width = 25)
closeButton.pack(padx=15, pady=15)
 
tkWindow.mainloop()