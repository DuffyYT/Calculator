#============================IMPORTS==============================

import tkinter as tk                         #Importing Tkinter module for GUI
from tkinter import *                        #Importing all tkinter files
import math                                  #Importing math module for arithmetic
import webbrowser                            #Plugging tool
import os                                    #For saving memory(OPENING FILES AND READING FILES)
import keyboard                              #For keyboard shortcuts
from EntryBox import *                       #Custom Entry Boxes
from PIL import ImageTk, Image               #For imagery
from tkinter import filedialog
import ctypes
if os.path.abspath("D:work/Python/"):
    os.chdir('D:/Work/Python/CALCULATOR')
    print("changed the CWD to{'D:/Work/Python/cps'}. [REMOVE ONCE COMPLETE!!]")
else:
    pass


#=================Memory_saving===============

memory = []

if os.path.isfile('mem.txt'):
    with open ('mem.txt', 'r') as f:
        memSplit = f.read()
        memSplit = memSplit.split(',')
        for i in range(len(memSplit)):
            memory.append(memSplit[i])
for space in range(len(memory)): #Removing extra space
    if memory[space]=='':
        memory.remove('')

#=====================globals=================

global counter #➡ History tab counter
counter = 0
global one
global sCounter #➡ Settings tab counter
sCounter = 0

#PADS#
global dPad
global Pad 
global sPad
global wPad
global tPad
dPad = 1
Pad = 0
sPad = 0
wPad = 0
tPad = 0

global padd
global theme
global ui
global texture
padd = 'entrypad'
theme = 'Dark'
ui = 'default'
texture = None

#==========================Settings===========================

if os.path.isfile('data/settings.txt'):
    with open('data/settings.txt','r') as f:
        tempInfo = f.read()
        info = eval(tempInfo)
        maindir = info['texture']
        mainthm = info['theme']
        mainui = info['ui']
        mainpad = info['padd']

settings = {
    "padd":"entrypad",
    "theme":"Dark",
    "ui":"default",
    "texture":texture,
    "sounds":True
}

try:
    settings["padd"] = mainpad
    settings["theme"] = mainthm
    settings["ui"] = mainui
    settings["texture"] = maindir
    
except:
    pass

#===========================CLASSES============================

class number:
    
    def __init__(self, value,):
        self.value = value
        global counter
        if counter == 1:
            HentryPad.destroy()
            counter=0
            if upperField.get()=='OVERFLOW!!':
                upperAns.delete(0,END)
                upperField.delete(0, END)
                field.delete(0,END)
                field.insert(0,self.value)
            else:
                upperAns.delete(0,END)
                field.insert(END,self.value)
        else:
            if upperField.get()=='OVERFLOW!!':
                upperAns.delete(0,END)
                upperField.delete(0, END)
                field.delete(0,END)
                field.insert(0,self.value)
            else:
                upperAns.delete(0,END)
                field.insert(END,self.value)
    
class weightNum:
    def __init__(self, value, button,):
        self.value = value
        self.button = button
        temp = entry1.get()
        entry1.delete(0,END)
        entry1.insert(0,str(temp) + str(self.value))
        #c#
        if converter == 'c':
            if converter2 == 'c':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'c':
            if converter2 == 'mg':
                co = float(entry1.get()) * 200
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'c':
            if converter2 == 'g':
                co = float(entry1.get()) / 5
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'c':
            if converter2 == 'kg':
                co = float(entry1.get()) / 5000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'c':
            if converter2 == 't':
                co = float(entry1.get()) / 4.536e+6
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'c':
            if converter2 == 'mt':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'c':
            if converter2 == 'o':
                co = float(entry1.get()) / 142
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'c':
            if converter2 == 'p':
                co = float(entry1.get()) / 2268
                entry2.delete(0, END)
                entry2.insert(0,co)
        #mg#
        if converter == 'mg':
            if converter2 == 'mg':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'mg':
            if converter2 == 'c':
                co = float(entry1.get()) / 200
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'mg':
            if converter2 == 'g':
                co = float(entry1.get()) / 1000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'mg':
            if converter2 == 'kg':
                co = float(entry1.get()) / 1e+6
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'mg':
            if converter2 == 't':
                co = float(entry1.get()) / 9.072e+8
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'mg':
            if converter2 == 'mt':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'mg':
            if converter2 == 'o':
                co = float(entry1.get()) / 28350
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'mg':
            if converter2 == 'p':
                co = float(entry1.get()) / 453592
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'g':
            if converter2 == 'g':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'g':
            if converter2 == 'c':
                co = float(entry1.get()) * 5
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'g':
            if converter2 == 'mg':
                co = float(entry1.get()) * 1000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'g':
            if converter2 == 'kg':
                co = float(entry1.get()) / 1000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'g':
            if converter2 == 't':
                co = float(entry1.get()) / 907185
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'g':
            if converter2 == 'mt':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'g':
            if converter2 == 'o':
                co = float(entry1.get()) / 28.35
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'g':
            if converter2 == 'p':
                co = float(entry1.get()) / 454
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'kg':
            if converter2 == 'kg':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'kg':
            if converter2 == 'c':
                co = float(entry1.get()) * 5000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'kg':
            if converter2 == 'mg':
                co = float(entry1.get()) / 1e+6
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'kg':
            if converter2 == 'g':
                co = float(entry1.get()) * 1000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'kg':
            if converter2 == 't':
                co = float(entry1.get()) / 907
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'kg':
            if converter2 == 'o':
                co = float(entry1.get()) * 35.274
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'kg':
            if converter2 == 'p':
                co = float(entry1.get()) * 2.205
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 't':
            if converter2 == 't':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 't':
            if converter2 == 'c':
                co = float(entry1.get()) * 4.536e+6
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 't':
            if converter2 == 'mg':
                co = float(entry1.get()) * 9.072e+8
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 't':
            if converter2 == 'g':
                co = float(entry1.get()) * 907185
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 't':
            if converter2 == 'kg':
                co = float(entry1.get()) * 907
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 't':
            if converter2 == 'mt':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 't':
            if converter2 == 'o':
                co = float(entry1.get()) * 32000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 't':
            if converter2 == 'p':
                co = float(entry1.get()) * 2000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'mt':
            if converter2 == 'mt':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'o':
            if converter2 == 'o':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'o':
            if converter2 == 'c':
                co = float(entry1.get()) * 142
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'o':
            if converter2 == 'mg':
                co = float(entry1.get()) * 28350
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'o':
            if converter2 == 'g':
                co = float(entry1.get()) * 28.35
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'o':
            if converter2 == 'kg':
                co = float(entry1.get()) / 35.274
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'o':
            if converter2 == 't':
                co = float(entry1.get()) / 32000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'o':
            if converter2 == 'mt':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'o':
            if converter2 == 'p':
                co = float(entry1.get()) / 16
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'p':
            if converter2 == 'p':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'p':
            if converter2 == 'c':
                co = float(entry1.get()) * 2268
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'p':
            if converter2 == 'mg':
                co = float(entry1.get()) * 453592
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'p':
            if converter2 == 'g':
                co = float(entry1.get()) * 454
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'p':
            if converter2 == 'kg':
                co = float(entry1.get()) / 2.205
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'p':
            if converter2 == 't':
                co = float(entry1.get()) / 2000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'p':
            if converter2 == 'mt':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'p':
            if converter2 == 'o':
                co = float(entry1.get()) * 16
                entry2.delete(0, END)
                entry2.insert(0,co)
        (self.button).config(relief=SUNKEN, bg="#262626", fg="cyan")
        (self.button).after(58, lambda: (self.button).config(relief=RAISED, bg="black", fg="white"))
      
class timeNum:

    def __init__(self, value, button):
        self.value = value
        self.button = button
        temp = Tentry1.get()
        Tentry1.delete(0,END)
        Tentry1.insert(0,str(temp) + str(self.value))
        #c#
        if Tonverter == 'ms':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) / 1000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) / 60000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) / 3.6e+6
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) / 8.64e+7
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 'y':
                co = float(Tentry1.get()) / 3.154e+10
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 3.154e+12
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 's':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 1000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) / 60
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) / 3600
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) / 86400
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'y':
                co = float(Tentry1.get()) / 3.154e+7
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 3.154e+9
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'm':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 6000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) * 60
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) * 1/60
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) * 1440
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'y':
                co = float(Tentry1.get()) / 525600
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 28.35 / 5.256e+7
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'h':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 3.6e+6
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) * 3600
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) * 60
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) / 24
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'y':
                co = float(Tentry1.get()) / 8760
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 876000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'd':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 8.64e+7
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) * 85400
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) * 1440
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) * 24
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'y':
                co = float(Tentry1.get()) / 365
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 36500
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'y':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 3.154e+10
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) * 3.154e+7
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) * 525600
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) * 8760
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) * 365
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 100
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 16
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 3.154e+12
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) * 3.154e+9
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) * 5.256e+7
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) * 876000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) * 36500
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'y':
                co = float(Tentry1.get()) * 100
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        (self.button).config(relief=SUNKEN, bg="#262626", fg="cyan")
        (self.button).after(58, lambda: (self.button).config(relief=RAISED, bg="black", fg="white"))

class decNum:

    def __init__(self,entry, button):
        self.entry = entry
        self.button = button
        decount = 0
        declst = list((self.entry).get())
        for i in declst:
            if i == '.':
                decount += 1
        if decount < 1:
            (self.entry).insert(END, ".")
            (self.button).config(relief=SUNKEN, bg="#262626", fg="white")
            (self.button).after(58, lambda: (self.button).config(relief=RAISED, bg="black", fg="cyan"))

class setting:

    def __init__(self, pad,one=None,two=None,three=None,four=None,five=None,six=None,seven=None,
                  eight=None,nine=None,zero=None,dot=None,dash=None,button=None,dele=None,delete=None,quit=None,ad=None,sub=None,mul=None,div=None,sq=None,sqr=None,eq=None):
            '''
            enter pad for creating main settings page in the the current comtext pad\n
            enter your pads to change the theme \n
            CONTAINS ALL SETTINGS.
            '''
            global sCounter
            global setPad
            self.pad = pad
            self.one = one
            self.two = two
            self.three = three
            self.four = four
            self.five = five
            self.six = six
            self.seven = seven
            self.eight = eight
            self.nine = nine
            self.zero = zero
            self.dot = dot
            self.dash = dash
            self.button = button
            self.dele = dele
            self.delete=delete
            self.quit = quit
            self.ad = ad
            self.sub = sub
            self.mul = mul
            self.div = div
            self.sq = sq
            self.sqr = sqr
            self.eq = eq

            tlist = [(self.one),(self.two),(self.three),(self.four),(self.five),(self.six),
                               (self.seven),(self.eight),(self.nine),(self.zero),(self.dot),(self.dash)] #list of primary buttons with <black> background and <white> foreground
            clst = [(self.dele),(self.delete),(self.quit)]
            olst = [(self.ad),(self.sub),(self.mul),(self.div),(self.sq),(self.sqr)]

            if sCounter == 0: #for detecting if settings page is not present
                global theme
                global texture
                setPad = tk.Frame((self.pad), bg="black")
                setPad.place(relwidth=0.98, relheight=0.42, rely=0.58, relx = 0.01)


                def thme(): # FOR SETTING DARK AND LIGHT THEME
                    global mainthm
                    global one
                    global two
                    global three
                    global four
                    global five
                    global six
                    global seven
                    global eight
                    global nine
                    global zero
                    global dot
                    global dash
                    global eq
                    global sq
                    global sqr
                    global Done
                    global Dtwo
                    global Dthree
                    global Dfour
                    global Dfive
                    global Dsix
                    global Dseven
                    global Deight
                    global Dnine
                    global Dzero
                    global Ddot
                    global Ddash
                    global Deq
                    global Dsq
                    global Dsqr
                    global theme
                    if mainui == 'default':
                        if theme == 'Dark' or mainthm == 'Dark': #for detecting the current theme to change to light mode 
                            for butts in tlist:#looping through primary buttons
                                try:
                                    butts.config(bg="#EEEFF4", fg="#2B2B2B",activebackground="#EEEFF4", activeforeground="#2B2B2B") # configuring primary buttons to light mode
                                    darkb.config(image=toggle_off_new) # changing the toggle button to off ('off' is the switch for light mode)
                                except AttributeError: # passing if there is an absent button attribute
                                    pass # passing
                            for butts in clst:
                                try:
                                    butts.config(bg="#ff0000",fg="black",activebackground="#ff0000",activeforeground="black")
                                except AttributeError:
                                    pass
                            for butts in olst:
                                try:
                                    butts.config(bg="tan",fg="black",activebackground="#ff0000",activeforeground="black")
                                except AttributeError:
                                    pass
                            (self.pad).config(bg="white")
                            theme = 'Light' #increasig the theme value to denote the present of light mode
                            settings["theme"]='Light'
                            mainthm = 'Light'

                        elif theme == 'Light' or mainthm == 'Light': #for detecting the current theme to change to dark mode 
                            for butts in tlist:#looping through primary buttons
                                try:
                                    butts.config(bg="black", fg="white") # configuring primary buttons to dark mode
                                    darkb.config(image=toggle_on_new) # changing the toggle button to on ('on' is the switch for dark mode)
                                except AttributeError: # passing if there is an absent button attribute
                                    pass # passing
                            for butts in clst:
                                try:
                                    butts.config(bg="#fc8700",fg="black",activebackground="#fc8700",activeforeground="black")
                                except AttributeError:
                                    pass
                            for butts in olst:
                                try:
                                    butts.config(bg="orange",fg="black",activebackground="#ff0000",activeforeground="black")
                                except AttributeError:
                                    pass
                            (self.pad).config(bg="black")
                            settings["theme"]='Dark'
                            mainthm = 'Dark'
                            theme = 'Dark' #defaulting theme value to denote the present dark mode

                    elif mainui == 'custom':
                      try:   
                        one = ImageTk.PhotoImage(file=f"{maindir}/one.png")
                        two = ImageTk.PhotoImage(file=f"{maindir}/two.png")
                        three = ImageTk.PhotoImage(file=f"{maindir}/three.png")
                        four = ImageTk.PhotoImage(file=f"{maindir}/four.png")
                        five = ImageTk.PhotoImage(file=f"{maindir}/five.png")
                        six = ImageTk.PhotoImage(file=f"{maindir}/six.png")
                        seven = ImageTk.PhotoImage(file=f"{maindir}/seven.png")
                        eight = ImageTk.PhotoImage(file=f"{maindir}/eight.png")
                        nine = ImageTk.PhotoImage(file=f"{maindir}/nine.png")
                        zero = ImageTk.PhotoImage(file=f"{maindir}/zero.png")
                        dot = ImageTk.PhotoImage(file=f"{maindir}/dot.png") 
                        dash = ImageTk.PhotoImage(file=f"{maindir}/dash.png")
                        eq = ImageTk.PhotoImage(file=f"{maindir}/eq.png")
                        sq = ImageTk.PhotoImage(file=f"{maindir}/sq.png")
                        sqr = ImageTk.PhotoImage(file =f"{maindir}/sqr.png")
                        Done = ImageTk.PhotoImage(file=f"{maindir}/Done.png")
                        Dtwo = ImageTk.PhotoImage(file=f"{maindir}/Dtwo.png")
                        Dthree = ImageTk.PhotoImage(file=f"{maindir}/Dthree.png")
                        Dfour = ImageTk.PhotoImage(file=f"{maindir}/Dfour.png")
                        Dfive = ImageTk.PhotoImage(file=f"{maindir}/Dfive.png")
                        Dsix = ImageTk.PhotoImage(file=f"{maindir}/Dsix.png")
                        Dseven = ImageTk.PhotoImage(file=f"{maindir}/Dseven.png")
                        Deight = ImageTk.PhotoImage(file=f"{maindir}/Deight.png")
                        Dnine = ImageTk.PhotoImage(file=f"{maindir}/Dnine.png")
                        Dzero = ImageTk.PhotoImage(file=f"{maindir}/Dzero.png")
                        Ddot = ImageTk.PhotoImage(file=f"{maindir}/Ddot.png") 
                        Ddash = ImageTk.PhotoImage(file=f"{maindir}/Ddash.png")
                        Deq = ImageTk.PhotoImage(file=f"{maindir}/Deq.png")
                        Dsq = ImageTk.PhotoImage(file=f"{maindir}/Dsq.png")
                        Dsqr = ImageTk.PhotoImage(file =f"{maindir}/Dsqr.png")
                        if mainthm == 'Dark' or theme == 'Dark': #for detecting the current theme to change to light mode 
                            (self.one).config(image=Done,bg="white")
                            (self.two).config(image=Dtwo,bg="white")
                            (self.three).config(image=Dthree,bg="white")
                            (self.four).config(image=Dfour,bg="white")
                            (self.five).config(image=Dfive,bg="white")
                            (self.six).config(image=Dsix,bg="white")
                            (self.seven).config(image=Dseven,bg="white")
                            (self.eight).config(image=Deight,bg="white")
                            (self.nine).config(image=Dnine,bg="white")
                            (self.zero).config(image=Dzero,bg="white")
                            (self.eq).config(image=Deq,bg="white")
                            (self.sq).config(image=Dsq,bg="white")
                            (self.sqr).config(image=Dsqr,bg="white")
                            try:
                                (self.dot).config(image=Ddot,bg="white")
                                (self.dash).config(image=Ddash,bg="white")
                            except:
                                print("pad has no dot button")
                            darkb.config(image=toggle_off_new,) 
                            print("changed to light")
                            settings["theme"]='Light'    
                            mainthm = 'Light'                   
                            theme = 'Light' #increasig the theme value to denote the present of light mode

                        elif mainthm == 'Light' or theme == 'Light': #for detecting the current theme to change to dark mode 
                            (self.one).config(image=one,bg="black")
                            (self.two).config(image=two,bg="black")
                            (self.three).config(image=three,bg="black")
                            (self.four).config(image=four,bg="black")
                            (self.five).config(image=five,bg="black")
                            (self.six).config(image=six,bg="black")
                            (self.seven).config(image=seven,bg="black")
                            (self.eight).config(image=eight,bg="black")
                            (self.nine).config(image=nine,bg="black")
                            (self.zero).config(image=zero,bg="black")
                            (self.eq).config(image=eq,bg="black")
                            (self.sq).config(image=sq,bg="black")
                            (self.sqr).config(image=sqr,bg="black")
                            try:
                                (self.dot).config(image=dot,bg="black")
                                (self.dash).config(image=dash,bg="black")
                            except:
                                print("pad has no dot button")
                            darkb.config(image=toggle_on_new)
                            print("changed to dark")
                            settings["theme"]='Dark'
                            mainthm = 'Dark'  
                            theme = 'Dark' #defaulting theme value to denote the present dark mode
                      except :
                          print("whats happening")
                
                def customTheme():
                    global maindir
                    global mainui
                    global ui
                    ui = 'custom'
                    mainui = 'custom'
                    global one
                    global two
                    global three
                    global four
                    global five
                    global six
                    global seven
                    global eight
                    global nine
                    global zero
                    global dot
                    global dash
                    global eq
                    global sq
                    global sqr
                    global Done
                    global Dtwo
                    global Dthree
                    global Dfour
                    global Dfive
                    global Dsix
                    global Dseven
                    global Deight
                    global Dnine
                    global Dzero
                    global Ddot
                    global Ddash
                    global Deq
                    global Dsq
                    global Dsqr
                    global texture
                    texture = filedialog.askdirectory(title="Select theme folder")
                    print("Texture:",texture)
                    maindir = texture
                    try:
                        if texture != '':
                            one = ImageTk.PhotoImage(file=f"{texture}/one.png")
                            two = ImageTk.PhotoImage(file=f"{texture}/two.png")
                            three = ImageTk.PhotoImage(file=f"{texture}/three.png")
                            four = ImageTk.PhotoImage(file=f"{texture}/four.png")
                            five = ImageTk.PhotoImage(file=f"{texture}/five.png")
                            six = ImageTk.PhotoImage(file=f"{texture}/six.png")
                            seven = ImageTk.PhotoImage(file=f"{texture}/seven.png")
                            eight = ImageTk.PhotoImage(file=f"{texture}/eight.png")
                            nine = ImageTk.PhotoImage(file=f"{texture}/nine.png")
                            zero = ImageTk.PhotoImage(file=f"{texture}/zero.png")
                            dot = ImageTk.PhotoImage(file=f"{texture}/dot.png")
                            dash = ImageTk.PhotoImage(file=f"{texture}/dash.png")
                            eq = ImageTk.PhotoImage(file=f"{maindir}/eq.png")
                            sq = ImageTk.PhotoImage(file=f"{maindir}/sq.png")
                            sqr = ImageTk.PhotoImage(file =f"{maindir}/sqr.png")
                            Done = ImageTk.PhotoImage(file=f"{texture}/Done.png")
                            Dtwo = ImageTk.PhotoImage(file=f"{texture}/Dtwo.png")
                            Dthree = ImageTk.PhotoImage(file=f"{texture}/Dthree.png")
                            Dfour = ImageTk.PhotoImage(file=f"{texture}/Dfour.png")
                            Dfive = ImageTk.PhotoImage(file=f"{texture}/Dfive.png")
                            Dsix = ImageTk.PhotoImage(file=f"{texture}/Dsix.png")
                            Dseven = ImageTk.PhotoImage(file=f"{texture}/Dseven.png")
                            Deight = ImageTk.PhotoImage(file=f"{texture}/Deight.png")
                            Dnine = ImageTk.PhotoImage(file=f"{texture}/Dnine.png")
                            Dzero = ImageTk.PhotoImage(file=f"{texture}/Dzero.png")
                            Ddot = ImageTk.PhotoImage(file=f"{texture}/Ddot.png")
                            Ddash = ImageTk.PhotoImage(file=f"{texture}/Ddash.png")
                            Deq = ImageTk.PhotoImage(file=f"{maindir}/Deq.png")
                            Dsq = ImageTk.PhotoImage(file=f"{maindir}/Dsq.png")
                            Dsqr = ImageTk.PhotoImage(file =f"{maindir}/Dsqr.png")
                            if theme == 'Dark':
                                (self.one).config(image=one)
                                (self.two).config(image=two)
                                (self.three).config(image=three)
                                (self.four).config(image=four)
                                (self.five).config(image=five)
                                (self.six).config(image=six)
                                (self.seven).config(image=seven)
                                (self.eight).config(image=eight)
                                (self.nine).config(image=nine)
                                (self.zero).config(image=zero)
                                (self.dot).config(image=dot)    
                                (self.dash).config(image=dash)
                                (self.eq).config(image=eq)
                                (self.sq).config(image=sq)
                                (self.sqr).config(image=sqr)
                                settings["texture"] = texture
                                settings["ui"] = 'custom'
                            elif theme == 'Light':
                                (self.one).config(image=Done)
                                (self.two).config(image=Dtwo)
                                (self.three).config(image=Dthree)
                                (self.four).config(image=Dfour)
                                (self.five).config(image=Dfive)
                                (self.six).config(image=Dsix)
                                (self.seven).config(image=Dseven)
                                (self.eight).config(image=Deight)
                                (self.nine).config(image=Dnine)
                                (self.zero).config(image=Dzero)
                                (self.dot).config(image=Ddot)    
                                (self.dash).config(image=Ddash)
                                (self.Deq).config(image=Deq)
                                (self.Dsq).config(image=Dsq)
                                (self.Dsqr).config(image=Dsqr)
                                settings["texture"] = texture
                                settings["ui"] = 'custom'
                        elif texture == '':
                            print("No folder was selected")
                    except:
                        print("something is wrong")

                def defaultTheme():
                    global theme
                    global mainui
                    global mainthm
                    if mainui == 'custom':
                        settings["ui"] = 'default'
                        mainui = 'default'
                        if mainthm == 'Light' or theme == 'Light':
                            (self.one).config(image='',fg="black")
                            (self.two).config(image='',fg="black")
                            (self.three).config(image='',fg="black")
                            (self.four).config(image='',fg="black")
                            (self.five).config(image='',fg="black")
                            (self.six).config(image='',fg="black")
                            (self.seven).config(image='',fg="black")
                            (self.eight).config(image='',fg="black")
                            (self.nine).config(image='',fg="black")
                            (self.zero).config(image='',fg="black")
                            (self.dot).config(image='',fg="black")
                            (self.dash).config(image='',fg="black")
                            (self.eq).config(image='',fg="black")
                            (self.sq).config(image='',fg="black")
                            (self.sqr).config(image='',fg="black")
                            print(mainthm,theme)
                        if mainthm == 'Dark' or theme == 'Dark':
                            (self.one).config(image='',fg="white")
                            (self.two).config(image='',fg="white")
                            (self.three).config(image='',fg="white")
                            (self.four).config(image='',fg="white")
                            (self.five).config(image='',fg="white")
                            (self.six).config(image='',fg="white")
                            (self.seven).config(image='',fg="white")
                            (self.eight).config(image='',fg="white")
                            (self.nine).config(image='',fg="white")
                            (self.zero).config(image='',fg="white")
                            (self.dot).config(image='',fg="white")
                            (self.dash).config(image='',fg="white")
                            (self.eq).config(image='',fg="white")
                            (self.sq).config(image='',fg="white")
                            (self.sqr).config(image='',fg="white")
                            print(mainthm,theme)
                    
                    else:
                        print("already default.")
                
                def dpi():
                    ctypes.windll.shcore.SetProcessDpiAwareness(True)

                # THEME SWITCHER #
                dark = tk.Label(setPad, text="Dark Theme ", bg="black", fg='white', font="bangers 12") # THEME LABEL
                dark.place(relheight=0.12, relwidth=0.18, rely=0.02, relx=0.01)
                darkb = tk.Button(setPad,bg="black", relief=FLAT, activebackground="black",borderwidth=0,border=0, command=thme) #THEME BUTTONS
                darkb.place(relheight=0.13, relwidth=0.1, rely=0.14, relx=0.05)

                ctheme = tk.Button(setPad, text="custom",command=customTheme)
                ctheme.place(relheight=0.12,relwidth=0.18,relx=0.2,rely=0.02)

                dtheme = tk.Button(setPad, text="default",command=defaultTheme)
                dtheme.place(relheight=0.12,relwidth=0.18,relx=0.5,rely=0.02)

                if theme == 'Light' or mainthm == 'Light':  #configuring the button to off if light mode is the current theme
                    darkb.config(image=toggle_off_new)
                    theme = "Light"
                elif theme == 'Dark' or mainthm == 'Dark': #configuring the button to on if dark mode is the current theme (dark theme is the default)
                    darkb.config(image=toggle_on_new)
                    theme = 'Dark'
                try:
                    self.button.lift() # lifting the main setting button
                except:
                    pass
                sCounter += 1 # increasing the setting page value to 1 to store current state of the page
            else: #for detecting if settings page is already present
                setPad.destroy()
                sCounter = 0

