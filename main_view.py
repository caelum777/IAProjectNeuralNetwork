
import view as v
from Tkinter import *
import pygame
import random
import os
global playing
__author__ = 'Lesmed'

import pygame
import view as v
import Tkinter as tk
from Tkinter import*
import os

v0=Tk(className="Lesmed")

def cargar_view():
    v.main()
def subir_imagen():
    from tkFileDialog import askopenfilename

    #Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)
v0.geometry("1000x700")
frame1 = tk.Frame(v0).pack(side= RIGHT)
b2=Button(frame1,text="Dibujar",command=lambda:cargar_view()).pack()
b3=Button(frame1,text="Subir imagenes",command=lambda:subir_imagen()).pack()




v0.mainloop()