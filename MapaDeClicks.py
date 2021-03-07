# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 12:13:34 2020

@author: dan_2
"""

import tkinter as tk
class Aplication:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1,width=600, height=400,background="black")
        self.canvas1.bind("<Motion>",self.moverMouse)
        self.canvas1.bind("<Button-1>",self.presionMouse)
        self.canvas1.grid(column=0,row=1)
        self.ventana1.mainloop()
        
    def presionMouse (self,evento):
        self.canvas1.create_oval(evento.x-5,evento.y-5,evento.x+5,evento.y+5,fill="purple")
    def moverMouse (self, evento):
        self.ventana1.title("("+str(evento.x)+","+str(evento.y)+")")

aplicacion1=Aplication()