class Lsetting:

    def __init__(self,one=None,two=None,three=None,four=None,five=None,six=None,seven=None,eight=None,nine=None,zero=None,dot=None,dash=None,dele=None,delete=None,quit=None):

        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six
        self.seven = seven
        self.eight = eight
        self.nine = nine
        self.zero = zero
        self.dot = dot
        self.dash = dash
        self.dele = dele
        self.delete = delete
        self.quit = quit
        llst=[(self.one),(self.two),(self.three),(self.four),(self.five),(self.six),(self.seven),(self.eight),(self.nine),(self.zero),(self.dot),(self.dash)]
        clst=[(self.dele),(self.delete),(self.quit)]
        for butts in llst:
            try:
                butts.config(bg="#EEEFF4",fg="#2B2B2B",activebackground="#EEEFF4",activeforeground="#2B2B2B")
            except:
                pass
        for butts in clst:
            try:
                butts.config(bg="#ff0000",fg="black",activebackground="#ff0000",activeforeground="black")
            except:
                pass

class Dsettings:

    def __init__(self,one=None,two=None,three=None,four=None,five=None,six=None,seven=None,eight=None,nine=None,zero=None,dot=None,dash=None,dele=None,delete=None,quit=None):

        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six
        self.seven = seven
        self.eight = eight
        self.nine = nine
        self.zero = zero
        self.dot = dot
        self.dash = dash
        self.dele = dele
        self.delete = delete
        self.quit = quit

        if mainthm == 'Dark':
            one.config(image=one)
            two.config(image=two)
            Stnum3.config(image=three)
            Stnum4.config(image=four)
            Stnum5.config(image=five)
            Stnum6.config(image=six)
            Stnum7.config(image=seven)
            Stnum8.config(image=eight)
            Stnum9.config(image=nine)
            Stnum0.config(image=zero)
        if mainthm == 'Light':
            Stnum1.config(image=Done)
            Stnum2.config(image=Dtwo)
            Stnum3.config(image=Dthree)
            Stnum4.config(image=Dfour)
            Stnum5.config(image=Dfive)
            Stnum6.config(image=Dsix)
            Stnum7.config(image=Dseven)
            Stnum8.config(image=Deight)
            Stnum9.config(image=Dnine)
            Stnum0.config(image=Dzero)

def setting1():
    setting(entryPad, num1, num2, num3, num4, num5, num6, num7, num8, num9, num0, decimal, Negative,settings1,Clear1,Clear2,Clear3,add,subtract,multiply,divide,Sqrt,Sqr,equals)
def setting2():
    setting(StentryPad, Stnum1, Stnum2, Stnum3, Stnum4, Stnum5, Stnum6, Stnum7, Stnum8, Stnum9, Stnum0, Stdecimal, StNegative,settings2,StC,StCE,StAC,Stadd,Stsubtract,Stmultiply,Stdivide,StSqrt,StSqr,Stequals)
def setting3():
    setting(SentryPad,Snum1,Snum2,Snum3,Snum4,Snum5,Snum6,Snum7,Snum8,Snum9,Snum0,Sdecimal,SNegative,settings3,SC,SCE,SAC,Sadd,Ssubtract,Smultiply,Sdivide,SSqr,Sqrt,Sequals)
def setting4():
    setting(WentryPad,Wnum1,Wnum2,Wnum3,Wnum4,Wnum5,Wnum6,Wnum7,Wnum8,Wnum9,Wnum0,Wdecimal,button=settings4)
def setting5():
    setting(TentryPad,Tnum1,Tnum2,Tnum3,Tnum4,Tnum5,Tnum6,Tnum7,Tnum8,Tnum9,Tnum0,Tdecimal,button=setting5)

#==========================NUMBER_BUTTONS_FUNCTIONS==========================
def num_1():
    number(1)

def num_2():
    number(2)

def num_3():
    number(3)

def num_4():
    number(4)

def num_5():
   number(5)

def num_6():
    number(6)

def num_7():
    number(7)

def num_8():
    number(8)

def num_9():
    number(9)

def num_0():
    number(0)
        
def Decimal():
    decount = 0
    declst = list(field.get())
    for i in declst:
        if i == '.':
            decount += 1
    if decount < 1:
        if field.get() == '':
            number("0.")
        elif field.get() != '':
            number(".")

def negative():
    if field.get() == '':
        number("-")
    if field.get()!= '':
        pass

#==============================OPERATOR_BUTTONS_FUNCTIONS================================

def Add():
 global counter
 if counter ==1:
    HentryPad.destroy()
    counter = 0
 else:
    if field.get()=='':
        global operator
        operator = 1
        upperOperator.delete(0, END)
        upperOperator.insert(0," [+]")
    else:
        if upperOperator.get()=='':
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 1
            upperOperator.delete(0, END)
            upperOperator.insert(0," [+]")
        elif upperOperator.get()==' [+]':
            if upperField.get() != '':
                first_num = str(upperField.get())
                second_num = str(field.get())
                dd = float(upperField.get()) + float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 1
                upperOperator.delete(0, END)
                upperOperator.insert(0," [+]")
                memory.append(f'{first_num}+{second_num}={dd}')
            else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 1
                upperOperator.delete(0, END)
                upperOperator.insert(0," [+]")
        elif upperOperator.get() == ' [-]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num = str(field.get())
            dd = float(upperField.get()) - float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 1
            upperOperator.delete(0, END)
            upperOperator.insert(0," [+]")
            memory.append(f'{first_num}-{second_num}={dd}')
         else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 1
                upperOperator.delete(0, END)
                upperOperator.insert(0," [+]")
        elif upperOperator.get() == ' [x]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num = str(field.get())
            dd = float(upperField.get()) * float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 1
            upperOperator.delete(0, END)
            upperOperator.insert(0," [+]")
            memory.append(f'{first_num}x{second_num}={dd}')
         else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 1
                upperOperator.delete(0, END)
                upperOperator.insert(0," [+]")
        elif upperOperator.get() == '[ / ]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num = str(field.get())
            dd = float(upperField.get()) / float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 1
            upperOperator.delete(0, END)
            upperOperator.insert(0," [+]")
            memory.append(f'{first_num}/{second_num}={dd}')
         else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 1
                upperOperator.delete(0, END)
                upperOperator.insert(0," [+]")
        else:
            if upperField.get() != '':
                dd = float(upperField.get()) + float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 1
                upperOperator.delete(0, END)
                upperOperator.insert(0," [+]")
            else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 1
                upperOperator.delete(0, END)
                upperOperator.insert(0," [+]")

def Subtract():
 global counter
 if counter ==1:
    HentryPad.destroy()
    counter = 0
 else:
    if field.get()=='':
        global operator
        operator = 2
        upperOperator.delete(0, END)
        upperOperator.insert(0," [-]")
    else:
        if upperOperator.get() == '':
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 2
            upperOperator.delete(0, END)
            upperOperator.insert(0," [-]")
        elif upperOperator.get() == ' [-]':
            if upperField.get() != '':
                first_num = str(upperField.get())
                second_num = str(field.get())
                dd = float(upperField.get()) - float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 2
                upperOperator.delete(0, END)
                upperOperator.insert(0," [-]")
                memory.append(f'{first_num}-{second_num}={dd}')
            else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 2
                upperOperator.delete(0, END)
                upperOperator.insert(0," [-]")
        elif upperOperator.get() == ' [+]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num = str(field.get())
            dd = float(upperField.get()) + float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 2
            upperOperator.delete(0, END)
            upperOperator.insert(0," [-]")
            memory.append(f'{first_num}+{second_num}={dd}')
         else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 2
                upperOperator.delete(0, END)
                upperOperator.insert(0," [-]")
        elif upperOperator.get() == ' [x]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num = str(field.get())
            dd = float(upperField.get()) * float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 2
            upperOperator.delete(0, END)
            upperOperator.insert(0," [-]")
            memory.append(f'{first_num}x{second_num}={dd}')
         else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 2
                upperOperator.delete(0, END)
                upperOperator.insert(0," [-]")
        elif upperOperator.get() == '[ / ]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num = str(field.get())
            dd = float(upperField.get()) / float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 2
            upperOperator.delete(0, END)
            upperOperator.insert(0," [-]")
            memory.append(f'{first_num}/{second_num}={dd}')
         else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 2
                upperOperator.delete(0, END)
                upperOperator.insert(0," [-]")
        else:
            if upperField.get() != '':
                dd = float(upperField.get()) - float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 2
                upperOperator.delete(0, END)
                upperOperator.insert(0," [-]")
            else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 2
                upperOperator.delete(0, END)
                upperOperator.insert(0," [-]")

def Multiply():
 global counter
 if counter ==1:
    HentryPad.destroy()
    counter = 0
 else:
    if field.get()=='':
        global operator
        operator = 3
        upperOperator.delete(0, END)
        upperOperator.insert(0," [x]")
    else:
        if upperOperator.get() == '':
            upperField.delete(0,END)
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 3
            upperOperator.delete(0, END)
            upperOperator.insert(0," [x]")
        elif upperOperator.get() == ' [x]':
            if upperField.get()!= '':
                first_num = str(upperField.get())
                second_num  = str(field.get())
                dd = float(upperField.get()) * float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 3
                upperOperator.delete(0, END)
                upperOperator.insert(0," [x]")
                memory.append(f'{first_num}x{second_num}={dd}')
            else:
                upperField.delete(0,END)
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 3
                upperOperator.delete(0, END)
                upperOperator.insert(0," [x]")
        elif upperOperator.get() == ' [+]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num  = str(field.get())
            dd = float(upperField.get()) + float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 3
            upperOperator.delete(0, END)
            upperOperator.insert(0," [x]")
            memory.append(f'{first_num}+{second_num}={dd}')
         else:
            upperField.delete(0,END)
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 3
            upperOperator.delete(0, END)
            upperOperator.insert(0," [x]")
        elif upperOperator.get() == ' [-]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num  = str(field.get())
            dd = float(upperField.get()) - float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 3
            upperOperator.delete(0, END)
            upperOperator.insert(0," [x]")
            memory.append(f'{first_num}-{second_num}={dd}')
         else:
            upperField.delete(0,END)
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 3
            upperOperator.delete(0, END)
            upperOperator.insert(0," [x]")
        elif upperOperator.get() == '[ / ]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num  = str(field.get())
            dd = float(upperField.get()) / float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 3
            upperOperator.delete(0, END)
            upperOperator.insert(0," [x]")
            memory.append(f'{first_num}/{second_num}={dd}')
         else:
            upperField.delete(0,END)
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 3
            upperOperator.delete(0, END)
            upperOperator.insert(0," [x]")
        else:
            if upperField.get()!= '':
                dd = float(upperField.get()) * float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 3
                upperOperator.delete(0, END)
                upperOperator.insert(0," [x]")
            else:
                upperField.delete(0,END)
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 3
                upperOperator.delete(0, END)
                upperOperator.insert(0," [x]")

def Divide():
 global counter
 if counter ==1:
    HentryPad.destroy()
    counter = 0
 else:
    if field.get()=='':
        global operator
        operator = 4
        upperOperator.delete(0, END)
        upperOperator.insert(0,"[ / ]")
    else:
        if upperOperator.get() == '':
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 4
            upperOperator.delete(0, END)
            upperOperator.insert(0,"[ / ]")
        elif upperOperator.get() == '[ / ]':
            if upperField.get() != '':
                first_num = str(upperField.get())
                second_num = str(field.get())
                dd = float(upperField.get()) / float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 4
                upperOperator.delete(0, END)
                upperOperator.insert(0,"[ / ]")
                memory.append(f'{first_num}/{second_num}={dd}')
            else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 4
                upperOperator.delete(0, END)
                upperOperator.insert(0,"[ / ]")
        elif upperOperator.get() == ' [+]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num = str(field.get())
            dd = float(upperField.get()) + float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 4
            upperOperator.delete(0, END)
            upperOperator.insert(0,"[ / ]")
            memory.append(f'{first_num}+{second_num}={dd}')
         else:
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 4
            upperOperator.delete(0, END)
            upperOperator.insert(0,"[ / ]")
        elif upperOperator.get() == ' [-]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num = str(field.get())
            dd = float(upperField.get()) - float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 4
            upperOperator.delete(0, END)
            upperOperator.insert(0,"[ / ]")
            memory.append(f'{first_num}-{second_num}={dd}')
         else:
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 4
            upperOperator.delete(0, END)
            upperOperator.insert(0,"[ / ]")
        elif upperOperator.get() == ' [x]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num = str(field.get())
            dd = float(upperField.get()) * float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 4
            upperOperator.delete(0, END)
            upperOperator.insert(0,"[ / ]")
            memory.append(f'{first_num}x{second_num}={dd}')
         else:
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 4
            upperOperator.delete(0, END)
            upperOperator.insert(0,"[ / ]")
        else:
            if upperField.get() != '':
                dd = float(upperField.get()) / float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 4
                upperOperator.delete(0, END)
                upperOperator.insert(0,"[ / ]")
            else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 4
                upperOperator.delete(0, END)
                upperOperator.insert(0,"[ / ]")

#=======================SQUARE_ROOTS_FUNCTIONS===========================

def sqrt():
 global counter
 if counter ==1:
    HentryPad.destroy()
    counter = 0
 else:
    if field.get()=='':
        sss=str(upperField.get())
        upperField.delete(0, END)
        root=math.sqrt(float(sss))
        upperField.insert(0, root)
        field.delete(0,END)
        global operator
        operator = 5
        upperOperator.delete(0, END)
        upperOperator.insert(0," [√]")
        upperAns.delete(0, END)
        upperAns.insert(0,"√" + sss + "=")
        memory.append(f'sqrt({sss})={root}')
    else:
        ss=str(field.get())
        root=math.sqrt(float(ss))
        upperField.delete(0, END)
        upperField.insert(0, root)
        field.delete(0,END)
        operator = 5
        upperOperator.delete(0, END)
        upperOperator.insert(0," [√]")
        upperAns.delete(0, END)
        upperAns.insert(0,"√" + ss + "=")
        memory.append(f'sqrt({ss})={root}')

def sqr():
 global counter
 if counter ==1:
    HentryPad.destroy()
    counter = 0
 else:
    global added
    global operator
    if upperField.get()=='':
        if field.get()=='':
            if upperField.get()=='':
                pass
        else:
            if field.get()=='':
             try:
                a = upperField.get()
                added = float(upperField.get())**float(upperField.get())
                upperField.delete(0,END)
                upperField.insert(0, added)
                upperOperator.delete(0, END)
                upperOperator.insert(0," [^]")
                upperAns.delete(0,END)
                upperAns.insert(0,str(a) + "^" + str(a))
                memory.append(f'{a}^{a}={added}')
             except:
                upperField.delete(0, END)
                upperField.insert(0, "OVERFLOW!!")
                upperOperator.delete(0, END)
                upperOperator.insert(0," [^]")
                upperAns.delete(0,END)
                upperAns.insert(0,"last Ans=" + str(added))
            else:
                upperField.delete(0,END)
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 6
                upperOperator.delete(0, END)
                upperOperator.insert(0," [^]")
    else:
        if field.get()=='':
            try:
                a = upperField.get()
                added = float(upperField.get())**float(upperField.get())
                upperField.delete(0,END)
                upperField.insert(0, added)
                upperOperator.delete(0, END)
                upperOperator.insert(0," [^]")
                upperAns.delete(0,END)
                upperAns.insert(0,str(a) + "^" + str(a))
                memory.append(f'{a}^{a}={added}')
            except:
                upperField.delete(0, END)
                upperField.insert(0, "OVERFLOW!!")
                upperOperator.delete(0, END)
                upperOperator.insert(0," [^]")
                upperAns.delete(0,END)
                upperAns.insert(0,"last Ans=" + str(added))
        else:
            upperField.delete(0,END)
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 6
            upperOperator.delete(0, END)
            upperOperator.insert(0," [^]")

