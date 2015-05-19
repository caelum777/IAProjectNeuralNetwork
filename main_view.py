__author__ = 'Lesmed'
import view as v
import pygame.font, pygame.event, pygame.draw
from Tkinter import *

from PIL import Image
import Tkinter as tk
import os

v0=Tk(className="OCR Lesmed - Randall")

def cargar_view():
    v.main(False, 0)
def subir_imagen():
    from tkFileDialog import askopenfilename


    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    bkgnd_draw = pygame.Surface((350, 350))

    img = Image.open(filename)
    img = v.Process_image(img)
    v.main(True, filename)
    """v.view_initialization_from_MV(bkgnd_draw)
    bkgnd_draw.fill((255, 255, 255))
    bkgnd_draw = pygame.image.load(filename)
    print bkgnd_draw
    v.net.variable_initialization()
    v.predict_image(bkgnd_draw,v.net)
"""
    #print(filename)
v0.geometry("500x500")
frame1 = tk.Frame(v0).pack(side= RIGHT)
b2=Button(frame1,text="Dibujar",command=lambda:cargar_view()).pack()
b3=Button(frame1,text="Subir imagenes",command=lambda:subir_imagen()).pack()




v0.mainloop()