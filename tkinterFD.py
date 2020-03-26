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
tkWindow.geometry('600x400')  
tkWindow.title('Face Detection')


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

sampleButton = Button(tkWindow,
	text = 'Face Detection',
    font = " bold ",
	command = faceDetection, 
    width = 25)  
sampleButton.pack(padx=15, pady=15)

captureImgButton = Button(tkWindow,
	text = 'Eye Detection',
    font = " bold ",
	command = eyeDetection, 
    width = 25)  
captureImgButton.pack(padx=15, pady=15) 

createYAMLButton = Button(tkWindow,
	text = 'Money Heist Mask',
    font = " bold ",
	command = mask, 
    width = 25)  
createYAMLButton.pack(padx=15, pady=15)  

startAtdButton = Button(tkWindow,
	text = 'Thug Life Goggles',
    font = " bold ",
	command = goggles, 
    width = 25)  
startAtdButton.pack(padx=15, pady=15) 

closeButton = Button(tkWindow,
                     text="Close",
                     fg="red",
                     font = " bold ",
                     command = close_window, 
                     width = 25)
closeButton.pack(padx=15, pady=15)
 
tkWindow.mainloop()