#===============================EQUAL_FUNCTIONS========================================

def Equals():
 try:

    #=====ADDITION=====#
    if operator==1:
        ss=field.get()
        field.delete(0,END)
        first_num = upperField.get()
        added=float(upperField.get())+float(ss)
        upperField.delete(0,END)
        upperField.insert(0,added)
        field.delete(0,END)
        upperAns.insert(0,"ANS=")
        a=float(first_num)
        b=float(ss)
        c=float(added)
        if a < 0 or b < 0 or c < 0:
            memory.append(f'({first_num})+({ss})=({added})')
        else:
            memory.append(f'{first_num}+{ss}={added}')

    #=====SUBTRACTION=====#
    if operator==2:
        ss=field.get()
        field.delete(0,END)
        first_num = upperField.get()
        added=float(upperField.get())-float(ss)
        upperField.delete(0,END)
        upperField.insert(0,added)
        field.delete(0,END)
        upperAns.insert(0,"ANS=")
        a=float(first_num)
        b=float(ss)
        c=float(added)
        if a < 0 or b < 0 or c < 0:
            memory.append(f'({first_num})-({ss})=({added})')
        else:
            memory.append(f'{first_num}-{ss}={added}')
    
    #=====MULTIPLICATION=====#
    if operator==3:
        ss=field.get()
        field.delete(0,END)
        first_num = upperField.get()
        added=float(upperField.get())*float(ss)
        upperField.delete(0,END)
        upperField.insert(0,added)
        field.delete(0,END)
        upperAns.insert(0,"ANS=")
        a=float(first_num)
        b=float(ss)
        c=float(added)
        if a < 0 or b < 0 or c < 0:
            memory.append(f'({first_num})x({ss})=({added})')
        else:
            memory.append(f'{first_num}x{ss}={added}')

    #=====DIVISION=====#
    if operator==4:
        ss=field.get()
        field.delete(0,END)
        first_num = upperField.get()
        added=float(upperField.get())/float(ss)
        upperField.delete(0,END)
        upperField.insert(0,added)
        field.delete(0,END)
        upperAns.insert(0,"ANS=")
        a=float(first_num)
        b=float(ss)
        c=float(added)
        if a < 0 or b < 0 or c < 0:
            memory.append(f'({first_num})/({ss})=({added})')
        else:
            memory.append(f'{first_num}/{ss}={added}')

    #=====SQUARE_ROOT=====#
    if operator==5:
        ss=field.get()
        field.delete(0,END)
        uf = upperField.get()
        added=math.sqrt(float(uf))
        upperField.delete(0,END)
        upperField.insert(0, added)
        field.delete(0,END)
        upperAns.delete(0, END)
        upperAns.insert(0,"√" + uf)
        memory.append(f'sqrt({uf})={added}')

    #=====POWER=====#
    if operator==6:
        try:
            power=field.get()
            field.delete(0,END)
            number=str(upperField.get())
            added=float(upperField.get())**float(power)
            upperField.delete(0,END)
            upperField.insert(0,added)
            upperField.insert(0, field.get())
            upperAns.insert(0, number + "^" + power + "=")
            memory.append(f'{number}^{power}={added}')
        except:
            field.delete(0,END)
            upperField.delete(0, END)
            upperField.insert(0, "OVERFLOW!!")
 except:
     pass

#=============================CLEAR_BUTTONS================================

def CE():
 global counter
 if counter ==1:
    HentryPad.destroy()
    counter = 0
 else:
    field.delete(0,END)

def C():
 global counter
 if counter ==1:
    HentryPad.destroy()
    counter = 0
 else:
    field.delete(0,END)
    upperField.delete(0,END)
    upperAns.delete(0,END)

def back():
 if Pad == 1 or dPad == 1 or sPad == 1:
    get = len(field.get())-1
    global counter
    if counter == 1:
        HentryPad.destroy()
        counter = 0
    else:
        field.delete(get)
 elif wPad == 1:
     get = len(entry1.get())-1
     if counter == 1:
         HentryPad.destroy()
         counter = 0
     else:
      entry1.delete(get)
      try:
        if entry1.get() == '':
            entry2.delete(0, END)
        if converter == 'c':
            if converter2 == 'c':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'c':
            if converter2 == 'mg':
                co = float(entry1.get()) * 200
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'c':
            if converter2 == 'g':
                co = float(entry1.get()) / 5
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'c':
            if converter2 == 'kg':
                co = float(entry1.get()) / 5000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'c':
            if converter2 == 't':
                co = float(entry1.get()) / 4.536e+6
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'c':
            if converter2 == 'mt':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'c':
            if converter2 == 'o':
                co = float(entry1.get()) / 142
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'c':
            if converter2 == 'p':
                co = float(entry1.get()) / 2268
                entry2.delete(0, END)
                entry2.insert(0,co)
        #mg#
        if converter == 'mg':
            if converter2 == 'mg':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'mg':
            if converter2 == 'c':
                co = float(entry1.get()) / 200
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'mg':
            if converter2 == 'g':
                co = float(entry1.get()) / 1000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'mg':
            if converter2 == 'kg':
                co = float(entry1.get()) / 1e+6
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'mg':
            if converter2 == 't':
                co = float(entry1.get()) / 9.072e+8
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'mg':
            if converter2 == 'mt':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'mg':
            if converter2 == 'o':
                co = float(entry1.get()) / 28350
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'mg':
            if converter2 == 'p':
                co = float(entry1.get()) / 453592
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'g':
            if converter2 == 'g':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'g':
            if converter2 == 'c':
                co = float(entry1.get()) * 5
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'g':
            if converter2 == 'mg':
                co = float(entry1.get()) * 1000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'g':
            if converter2 == 'kg':
                co = float(entry1.get()) / 1000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'g':
            if converter2 == 't':
                co = float(entry1.get()) / 907185
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'g':
            if converter2 == 'mt':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'g':
            if converter2 == 'o':
                co = float(entry1.get()) / 28.35
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'g':
            if converter2 == 'p':
                co = float(entry1.get()) / 454
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'kg':
            if converter2 == 'kg':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'kg':
            if converter2 == 'c':
                co = float(entry1.get()) * 5000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'kg':
            if converter2 == 'mg':
                co = float(entry1.get()) / 1e+6
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'kg':
            if converter2 == 'g':
                co = float(entry1.get()) * 1000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'kg':
            if converter2 == 't':
                co = float(entry1.get()) / 907
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'kg':
            if converter2 == 'o':
                co = float(entry1.get()) * 35.274
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'kg':
            if converter2 == 'p':
                co = float(entry1.get()) * 2.205
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 't':
            if converter2 == 't':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 't':
            if converter2 == 'c':
                co = float(entry1.get()) * 4.536e+6
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 't':
            if converter2 == 'mg':
                co = float(entry1.get()) * 9.072e+8
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 't':
            if converter2 == 'g':
                co = float(entry1.get()) * 907185
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 't':
            if converter2 == 'kg':
                co = float(entry1.get()) * 907
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 't':
            if converter2 == 'mt':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 't':
            if converter2 == 'o':
                co = float(entry1.get()) * 32000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 't':
            if converter2 == 'p':
                co = float(entry1.get()) * 2000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'mt':
            if converter2 == 'mt':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'o':
            if converter2 == 'o':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'o':
            if converter2 == 'c':
                co = float(entry1.get()) * 142
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'o':
            if converter2 == 'mg':
                co = float(entry1.get()) * 28350
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'o':
            if converter2 == 'g':
                co = float(entry1.get()) * 28.35
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'o':
            if converter2 == 'kg':
                co = float(entry1.get()) / 35.274
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'o':
            if converter2 == 't':
                co = float(entry1.get()) / 32000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'o':
            if converter2 == 'mt':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'o':
            if converter2 == 'p':
                co = float(entry1.get()) / 16
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'p':
            if converter2 == 'p':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'p':
            if converter2 == 'c':
                co = float(entry1.get()) * 2268
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'p':
            if converter2 == 'mg':
                co = float(entry1.get()) * 453592
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'p':
            if converter2 == 'g':
                co = float(entry1.get()) * 454
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'p':
            if converter2 == 'kg':
                co = float(entry1.get()) / 2.205
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'p':
            if converter2 == 't':
                co = float(entry1.get()) / 2000
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'p':
            if converter2 == 'mt':
                co = float(entry1.get())
                entry2.delete(0, END)
                entry2.insert(0,co)
        if converter == 'p':
            if converter2 == 'o':
                co = float(entry1.get()) * 16
                entry2.delete(0, END)
                entry2.insert(0,co)
      except:
         pass
 elif tPad == 1:
    get = len(Tentry1.get())-1
    if counter == 1:
        HentryPad.destroy()
        counter = 0
    else:
     Tentry1.delete(get)
     try:
        if Tentry1.get() == '':
            Tentry2.delete(0, END)
        if Tonverter == 'ms':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) / 1000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) / 60000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) / 3.6e+6
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) / 8.64e+7
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 'y':
                co = float(Tentry1.get()) / 3.154e+10
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 3.154e+12
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 's':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 1000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) / 60
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) / 3600
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) / 86400
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'y':
                co = float(Tentry1.get()) / 3.154e+7
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 3.154e+9
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'm':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 6000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) * 60
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) * 1/60
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) * 1440
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'y':
                co = float(Tentry1.get()) / 525600
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 28.35 / 5.256e+7
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'h':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 3.6e+6
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) * 3600
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) * 60
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) / 24
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'y':
                co = float(Tentry1.get()) / 8760
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 876000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'd':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 8.64e+7
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) * 85400
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) * 1440
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) * 24
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'y':
                co = float(Tentry1.get()) / 365
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 36500
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'y':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 3.154e+10
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) * 3.154e+7
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) * 525600
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) * 8760
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) * 365
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 100
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 16
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 3.154e+12
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) * 3.154e+9
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) * 5.256e+7
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) * 876000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) * 36500
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'y':
                co = float(Tentry1.get()) * 100
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
     except:
         pass

def AC():
 global counter
 if counter ==1:
    HentryPad.destroy()
    counter = 0
 else:
    window.destroy()
#Brrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
def num_1s():
 if Pad == 1 or dPad ==1 or sPad == 1:
    num_1()
    if dPad == 1:
        if theme == 'Dark':
            num1.config(relief=SUNKEN,bg="#262626", fg="cyan")
            num1.after(58, lambda: num1.config(relief=RAISED, bg="black", fg="white"))
        else:
            num1.config(relief=SUNKEN,bg="gray", fg="cyan")
            num1.after(58, lambda: num1.config(relief=RAISED, bg="white", fg="black"))
    if Pad == 1:
        Stnum1.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Stnum1.after(58, lambda: Stnum1.config(relief=RAISED, bg="black", fg="white"))
    if sPad == 1:
        Snum1.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Snum1.after(58, lambda: Snum1.config(relief=RAISED, bg="black", fg="white"))
 elif wPad == 1:
        weightNum(1,Wnum1)
 elif tPad == 1:
        timeNum(1,Tnum1)

def num_2s():
 if Pad == 1 or dPad == 1 or sPad == 1:
    num_2()
    if dPad == 1:
        num2.config(relief=SUNKEN,bg="#262626", fg="cyan")
        num2.after(58, lambda: num2.config(relief=RAISED, bg="black", fg="white"))
    if Pad == 1:
        Stnum2.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Stnum2.after(58, lambda: Stnum2.config(relief=RAISED, bg="black", fg="white"))
    if sPad == 1:
        Snum2.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Snum2.after(58, lambda: Snum2.config(relief=RAISED, bg="black", fg="white"))
 elif wPad == 1:
        weightNum(2,Wnum2)
 elif tPad == 1:
        timeNum(2,Tnum2)

def num_3s():
 if Pad == 1 or dPad == 1 or sPad == 1:
    num_3()
    if dPad == 1:
        num3.config(relief=SUNKEN,bg="#262626", fg="cyan")
        num3.after(58, lambda: num3.config(relief=RAISED, bg="black", fg="white"))
    if Pad == 1:
        Stnum3.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Stnum3.after(58, lambda: Stnum3.config(relief=RAISED, bg="black", fg="white"))
    if sPad == 1:
        Snum3.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Snum3.after(58, lambda: Snum3.config(relief=RAISED, bg="black", fg="white"))
 elif wPad == 1:
        weightNum(3,Wnum3)
 elif tPad == 1:
        timeNum(3,Tnum3)

def num_4s():
 if Pad == 1 or dPad == 1 or sPad == 1:
    num_4()
    if dPad == 1:
        num4.config(relief=SUNKEN,bg="#262626", fg="cyan")
        num4.after(58, lambda: num4.config(relief=RAISED, bg="black", fg="white"))
    if Pad == 1:
        Stnum4.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Stnum4.after(58, lambda: Stnum4.config(relief=RAISED, bg="black", fg="white"))
    if sPad == 1:
        Snum4.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Snum4.after(58, lambda: Snum4.config(relief=RAISED, bg="black", fg="white"))
 elif wPad == 1:
        weightNum(4,Wnum4)
 elif tPad == 1:
        timeNum(4,Tnum4)

def num_5s():
 if Pad == 1 or dPad == 1 or sPad == 1:
    num_5()
    if dPad == 1:
        num5.config(relief=SUNKEN,bg="#262626", fg="cyan")
        num5.after(58, lambda: num5.config(relief=RAISED, bg="black", fg="white"))
    if Pad == 1:
        Stnum5.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Stnum5.after(58, lambda: Stnum5.config(relief=RAISED, bg="black", fg="white"))
    if sPad == 1:
        Snum5.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Snum5.after(58, lambda: Snum5.config(relief=RAISED, bg="black", fg="white"))
 elif wPad == 1:
        weightNum(5, Wnum5)
 elif tPad == 1:
        timeNum(5,Tnum5)

def num_6s():
 if Pad == 1 or dPad == 1 or sPad == 1:
    num_6()
    if dPad == 1:
        num6.config(relief=SUNKEN,bg="#262626", fg="cyan")
        num6.after(58, lambda: num6.config(relief=RAISED, bg="black", fg="white"))
    if Pad == 1:
        Stnum6.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Stnum6.after(58, lambda: Stnum6.config(relief=RAISED, bg="black", fg="white"))
    if sPad == 1:
        Snum6.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Snum6.after(58, lambda: Snum6.config(relief=RAISED, bg="black", fg="white"))
 elif wPad == 1:
        weightNum(6, Wnum6)
 elif tPad == 1:
        timeNum(6,Tnum6)

def num_7s():
 if Pad == 1 or dPad == 1 or sPad == 1:
    num_7()
    if dPad == 1:
        num7.config(relief=SUNKEN,bg="#262626", fg="cyan")
        num7.after(58, lambda: num7.config(relief=RAISED, bg="black", fg="white"))
    if Pad == 1:
        Stnum7.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Stnum7.after(58, lambda: Stnum7.config(relief=RAISED, bg="black", fg="white"))
    if sPad == 1:
        Snum7.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Snum7.after(58, lambda: Snum7.config(relief=RAISED, bg="black", fg="white"))
 elif wPad == 1:
        weightNum(7, Wnum7)
 elif tPad == 1:
        timeNum(7,Tnum7)

def num_8s():
 if Pad == 1 or dPad == 1 or sPad == 1:
    num_8()
    if dPad == 1:
        num8.config(relief=SUNKEN,bg="#262626", fg="cyan")
        num8.after(58, lambda: num8.config(relief=RAISED, bg="black", fg="white"))
    if Pad == 1:
        Stnum8.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Stnum8.after(58, lambda: Stnum8.config(relief=RAISED, bg="black", fg="white"))
    if sPad == 1:
        Snum8.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Snum8.after(58, lambda: Snum8.config(relief=RAISED, bg="black", fg="white"))
 elif wPad == 1:
        weightNum(8, Wnum8)
 elif tPad == 1:
        timeNum(8, Tnum8)

def num_9s():
 if Pad == 1 or dPad == 1 or sPad == 1:
    num_9()
    if dPad == 1:
        num9.config(relief=SUNKEN,bg="#262626", fg="cyan")
        num9.after(58, lambda: num9.config(relief=RAISED, bg="black", fg="white"))
    if Pad == 1:
        Stnum9.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Stnum9.after(58, lambda: Stnum9.config(relief=RAISED, bg="black", fg="white"))
    if sPad == 1:
        Snum9.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Snum9.after(58, lambda: Snum9.config(relief=RAISED, bg="black", fg="white"))
 elif wPad == 1:
        weightNum(9, Wnum9)
 elif tPad ==1:
        timeNum(9,Tnum9)

def num_0s():
 if Pad == 1 or dPad == 1 or sPad == 1:
    num_0()
    if dPad == 1:
        num0.config(relief=SUNKEN,bg="#262626", fg="cyan")
        num0.after(58, lambda: num0.config(relief=RAISED, bg="black", fg="white"))
    if Pad == 1:
        Stnum0.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Stnum0.after(58, lambda: Stnum0.config(relief=RAISED, bg="black", fg="white"))
    if sPad == 1:
        Snum0.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Snum0.after(58, lambda: Snum0.config(relief=RAISED, bg="black", fg="white"))
 elif wPad == 1:
        weightNum(0, Wnum0)
 elif tPad == 1:
        timeNum(0, Tnum0)

def Decimals():
 if Pad == 1 or dPad == 1 or sPad == 1:
    Decimal()
    if dPad == 1:
        decimal.config(relief=SUNKEN,bg="black", fg="white")
        decimal.after(58, lambda: decimal.config(relief=RAISED, bg="#262626", fg="cyan"))
    if Pad ==1:
        Stdecimal.config(relief=SUNKEN,bg="black", fg="white")
        Stdecimal.after(58, lambda: Stdecimal.config(relief=RAISED, bg="#262626", fg="cyan"))
    if sPad == 1:
        Sdecimal.config(relief=SUNKEN,bg="#262626", fg="cyan")
        Sdecimal.after(58, lambda: Sdecimal.config(relief=RAISED, bg="black", fg="white"))
 elif wPad == 1:
       decNum(entry1,Wdecimal)
 elif tPad == 1:
       decNum(Tentry1,Tdecimal)

def negatives():
 if Pad == 1 or dPad == 1 or sPad == 1:
    negative()
    if dPad == 1:
        Negative.config(relief=SUNKEN,bg="black", fg="white")
        Negative.after(58, lambda: Negative.config(relief=RAISED, bg="#262626", fg="cyan"))
    if Pad == 1:
        StNegative.config(relief=SUNKEN,bg="black", fg="white")
        StNegative.after(58, lambda: StNegative.config(relief=RAISED, bg="#262626", fg="cyan"))
    if sPad == 1:
        SNegative.config(relief=SUNKEN,bg="#262626", fg="cyan")
        SNegative.after(58, lambda: SNegative.config(relief=RAISED, bg="black", fg="white"))
 elif wPad == 1:
     pass
 elif tPad == 1:
     pass
#==============================OPERATOR_BUTTONS_FUNCTIONS================================

def Adds():
 if Pad == 1 or dPad == 1 or sPad == 1:
    global counter
    if counter ==1:
        HentryPad.destroy()
        counter = 0
    else:
        if field.get()=='':
            global operator
            operator = 1
            upperOperator.delete(0, END)
            upperOperator.insert(0," [+]")
        else:
            if upperOperator.get()=='':
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 1
                upperOperator.delete(0, END)
                upperOperator.insert(0," [+]")
            elif upperOperator.get()==' [+]':
                if upperField.get() != '':
                    first_num = str(upperField.get())
                    second_num = str(field.get())
                    dd = float(upperField.get()) + float(field.get())
                    upperField.delete(0,END)
                    upperField.insert(0,dd)
                    field.delete(0,END)
                    operator = 1
                    upperOperator.delete(0, END)
                    upperOperator.insert(0," [+]")
                    memory.append(f'{first_num}+{second_num}={dd}')
                else:
                    upperField.insert(0,field.get())
                    field.delete(0,END)
                    operator = 1
                    upperOperator.delete(0, END)
                    upperOperator.insert(0," [+]")
            elif upperOperator.get() == ' [-]':
             if upperField.get() != '':
                first_num = str(upperField.get())
                second_num = str(field.get())
                dd = float(upperField.get()) - float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 1
                upperOperator.delete(0, END)
                upperOperator.insert(0," [+]")
                memory.append(f'{first_num}-{second_num}={dd}')
             else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 1
                upperOperator.delete(0, END)
                upperOperator.insert(0," [+]")
            elif upperOperator.get() == ' [x]':
             if upperField.get() != '':
                first_num = str(upperField.get())
                second_num = str(field.get())
                dd = float(upperField.get()) * float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 1
                upperOperator.delete(0, END)
                upperOperator.insert(0," [+]")
                memory.append(f'{first_num}x{second_num}={dd}')
             else:
                    upperField.insert(0,field.get())
                    field.delete(0,END)
                    operator = 1
                    upperOperator.delete(0, END)
                    upperOperator.insert(0," [+]")
            elif upperOperator.get() == '[ / ]':
             if upperField.get() != '':
                first_num = str(upperField.get())
                second_num = str(field.get())
                dd = float(upperField.get()) / float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 1
                upperOperator.delete(0, END)
                upperOperator.insert(0," [+]")
                memory.append(f'{first_num}/{second_num}={dd}')
             else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 1
                upperOperator.delete(0, END)
                upperOperator.insert(0," [+]")
            else:
             if upperField.get() != '':
                dd = float(upperField.get()) + float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 1
                upperOperator.delete(0, END)
                upperOperator.insert(0," [+]")
             else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 1
                upperOperator.delete(0, END)
                upperOperator.insert(0," [+]")
    if dPad == 1:
            add.config(relief=SUNKEN)
            add.after(58, lambda: add.config(relief=RAISED))
    if Pad == 1:
            Stadd.config(relief=SUNKEN)
            Stadd.after(58, lambda: Stadd.config(relief=RAISED))
    if sPad == 1:
            Sadd.config(relief=SUNKEN)
            Sadd.after(58, lambda: Sadd.config(relief=RAISED))

