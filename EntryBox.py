import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

#Custom Entry fields [Credits:- User form StackOverflow]#

class Entry(tk.Entry):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.config(state='disabled', disabledforeground='white', disabledbackground='black', bg="black", fg="white")

    def insert(self, pos, value):
        self.config(state='normal')
        super().insert(pos, value)
        self.config(state='disabled')
    
    def delete(self, pos, value = END):
        self.config(state='normal')
        super().delete(pos, value)
        self.config(state='disabled')

class OPEntry(tk.Entry):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.config(state='disabled', disabledforeground='cyan', disabledbackground='#353340', bg="black", fg="white")

    def insert(self, pos, value):
        self.config(state='normal')
        super().insert(pos, value)
        self.config(state='disabled')
    
    def delete(self, pos, value = END):
        self.config(state='normal')
        super().delete(pos, value)
        self.config(state='disabled')