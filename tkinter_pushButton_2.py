# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 14:38:07 2021

@author: Administrator
"""


import tkinter as tk

class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("250x100")
        self.buttonA = tk.Button(self.root,
                                 text = "Color",
                                 background = "blue",
                                 foreground = "red")

        self.buttonB = tk.Button(self.root,
                                text="Click to change color",
                                background = "gray",
                                foreground = "purple")
        self.buttonA.pack(side=tk.LEFT)
        self.buttonB.pack(side=tk.RIGHT)
        self.root.mainloop()     

app=Test()