def Subtracts():
 if Pad == 1 or dPad == 1 or sPad == 1:
  global counter
  if counter ==1:
    HentryPad.destroy()
    counter = 0
  else:
    if field.get()=='':
        global operator
        operator = 2
        upperOperator.delete(0, END)
        upperOperator.insert(0," [-]")
    else:
        if upperOperator.get() == '':
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 2
            upperOperator.delete(0, END)
            upperOperator.insert(0," [-]")
        elif upperOperator.get() == ' [-]':
            if upperField.get() != '':
                first_num = str(upperField.get())
                second_num = str(field.get())
                dd = float(upperField.get()) - float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 2
                upperOperator.delete(0, END)
                upperOperator.insert(0," [-]")
                memory.append(f'{first_num}-{second_num}={dd}')
            else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 2
                upperOperator.delete(0, END)
                upperOperator.insert(0," [-]")
        elif upperOperator.get() == ' [+]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num = str(field.get())
            dd = float(upperField.get()) + float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 2
            upperOperator.delete(0, END)
            upperOperator.insert(0," [-]")
            memory.append(f'{first_num}+{second_num}={dd}')
         else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 2
                upperOperator.delete(0, END)
                upperOperator.insert(0," [-]")
        elif upperOperator.get() == ' [x]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num = str(field.get())
            dd = float(upperField.get()) * float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 2
            upperOperator.delete(0, END)
            upperOperator.insert(0," [-]")
            memory.append(f'{first_num}x{second_num}={dd}')
         else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 2
                upperOperator.delete(0, END)
                upperOperator.insert(0," [-]")
        elif upperOperator.get() == '[ / ]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num = str(field.get())
            dd = float(upperField.get()) / float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 2
            upperOperator.delete(0, END)
            upperOperator.insert(0," [-]")
            memory.append(f'{first_num}/{second_num}={dd}')
         else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 2
                upperOperator.delete(0, END)
                upperOperator.insert(0," [-]")
        else:
            if upperField.get() != '':
                dd = float(upperField.get()) - float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 2
                upperOperator.delete(0, END)
                upperOperator.insert(0," [-]")
            else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 2
                upperOperator.delete(0, END)
                upperOperator.insert(0," [-]")
  if dPad == 1:
    subtract.config(relief=SUNKEN)
    subtract.after(58, lambda: subtract.config(relief=RAISED))
  if Pad == 1:
    Stsubtract.config(relief=SUNKEN)
    Stsubtract.after(58, lambda: Stsubtract.config(relief=RAISED))
  if sPad == 1:
        Ssubtract.config(relief=SUNKEN)
        Ssubtract.after(58, lambda: Ssubtract.config(relief=RAISED))

def Multiplys():
 if Pad == 1 or dPad == 1 or sPad == 1:
  global counter
  if counter ==1:
    HentryPad.destroy()
    counter = 0
  else:
    if field.get()=='':
        global operator
        operator = 3
        upperOperator.delete(0, END)
        upperOperator.insert(0," [x]")
    else:
        if upperOperator.get() == '':
            upperField.delete(0,END)
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 3
            upperOperator.delete(0, END)
            upperOperator.insert(0," [x]")
        elif upperOperator.get() == ' [x]':
            if upperField.get()!= '':
                first_num = str(upperField.get())
                second_num  = str(field.get())
                dd = float(upperField.get()) * float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 3
                upperOperator.delete(0, END)
                upperOperator.insert(0," [x]")
                memory.append(f'{first_num}x{second_num}={dd}')
            else:
                upperField.delete(0,END)
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 3
                upperOperator.delete(0, END)
                upperOperator.insert(0," [x]")
        elif upperOperator.get() == ' [+]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num  = str(field.get())
            dd = float(upperField.get()) + float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 3
            upperOperator.delete(0, END)
            upperOperator.insert(0," [x]")
            memory.append(f'{first_num}+{second_num}={dd}')
         else:
            upperField.delete(0,END)
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 3
            upperOperator.delete(0, END)
            upperOperator.insert(0," [x]")
        elif upperOperator.get() == ' [-]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num  = str(field.get())
            dd = float(upperField.get()) - float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 3
            upperOperator.delete(0, END)
            upperOperator.insert(0," [x]")
            memory.append(f'{first_num}-{second_num}={dd}')
         else:
            upperField.delete(0,END)
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 3
            upperOperator.delete(0, END)
            upperOperator.insert(0," [x]")
        elif upperOperator.get() == '[ / ]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num  = str(field.get())
            dd = float(upperField.get()) / float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 3
            upperOperator.delete(0, END)
            upperOperator.insert(0," [x]")
            memory.append(f'{first_num}/{second_num}={dd}')
         else:
            upperField.delete(0,END)
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 3
            upperOperator.delete(0, END)
            upperOperator.insert(0," [x]")
        else:
            if upperField.get()!= '':
                dd = float(upperField.get()) * float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 3
                upperOperator.delete(0, END)
                upperOperator.insert(0," [x]")
            else:
                upperField.delete(0,END)
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 3
                upperOperator.delete(0, END)
                upperOperator.insert(0," [x]")
  if dPad == 1:
    multiply.config(relief=SUNKEN)
    multiply.after(58, lambda: multiply.config(relief=RAISED))
  if Pad == 1:
    Stmultiply.config(relief=SUNKEN)
    Stmultiply.after(58, lambda: Stmultiply.config(relief=RAISED))
  if sPad == 1:
        Smultiply.config(relief=SUNKEN)
        Smultiply.after(58, lambda: Smultiply.config(relief=RAISED))

def Divides():
 if Pad == 1 or dPad == 1 or sPad == 1:
  global counter
  if counter ==1:
    HentryPad.destroy()
    counter = 0
  else:
    if field.get()=='':
        global operator
        operator = 4
        upperOperator.delete(0, END)
        upperOperator.insert(0,"[ / ]")
    else:
        if upperOperator.get() == '':
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 4
            upperOperator.delete(0, END)
            upperOperator.insert(0,"[ / ]")
        elif upperOperator.get() == '[ / ]':
            if upperField.get() != '':
                first_num = str(upperField.get())
                second_num = str(field.get())
                dd = float(upperField.get()) / float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 4
                upperOperator.delete(0, END)
                upperOperator.insert(0,"[ / ]")
                memory.append(f'{first_num}/{second_num}={dd}')
            else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 4
                upperOperator.delete(0, END)
                upperOperator.insert(0,"[ / ]")
        elif upperOperator.get() == ' [+]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num = str(field.get())
            dd = float(upperField.get()) + float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 4
            upperOperator.delete(0, END)
            upperOperator.insert(0,"[ / ]")
            memory.append(f'{first_num}+{second_num}={dd}')
         else:
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 4
            upperOperator.delete(0, END)
            upperOperator.insert(0,"[ / ]")
        elif upperOperator.get() == ' [-]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num = str(field.get())
            dd = float(upperField.get()) - float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 4
            upperOperator.delete(0, END)
            upperOperator.insert(0,"[ / ]")
            memory.append(f'{first_num}-{second_num}={dd}')
         else:
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 4
            upperOperator.delete(0, END)
            upperOperator.insert(0,"[ / ]")
        elif upperOperator.get() == ' [x]':
         if upperField.get() != '':
            first_num = str(upperField.get())
            second_num = str(field.get())
            dd = float(upperField.get()) * float(field.get())
            upperField.delete(0,END)
            upperField.insert(0,dd)
            field.delete(0,END)
            operator = 4
            upperOperator.delete(0, END)
            upperOperator.insert(0,"[ / ]")
            memory.append(f'{first_num}x{second_num}={dd}')
         else:
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 4
            upperOperator.delete(0, END)
            upperOperator.insert(0,"[ / ]")
        else:
            if upperField.get() != '':
                dd = float(upperField.get()) / float(field.get())
                upperField.delete(0,END)
                upperField.insert(0,dd)
                field.delete(0,END)
                operator = 4
                upperOperator.delete(0, END)
                upperOperator.insert(0,"[ / ]")
            else:
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 4
                upperOperator.delete(0, END)
                upperOperator.insert(0,"[ / ]")
  if dPad == 1:
    divide.config(relief=SUNKEN)
    divide.after(58, lambda: divide.config(relief=RAISED))
  if Pad == 1:
    Stdivide.config(relief=SUNKEN)
    Stdivide.after(58, lambda: Stdivide.config(relief=RAISED))
  if sPad == 1:
        Sdivide.config(relief=SUNKEN)
        Sdivide.after(58, lambda: Sdivide.config(relief=RAISED))

#=======================SQUARE_ROOTS_FUNCTIONS===========================

def sqrts():
 if Pad == 1 or dPad == 1 or sPad == 1:
  global counter
  if counter ==1:
   try:
    HentryPad.destroy()
    counter = 0
   except:
      pass
  else:
   try:
    if field.get()=='':
        sss=str(upperField.get())
        upperField.delete(0, END)
        root=math.sqrt(float(sss))
        upperField.insert(0, root)
        field.delete(0,END)
        global operator
        operator = 5
        upperOperator.delete(0, END)
        upperOperator.insert(0," [√]")
        upperAns.delete(0, END)
        upperAns.insert(0,"√" + sss + "=")
        memory.append(f'sqrt({sss})={root}')
    else:
        ss=str(field.get())
        root=math.sqrt(float(ss))
        upperField.delete(0, END)
        upperField.insert(0, root)
        field.delete(0,END)
        operator = 5
        upperOperator.delete(0, END)
        upperOperator.insert(0," [√]")
        upperAns.delete(0, END)
        upperAns.insert(0,"√" + ss + "=")
        memory.append(f'sqrt({ss})={root}')
    if dPad == 1:
     Sqrt.config(relief=SUNKEN)
     Sqrt.after(58, lambda: Sqrt.config(relief=RAISED))
    if Pad == 1:
     StSqrt.config(relief=SUNKEN)
     StSqrt.after(58, lambda: StSqrt.config(relief=RAISED))
    if sPad == 1:
     SSqrt.config(relief=SUNKEN,bg="#262626", fg="cyan")
     SSqrt.after(58, lambda: SSqrt.config(relief=RAISED, bg="black", fg="white"))
   except:
       if dPad == 1:
        Sqrt.config(relief=SUNKEN)
        Sqrt.after(58, lambda: Sqrt.config(relief=RAISED))
       if Pad == 1:
        StSqrt.config(relief=SUNKEN)
        StSqrt.after(58, lambda: StSqrt.config(relief=RAISED))
       if sPad == 1:
        SSqrt.config(relief=SUNKEN)
        SSqrt.after(58, lambda: SSqrt.config(relief=RAISED))

def sqrs():
 if Pad == 1 or dPad == 1 or sPad == 1:
  global counter
  if counter ==1:
   try:
    HentryPad.destroy()
    counter = 0
   except:
      pass
  else:
   try:
    global added
    global operator
    if upperField.get()=='':
        if field.get()=='':
            if upperField.get()=='':
                pass
        else:
            if field.get()=='':
             try:
                a = upperField.get()
                added = float(upperField.get())**float(upperField.get())
                upperField.delete(0,END)
                upperField.insert(0, added)
                upperOperator.delete(0, END)
                upperOperator.insert(0," [^]")
                upperAns.delete(0,END)
                upperAns.insert(0,str(a) + "^" + str(a))
                memory.append(f'{a}^{a}={added}')
             except:
                upperField.delete(0, END)
                upperField.insert(0, "OVERFLOW!!")
                upperOperator.delete(0, END)
                upperOperator.insert(0," [^]")
                upperAns.delete(0,END)
                upperAns.insert(0,"last Ans=" + str(added))
            else:
                upperField.delete(0,END)
                upperField.insert(0,field.get())
                field.delete(0,END)
                operator = 6
                upperOperator.delete(0, END)
                upperOperator.insert(0," [^]")
    else:
        if field.get()=='':
            try:
                a = upperField.get()
                added = float(upperField.get())**float(upperField.get())
                upperField.delete(0,END)
                upperField.insert(0, added)
                upperOperator.delete(0, END)
                upperOperator.insert(0," [^]")
                upperAns.delete(0,END)
                upperAns.insert(0,str(a) + "^" + str(a))
                memory.append(f'{a}^{a}={added}')
            except:
                upperField.delete(0, END)
                upperField.insert(0, "OVERFLOW!!")
                upperOperator.delete(0, END)
                upperOperator.insert(0," [^]")
                upperAns.delete(0,END)
                upperAns.insert(0,"last Ans=" + str(added))
        else:
            upperField.delete(0,END)
            upperField.insert(0,field.get())
            field.delete(0,END)
            operator = 6
            upperOperator.delete(0, END)
            upperOperator.insert(0," [^]")
    if dPad == 1:
        Sqr.config(relief=SUNKEN)
        Sqr.after(58, lambda: Sqr.config(relief=RAISED))
    if Pad == 1:
        StSqr.config(relief=SUNKEN)
        StSqr.after(58, lambda: StSqr.config(relief=RAISED))
    if sPad == 1:
        SSqr.config(relief=SUNKEN)
        SSqr.after(58, lambda: SSqr.config(relief=RAISED))
   except:
      pass

#===============================EQUAL_FUNCTIONS========================================

def Equalss(): 
 if Pad == 1 or dPad == 1 or sPad == 1:
  try:

 #=====ADDITION=====#
    if operator==1:
        ss=field.get()
        field.delete(0,END)
        first_num = upperField.get()
        added=float(upperField.get())+float(ss)
        upperField.delete(0,END)
        upperField.insert(0,added)
        field.delete(0,END)
        upperAns.insert(0,"ANS=")
        a=float(first_num)
        b=float(ss)
        c=float(added)
        if a < 0 or b < 0 or c < 0:
            memory.append(f'({first_num})+({ss})=({added})')
        else:
            memory.append(f'{first_num}+{ss}={added}')

 #=====SUBTRACTION=====#
    if operator==2:
        ss=field.get()
        field.delete(0,END)
        first_num = upperField.get()
        added=float(upperField.get())-float(ss)
        upperField.delete(0,END)
        upperField.insert(0,added)
        field.delete(0,END)
        upperAns.insert(0,"ANS=")
        a=float(first_num)
        b=float(ss)
        c=float(added)
        if a < 0 or b < 0 or c < 0:
            memory.append(f'({first_num})-({ss})=({added})')
        else:
            memory.append(f'{first_num}-{ss}={added}')
    
 #=====MULTIPLICATION=====#
    if operator==3:
        ss=field.get()
        field.delete(0,END)
        first_num = upperField.get()
        added=float(upperField.get())*float(ss)
        upperField.delete(0,END)
        upperField.insert(0,added)
        field.delete(0,END)
        upperAns.insert(0,"ANS=")
        a=float(first_num)
        b=float(ss)
        c=float(added)
        if a < 0 or b < 0 or c < 0:
            memory.append(f'({first_num})x({ss})=({added})')
        else:
            memory.append(f'{first_num}x{ss}={added}')

 #=====DIVISION=====#
    if operator==4:
        ss=field.get()
        field.delete(0,END)
        first_num = upperField.get()
        added=float(upperField.get())/float(ss)
        upperField.delete(0,END)
        upperField.insert(0,added)
        field.delete(0,END)
        upperAns.insert(0,"ANS=")
        a=float(first_num)
        b=float(ss)
        c=float(added)
        if a < 0 or b < 0 or c < 0:
            memory.append(f'({first_num})/({ss})=({added})')
        else:
            memory.append(f'{first_num}/{ss}={added}')

 #=====SQUARE_ROOT=====#
    if operator==5:
        ss=field.get()
        field.delete(0,END)
        uf = upperField.get()
        added=math.sqrt(float(uf))
        upperField.delete(0,END)
        upperField.insert(0, added)
        field.delete(0,END)
        upperAns.delete(0, END)
        upperAns.insert(0,"√" + uf)
        memory.append(f'sqrt({uf})={added}')

 #=====POWER=====#
    if operator==6:
        try:
            power=field.get()
            field.delete(0,END)
            number=str(upperField.get())
            added=float(upperField.get())**float(power)
            upperField.delete(0,END)
            upperField.insert(0,added)
            upperField.insert(0, field.get())
            upperAns.insert(0, number + "^" + power + "=")
            memory.append(f'{number}^{power}={added}')
        except:
            field.delete(0,END)
            upperField.delete(0, END)
            upperField.insert(0, "OVERFLOW!!")
    if dPad == 1:
        equals.config(relief=SUNKEN)
        equals.after(58, lambda: equals.config(relief=RAISED))
    if Pad == 1:
        Stequals.config(relief=SUNKEN)
        Stequals.after(58, lambda: Stequals.config(relief=RAISED))
    if sPad == 1:
        Sequals.config(relief=SUNKEN)
        Sequals.after(58, lambda: Sequals.config(relief=RAISED))
  except:
     pass

#=============================CLEAR_BUTTONS================================

def CEd():
 if Pad == 1 or dPad == 1 or sPad == 1:
  global counter
  if counter ==1:
    HentryPad.destroy()
    counter = 0
  else:
    field.delete(0,END)
  if dPad == 1:
    Clear2.config(relief=SUNKEN)
    Clear2.after(58, lambda: Clear2.config(relief=RAISED)) 
  if Pad == 1:
    StCE.config(relief=SUNKEN)
    StCE.after(58, lambda: StCE.config(relief=RAISED))
  if sPad == 1:
        SCE.config(relief=SUNKEN)
        SCE.after(58, lambda: SCE.config(relief=RAISED))
 elif wPad == 1:
     entry1.delete(0, END)
     entry2.delete(0, END)
 elif tPad == 1:
     Tentry1.delete(0, END)
     Tentry2.delete(0, END)

def Cd():
 if Pad == 1 or dPad == 1 or sPad == 1:
  global counter
  if counter ==1:
    HentryPad.destroy()
    counter = 0
  else:
    field.delete(0,END)
    upperField.delete(0,END)
    upperAns.delete(0,END)
  if dPad == 1:
    Clear1.config(relief=SUNKEN)
    Clear1.after(58, lambda: Clear1.config(relief=RAISED))
  if Pad == 1:
    StC.config(relief=SUNKEN)
    StC.after(58, lambda: StC.config(relief=RAISED))
  if sPad == 1:
        SC.config(relief=SUNKEN)
        SC.after(58, lambda: SC.config(relief=RAISED))
 elif wPad == 1:
      entry1.delete(0, END)
      entry2.delete(0, END)
      WC.config(relief=SUNKEN)
      WC.after(58, lambda: WC.config(relief=RAISED))
 elif tPad == 1:
      Tentry1.delete(0, END)
      Tentry2.delete(0, END)
      TC.config(relief=SUNKEN)
      TC.after(58, lambda: TC.config(relief=RAISED))

#/Brrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr

#===========================Memory_management=========================

def pop():
    global counter
    memory.clear()
    if counter == 1:
        HentryPad.destroy()
        counter=0

def fHistory():
    root=tk.Tk()
    root.title("History")
    root.iconbitmap('ICON\calc.ico')
    def Fpop():
        global counter
        memory.clear()
        if counter == 1:
            HentryPad.destroy()
            root.destroy()
            counter=0
    def destroy():
        root.destroy()
    root.geometry("500x500")
    r = tk.Frame(root, bg="#262626")
    r.place(relwidth=1, relheight=1)
    w = tk.Label(r, text ='FULL HISTORY ',font = "bangers 50", bg="#262626", fg="cyan") 
    w.pack()
    e = tk.Label(r, text="Complete Calculations for easy view", bg="#262626", fg="cyan",)
    e.pack()
    close = tk.Button(r, text="Close", command=destroy, bg="#262626", fg="red",activeforeground="black", activebackground="red")
    close.place(relheight=0.1, relwidth=0.1, relx=0.9)
    Clear = tk.Button(r, text="C L E A R", command=Fpop, bg="#262626", fg="cyan", padx=250, activebackground="#262629", activeforeground="red")
    Clear.pack()
    scroll_bar = tk.Scrollbar(r,)
    scroll_bar.pack( side = RIGHT,fill = Y )
    mylist = tk.Listbox(r, yscrollcommand = scroll_bar.set, bg="#262626", fg="white")
    mylist.pack(side="left",fill="both",expand=True)
    if len(memory) == 0:
            l = tk.Label(mylist, text="There is no\nhistory yet", bg="#262626", fg="red", font="SFprodisplay 13")
            l.place(relheight=1, relwidth=1)
    elif len(memory) > 0:
            for meme in reversed(memory):
                    mylist.insert(END,meme)
    scroll_bar.config( command = mylist.yview )
    root.mainloop()

#===========================COPY_PASTE_BUTTONS========================

def copyf():
    window.clipboard_clear()
    window.clipboard_append(field.get())

def pastef():
    field.delete(0, END)
    field.insert(0, window.clipboard_get())

