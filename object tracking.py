from Tkinter import Tk, Frame, BOTH
from Tkinter import *
import time
import cv2
import ttk
import os,glob,sys
import numpy as np
from numpy import array
import tkFileDialog
from PIL import Image, ImageTk
from PIL import *

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent,background="light grey")            
        self.parent = parent        
        self.initUI()
    
    def initUI(self):
        
        self.parent.title("TrackMe")
        self.pack(fill=BOTH, expand=1)

def AboutUs():
    global win
    win = Toplevel()
    img1 = Image.open('AboutUs.png')
    b_img1 = ImageTk.PhotoImage(img1)
    labe = Label(win, image = b_img1)
    labe.image = b_img1
    labe.pack()
    
def Home():
    root.deiconify()
    window1.destroy()

def VirtualMouse():
    #put virtual mouse code
    global window1
    root.withdraw()
    window1 = Toplevel()
    window1.geometry("1105x605+300+300")
    
    imge = Image.open('home.png')
    b_imge = ImageTk.PhotoImage(imge)
    b1 = Button(window1,command = Home)
    b1.pack()
    

def TrackPath():
    #path tacking code
    global window2

def MultipleObjectDetection():
    # multiple object detection code
    global window3
    
def PharmaInspectionSys():
    #code
    global window4
    
        
root = Tk()
root.geometry("1105x605+300+300")
app = Example(root)

image = Image.open('TrackMe.jpg')
background_image = ImageTk.PhotoImage(image)
background_label = Label(app,image = background_image)
background_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

img = Image.open('mot.png')
b_img = ImageTk.PhotoImage(img)
vm = Button(app,image = b_img, command = MultipleObjectDetection)
vm.place(y = 300, x = 150)

img1 = Image.open('twp.png')
b_img1 = ImageTk.PhotoImage(img1)
vm = Button(app,image = b_img1, command = TrackPath)
vm.place(y = 300, x = 450)

img2 = Image.open('phin.png')
b_img2 = ImageTk.PhotoImage(img2)
vm = Button(app,image = b_img2, command = PharmaInspectionSys)
vm.place(y = 300, x = 750)

img3 = Image.open('vm.png')
b_img3 = ImageTk.PhotoImage(img3)
vm = Button(app,image = b_img3, command = VirtualMouse)
vm.place(y = 300, x = 1050)

la = Button(app, text = 'Powered by ITIE Knowledge Solutions,Bangalore-56', command = AboutUs)
la.pack(side = BOTTOM)

root.mainloop()