def copyuf():
    window.clipboard_clear()
    window.clipboard_append(upperField.get())

def duffy():
    url='https://youtube.com/duffyyt'
    webbrowser.open(url)

#======================Keyboard===========================

keyboard.on_press_key("1", lambda _:num_1s())
keyboard.on_press_key("2", lambda _:num_2s())
keyboard.on_press_key("3", lambda _:num_3s())
keyboard.on_press_key("4", lambda _:num_4s())
keyboard.on_press_key("5", lambda _:num_5s())
keyboard.add_hotkey("6", lambda  :num_6s())
keyboard.on_press_key("7", lambda _:num_7s())
keyboard.add_hotkey("8", lambda :num_8s())
keyboard.on_press_key("9", lambda _:num_9s())
keyboard.on_press_key("0", lambda _:num_0s())

keyboard.on_press_key(".", lambda _:Decimals())
keyboard.add_hotkey('shift + -', lambda: negatives())

keyboard.add_hotkey("=", lambda:Equalss())
keyboard.on_press_key("Enter", lambda _:Equalss())

keyboard.add_hotkey('shift + =', lambda: Adds())
keyboard.add_hotkey('-', lambda: Subtracts())
keyboard.add_hotkey('shift + 8', lambda: Multiplys())
keyboard.add_hotkey('/', lambda: Divides())
keyboard.add_hotkey('shift + 6', lambda: sqrs())
keyboard.on_press_key('q', lambda _: sqrts())

keyboard.add_hotkey("ctrl + backspace", lambda :CEd())
keyboard.on_press_key("esc", lambda _:Cd())
keyboard.on_press_key("backspace", lambda _:back())

keyboard.on_press_key("f1", lambda _:duffy())

#============================MAIN_WINDOW==============================

window = tk.Tk()
window.title("Calculator")
window.iconbitmap('resource\icon\calc1.ico')
window.minsize(400,500)
window.maxsize(400,500)
background = tk.PhotoImage(file="resource/background/background.png")
mainFrame = tk.Label(window, bg="black", image=background)#frame(MAIN)
mainFrame.place(relheight=1, relwidth=1)

#==========================IMAGES=======================

settingsImg = Image.open('resource/UI_icons/gear.png')
resizedImg = settingsImg.resize((40,41), Image.ADAPTIVE)
newpic = ImageTk.PhotoImage(resizedImg)#FINAL

toggle_on = Image.open("resource/switches\on.png")
toggle_on_resize = toggle_on.resize((35,17), Image.ANTIALIAS)
toggle_on_new = ImageTk.PhotoImage(toggle_on_resize)#FINAL

toggle_off = Image.open("resource/switches/off.png")
toggle_off_resize = toggle_off.resize((35,17), Image.ANTIALIAS)
toggle_off_new = ImageTk.PhotoImage(toggle_off_resize)#FINAL

#=========================ENTRY_FIELDS=================================[Using EntryBox module]

# MAIN_FIELD #
field = Entry(window, bg="black", fg="white", border=0, font="calibri 22", justify=RIGHT, cursor='arrow')
field.place(relheight=0.25, relwidth=0.98, relx=0.01, rely=0.01)

# SECONDARY_FIELD #
upperField = Entry(field,bg="black", fg="white", borderwidth=0, border=0, font="calibri 10",justify=RIGHT, cursor='arrow')
upperField.place(relheight=0.2, relwidth=1,)

# ANSWER_FIELD #
upperAns = Entry(upperField,bg="black", fg="white", borderwidth=0, border=0, font="calibri 10", cursor='arrow')
upperAns.place(relheight=1, relx=0.06)

# OPERATOR_FIELD #
upperOperator = OPEntry(upperField,bg="#353340", fg="cyan", borderwidth=0.01, border=1, font="calibri 10", cursor='arrow')
upperOperator.place(relheight=1, relwidth=0.06,)

#=======================COPY_PASTE======================

Fcopy = tk.Button(field, bg="#353340", fg="cyan", text="Copy", command=copyf,activebackground="black", activeforeground="white", cursor='arrow')
Fcopy.place(relheight=0.2, relwidth=0.1, rely=0.8, relx=0.8)

Fpaste = tk.Button(field, bg="#353340", fg="cyan", text="Paste", command=pastef,activebackground="black", activeforeground="white", cursor='arrow')
Fpaste.place(relheight=0.2, relwidth=0.1, rely=0.8, relx=0.9)

UFcopy = tk.Button(field, bg="#353340", fg="cyan", text="Copy", command=copyuf,activebackground="black", activeforeground="white", cursor='arrow')
UFcopy.place(relheight=0.2, relwidth=0.1, rely=0.15, relx=0.9)

#============================MENU==================================
                                                                              
menu = tk.LabelFrame(window, bg="#636D73")                                         
menu.place(relheight=0.062, relwidth=0.98, relx=0.01, rely=0.27)                                                   
                                                                                 
#=============================ENTRY_PAD================================

entryPad = tk.LabelFrame(window, bg="black",)
entryPad.place(relheight=0.65, relwidth=0.98, relx=0.01, rely=0.34)

#===========================NUMBER_BUTTONS====================================

# 1 #
num1 = tk.Button(entryPad, bg="black", fg = "white", text="1",command=num_1, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0,)
num1.place(relwidth=0.14, relheight=0.14, relx=0.005, rely=0.005)

# 2 #
num2 = tk.Button(entryPad, bg="black", fg = "white", text="2",command=num_2, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0,)
num2.place(relwidth=0.14, relheight=0.14, relx=0.15, rely=0.005)

# 3 #
num3 = tk.Button(entryPad, bg="black", fg = "white", text="3",command=num_3, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0,)
num3.place(relwidth=0.14, relheight=0.14, relx=0.295, rely=0.005)

# 4 #
num4 = tk.Button(entryPad, bg="black", fg = "white", text="4",command=num_4, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0,)
num4.place(relheight=0.14, relwidth=0.14, relx=0.005, rely=0.15)

# 5 #
num5 = tk.Button(entryPad, bg="black", fg = "white", text="5",command=num_5, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0,)
num5.place(relheight=0.14, relwidth=0.14, relx=0.15, rely=0.15)

# 6 #
num6 = tk.Button(entryPad, bg="black", fg = "white", text="6",command=num_6, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0,)
num6.place(relheight=0.14, relwidth=0.14, relx=0.295, rely=0.15)

# 7 #
num7 = tk.Button(entryPad, bg="black", fg = "white", text="7",command=num_7, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0,)
num7.place(relheight=0.14, relwidth=0.14, relx=0.005, rely=0.295)

# 8 #
num8 = tk.Button(entryPad, bg="black", fg = "white", text="8",command=num_8, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0,)
num8.place(relheight=0.14, relwidth=0.14, relx=0.15, rely=0.295)

# 9 #
num9 = tk.Button(entryPad, bg="black", fg = "white", text="9",command=num_9, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0,)
num9.place(relheight=0.14, relwidth=0.14, relx=0.295, rely=0.295)

# 0 #
num0 = tk.Button(entryPad, bg="black", fg = "white", text="0",command=num_0, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0,)
num0.place(relheight=0.14, relwidth=0.14, relx=0.15, rely=0.44)

# - #
Negative = tk.Button(entryPad, bg="#262626", fg = "cyan", text="-",  command=negative, activeforeground="white", activebackground="black",border=0,borderwidth=0,)
Negative.place(relheight=0.14, relwidth=0.14, relx=0.005, rely=0.44)

# . #
decimal = tk.Button(entryPad, bg="#262626", fg = "cyan", text=".",command=Decimal, activeforeground="white", activebackground="black",border=0,borderwidth=0,)
decimal.place(relheight=0.14, relwidth=0.14, relx=0.295, rely=0.44)

#========================OPERATOR_BUTTONS===========================

# + #
add = tk.Button(entryPad, bg="#5D8AA6", text="+", padx=19.48, pady=10, command=Add, activebackground="#5D8AA6",border=0,borderwidth=0,)
add.place(relheight=0.14, relwidth=0.14, relx=0.44, rely=0.005)

# - #
subtract = tk.Button(entryPad, bg="#5D8AA6", text="-", padx=19.48, pady=10, command=Subtract, activebackground="#5D8AA6",border=0,borderwidth=0,)
subtract.place(relheight=0.14, relwidth=0.14, relx=0.585, rely=0.005)

# * #
multiply = tk.Button(entryPad, bg="#5D8AA6", text="x", padx=20, pady=10, command=Multiply, activebackground="#5D8AA6",border=0,borderwidth=0,)
multiply.place(relheight=0.14, relwidth=0.14, relx=0.44, rely=0.15)

# / #
divide = tk.Button(entryPad, bg="#5D8AA6", text="/", padx=19.48, pady=10, command=Divide, activebackground="#5D8AA6",border=0,borderwidth=0,)
divide.place(relheight=0.14, relwidth=0.14, relx=0.585, rely=0.15)

# = #
equals = tk.Button(entryPad, bg="#D7D7D9", text="=", padx=46, pady=10, command=Equals, activebackground="#D7D7D9",border=0,borderwidth=0,)
equals.place(relheight=0.14, relwidth=0.285, relx=0.44, rely=0.295)

# √ #
Sqrt = tk.Button(entryPad, bg="#5D8AA6", text="√", padx=19.48, pady=10, command=sqrt, activebackground="#5D8AA6",border=0,borderwidth=0,)
Sqrt.place(relheight=0.14, relwidth=0.14, relx=0.44, rely=0.44)

# ^ #
Sqr = tk.Button(entryPad, bg="#5D8AA6", text="^", padx=17, pady=10, command=sqr, activebackground="#5D8AA6",border=0,borderwidth=0,)
Sqr.place(relheight=0.14, relwidth=0.14, relx=0.585, rely=0.44)

#=========================CLEAR_BUTTONS=======================

# COMPLETE_CLEAR #
Clear1 = tk.Button(entryPad, bg="#fc8700", text="C", padx=43.2, pady=33, command=C, activebackground="black", activeforeground="#fc8700",border=0,borderwidth=0,)
Clear1.place(relheight=0.285, relwidth=0.27, relx=0.73, rely=0.005)

# MAIN_FIELD_CLEAR #
Clear2 = tk.Button(entryPad, bg="#fc8700", text="CE", padx=40, pady=10, command=CE, activebackground="black", activeforeground="#fc8700",border=0,borderwidth=0,)
Clear2.place(relheight=0.14, relwidth=0.27, relx=0.73, rely=0.295)

# EXIT BUTTONS #
Clear3 = tk.Button(entryPad, bg="#F24607", text="AC", padx=39.15, pady=10, command=AC, activebackground="black", activeforeground="#F24607",border=0,borderwidth=0,)
Clear3.place(relheight=0.14, relwidth=0.27, relx=0.73, rely=0.44)

settings1 = tk.Button(entryPad, bg="black", relief=FLAT, activebackground="black", image=newpic, border=0, borderwidth=0, command=setting1)
settings1.place(relwidth=0.1, relheight=0.1, relx = 0.01, rely=0.89)

#=========================MENU_FUNCTIONS===================

#STANDARD#
def standard():
 settings["padd"] = 'Stentrypad'
 global sCounter
 sCounter = 0
 global dPad
 global Pad
 global sPad
 global wPad
 global tPad
 if dPad == 1:
     entryPad.destroy()
     print("dele")
 if sPad == 1:
     SentryPad.destroy()
     print("scientific is destroyed")
 if wPad == 1:
     WentryPad.destroy()
     print("Weights is destroyed")
 if tPad == 1:
     TentryPad.destroy()
     print("Time is destroyed")
 global StentryPad
 global settings2
 global Stnum1
 global Stnum2
 global Stnum3
 global Stnum4
 global Stnum5
 global Stnum6
 global Stnum7
 global Stnum8
 global Stnum9
 global Stnum0
 global Stdecimal
 global StNegative
 global Stadd
 global Stsubtract
 global Stmultiply
 global Stdivide
 global StC
 global StCE
 global Stequals
 global StSqr
 global StSqrt
 global StC
 global StCE
 global StAC
 
 if Pad == 0:
    dPad = 0
    Pad = 1
    sPad = 0
    wPad = 0
    tPad = 0

    def ACSt():
        window.destroy()

    def CESt():
        field.delete(0,END)

    def CSt():
        field.delete(0,END)
        upperAns.delete(0,END)
        upperField.delete(0, END)


    StentryPad = tk.LabelFrame(window, bg="black")
    StentryPad.place(relheight=0.65, relwidth=0.98, relx=0.01, rely=0.34)

    # 1 #
    Stnum1 = tk.Button(StentryPad, bg="black", fg = "white", text="1", pady=10, padx=20,command=num_1, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0)
    Stnum1.place(relwidth=0.14, relheight=0.14, relx=0.005, rely=0.005)

    # 2 #
    Stnum2 = tk.Button(StentryPad, bg="black", fg = "white", text="2", pady=10, padx=20,command=num_2, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0)
    Stnum2.place(relwidth=0.14, relheight=0.14, relx=0.15, rely=0.005)

    # 3 #
    Stnum3 = tk.Button(StentryPad, bg="black", fg = "white", text="3", pady=10, padx=20,command=num_3, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0)
    Stnum3.place(relwidth=0.14, relheight=0.14, relx=0.295, rely=0.005)

    # 4 #
    Stnum4 = tk.Button(StentryPad, bg="black", fg = "white", text="4", pady=10, padx=20,command=num_4, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0)
    Stnum4.place(relheight=0.14, relwidth=0.14, relx=0.005, rely=0.15)

    # 5 #
    Stnum5 = tk.Button(StentryPad, bg="black", fg = "white", text="5", pady=10, padx=20,command=num_5, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0)
    Stnum5.place(relheight=0.14, relwidth=0.14, relx=0.15, rely=0.15)

    # 6 #
    Stnum6 = tk.Button(StentryPad, bg="black", fg = "white", text="6", pady=10, padx=20,command=num_6, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0)
    Stnum6.place(relheight=0.14, relwidth=0.14, relx=0.295, rely=0.15)

    # 7 #
    Stnum7 = tk.Button(StentryPad, bg="black", fg = "white", text="7", pady=10, padx=20,command=num_7, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0)
    Stnum7.place(relheight=0.14, relwidth=0.14, relx=0.005, rely=0.295)

    # 8 #
    Stnum8 = tk.Button(StentryPad, bg="black", fg = "white", text="8", pady=10, padx=20,command=num_8, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0)
    Stnum8.place(relheight=0.14, relwidth=0.14, relx=0.15, rely=0.295)

    # 9 #
    Stnum9 = tk.Button(StentryPad, bg="black", fg = "white", text="9", pady=10, padx=20,command=num_9, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0)
    Stnum9.place(relheight=0.14, relwidth=0.14, relx=0.295, rely=0.295)

    # 0 #
    Stnum0 = tk.Button(StentryPad, bg="black", fg = "white", text="0", pady=10, padx=20,command=num_0, activebackground="#262626", activeforeground="cyan",border=0,borderwidth=0)
    Stnum0.place(relheight=0.14, relwidth=0.14, relx=0.15, rely=0.44)

    # - #
    StNegative = tk.Button(StentryPad, bg="#262626", fg = "cyan", text="-", pady=10, padx=20,command=negative, activeforeground="white", activebackground="black",border=0,borderwidth=0)
    StNegative.place(relheight=0.14, relwidth=0.14, relx=0.005, rely=0.44)

    # . #
    Stdecimal = tk.Button(StentryPad, bg="#262626", fg = "cyan", text=".", pady=10, padx=21.499999999999998222,command=Decimal, activeforeground="white", activebackground="black",border=0,borderwidth=0)
    Stdecimal.place(relheight=0.14, relwidth=0.14, relx=0.295, rely=0.44)

    #========================OPERATOR_BUTTONS===========================

    # + #
    Stadd = tk.Button(StentryPad, bg="#5D8AA6", text="+", padx=19.48, pady=10, command=Add, activebackground="#5D8AA6",border=0,borderwidth=0)
    Stadd.place(relheight=0.14, relwidth=0.14, relx=0.44, rely=0.005)

    # - #
    Stsubtract = tk.Button(StentryPad, bg="#5D8AA6", text="-", padx=19.48, pady=10, command=Subtract, activebackground="#5D8AA6",border=0,borderwidth=0)
    Stsubtract.place(relheight=0.14, relwidth=0.14, relx=0.585, rely=0.005)

    # * #
    Stmultiply = tk.Button(StentryPad, bg="#5D8AA6", text="x", padx=20, pady=10, command=Multiply, activebackground="#5D8AA6",border=0,borderwidth=0)
    Stmultiply.place(relheight=0.14, relwidth=0.14, relx=0.44, rely=0.15)

    # / #
    Stdivide = tk.Button(StentryPad, bg="#5D8AA6", text="/", padx=19.48, pady=10, command=Divide, activebackground="#5D8AA6",border=0,borderwidth=0)
    Stdivide.place(relheight=0.14, relwidth=0.14, relx=0.585, rely=0.15)

    # = #
    Stequals = tk.Button(StentryPad, bg="#3CA6E5", text="=", padx=46, pady=10, command=Equals, activebackground="#D7D7D9",border=0,borderwidth=0)
    Stequals.place(relheight=0.14, relwidth=0.285, relx=0.44, rely=0.295)

    # √ #
    StSqrt = tk.Button(StentryPad, bg="#5D8AA6", text="√", padx=19.48, pady=10, command=sqrt, activebackground="#5D8AA6",border=0,borderwidth=0)
    StSqrt.place(relheight=0.14, relwidth=0.14, relx=0.44, rely=0.44)

    # ^ #
    StSqr = tk.Button(StentryPad, bg="#5D8AA6", text="^", padx=17, pady=10, command=sqr, activebackground="#5D8AA6",border=0,borderwidth=0)
    StSqr.place(relheight=0.14, relwidth=0.14, relx=0.585, rely=0.44)

    #=========================CLEAR_BUTTONS=======================

    # COMPLETE_CLEAR #
    StC = tk.Button(StentryPad, bg="#fc8700", text="C", padx=43.2, pady=33, command=CSt, activebackground="black", activeforeground="#fc8700",border=0,borderwidth=0)
    StC.place(relheight=0.285, relwidth=0.27, relx=0.73, rely=0.005)

    # MAIN_FIELD_CLEAR #
    StCE = tk.Button(StentryPad, bg="#fc8700", text="CE", padx=40, pady=10, command=CESt, activebackground="black", activeforeground="#fc8700",border=0,borderwidth=0)
    StCE.place(relheight=0.14, relwidth=0.27, relx=0.73, rely=0.295)

    # EXIT BUTTONS #
    StAC = tk.Button(StentryPad, bg="#F24607", text="AC", padx=39.15, pady=10, command=ACSt, activebackground="black", activeforeground="#F24607",border=0,borderwidth=0)
    StAC.place(relheight=0.14, relwidth=0.27, relx=0.73, rely=0.44)

    if mainthm == 'Light' and mainui == 'default':
        Lsetting( Stnum1,Stnum2,Stnum3,Stnum4,Stnum5,Stnum6,Stnum7,Stnum8,Stnum9,Stnum0,Stdecimal,StNegative,StC,StCE,StAC)

    settings2 = tk.Button(StentryPad, bg="black", relief='flat', image=newpic, border=0, borderwidth=0, activebackground="black",command=setting2)
    settings2.place(relwidth=0.1, relheight=0.1, relx = 0.01, rely=0.89)
 else:
     print("already there")

#SCIENTIFIC#
def scientific():
 settings["padd"] = 'Sentrypad'
 global sCounter
 sCounter = 0
 global SentryPad
 global settings3
 global Snum1
 global Snum2
 global Snum3
 global Snum4
 global Snum5
 global Snum6
 global Snum7
 global Snum8
 global Snum9
 global Snum0
 global Sadd
 global Ssubtract
 global Smultiply
 global Sdivide
 global SSqr
 global SSqrt
 global SNegative
 global Sdecimal
 global SCE
 global SC
 global SAC
 global Sequals
 global dPad
 global Pad
 global sPad
 global wPad
 global tPad
 if dPad == 1:
     entryPad.destroy()
     print("dele")
 if Pad == 1:
     StentryPad.destroy()
     print(" Standard is destroyed")
 if wPad == 1:
     WentryPad.destroy()
     print("Weights is destroyed")
 if tPad == 1:
     TentryPad.destroy()
     print("Time is destroyed")
 if sPad ==0:
    dPad = 0
    Pad = 0
    sPad = 1
    wPad = 0
    tPad = 0
    global trig
    trig = 'rad'

    def Rad():
        try:
            global trig
            deg.config(fg="gray")
            rad.config(fg="black")
            trig = 'rad'       
        except:
            pass

    def Deg():
     try:
        global trig
        rad.config(fg="gray")
        deg.config(fg="black")
        trig = 'deg'
     except:
         pass

    def trigChoose():
        if trig == 'rad':
            Deg()
        else:
            Rad()
    
    def ACS():
        window.destroy()

    def CES():
        field.delete(0,END)

    def CS():
        field.delete(0,END)
        upperAns.delete(0,END)
        upperField.delete(0, END)

    def Sin():
     try:
        if trig == 'rad':
            x=float(field.get())
            siner = math.sin(x)
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"sin" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'sin({x})={siner}rad')
        if trig == 'deg':
            x=float(field.get())
            siner = math.sin(math.radians(x))
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"sin" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'sin({x})={siner}deg')
     except:
         pass

    def Cos():
     try:
        if trig == 'rad':
            x=float(field.get())
            siner = math.cos(x)
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"cos" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'cos({x})={siner}rad')
        if trig == 'deg':
            x=float(field.get())
            siner = math.cos(math.radians(x))
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"cos" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'cos({x})={siner}deg')
     except:
         pass

    def Tan():
     try:
        if trig == 'rad':
            x=float(field.get())
            siner = math.tan(x)
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"tan" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'tan({x})={siner}rad')
        if trig == 'deg':
            x=float(field.get())
            siner = math.tan(math.radians(x))
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"tan" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'tan({x})={siner}deg')
     except:
         pass

    def Csc():
     try:
        if trig == 'rad':
            x=float(field.get())
            c_siner = math.sin(x)
            siner = 1/c_siner
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"Csc" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'csc({x})={siner}rad')
        if trig == 'deg':
            x=float(field.get())
            c_siner = math.sin(math.radians(x))
            siner = 1/c_siner
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"Csc" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'csc({x})={siner}deg')
     except:
         pass

    def Sec():
     try:
        if trig == 'rad':
            x=float(field.get())
            c_siner = math.cos(x)
            siner = 1/c_siner
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"Sec" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'sec({x})={siner}rad')
        if trig == 'deg':
            x=float(field.get())
            c_siner = math.cos(math.radians(x))
            siner = 1/c_siner
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"sec" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'sec({x})={siner}deg')
     except:
         pass

    def Cot():
     try:
        if trig == 'rad':
            x=float(field.get())
            c_siner = math.tan(x)
            siner = 1/c_siner
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"Cot" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'cot({x})={siner}rad')
        if trig == 'deg':
            x=float(field.get())
            c_siner = math.tan(math.radians(x))
            siner = 1/c_siner
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner  )
            upperAns.delete(0, END),
            upperAns.insert(0,"Cot" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'cot({x})={siner}deg')
     except:
         pass
    
    def Pi():
     try:
        field.delete(0, END)
        field.insert(0, 2384626433832795)
        field.insert(0, 3.141592653589793)
     except:
         pass

 #Brrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
    
    def SSin():
     try:
        if trig == 'rad':
            x=float(field.get())
            siner = math.sin(x)
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"sin" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            sin.config(relief=SUNKEN)
            sin.after(58, lambda: sin.config(relief=RAISED))
            memory.append(f'sin({x})={siner}rad')
        if trig == 'deg':
            x=float(field.get())
            siner = math.sin(math.radians(x))
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"sin" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'sin({x})={siner}deg')
            sin.config(relief=SUNKEN)
            sin.after(58, lambda: sin.config(relief=RAISED))
     except:
         pass

    def SCos():
     try:
        if trig == 'rad':
            x=float(field.get())
            siner = math.cos(x)
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"cos" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'cos({x})={siner}rad')
            cos.config(relief=SUNKEN)
            cos.after(58, lambda: cos.config(relief=RAISED))
        if trig == 'deg':
            x=float(field.get())
            siner = math.cos(math.radians(x))
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"cos" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'cos({x})={siner}deg')
            cos.config(relief=SUNKEN)
            cos.after(58, lambda: cos.config(relief=RAISED))
     except:
         pass

    def STan():
     try:
        if trig == 'rad':
            x=float(field.get())
            siner = math.tan(x)
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"tan" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'tan({x})={siner}rad')
            tan.config(relief=SUNKEN)
            tan.after(58, lambda: tan.config(relief=RAISED))
        if trig == 'deg':
            x=float(field.get())
            siner = math.tan(math.radians(x))
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"tan" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'tan({x})={siner}deg')
            tan.config(relief=SUNKEN)
            tan.after(58, lambda: tan.config(relief=RAISED))
     except:
         pass

    def SCsc():
     try:
        if trig == 'rad':
            x=float(field.get())
            c_siner = math.sin(x)
            siner = 1/c_siner
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"Csc" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'csc({x})={siner}rad')
            csc.config(relief=SUNKEN)
            csc.after(58, lambda: csc.config(relief=RAISED))
        if trig == 'deg':
            x=float(field.get())
            c_siner = math.sin(math.radians(x))
            siner = 1/c_siner
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"Csc" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'csc({x})={siner}deg')
            csc.config(relief=SUNKEN)
            csc.after(58, lambda: csc.config(relief=RAISED))
     except:
         pass

    def SSec():
     try:
        if trig == 'rad':
            x=float(field.get())
            c_siner = math.cos(x)
            siner = 1/c_siner
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"Sec" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'sec({x})={siner}rad')
            sec.config(relief=SUNKEN)
            sec.after(58, lambda: sec.config(relief=RAISED))
        if trig == 'deg':
            x=float(field.get())
            c_siner = math.cos(math.radians(x))
            siner = 1/c_siner
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"sec" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'sec({x})={siner}deg')
            sec.config(relief=SUNKEN)
            sec.after(58, lambda: sec.config(relief=RAISED))
     except:
         pass

    def SCot():
     try:
        if trig == 'rad':
            x=float(field.get())
            c_siner = math.tan(x)
            siner = 1/c_siner
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"Cot" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'cot({x})={siner}rad')
            cot.config(relief=SUNKEN)
            cot.after(58, lambda: cot.config(relief=RAISED))
        if trig == 'deg':
            x=float(field.get())
            c_siner = math.tan(math.radians(x))
            siner = 1/c_siner
            field.after(3, lambda:field.delete(0, END))
            upperField.delete(0, END)
            upperField.insert(0, siner  )
            upperAns.delete(0, END),
            upperAns.insert(0,"Cot" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
            memory.append(f'cot({x})={siner}deg')
            cot.config(relief=SUNKEN)
            cot.after(58, lambda: cot.config(relief=RAISED))
     except:
         pass
    
    def SPi():
     try:
        field.delete(0, END)
        field.insert(0, 2384626433832795)
        field.insert(0, 3.141592653589793)
        pi.config(relief=SUNKEN)
        pi.after(58, lambda: pi.config(relief=RAISED))
     except:
         pass

    keyboard.on_press_key("s", lambda _:SSin())
    keyboard.on_press_key("o", lambda _:SCos())
    keyboard.on_press_key("t", lambda _:STan())
    #========================================#
    keyboard.on_press_key("i", lambda _:SCsc())
    keyboard.on_press_key("u", lambda _:SSec())
    keyboard.on_press_key("j", lambda _:SCot())
    #========================================#
    keyboard.on_press_key("p", lambda _:SPi())
    #========================================#
    keyboard.on_press_key("space", lambda _:trigChoose())

    SentryPad = tk.LabelFrame(window, bg="black")
    SentryPad.place(relheight=0.65, relwidth=0.98, relx=0.01, rely=0.34)
    # 1 #
    Snum1 = tk.Button(SentryPad, bg="black", fg="white", text="1",command=num_1, activebackground="#262626", activeforeground="cyan")
    Snum1.place(relheight=0.14,relwidth=0.14,relx=0.005,rely=0.15)

    # 2 #
    Snum2 = tk.Button(SentryPad, bg="black", fg="white", text="2",command=num_2, activebackground="#262626", activeforeground="cyan")
    Snum2.place(relheight=0.14,relwidth=0.14,relx=0.15,rely=0.15)

    # 3 #
    Snum3 = tk.Button(SentryPad, bg="black", fg="white", text="3",command=num_3, activebackground="#262626", activeforeground="cyan")
    Snum3.place(relheight=0.14,relwidth=0.14,relx=0.295,rely=0.15)

    # 4 #
    Snum4 = tk.Button(SentryPad, bg="black", fg="white", text="4",command=num_4, activebackground="#262626", activeforeground="cyan")
    Snum4.place(relheight=0.14,relwidth=0.14,relx=0.005,rely=0.295)

    # 5 #
    Snum5 = tk.Button(SentryPad, bg="black", fg="white", text="5",command=num_5, activebackground="#262626", activeforeground="cyan")
    Snum5.place(relheight=0.14,relwidth=0.14,relx=0.15,rely=0.295)

    # 6 #
    Snum6 = tk.Button(SentryPad, bg="black", fg="white", text="6",command=num_6, activebackground="#262626", activeforeground="cyan")
    Snum6.place(relheight=0.14,relwidth=0.14,relx=0.295,rely=0.295)

    # 7 #
    Snum7 = tk.Button(SentryPad, bg="black", fg="white", text="7",command=num_7, activebackground="#262626", activeforeground="cyan")
    Snum7.place(relheight=0.14,relwidth=0.14,relx=0.005,rely=0.44)

    # 8 #
    Snum8 = tk.Button(SentryPad, bg="black", fg="white", text="8",command=num_8, activebackground="#262626", activeforeground="cyan")
    Snum8.place(relheight=0.14,relwidth=0.14,relx=0.15,rely=0.44)
    # 9 #
    Snum9 = tk.Button(SentryPad, bg="black", fg="white", text="9",command=num_9, activebackground="#262626", activeforeground="cyan")
    Snum9.place(relheight=0.14,relwidth=0.14,relx=0.295,rely=0.44)

    # 0 #
    Snum0 = tk.Button(SentryPad, bg="black", fg="white", text="0",command=num_0, activebackground="#262626", activeforeground="cyan")
    Snum0.place(relheight=0.14,relwidth=0.14,relx=0.15,rely=0.585)

    # - #
    SNegative = tk.Button(SentryPad, bg="#262626", fg="cyan", text="-",command=negative, activebackground="black", activeforeground="white")
    SNegative.place(relheight=0.14,relwidth=0.14,relx=0.005,rely=0.585)

    # . #
    Sdecimal = tk.Button(SentryPad, bg="#262626", fg="cyan", text=".",command=Decimal, activebackground="black", activeforeground="white")
    Sdecimal.place(relheight=0.14,relwidth=0.14,relx=0.295,rely=0.585)

    #========================OPERATOR_BUTTONS===========================

    # + #
    Sadd = tk.Button(SentryPad, bg="#5D8AA6", text="+", command=Add, activebackground="#5D8AA6")
    Sadd.place(relheight=0.14,relwidth=0.14,relx=0.44,rely=0.15)

    # - #
    Ssubtract = tk.Button(SentryPad, bg="#5D8AA6", text="-", command=Subtract, activebackground="#5D8AA6")
    Ssubtract.place(relheight=0.14,relwidth=0.14,relx=0.585,rely=0.15)

    # * #
    Smultiply = tk.Button(SentryPad, bg="#5D8AA6", text="x", command=Multiply, activebackground="#5D8AA6")
    Smultiply.place(relheight=0.14,relwidth=0.14,relx=0.44,rely=0.295)

    # / #
    Sdivide = tk.Button(SentryPad, bg="#5D8AA6", text="/", command=Divide, activebackground="#5D8AA6")
    Sdivide.place(relheight=0.14,relwidth=0.14,relx=0.585,rely=0.295)

    # = #
    Sequals = tk.Button(SentryPad, bg="#D7D7D9", text="=", command=Equals, activebackground="#D7D7D9")
    Sequals.place(relheight=0.14,relwidth=0.285,relx=0.44,rely=0.44)

    # √ #
    SSqrt = tk.Button(SentryPad, bg="#5D8AA6", text="√", command=sqrt,activebackground="#5D8AA6")
    SSqrt.place(relheight=0.14,relwidth=0.14,relx=0.44,rely=0.585)

    # ^ #
    SSqr = tk.Button(SentryPad, bg="#5D8AA6", text="^", command=sqr, activebackground="#5D8AA6")
    SSqr.place(relheight=0.14,relwidth=0.14,relx=0.585,rely=0.585)

    #========================TRIGNOMETRY========================

    #sin#
    sin = tk.Button(SentryPad, bg="#C6FC00", text="sin", command=Sin)
    sin.place(relheight=0.14,relwidth=0.14,relx=0.005,rely=0.005)

    #cos#
    cos = tk.Button(SentryPad, bg="#B3D600", text="cos", command=Cos)
    cos.place(relheight=0.14,relwidth=0.14,relx=0.15,rely=0.005)

    #tan#
    tan = tk.Button(SentryPad, bg="#8AB000", text="tan", command=Tan)
    tan.place(relheight=0.14,relwidth=0.14,relx=0.295,rely=0.005)

    #cosec#
    csc = tk.Button(SentryPad, bg="#C6FC00", text="csc", command=Csc)
    csc.place(relheight=0.14,relwidth=0.14,relx=0.44,rely=0.005)

    #secent#
    sec = tk.Button(SentryPad, bg="#B3D600", text="sec", command=Sec)
    sec.place(relheight=0.14,relwidth=0.14,relx=0.585,rely=0.005)

    #cotangent#
    cot = tk.Button(SentryPad, bg="#8AB000", text="cot", command=Cot)
    cot.place(relheight=0.14,relwidth=0.14,relx=0.73,rely=0.005)

    #PI#
    pi = tk.Button(SentryPad, bg="#9D69F0", text="π", command=Pi)
    pi.place(relheight=0.14,relwidth=0.125,relx=0.875,rely=0.005)

    #RADIAN#
    rad = tk.Button(SentryPad, bg="#d4ff00", text="RAD", command=Rad)
    rad.place(relheight=0.14,relwidth=0.14,relx=0.295,rely=0.73)

    #DEGREES#
    deg = tk.Button(SentryPad, bg="#d4ff00", text="DEG",command=Deg, fg="gray")
    deg.place(relheight=0.14,relwidth=0.14,relx=0.44,rely=0.73)

    #=========================CLEAR_BUTTONS=======================

    # COMPLETE_CLEAR #
    SC = tk.Button(SentryPad, bg="#fc8700", text="C", command=CS, activebackground="black", activeforeground="#fc8700")
    SC.place(relheight=0.285,relwidth=0.27,relx=0.73,rely=0.15)

    # MAIN_FIELD_CLEAR #
    SCE = tk.Button(SentryPad, bg="#fc8700", text="CE", command=CES, activebackground="black", activeforeground="#fc8700")
    SCE.place(relheight=0.14,relwidth=0.27,relx=0.73,rely=0.44)

    # EXIT BUTTONS #
    SAC= tk.Button(SentryPad, bg="#F24607", text="AC", command=ACS, activebackground="black", activeforeground="#F24607")
    SAC.place(relheight=0.14,relwidth=0.27,relx=0.73,rely=0.585)

    if theme == 'Light':
        Lsetting(Snum1,Snum2,Snum3,Snum4,Snum5,Snum6,Snum7,Snum8,Snum9,Snum0,Sdecimal,SNegative)

    settings3 = tk.Button(SentryPad, bg="black", relief='flat', image=newpic, border=0, borderwidth=0, activebackground="black",command=setting3)
    settings3.place(relwidth=0.1, relheight=0.1, relx = 0.01, rely=0.89)
 else:
     print("already there [s c i e n t i f i c]")

#WEIGHTS#
def weight():
 settings["padd"] = "Wentrypad"
 global sCounter
 sCounter = 0
 global settings4
 global WentryPad
 global Wnum1
 global Wnum2
 global Wnum3
 global Wnum4
 global Wnum5
 global Wnum6
 global Wnum7
 global Wnum8
 global Wnum9
 global Wnum0
 global Wdecimal
 global WC
 global WCE
 global entry1
 global entry2
 global dPad
 global Pad
 global sPad
 global wPad
 global tPad
 if dPad == 1:
     entryPad.destroy()
     print("dele")
 if sPad == 1:
     SentryPad.destroy()
     print("scientific is destroyed")
 if Pad == 1:
     StentryPad.destroy()
     print("Standard is destroyed")
 if tPad == 1:
     TentryPad.destroy()
     print("Time is destroyed")
 if wPad ==0:
    dPad = 0
    Pad = 0
    sPad = 0
    wPad = 1
    tPad = 0

    global converter
    global converter2
    converter = 'kg'
    converter2 = 'g'

    def Crt():
        global converter
        converter = 'c'
        Carats.config(fg="cyan")
        MilliGrams.config(fg="white")
        Grams.config(fg="white")
        KilloGrams.config(fg="white")
        Tons.config(fg="white")
        MetricTons.config(fg="white")
        Ounces.config(fg="white")
        Pounds.config(fg="white")
        con.config(state='normal')
        con.delete(0, END)
        con.insert(0, "Karat")
        con.config(state='disabled')

    def mg():
        global converter
        converter = 'mg'
        Carats.config(fg="white")
        MilliGrams.config(fg="cyan")
        Grams.config(fg="white")
        KilloGrams.config(fg="white")
        Tons.config(fg="white")
        MetricTons.config(fg="white")
        Ounces.config(fg="white")
        Pounds.config(fg="white")
        con.config(state='normal')
        con.delete(0, END)
        con.insert(0, "MilliGram")
        con.config(state='disabled')

    def g():
        global converter
        converter = 'g'
        Carats.config(fg="white")
        MilliGrams.config(fg="white")
        Grams.config(fg="cyan")
        KilloGrams.config(fg="white")
        Tons.config(fg="white")
        MetricTons.config(fg="white")
        Ounces.config(fg="white")
        Pounds.config(fg="white")
        con.config(state='normal')
        con.delete(0, END)
        con.insert(0, "Grams")
        con.config(state='disabled')

    def kg():
        global converter
        converter = 'kg'
        Carats.config(fg="white")
        MilliGrams.config(fg="white")
        Grams.config(fg="white")
        KilloGrams.config(fg="cyan")
        Tons.config(fg="white")
        MetricTons.config(fg="white")
        Ounces.config(fg="white")
        Pounds.config(fg="white")
        con.config(state='normal')
        con.delete(0, END)
        con.insert(0, "Killogram")
        con.config(state='disabled')

    def t():
        global converter
        converter = 't'
        Carats.config(fg="white")
        MilliGrams.config(fg="white")
        Grams.config(fg="white")
        KilloGrams.config(fg="white")
        Tons.config(fg="cyan")
        MetricTons.config(fg="white")
        Ounces.config(fg="white")
        Pounds.config(fg="white")
        con.config(state='normal')
        con.delete(0, END)
        con.insert(0, "US Tonne")
        con.config(state='disabled')

    def mt():
        global converter
        converter = 'mt'
        Carats.config(fg="white")
        MilliGrams.config(fg="white")
        Grams.config(fg="white")
        KilloGrams.config(fg="white")
        Tons.config(fg="white")
        MetricTons.config(fg="cyan")
        Ounces.config(fg="white")
        Pounds.config(fg="white")
        con.config(state='normal')
        con.delete(0, END)
        con.insert(0, "Tonne")
        con.config(state='disabled')

    def o():
        global converter
        converter = 'o'
        Carats.config(fg="white")
        MilliGrams.config(fg="white")
        Grams.config(fg="white")
        KilloGrams.config(fg="white")
        Tons.config(fg="white")
        MetricTons.config(fg="white")
        Ounces.config(fg="cyan")
        Pounds.config(fg="white")
        con.config(state='normal')
        con.delete(0, END)
        con.insert(0, "Ounce")
        con.config(state='disabled')

    def p():
        global converter
        converter = 'p'
        Carats.config(fg="white")
        MilliGrams.config(fg="white")
        Grams.config(fg="white")
        KilloGrams.config(fg="white")
        Tons.config(fg="white")
        MetricTons.config(fg="white")
        Ounces.config(fg="white")
        Pounds.config(fg="cyan")
        con.config(state='normal')
        con.delete(0, END)
        con.insert(0, "Pounds")
        con.config(state='disabled')

    def Crt1():
        global converter2
        converter2 = 'c'
        Carats1.config(fg="cyan")
        MilliGrams1.config(fg="white")
        Grams1.config(fg="white")
        KilloGrams1.config(fg="white")
        Tons1.config(fg="white")
        MetricTons1.config(fg="white")
        Ounces1.config(fg="white")
        Pounds1.config(fg="white")
        con1.config(state='normal')
        con1.delete(0, END)
        con1.insert(0, "Karat")
        con1.config(state='disabled')

    def mg1():
        global converter2
        converter2 = 'mg'
        Carats1.config(fg="white")
        MilliGrams1.config(fg="cyan")
        Grams1.config(fg="white")
        KilloGrams1.config(fg="white")
        Tons1.config(fg="white")
        MetricTons1.config(fg="white")
        Ounces1.config(fg="white")
        Pounds1.config(fg="white")
        con1.config(state='normal')
        con1.delete(0, END)
        con1.insert(0, "MilliGram")
        con1.config(state='disabled')

    def g1():
        global converter2
        converter2 = 'g'
        Carats1.config(fg="white")
        MilliGrams1.config(fg="white")
        Grams1.config(fg="cyan")
        KilloGrams1.config(fg="white")
        Tons1.config(fg="white")
        MetricTons1.config(fg="white")
        Ounces1.config(fg="white")
        Pounds1.config(fg="white")
        con1.config(state='normal')
        con1.delete(0, END)
        con1.insert(0, "Gram")
        con1.config(state='disabled')

    def kg1():
        global converter2
        converter2 = 'kg'
        Carats1.config(fg="white")
        MilliGrams1.config(fg="white")
        Grams1.config(fg="white")
        KilloGrams1.config(fg="cyan")
        Tons1.config(fg="white")
        MetricTons1.config(fg="white")
        Ounces1.config(fg="white")
        Pounds1.config(fg="white")
        con1.config(state='normal')
        con1.delete(0, END)
        con1.insert(0, "Killogram")
        con1.config(state='disabled')

    def t1():
        global converter2
        converter2 = 't'
        Carats1.config(fg="white")
        MilliGrams1.config(fg="white")
        Grams1.config(fg="white")
        KilloGrams1.config(fg="white")
        Tons1.config(fg="cyan")
        MetricTons1.config(fg="white")
        Ounces1.config(fg="white")
        Pounds1.config(fg="white")
        con1.config(state='normal')
        con1.delete(0, END)
        con1.insert(0, "US Tonne")
        con1.config(state='disabled')

    def mt1():
        global converter2
        converter2 = 'mt'
        Carats1.config(fg="white")
        MilliGrams1.config(fg="white")
        Grams1.config(fg="white")
        KilloGrams1.config(fg="white")
        Tons1.config(fg="white")
        MetricTons1.config(fg="cyan")
        Ounces1.config(fg="white")
        Pounds1.config(fg="white")
        con1.config(state='normal')
        con1.delete(0, END)
        con1.insert(0, "Tonne")
        con1.config(state='disabled')

    def o1():
        global converter2
        converter2 = 'o'
        Carats1.config(fg="white")
        MilliGrams1.config(fg="white")
        Grams1.config(fg="white")
        KilloGrams1.config(fg="white")
        Tons1.config(fg="white")
        MetricTons1.config(fg="white")
        Ounces1.config(fg="cyan")
        Pounds1.config(fg="white")
        con1.config(state='normal')
        con1.delete(0, END)
        con1.insert(0, "Ounce")
        con1.config(state='disabled')

    def p1():
        global converter2
        converter2 = 'p'
        Carats1.config(fg="white")
        MilliGrams1.config(fg="white")
        Grams1.config(fg="white")
        KilloGrams1.config(fg="white")
        Tons1.config(fg="white")
        MetricTons1.config(fg="white")
        Ounces1.config(fg="white")
        Pounds1.config(fg="cyan")
        con1.config(state='normal')
        con1.delete(0, END)
        con1.insert(0, "Pound")
        con1.config(state='disabled')

    def ACW():
        window.destroy()

    def CW():
        entry1.delete(0, END)
        entry2.delete(0, END)

    def CEW():
        entry1.delete(0, END)

    def W_1():
        weightNum(1,Wnum1)

    def W_2():
        weightNum(2, Wnum2)

    def W_3():
        weightNum(3, Wnum3)

    def W_4():
        weightNum(4, Wnum4)

    def W_5():
        weightNum(5, Wnum5)

    def W_6():
        weightNum(6, Wnum6)

    def W_7():
        weightNum(7, Wnum7)

    def W_8():
        weightNum(8, Wnum8)

    def W_9():
        weightNum(9, Wnum9)

    def W_0():
        weightNum(0, Wnum0)
            
    def W_Decimal():
        decNum(entry1,Wdecimal)

    def Copy1():
        window.clipboard_clear()
        window.clipboard_append(entry1.get())
    def Copy2():
        window.clipboard_clear()
        window.clipboard_append(entry2.get())
    def Paste1():
     try:
        entry1.delete(0, END)
        weightNum((float(window.clipboard_get())) , entry1)
     except:
         pass
        
    WentryPad = tk.LabelFrame(window, bg="black")
    WentryPad.place(relheight=0.65, relwidth=0.98, relx=0.01, rely=0.34)

    con = tk.Entry(WentryPad, bg="red", border=0, borderwidth=0, justify=CENTER, state=DISABLED, disabledbackground="black", disabledforeground="cyan")
    con.place(relheight=0.05, relwidth=0.2, relx=0.15, rely=0.34)
    con.config(state='normal')
    con.insert(0, "KilloGrams")
    con.config(state='disabled')

    con1 = tk.Entry(WentryPad, bg="red", border=0, borderwidth=0, justify=CENTER, state=DISABLED, disabledbackground="black", disabledforeground="cyan")
    con1.place(relheight=0.05, relwidth=0.2, relx=0.15, rely=0.47)
    con1.config(state='normal')
    con1.insert(0, "Grams")
    con1.config(state='disabled')

    con2 = tk.Entry(WentryPad, bg="white", border=0, borderwidth=0, justify=CENTER, state=DISABLED, disabledbackground="black", disabledforeground="cyan")
    con2.place(relheight=0.05, relwidth=0.05, relx=0.225, rely=0.405)
    con2.config(state='normal')
    con2.insert(0, "⬇")
    con2.config(state='disabled', takefocus=True)

    entry1 = Entry(WentryPad, bg="black", fg = "white", borderwidth=0, justify=CENTER)
    entry1.place(relheight=0.1, relwidth=0.4, relx=0.05, rely=0.09)

    Carats = tk.Button(WentryPad, bg="#353340", text="Crt", fg="white", command=Crt, activebackground="black", activeforeground="cyan")
    Carats.place(relheight=0.07, relwidth=0.1, relx=0.05, rely=0.19)

    MilliGrams = tk.Button(WentryPad, bg="#353340", text="Mg", fg="white", command=mg, activebackground="black", activeforeground="cyan")
    MilliGrams.place(relheight=0.07, relwidth=0.1, relx=0.15, rely=0.19)

    Grams = tk.Button(WentryPad, bg="#353340", text="g", fg="white", command=g, activebackground="black", activeforeground="cyan")
    Grams.place(relheight=0.07, relwidth=0.1, relx=0.25, rely=0.19)

    KilloGrams = tk.Button(WentryPad, bg="#353340", fg="cyan", text="Kg", command=kg, activebackground="black", activeforeground="cyan")
    KilloGrams.place(relheight=0.07, relwidth=0.1, relx=0.35, rely=0.19)

    Tons = tk.Button(WentryPad, bg="#353340", text="Ton", fg="white", command=t, activebackground="black", activeforeground="cyan")
    Tons.place(relheight=0.07, relwidth=0.1, relx=0.05, rely=0.26)

    MetricTons = tk.Button(WentryPad, bg="#353340", text="M.Ton", fg="white", command=mt, activebackground="black", activeforeground="cyan")
    MetricTons.place(relheight=0.07, relwidth=0.1, relx=0.15, rely=0.26)

    Ounces = tk.Button(WentryPad, bg="#353340", text="Ou", fg="white", command=o, activebackground="black", activeforeground="cyan")
    Ounces.place(relheight=0.07, relwidth=0.1, relx=0.25, rely=0.26)

    Pounds = tk.Button(WentryPad, bg="#353340", text="Pn", fg="white", command=p, activebackground="black", activeforeground="cyan")
    Pounds.place(relheight=0.07, relwidth=0.1, relx=0.35, rely=0.26)

    copy1 = tk.Button(WentryPad, bg="#353340", fg="cyan", text="copy", font="roboto 8", command=Copy1, activebackground="black", activeforeground="cyan")
    copy1.place(relheight=0.05, relwidth=0.1, relx=0.46, rely=0.09)

    paste1 = tk.Button(WentryPad, bg="#353340", fg="cyan", text="paste", font="roboto 8", command=Paste1, activebackground="black", activeforeground="cyan")
    paste1.place(relheight=0.05, relwidth=0.1, relx=0.46, rely=0.14)

    entry2 = Entry(WentryPad, bg="black", fg = "white", borderwidth=0, justify=CENTER)
    entry2.place(relheight=0.1, relwidth=0.4, relx=0.05, rely=0.54)

    Carats1 = tk.Button(WentryPad, bg="#353340", text="Crt", fg="white", command=Crt1, activebackground="black", activeforeground="cyan")
    Carats1.place(relheight=0.07, relwidth=0.1, relx=0.05, rely=0.64)

    MilliGrams1 = tk.Button(WentryPad, bg="#353340", text="Mg", fg="white", command=mg1, activebackground="black", activeforeground="cyan")
    MilliGrams1.place(relheight=0.07, relwidth=0.1, relx=0.15, rely=0.64)

    Grams1 = tk.Button(WentryPad, bg="#353340", fg="cyan", text="g", command=g1, activebackground="black", activeforeground="cyan")
    Grams1.place(relheight=0.07, relwidth=0.1, relx=0.25, rely=0.64)

    KilloGrams1 = tk.Button(WentryPad, bg="#353340", text="Kg", fg="white", command=kg1, activebackground="black", activeforeground="cyan")
    KilloGrams1.place(relheight=0.07, relwidth=0.1, relx=0.35, rely=0.64)

    Tons1 = tk.Button(WentryPad, bg="#353340", text="Ton", fg="white", command=t1, activebackground="black", activeforeground="cyan")
    Tons1.place(relheight=0.07, relwidth=0.1, relx=0.05, rely=0.71)

    MetricTons1 = tk.Button(WentryPad, bg="#353340", text="M.Ton", fg="white", command=mt1, activebackground="black", activeforeground="cyan")
    MetricTons1.place(relheight=0.07, relwidth=0.1, relx=0.15, rely=0.71)

    Ounces1 = tk.Button(WentryPad, bg="#353340", text="Ou", fg="white", command=o1, activebackground="black", activeforeground="cyan")
    Ounces1.place(relheight=0.07, relwidth=0.1, relx=0.25, rely=0.71)

    Pounds1 = tk.Button(WentryPad, bg="#353340", text="Pn", fg="white", command=p1, activebackground="black", activeforeground="cyan")
    Pounds1.place(relheight=0.07, relwidth=0.1, relx=0.35, rely=0.71)

    copy2 = tk.Button(WentryPad, bg="#353340", fg="cyan", text="copy", font="roboto 8", command=Copy2, activebackground="black", activeforeground="cyan")
    copy2.place(relheight=0.05, relwidth=0.1, relx=0.46, rely=0.54)

    Wnum1 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="1", command=W_1, activebackground="#262626", activeforeground="cyan")
    Wnum1.place(relheight=0.17, relwidth=0.13, rely=0.01, relx=0.58)

    Wnum2 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="2", command=W_2, activebackground="#262626", activeforeground="cyan")
    Wnum2.place(relheight=0.17, relwidth=0.13, rely=0.01, relx=0.72)

    Wnum3 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="3", command=W_3, activebackground="#262626", activeforeground="cyan")
    Wnum3.place(relheight=0.17, relwidth=0.13, rely=0.01, relx=0.86)

    Wnum4 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="4", command=W_4, activebackground="#262626", activeforeground="cyan")
    Wnum4.place(relheight=0.17, relwidth=0.13, rely=0.19, relx=0.58)

    Wnum5 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="5", command=W_5, activebackground="#262626", activeforeground="cyan")
    Wnum5.place(relheight=0.17, relwidth=0.13, rely=0.19, relx=0.72)

    Wnum6 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="6", command=W_6, activebackground="#262626", activeforeground="cyan")
    Wnum6.place(relheight=0.17, relwidth=0.13, rely=0.19, relx=0.86)

    Wnum7 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="7", command=W_7, activebackground="#262626", activeforeground="cyan")
    Wnum7.place(relheight=0.17, relwidth=0.13, rely=0.37, relx=0.58)

    Wnum8 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="8", command=W_8, activebackground="#262626", activeforeground="cyan")
    Wnum8.place(relheight=0.17, relwidth=0.13, rely=0.37, relx=0.72)

    Wnum9 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="9", command=W_9, activebackground="#262626", activeforeground="cyan")
    Wnum9.place(relheight=0.17, relwidth=0.13, rely=0.37, relx=0.86)

    Wnum0 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="0", command=W_0, activebackground="#262626", activeforeground="cyan")
    Wnum0.place(relheight=0.17, relwidth=0.13, rely=0.55, relx=0.72)

    Wdecimal = tk.Button(WentryPad, bg="black", fg="cyan", text=".", command=W_Decimal, activebackground="black", activeforeground="white")
    Wdecimal.place(relheight=0.17, relwidth=0.13, rely=0.55, relx=0.86)

    WC = tk.Button(WentryPad, bg="#fc8700", font="calibri 10", text="C", command=CW, activebackground="black", activeforeground="#fc8700")
    WC.place(relheight=0.17, relwidth=0.13, rely=0.55, relx=0.58)

    WCE = tk.Button(WentryPad, bg="#fc8700", font="calibri 10", text="⌫", command=back, activebackground="black", activeforeground="#fc8700")
    WCE.place(relheight=0.17, relwidth=0.13, rely=0.73, relx=0.58)

    WAC = tk.Button(WentryPad, bg="#F24607", font="calibri 10", text="AC",command=ACW, activebackground="black", activeforeground="#F24607")
    WAC.place(relheight=0.17, relwidth=0.27, rely=0.73, relx=0.72)

    if theme == 'Light':
        Lsetting(Wnum1,Wnum2,Wnum3,Wnum4,Wnum5,Wnum6,Wnum7,Wnum8,Wnum9,Wnum0,Wdecimal)

    settings4 = tk.Button(WentryPad, bg="black", relief='flat', image=newpic, border=0, borderwidth=0, activebackground="black", command=setting4)
    settings4.place(relwidth=0.1, relheight=0.1, relx = 0.01, rely=0.89)
 else:
     print('already there [Weight]')

#TIME#
def time():
 settings["padd"] = "Tentrypad"
 global sCounter
 sCounter = 0
 global settings5
 global TentryPad
 global Tnum1
 global Tnum2
 global Tnum3
 global Tnum4
 global Tnum5
 global Tnum6
 global Tnum7
 global Tnum8
 global Tnum9
 global Tnum0
 global Tdecimal
 global TC
 global TCE
 global Tentry1
 global Tentry2
 global dPad
 global Pad
 global sPad
 global wPad
 global tPad
 if dPad == 1:
     entryPad.destroy()
     print("dele")
 if sPad == 1:
     SentryPad.destroy()
     print("scientific is destroyed")
 if wPad == 1:
     WentryPad.destroy()
     print("Weights is destroyed")
 if Pad == 1:
     StentryPad.destroy()
     print("Standard is destroyed")
 if tPad ==0:
    dPad = 0
    Pad = 0
    sPad = 0
    wPad = 0
    tPad = 1
    global Tonverter
    global Tonverter2
    Tonverter = 'm'
    Tonverter2 = 's'

    def MS():
        global Tonverter
        Tonverter = 'ms'
        MilliSeconds.config(fg="cyan")
        Seconds.config(fg="white")
        Minutes.config(fg="white")
        Hours.config(fg="white")
        Days.config(fg="white")
        Years.config(fg="white")
        Century.config(fg="white")
        Tcon.config(state='normal')
        Tcon.delete(0, END)
        Tcon.insert(0, "MilliSeconds")
        Tcon.config(state='disabled')

    def S():
        global Tonverter
        Tonverter = 's'
        MilliSeconds.config(fg="white")
        Seconds.config(fg="cyan")
        Minutes.config(fg="white")
        Hours.config(fg="white")
        Days.config(fg="white")
        Years.config(fg="white")
        Century.config(fg="white")
        Tcon.config(state='normal')
        Tcon.delete(0, END)
        Tcon.insert(0, "Seconds")
        Tcon.config(state='disabled')

    def M():
        global Tonverter
        Tonverter = 'm'
        MilliSeconds.config(fg="white")
        Seconds.config(fg="white")
        Minutes.config(fg="cyan")
        Hours.config(fg="white")
        Days.config(fg="white")
        Years.config(fg="white")
        Century.config(fg="white")
        Tcon.config(state='normal')
        Tcon.delete(0, END)
        Tcon.insert(0, "Minutes")
        Tcon.config(state='disabled')

    def H():
        global Tonverter
        Tonverter = 'h'
        MilliSeconds.config(fg="white")
        Seconds.config(fg="white")
        Minutes.config(fg="white")
        Hours.config(fg="cyan")
        Days.config(fg="white")
        Years.config(fg="white")
        Century.config(fg="white")
        Tcon.config(state='normal')
        Tcon.delete(0, END)
        Tcon.insert(0, "Hours")
        Tcon.config(state='disabled')

    def D():
        global Tonverter
        Tonverter = 'd'
        MilliSeconds.config(fg="white")
        Seconds.config(fg="white")
        Minutes.config(fg="white")
        Hours.config(fg="white")
        Days.config(fg="cyan")
        Years.config(fg="white")
        Century.config(fg="white")
        Tcon.config(state='normal')
        Tcon.delete(0, END)
        Tcon.insert(0, "Days")
        Tcon.config(state='disabled')

    def Y():
        global Tonverter
        Tonverter = 'y'
        MilliSeconds.config(fg="white")
        Seconds.config(fg="white")
        Minutes.config(fg="white")
        Hours.config(fg="white")
        Days.config(fg="white")
        Years.config(fg="cyan")
        Century.config(fg="white")
        Tcon.config(state='normal')
        Tcon.delete(0, END)
        Tcon.insert(0, "Years")
        Tcon.config(state='disabled')

    def C():
        global Tonverter
        Tonverter = 'c'
        MilliSeconds.config(fg="white")
        Seconds.config(fg="white")
        Minutes.config(fg="white")
        Hours.config(fg="white")
        Days.config(fg="white")
        Years.config(fg="white")
        Century.config(fg="cyan")
        Tcon.config(state='normal')
        Tcon.delete(0, END)
        Tcon.insert(0, "Century")
        Tcon.config(state='disabled')

    def MS1():
        global Tonverter2
        Tonverter2 = 'ms'
        MilliSeconds1.config(fg="cyan")
        Seconds1.config(fg="white")
        Minutes1.config(fg="white")
        Hours1.config(fg="white")
        Days1.config(fg="white")
        Years1.config(fg="white")
        Century1.config(fg="white")
        Tcon1.config(state='normal')
        Tcon1.delete(0, END)
        Tcon1.insert(0, "MilliSeconds")
        Tcon1.config(state='disabled')

    def S1():
        global Tonverter2
        Tonverter2 = 's'
        MilliSeconds1.config(fg="white")
        Seconds1.config(fg="cyan")
        Minutes1.config(fg="white")
        Hours1.config(fg="white")
        Days1.config(fg="white")
        Years1.config(fg="white")
        Century1.config(fg="white")
        Tcon1.config(state='normal')
        Tcon1.delete(0, END)
        Tcon1.insert(0, "Seconds")
        Tcon1.config(state='disabled')

    def M1():
        global Tonverter2
        Tonverter2 = 'm'
        MilliSeconds1.config(fg="white")
        Seconds1.config(fg="white")
        Minutes1.config(fg="cyan")
        Hours1.config(fg="white")
        Days1.config(fg="white")
        Years1.config(fg="white")
        Century1.config(fg="white")
        Tcon1.config(state='normal')
        Tcon1.delete(0, END)
        Tcon1.insert(0, "Minutes")
        Tcon1.config(state='disabled')

    def H1():
        global Tonverter2
        Tonverter2 = 'h'
        MilliSeconds1.config(fg="white")
        Seconds1.config(fg="white")
        Minutes1.config(fg="white")
        Hours1.config(fg="cyan")
        Days1.config(fg="white")
        Years1.config(fg="white")
        Century1.config(fg="white")
        Tcon1.config(state='normal')
        Tcon1.delete(0, END)
        Tcon1.insert(0, "Hours")
        Tcon1.config(state='disabled')

    def D1():
        global Tonverter2
        Tonverter2 = 'd'
        MilliSeconds1.config(fg="white")
        Seconds1.config(fg="white")
        Minutes1.config(fg="white")
        Hours1.config(fg="white")
        Days1.config(fg="cyan")
        Years1.config(fg="white")
        Century1.config(fg="white")
        Tcon1.config(state='normal')
        Tcon1.delete(0, END)
        Tcon1.insert(0, "Days")
        Tcon1.config(state='disabled')

    def Y1():
        global Tonverter2
        Tonverter2 = 'y'
        MilliSeconds1.config(fg="white")
        Seconds1.config(fg="white")
        Minutes1.config(fg="white")
        Hours1.config(fg="white")
        Days1.config(fg="white")
        Years1.config(fg="cyan")
        Century1.config(fg="white")
        Tcon1.config(state='normal')
        Tcon1.delete(0, END)
        Tcon1.insert(0, "Years")
        Tcon1.config(state='disabled')

    def C1():
        global Tonverter2
        Tonverter2 = 'c'
        MilliSeconds1.config(fg="white")
        Seconds1.config(fg="white")
        Minutes1.config(fg="white")
        Hours1.config(fg="white")
        Days1.config(fg="white")
        Years1.config(fg="white")
        Century1.config(fg="cyan")
        Tcon1.config(state='normal')
        Tcon1.delete(0, END)
        Tcon1.insert(0, "Century")
        Tcon1.config(state='disabled')

    def ACT():
        window.destroy()

    def CT():
        Tentry1.delete(0, END)
        Tentry2.delete(0, END)

    def T_1():
        timeNum(1, Tnum1)

    def T_2():
        timeNum(2, Tnum2)

    def T_3():
        timeNum(3, Tnum3)

    def T_4():
        timeNum(4, Tnum4)

    def T_5():
        timeNum(5, Tnum5)

    def T_6():
        timeNum(6, Tnum6)

    def T_7():
        timeNum(7, Tnum7)

    def T_8():
        timeNum(8, Tnum8)

    def T_9():
        timeNum(9, Tnum9)

    def T_0():
        timeNum(0, Wnum0)
            
    def T_Decimal():
        decNum(Tentry1,Tdecimal)

    def Copy1():
        window.clipboard_clear()
        window.clipboard_append(Tentry1.get())
    def Copy2():
        window.clipboard_clear()
        window.clipboard_append(Tentry2.get())
    def Paste1():
     try:
        Tentry1.delete(0, END)
        timeNum((float(window.clipboard_get())), Tpaste1)
     except:
         pass
        
    TentryPad = tk.LabelFrame(window, bg="black")
    TentryPad.place(relheight=0.65, relwidth=0.98, relx=0.01, rely=0.34)

    Tcon = tk.Entry(TentryPad, bg="red", border=0, borderwidth=0, justify=CENTER, state=DISABLED, disabledbackground="black", disabledforeground="cyan")
    Tcon.place(relheight=0.05, relwidth=0.2, relx=0.15, rely=0.34)
    Tcon.config(state='normal')
    Tcon.insert(0, "Minute")
    Tcon.config(state='disabled')

    Tcon1 = tk.Entry(TentryPad, bg="red", border=0, borderwidth=0, justify=CENTER, state=DISABLED, disabledbackground="black", disabledforeground="cyan")
    Tcon1.place(relheight=0.05, relwidth=0.2, relx=0.15, rely=0.47)
    Tcon1.config(state='normal')
    Tcon1.insert(0, "Seconds")
    Tcon1.config(state='disabled')

    Tcon2 = tk.Entry(TentryPad, bg="red", border=0, borderwidth=0, justify=CENTER, state=DISABLED, disabledbackground="black", disabledforeground="cyan")
    Tcon2.place(relheight=0.05, relwidth=0.05, relx=0.225, rely=0.405)
    Tcon2.config(state='normal')
    Tcon2.insert(0, "⬇")
    Tcon2.config(state='disabled')

    Tentry1 = tk.Entry(TentryPad, bg="black", fg = "white", borderwidth=0, justify=CENTER)
    Tentry1.place(relheight=0.1, relwidth=0.4, relx=0.05, rely=0.09)

    MilliSeconds = tk.Button(TentryPad, bg="#353340", text="ms", fg="white", command=MS, activebackground="black", activeforeground="cyan")
    MilliSeconds.place(relheight=0.07, relwidth=0.1, relx=0.05, rely=0.19)

    Seconds = tk.Button(TentryPad, bg="#353340", text="s", fg="white", command=S, activebackground="black", activeforeground="cyan")
    Seconds.place(relheight=0.07, relwidth=0.1, relx=0.15, rely=0.19)

    Minutes = tk.Button(TentryPad, bg="#353340", fg="cyan", text="m", command=M)
    Minutes.place(relheight=0.07, relwidth=0.1, relx=0.25, rely=0.19)

    Hours = tk.Button(TentryPad, bg="#353340", text="h", fg="white", command=H, activebackground="black", activeforeground="cyan")
    Hours.place(relheight=0.07, relwidth=0.1, relx=0.35, rely=0.19)

    Days = tk.Button(TentryPad, bg="#353340", text="day", fg="white", command=D, activebackground="black", activeforeground="cyan")
    Days.place(relheight=0.07, relwidth=0.1, relx=0.1, rely=0.26)

    Years = tk.Button(TentryPad, bg="#353340", text="yrs", fg="white", command=Y, activebackground="black", activeforeground="cyan")
    Years.place(relheight=0.07, relwidth=0.1, relx=0.2, rely=0.26)

    Century = tk.Button(TentryPad, bg="#353340", text="Cent", fg="white", command=C, activebackground="black", activeforeground="cyan")
    Century.place(relheight=0.07, relwidth=0.1, relx=0.3, rely=0.26)

    Tcopy1 = tk.Button(TentryPad, bg="#353340", fg="cyan", text="copy", font="roboto 8", command=Copy1, activebackground="black", activeforeground="cyan")
    Tcopy1.place(relheight=0.05, relwidth=0.1, relx=0.46, rely=0.09)

    Tpaste1 = tk.Button(TentryPad, bg="#353340", fg="cyan", text="paste", font="roboto 8", command=Paste1, activebackground="black", activeforeground="cyan")
    Tpaste1.place(relheight=0.05, relwidth=0.1, relx=0.46, rely=0.14)

    Tentry2 = tk.Entry(TentryPad, bg="black", fg = "white", borderwidth=0, justify=CENTER)
    Tentry2.place(relheight=0.1, relwidth=0.4, relx=0.05, rely=0.54)

    copy2 = tk.Button(TentryPad, bg="#353340", fg="cyan", text="copy", font="roboto 8", command=Copy2, activebackground="black", activeforeground="cyan")
    copy2.place(relheight=0.05, relwidth=0.1, relx=0.46, rely=0.54)

    MilliSeconds1 = tk.Button(TentryPad, bg="#353340", text="ms", fg="white", command=MS1, activebackground="black", activeforeground="cyan")
    MilliSeconds1.place(relheight=0.07, relwidth=0.1, relx=0.05, rely=0.64)

    Seconds1 = tk.Button(TentryPad, bg="#353340", fg="cyan", text="s", command=S1, activebackground="black", activeforeground="cyan")
    Seconds1.place(relheight=0.07, relwidth=0.1, relx=0.15, rely=0.64)

    Minutes1 = tk.Button(TentryPad, bg="#353340", text="m", fg="white", command=M1, activebackground="black", activeforeground="cyan")
    Minutes1.place(relheight=0.07, relwidth=0.1, relx=0.25, rely=0.64)

    Hours1 = tk.Button(TentryPad, bg="#353340", text="h", fg="white", command=H1, activebackground="black", activeforeground="cyan")
    Hours1.place(relheight=0.07, relwidth=0.1, relx=0.35, rely=0.64)

    Days1 = tk.Button(TentryPad, bg="#353340", text="day", fg="white", command=D1, activebackground="black", activeforeground="cyan")
    Days1.place(relheight=0.07, relwidth=0.1, relx=0.1, rely=0.71)

    Years1 = tk.Button(TentryPad, bg="#353340", text="yrs", fg="white", command=Y1, activebackground="black", activeforeground="cyan")
    Years1.place(relheight=0.07, relwidth=0.1, relx=0.2, rely=0.71)

    Century1 = tk.Button(TentryPad, bg="#353340", text="Cent", fg="white", command=C1, activebackground="black", activeforeground="cyan")
    Century1.place(relheight=0.07, relwidth=0.1, relx=0.3, rely=0.71)

    Tnum1 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="1", command=T_1, activebackground="#262626", activeforeground="cyan")
    Tnum1.place(relheight=0.17, relwidth=0.13, rely=0.01, relx=0.58)

    Tnum2 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="2", command=T_2, activebackground="#262626", activeforeground="cyan")
    Tnum2.place(relheight=0.17, relwidth=0.13, rely=0.01, relx=0.72)

    Tnum3 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="3", command=T_3, activebackground="#262626", activeforeground="cyan")
    Tnum3.place(relheight=0.17, relwidth=0.13, rely=0.01, relx=0.86)

    Tnum4 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="4", command=T_4, activebackground="#262626", activeforeground="cyan")
    Tnum4.place(relheight=0.17, relwidth=0.13, rely=0.19, relx=0.58)

    Tnum5 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="5", command=T_5, activebackground="#262626", activeforeground="cyan")
    Tnum5.place(relheight=0.17, relwidth=0.13, rely=0.19, relx=0.72)

    Tnum6 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="6", command=T_6, activebackground="#262626", activeforeground="cyan")
    Tnum6.place(relheight=0.17, relwidth=0.13, rely=0.19, relx=0.86)

    Tnum7 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="7", command=T_7, activebackground="#262626", activeforeground="cyan")
    Tnum7.place(relheight=0.17, relwidth=0.13, rely=0.37, relx=0.58)

    Tnum8 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="8", command=T_8, activebackground="#262626", activeforeground="cyan")
    Tnum8.place(relheight=0.17, relwidth=0.13, rely=0.37, relx=0.72)

    Tnum9 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="9", command=T_9, activebackground="#262626", activeforeground="cyan")
    Tnum9.place(relheight=0.17, relwidth=0.13, rely=0.37, relx=0.86)

    Tnum0 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="0", command=T_0, activebackground="#262626", activeforeground="cyan")
    Tnum0.place(relheight=0.17, relwidth=0.13, rely=0.55, relx=0.72)

    Tdecimal = tk.Button(TentryPad, bg="black", fg="cyan", text=".", command=T_Decimal, activebackground="#262626", activeforeground="white")
    Tdecimal.place(relheight=0.17, relwidth=0.13, rely=0.55, relx=0.86)

    TC = tk.Button(TentryPad, bg="#fc8700", font="calibri 10", text="C", command=CT, activebackground="black", activeforeground="#fc8700")
    TC.place(relheight=0.17, relwidth=0.13, rely=0.55, relx=0.58)

    TCE = tk.Button(TentryPad, bg="#fc8700", font="calibri 10", text="⌫", command=back, activebackground="black", activeforeground="#fc8700")
    TCE.place(relheight=0.17, relwidth=0.13, rely=0.73, relx=0.58)

    AC = tk.Button(TentryPad, bg="#F24607", font="calibri 10", text="AC",command=ACT, activebackground="black", activeforeground="#F24607")
    AC.place(relheight=0.17, relwidth=0.27, rely=0.73, relx=0.72)

    if theme == 'Light':
        Lsetting(Tnum1,Tnum2,Tnum3,Tnum4,Tnum5,Tnum6,Tnum7,Tnum8,Tnum9,Tnum0,Tdecimal)

    settings5 = tk.Button(TentryPad, bg="black", relief='flat', image=newpic, border=0, borderwidth=0, activebackground="black", command=setting5)
    settings5.place(relwidth=0.1, relheight=0.1, relx = 0.01, rely=0.89)
 else:
     print("already there [T I M E]")

#HISTORY
def history():
    global counter

    if counter==0:
        global HentryPad
        HentryPad = tk.LabelFrame(window, bg="#262626",)
        HentryPad.place(relheight=0.65, relwidth=0.3, relx=0.69, rely=0.34)  

        mclear = tk.Button(HentryPad, bg="#262626", fg="white", text="🗑", font="bangers", command=pop, borderwidth=0, activebackground="#262626", activeforeground="red",)
        mclear.place(relheight=0.09, relwidth=0.2, relx=0.02, rely=0.01)

        completeHistory = tk.Button(HentryPad, bg="#262626", fg="white", text="Full History\n➡", command=fHistory, borderwidth=0, activebackground="#262626", activeforeground="cyan")
        completeHistory.place(relheight=0.09, relx=0.25, rely=0.001)

        yscroll = tk.Scrollbar(HentryPad, orient=VERTICAL)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll = tk.Scrollbar(HentryPad, orient=HORIZONTAL)
        xscroll.pack(side=BOTTOM, fill=X)

        mlist = tk.Listbox(HentryPad, yscrollcommand=yscroll.set, xscrollcommand=xscroll.set, bg="#262626", fg="white", borderwidth=2,)
        mlist.place(relheight=0.85, relwidth=0.85, rely=0.1)

        yscroll.config( command = mlist.yview )
        xscroll.config( command = mlist.xview )
        bcounter = 0
        if len(memory) == 0:
            # mlist.insert(END,"EMPTY")
            l = tk.Label(mlist, text="There is no\nhistory yet", bg="#262626", fg="red", font="SFprodisplay 13")
            l.place(relheight=1, relwidth=1)
        elif len(memory) > 0:
            for meme in reversed(memory):
                bcounter += 1
                if bcounter <= 200:
                    mlist.insert(END,meme)
                else:
                    pass
        counter +=1
    else:
        HentryPad.destroy()
        counter = 0

keyboard.on_press_key("f2", lambda _:history())

#=========MENU_BUTTONS==========

# STANDARD #                                                                                 
Standard = tk.Button(menu, bg="#BF907E", text="Standard", command=standard, activebackground="#BF907E")                          
Standard.place(relheight=0.94, relwidth=0.2, rely=0.02, relx=0.01)    

# SCIENTIFIC #                                                                                 
Scientific = tk.Button(menu, bg="#BF907E", text="Scientific", command=scientific, activebackground="#BF907E")                      
Scientific.place(relheight=0.94, relwidth=0.2, rely=0.02, relx=0.22)                                           
                                
# WIEGHTS #                                                                                 
Weight = tk.Button(menu, bg="#BF907E", text="    Weights   ", command=weight, activebackground="#BF907E")                      
Weight.place(relheight=0.94, relwidth=0.2, rely=0.02, relx=0.43)   

# TIME #                                                                                 
Time = tk.Button(menu, bg="#BF907E", text="      Time      ", command=time, activebackground="#BF907E")                      
Time.place(relheight=0.94, relwidth=0.2, rely=0.02, relx=0.64)   

#HISTORY#

History = tk.Button(menu, bg="#d4ff00", text="HISTORY", command=history, activebackground="#d4ff00")
History.place(relheight=0.94, relwidth=0.143, rely=0.02, relx=0.85)

keyboard.add_hotkey("alt + r", lambda: standard())
keyboard.add_hotkey("alt + s", lambda: scientific())
keyboard.add_hotkey("alt + w", lambda: weight())
keyboard.add_hotkey("alt + t", lambda: time())

if mainpad == 'entrypad':
    print("Entrypad")
    try:
        if maindir:
            if mainui == 'custom':
                if mainthm == 'Dark':
                    one = ImageTk.PhotoImage(file=f'{maindir}/one.png')
                    two = ImageTk.PhotoImage(file=f"{maindir}/two.png")
                    three = ImageTk.PhotoImage(file=f"{maindir}/three.png")
                    four = ImageTk.PhotoImage(file=f"{maindir}/four.png")
                    five = ImageTk.PhotoImage(file=f"{maindir}/five.png")
                    six = ImageTk.PhotoImage(file=f"{maindir}/six.png")
                    seven = ImageTk.PhotoImage(file=f"{maindir}/seven.png")
                    eight = ImageTk.PhotoImage(file=f"{maindir}/eight.png")
                    nine = ImageTk.PhotoImage(file=f"{maindir}/nine.png")
                    zero = ImageTk.PhotoImage(file=f"{maindir}/zero.png")
                    num1.config(image=one,bg="black")
                    num2.config(image=two,bg="black")
                    num3.config(image=three,bg="black")
                    num4.config(image=four,bg="black")
                    num5.config(image=five,bg="black")
                    num6.config(image=six,bg="black")
                    num7.config(image=seven,bg="black")
                    num8.config(image=eight,bg="black")
                    num9.config(image=nine,bg="black")
                    num0.config(image=zero,bg="black")
                
                if mainthm == 'Light':
                    one = ImageTk.PhotoImage(file=f'{maindir}/Done.png')
                    two = ImageTk.PhotoImage(file=f"{maindir}/Dtwo.png")
                    three = ImageTk.PhotoImage(file=f"{maindir}/Dthree.png")
                    four = ImageTk.PhotoImage(file=f"{maindir}/Dfour.png")
                    five = ImageTk.PhotoImage(file=f"{maindir}/Dfive.png")
                    six = ImageTk.PhotoImage(file=f"{maindir}/Dsix.png")
                    seven = ImageTk.PhotoImage(file=f"{maindir}/Dseven.png")
                    eight = ImageTk.PhotoImage(file=f"{maindir}/Deight.png")
                    nine = ImageTk.PhotoImage(file=f"{maindir}/Dnine.png")
                    zero = ImageTk.PhotoImage(file=f"{maindir}/Dzero.png")
                    num1.config(image=one,bg="white")
                    num2.config(image=two,bg="white")
                    num3.config(image=three,bg="white")
                    num4.config(image=four,bg="white")
                    num5.config(image=five,bg="white")
                    num6.config(image=six,bg="white")
                    num7.config(image=seven,bg="white")
                    num8.config(image=eight,bg="white")
                    num9.config(image=nine,bg="white")
                    num0.config(image=zero,bg="white")
        if mainui == 'default':
            if mainthm == 'Dark':
                num1.config(bg="black")
                num2.config(bg="black")
                num3.config(bg="black")
                num4.config(bg="black")
                num5.config(bg="black")
                num6.config(bg="black")
                num7.config(bg="black")
                num8.config(bg="black")
                num9.config(bg="black")
                num0.config(bg="black")
                Clear1.config(bg="#fc8700")
                Clear2.config(bg="#fc8700")
                Clear3.config(bg="#fc8700")
            if mainthm == 'Light':
                num1.config(bg="white",fg="black")
                num2.config(bg="white",fg="black")
                num3.config(bg="white",fg="black")
                num4.config(bg="white",fg="black")
                num5.config(bg="white",fg="black")
                num6.config(bg="white",fg="black")
                num7.config(bg="white",fg="black")
                num8.config(bg="white",fg="black")
                num9.config(bg="white",fg="black")
                num0.config(bg="white",fg="black") 
                Clear1.config(bg="#ff0000")
                Clear2.config(bg="#ff0000")
                Clear3.config(bg="#ff0000") 
    except:
        pass
elif mainpad == 'Stentrypad':
    print("Entrypad")
    try:
        if maindir:
            if mainui == 'custom':
                if mainthm == 'Dark':
                    one = ImageTk.PhotoImage(file=f'{maindir}/one.png')
                    two = ImageTk.PhotoImage(file=f"{maindir}/two.png")
                    three = ImageTk.PhotoImage(file=f"{maindir}/three.png")
                    four = ImageTk.PhotoImage(file=f"{maindir}/four.png")
                    five = ImageTk.PhotoImage(file=f"{maindir}/five.png")
                    six = ImageTk.PhotoImage(file=f"{maindir}/six.png")
                    seven = ImageTk.PhotoImage(file=f"{maindir}/seven.png")
                    eight = ImageTk.PhotoImage(file=f"{maindir}/eight.png")
                    nine = ImageTk.PhotoImage(file=f"{maindir}/nine.png")
                    zero = ImageTk.PhotoImage(file=f"{maindir}/zero.png")
                    num1.config(image=one,bg="black")
                    num2.config(image=two,bg="black")
                    num3.config(image=three,bg="black")
                    num4.config(image=four,bg="black")
                    num5.config(image=five,bg="black")
                    num6.config(image=six,bg="black")
                    num7.config(image=seven,bg="black")
                    num8.config(image=eight,bg="black")
                    num9.config(image=nine,bg="black")
                    num0.config(image=zero,bg="black")
                
                if mainthm == 'Light':
                    one = ImageTk.PhotoImage(file=f'{maindir}/Done.png')
                    two = ImageTk.PhotoImage(file=f"{maindir}/Dtwo.png")
                    three = ImageTk.PhotoImage(file=f"{maindir}/Dthree.png")
                    four = ImageTk.PhotoImage(file=f"{maindir}/Dfour.png")
                    five = ImageTk.PhotoImage(file=f"{maindir}/Dfive.png")
                    six = ImageTk.PhotoImage(file=f"{maindir}/Dsix.png")
                    seven = ImageTk.PhotoImage(file=f"{maindir}/Dseven.png")
                    eight = ImageTk.PhotoImage(file=f"{maindir}/Deight.png")
                    nine = ImageTk.PhotoImage(file=f"{maindir}/Dnine.png")
                    zero = ImageTk.PhotoImage(file=f"{maindir}/Dzero.png")
                    num1.config(image=one,bg="white")
                    num2.config(image=two,bg="white")
                    num3.config(image=three,bg="white")
                    num4.config(image=four,bg="white")
                    num5.config(image=five,bg="white")
                    num6.config(image=six,bg="white")
                    num7.config(image=seven,bg="white")
                    num8.config(image=eight,bg="white")
                    num9.config(image=nine,bg="white")
                    num0.config(image=zero,bg="white")
        if mainui == 'default':
            if mainthm == 'Dark':
                num1.config(bg="black")
                num2.config(bg="black")
                num3.config(bg="black")
                num4.config(bg="black")
                num5.config(bg="black")
                num6.config(bg="black")
                num7.config(bg="black")
                num8.config(bg="black")
                num9.config(bg="black")
                num0.config(bg="black")
                Clear1.config(bg="#fc8700")
                Clear2.config(bg="#fc8700")
                Clear3.config(bg="#fc8700")
            if mainthm == 'Light':
                num1.config(bg="white",fg="black")
                num2.config(bg="white",fg="black")
                num3.config(bg="white",fg="black")
                num4.config(bg="white",fg="black")
                num5.config(bg="white",fg="black")
                num6.config(bg="white",fg="black")
                num7.config(bg="white",fg="black")
                num8.config(bg="white",fg="black")
                num9.config(bg="white",fg="black")
                num0.config(bg="white",fg="black") 
                Clear1.config(bg="#ff0000")
                Clear2.config(bg="#ff0000")
                Clear3.config(bg="#ff0000") 
    except:
        pass
elif mainpad == 'Sentrypad':
    print("Sentrypad")
    scientific()
elif mainpad == 'Wentrypad':
    print("Wentrypad")
    weight()
elif mainpad == 'Tentrypad':
    print("Tentrypad")
    time()
else:
    print ("unusual problem!")

mainFrame.focus()

#================MAINLOOP===================
if __name__ == '__main__':
    window.mainloop()
#===============File_open==================

with open('data/mem.txt','w+')as f:
    for mem in memory:
        if mem=='':
            pass
        else:
            f.write(mem + ',')

with open('data/settings.txt','w') as f:
    f.write(str(settings))
#=============CREDITS===============#())
# Made by THIRUCHLVAN (AKA) DUFFY
# MY YOUTUBE CHANNEL:- https://youtube.com/duffyyt