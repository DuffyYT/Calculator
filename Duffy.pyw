#============================IMPORTS==============================

import tkinter as tk                         #Importing Tkinter module for GUI
from tkinter import *                        #Importing all tkinter files
import math                                  #Importing math module for arithmetic
import webbrowser                            #Plugging tool
import os                                    #For saving memory(OPENING FILES AND READING FILES)

#=================Memory_saving===============

memory = []

if os.path.isfile('mem.txt'):
    with open ('mem.txt', 'r') as f:
        memSplit = f.read()
        memSplit = memSplit.split(',')
        for i in range(len(memSplit)):
            memory.append(memSplit[i])
for space in range(len(memory)): #Removing extra whitespace
    if memory[space]=='':
        memory.remove('')
global counter #WM#
counter = 0
global dd    #WM#
#==========================NUMBER_BUTTONS_FUNCTIONS==========================
def num_1():
    global counter
    if counter == 1:
        HentryPad.destroy()
        counter=0
    else:
        if upperField.get()=='OVERFLOW!!':
            upperAns.delete(0,END)
            upperField.delete(0, END)
            temp = field.get()
            field.delete(0,END)
            field.insert(0,1)
        else:
            upperAns.delete(0,END)
            temp = field.get()
            field.insert(END,1)

def num_2():
    global counter
    if counter == 1:
        HentryPad.destroy()
        counter=0
    else:
        if upperField.get()=='OVERFLOW!!':
            upperAns.delete(0,END)
            upperField.delete(0, END)
            temp = field.get()
            field.delete(0,END)
            field.insert(0,2)
        else:
            upperAns.delete(0,END)
            temp = field.get()
            field.insert(END,2)

def num_3():
    global counter
    if counter == 1:
        HentryPad.destroy()
        counter=0
    else:
        if upperField.get()=='OVERFLOW!!':
            upperAns.delete(0,END)
            upperField.delete(0, END)
            temp = field.get()
            field.delete(0,END)
            field.insert(0,3)
        else:
            upperAns.delete(0,END)
            temp = field.get()
            field.insert(END,3)

def num_4():
    global counter
    if counter == 1:
        HentryPad.destroy()
        counter=0
    else:
        if upperField.get()=='OVERFLOW!!':
            upperAns.delete(0,END)
            upperField.delete(0, END)
            temp = field.get()
            field.delete(0,END)
            field.insert(0,4)
        else:
            upperAns.delete(0,END)
            temp = field.get()
            field.insert(END,4)

def num_5():
    global counter
    if counter == 1:
        HentryPad.destroy()
        counter=0
    else:
        if upperField.get()=='OVERFLOW!!':
            upperAns.delete(0,END)
            upperField.delete(0, END)
            temp = field.get()
            field.delete(0,END)
            field.insert(0,5)
        else:
            upperAns.delete(0,END)
            temp = field.get()
            field.insert(END,5)

def num_6():
    global counter
    if counter == 1:
        HentryPad.destroy()
        counter=0
    else:
        if upperField.get()=='OVERFLOW!!':
            upperAns.delete(0,END)
            upperField.delete(0, END)
            temp = field.get()
            field.delete(0,END)
            field.insert(0,6)
        else:
            upperAns.delete(0,END)
            temp = field.get()
            field.insert(END,6)

def num_7():
    global counter
    if counter == 1:
        HentryPad.destroy()
        counter=0
    else:
        if upperField.get()=='OVERFLOW!!':
            upperAns.delete(0,END)
            upperField.delete(0, END)
            temp = field.get()
            field.delete(0,END)
            field.insert(0,7)
        else:
            upperAns.delete(0,END)
            temp = field.get()
            field.insert(END,7)

def num_8():
    global counter
    if counter == 1:
        HentryPad.destroy()
        counter=0
    else:
        if upperField.get()=='OVERFLOW!!':
            upperAns.delete(0,END)
            upperField.delete(0, END)
            temp = field.get()
            field.delete(0,END)
            field.insert(0,8)
        else:
            upperAns.delete(0,END)
            temp = field.get()
            field.insert(END,8)

def num_9():
    global counter
    if counter == 1:
        HentryPad.destroy()
        counter=0
    else:
        if upperField.get()=='OVERFLOW!!':
            upperAns.delete(0,END)
            upperField.delete(0, END)
            temp = field.get()
            field.delete(0,END)
            field.insert(0,9)
        else:
            upperAns.delete(0,END)
            temp = field.get()
            field.insert(END,9)

def num_0():
    global counter
    if counter == 1:
        HentryPad.destroy()
        counter=0
    else:
        if upperField.get()=='OVERFLOW!!':
            upperAns.delete(0,END)
            upperField.delete(0, END)
            temp = field.get()
            field.delete(0,END)
            field.insert(END,0)
        else:
            upperAns.delete(0,END)
            temp = field.get()
            field.insert(END,0)
        
def Decimal():
    global counter
    if counter == 1:
        HentryPad.destroy()
        counter=0
    else:
        if field.get() != '':
            if upperField.get()=='OVERFLOW!!':
                upperAns.delete(0,END)
                upperField.delete(0, END)
                field.delete(0,END)
                field.insert(END,".")
            else:
                upperAns.delete(0,END)
                field.insert(END,".")
        else:
            upperAns.delete(0,END)
            field.insert(0,"0.")

def negative():
    global counter
    if counter == 1:
        HentryPad.destroy()
        counter=0
    else:
        if upperField.get()=="OVERFLOW!!":
            upperAns.delete(0,END)
            temp = field.get()
            field.delete(0,END)
            field.insert(0,str(temp) + "-")
        else:
            upperAns.delete(0,END)
            temp = field.get()
            if temp=='':
                field.delete(0,END)
                field.insert(0,str(temp) + "-")
            else:
                pass
#==============================OPERATOR_BUTTONS_FUNCTIONS================================

def Add():
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
        elif upperOperator.get() == ' [-]':
         if upperField.get() != '':
            dd = float(upperField.get()) - float(field.get())
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
        elif upperOperator.get() == ' [x]':
         if upperField.get() != '':
            dd = float(upperField.get()) * float(field.get())
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
        elif upperOperator.get() == '[ / ]':
         if upperField.get() != '':
            dd = float(upperField.get()) / float(field.get())
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
        elif upperOperator.get() == ' [+]':
         if upperField.get() != '':
            dd = float(upperField.get()) + float(field.get())
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
        elif upperOperator.get() == ' [x]':
         if upperField.get() != '':
            dd = float(upperField.get()) * float(field.get())
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
        elif upperOperator.get() == '[ / ]':
         if upperField.get() != '':
            dd = float(upperField.get()) / float(field.get())
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
        elif upperOperator.get() == ' [+]':
         if upperField.get() != '':
            dd = float(upperField.get()) + float(field.get())
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
        elif upperOperator.get() == ' [-]':
         if upperField.get() != '':
            dd = float(upperField.get()) - float(field.get())
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
        elif upperOperator.get() == '[ / ]':
         if upperField.get() != '':
            dd = float(upperField.get()) / float(field.get())
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
        elif upperOperator.get() == ' [+]':
         if upperField.get() != '':
            dd = float(upperField.get()) + float(field.get())
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
        elif upperOperator.get() == ' [-]':
         if upperField.get() != '':
            dd = float(upperField.get()) - float(field.get())
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
        elif upperOperator.get() == ' [x]':
         if upperField.get() != '':
            dd = float(upperField.get()) * float(field.get())
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

#=============================CLEAR_BUTTONS================================

def CE():
    field.delete(0,END)

def C():
    field.delete(0,END)
    upperField.delete(0,END)
    upperAns.delete(0,END)

def AC():
    window.destroy()

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
            counter=0
    def close():
        root.destroy()
    root.geometry("500x500")
    r = tk.Frame(root, bg="#262626")
    r.place(relwidth=1, relheight=1)
    w = tk.Label(r, text ='FULL HISTORY ',font = "bangers 50", bg="#262626", fg="cyan") 
    w.pack()
    e = tk.Label(r, text="Records with large calculations and older history will appear here", bg="#262626", fg="cyan",)
    e.pack()
    close = tk.Button(r, text="Close", command=close, bg="#262626", fg="red",activeforeground="black", activebackground="red")
    close.place(relheight=0.1, relwidth=0.1, relx=0.9)
    Clear = tk.Button(r, text="C L E A R", command=Fpop, bg="#262626", fg="cyan", padx=250, activebackground="#262629", activeforeground="red")
    Clear.pack()
    scroll_bar = tk.Scrollbar(r,)
    scroll_bar.pack( side = RIGHT,fill = Y )
    mylist = tk.Listbox(r, yscrollcommand = scroll_bar.set, bg="#262626", fg="white")
    mylist.pack(side="left",fill="both",expand=True)
    for meme in reversed(memory):
        mylist.insert(END, meme)
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

#============================MAIN_WINDOW==============================
window = tk.Tk()
window.title("Calculator")
window.iconbitmap('ICON\calc1.ico')
window.minsize(400,500)
window.maxsize(400,500)
mainFrame = tk.Frame(window, bg="black")#frame(MAIN)
mainFrame.place(relheight=1, relwidth=1)

#=========================ENTRY_FIELDS=================================

# MAIN_FIELD #
field = tk.Entry(window, bg="black", fg="white", border=0, font="calibri 35", justify=RIGHT,)
field.place(relheight=0.25, relwidth=0.98, relx=0.01, rely=0.01)

# SECONDARY_FIELD #
upperField = tk.Entry(field,bg="black", fg="white", borderwidth=0, border=0, font="calibri 10", justify=RIGHT)
upperField.place(relheight=0.2, relwidth=1,)

# ANSWER_FIELD #
upperAns = tk.Entry(upperField,bg="black", fg="white", borderwidth=0, border=0, font="calibri 10")
upperAns.place(relheight=1, relx=0.06)

# OPERATOR_FIELD #
upperOperator = tk.Entry(upperField,bg="#353340", fg="cyan", borderwidth=0.01, border=1, font="calibri 10")
upperOperator.place(relheight=1, relwidth=0.06,)

#=======================COPY_PASTE======================

Fcopy = tk.Button(field, bg="#353340", fg="cyan", text="Copy", command=copyf,activebackground="black", activeforeground="white")
Fcopy.place(relheight=0.2, relwidth=0.1, rely=0.8, relx=0.8)

Fpaste = tk.Button(field, bg="#353340", fg="cyan", text="Paste", command=pastef,activebackground="black", activeforeground="white")
Fpaste.place(relheight=0.2, relwidth=0.1, rely=0.8, relx=0.9)

UFcopy = tk.Button(field, bg="#353340", fg="cyan", text="Copy", command=copyuf,activebackground="black", activeforeground="white")
UFcopy.place(relheight=0.2, relwidth=0.1, rely=0.15, relx=0.9)

#============================MENU==================================
                                                                              
menu = tk.LabelFrame(window, bg="#636D73")                                         
menu.place(relheight=0.062, relwidth=0.98, relx=0.01, rely=0.27)                                                   
                                                                                 
#=============================ENTRY_PAD================================

entryPad = tk.LabelFrame(window, bg="black",)
entryPad.place(relheight=0.65, relwidth=0.98, relx=0.01, rely=0.34)

#===========================NUMBER_BUTTONS========================================

# 1 #
num1 = tk.Button(entryPad, bg="black", fg = "white", text="1", pady=10, padx=20,command=num_1, activebackground="#262626", activeforeground="cyan")
num1.grid(row=0, column=0, padx=1, pady=1)

# 2 #
num2 = tk.Button(entryPad, bg="black", fg = "white", text="2", pady=10, padx=20,command=num_2, activebackground="#262626", activeforeground="cyan")
num2.grid(row=0, column=1, padx=1, pady=1)

# 3 #
num3 = tk.Button(entryPad, bg="black", fg = "white", text="3", pady=10, padx=20,command=num_3, activebackground="#262626", activeforeground="cyan")
num3.grid(row=0, column=2, padx=1, pady=1)

# 4 #
num4 = tk.Button(entryPad, bg="black", fg = "white", text="4", pady=10, padx=20,command=num_4, activebackground="#262626", activeforeground="cyan")
num4.grid(row=1, column=0, padx=1, pady=1)

# 5 #
num5 = tk.Button(entryPad, bg="black", fg = "white", text="5", pady=10, padx=20,command=num_5, activebackground="#262626", activeforeground="cyan")
num5.grid(row=1, column=1, padx=1, pady=1)

# 6 #
num6 = tk.Button(entryPad, bg="black", fg = "white", text="6", pady=10, padx=20,command=num_6, activebackground="#262626", activeforeground="cyan")
num6.grid(row=1, column=2, padx=1, pady=1)

# 7 #
num7 = tk.Button(entryPad, bg="black", fg = "white", text="7", pady=10, padx=20,command=num_7, activebackground="#262626", activeforeground="cyan")
num7.grid(row=2, column=0, padx=1, pady=1)

# 8 #
num8 = tk.Button(entryPad, bg="black", fg = "white", text="8", pady=10, padx=20,command=num_8, activebackground="#262626", activeforeground="cyan")
num8.grid(row=2, column=1, padx=1, pady=1)

# 9 #
num9 = tk.Button(entryPad, bg="black", fg = "white", text="9", pady=10, padx=20,command=num_9, activebackground="#262626", activeforeground="cyan")
num9.grid(row=2, column=2, padx=1, pady=1)

# 0 #
num0 = tk.Button(entryPad, bg="black", fg = "white", text="0", pady=10, padx=20,command=num_0, activebackground="#262626", activeforeground="cyan")
num0.grid(row=3, column=1, padx=1, pady=1,)

# - #
Negative = tk.Button(entryPad, bg="#262626", fg = "cyan", text="-", pady=10, padx=20,command=negative, activeforeground="white", activebackground="black")
Negative.grid(row=3, column=0, padx=1, pady=1,)

# . #
decimal = tk.Button(entryPad, bg="#262626", fg = "cyan", text=".", pady=10, padx=21.499999999999998222,command=Decimal, activeforeground="white", activebackground="black")
decimal.grid(row=3, column=2, padx=1, pady=1,)

#========================OPERATOR_BUTTONS===========================

# + #
add = tk.Button(entryPad, bg="#5D8AA6", text="+", padx=19.48, pady=10, command=Add, activebackground="#5D8AA6")
add.grid(row=0, column=3, pady=1, padx=1,)

# - #
subtract = tk.Button(entryPad, bg="#5D8AA6", text="-", padx=19.48, pady=10, command=Subtract, activebackground="#5D8AA6")
subtract.grid(row=0, column=4, pady=1, padx=1,)

# * #
multiply = tk.Button(entryPad, bg="#5D8AA6", text="x", padx=20, pady=10, command=Multiply, activebackground="#5D8AA6")
multiply.grid(row=1, column=3, pady=1, padx=1,)

# / #
divide = tk.Button(entryPad, bg="#5D8AA6", text="/", padx=19.48, pady=10, command=Divide, activebackground="#5D8AA6")
divide.grid(row=1, column=4, pady=1, padx=1,)

# = #
equals = tk.Button(entryPad, bg="#D7D7D9", text="=", padx=46, pady=10, command=Equals, activebackground="#D7D7D9")
equals.grid(row=2, column=3, pady=1, padx=1, columnspan=2)

# √ #
Sqrt = tk.Button(entryPad, bg="#5D8AA6", text="√", padx=19.48, pady=10, command=sqrt, activebackground="#5D8AA6")
Sqrt.grid(row=3, column=3, pady=1, padx=1, columnspan=1)

# ^ #
Sqr = tk.Button(entryPad, bg="#5D8AA6", text="^", padx=17, pady=10, command=sqr, activebackground="#5D8AA6")
Sqr.grid(row=3, column=4, pady=1, padx=1, columnspan=1)

#=========================CLEAR_BUTTONS=======================

# COMPLETE_CLEAR #
C = tk.Button(entryPad, bg="#fc8700", text="C", padx=43.2, pady=33, command=C, activebackground="black", activeforeground="#fc8700")
C.grid(row=0, column=5, rowspan=2, padx=1, pady=1)

# MAIN_FIELD_CLEAR #
CE = tk.Button(entryPad, bg="#fc8700", text="CE", padx=40, pady=10, command=CE, activebackground="black", activeforeground="#fc8700")
CE.grid(row=2, column=5, padx=1, pady=1)

# EXIT BUTTONS #
AC = tk.Button(entryPad, bg="#F24607", text="AC", padx=39.15, pady=10, command=AC, activebackground="black", activeforeground="#F24607")
AC.grid(row=3, column=5, padx=1, pady=1)

wrk = tk.Button(entryPad, bg="cyan", text="https://youtube.com/duffyyt", font="roboto 10",fg="black", command=duffy) #Shameless plug!
wrk.place(relheight=0.35, relwidth=0.8, relx=0.1, rely=0.6)

#=========================MENU_FUNCTIONS===================

#STANDARD#

def standard():

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
    num1 = tk.Button(StentryPad, bg="black", fg="white", text="1", pady=10, padx=20,command=num_1, activebackground="#262626", activeforeground="cyan")
    num1.grid(row=0, column=0, padx=1, pady=1)

    # 2 #
    num2 = tk.Button(StentryPad, bg="black", fg="white", text="2", pady=10, padx=20,command=num_2, activebackground="#262626", activeforeground="cyan")
    num2.grid(row=0, column=1, padx=1, pady=1)

    # 3 #
    num3 = tk.Button(StentryPad, bg="black", fg="white", text="3", pady=10, padx=20,command=num_3, activebackground="#262626", activeforeground="cyan")
    num3.grid(row=0, column=2, padx=1, pady=1)

    # 4 #
    num4 = tk.Button(StentryPad, bg="black", fg="white", text="4", pady=10, padx=20,command=num_4, activebackground="#262626", activeforeground="cyan")
    num4.grid(row=1, column=0, padx=1, pady=1)

    # 5 #
    num5 = tk.Button(StentryPad, bg="black", fg="white", text="5", pady=10, padx=20,command=num_5, activebackground="#262626", activeforeground="cyan")
    num5.grid(row=1, column=1, padx=1, pady=1)

    # 6 #
    num6 = tk.Button(StentryPad, bg="black", fg="white", text="6", pady=10, padx=20,command=num_6, activebackground="#262626", activeforeground="cyan")
    num6.grid(row=1, column=2, padx=1, pady=1)

    # 7 #
    num7 = tk.Button(StentryPad, bg="black", fg="white", text="7", pady=10, padx=20,command=num_7, activebackground="#262626", activeforeground="cyan")
    num7.grid(row=2, column=0, padx=1, pady=1)

    # 8 #
    num8 = tk.Button(StentryPad, bg="black", fg="white", text="8", pady=10, padx=20,command=num_8, activebackground="#262626", activeforeground="cyan")
    num8.grid(row=2, column=1, padx=1, pady=1)

    # 9 #
    num9 = tk.Button(StentryPad, bg="black", fg="white", text="9", pady=10, padx=20,command=num_9, activebackground="#262626", activeforeground="cyan")
    num9.grid(row=2, column=2, padx=1, pady=1)

    # 0 #
    num0 = tk.Button(StentryPad, bg="black", fg="white", text="0", pady=10, padx=20,command=num_0, activebackground="#262626", activeforeground="cyan")
    num0.grid(row=3, column=1, padx=1, pady=1,)

    # - #
    Negative = tk.Button(StentryPad, bg="#262626", fg="cyan", text="-", pady=10, padx=20,command=negative, activeforeground="white", activebackground="black")
    Negative.grid(row=3, column=0, padx=1, pady=1,)

    # . #
    decimal = tk.Button(StentryPad, bg="#262626", fg="cyan", text=".", pady=10, padx=21.499999999999998222,command=Decimal, activeforeground="white", activebackground="black")
    decimal.grid(row=3, column=2, padx=1, pady=1,)

    #========================OPERATOR_BUTTONS===========================

    # + #
    add = tk.Button(StentryPad, bg="#5D8AA6", text="+", padx=19.48, pady=10, command=Add, activebackground="#5D8AA6")
    add.grid(row=0, column=3, pady=1, padx=1,)

    # - #
    subtract = tk.Button(StentryPad, bg="#5D8AA6", text="-", padx=19.48, pady=10, command=Subtract, activebackground="#5D8AA6")
    subtract.grid(row=0, column=4, pady=1, padx=1,)

    # * #
    multiply = tk.Button(StentryPad, bg="#5D8AA6", text="x", padx=20, pady=10, command=Multiply, activebackground="#5D8AA6")
    multiply.grid(row=1, column=3, pady=1, padx=1,)

    # / #
    divide = tk.Button(StentryPad, bg="#5D8AA6", text="/", padx=19.48, pady=10, command=Divide, activebackground="#5D8AA6")
    divide.grid(row=1, column=4, pady=1, padx=1,)

    # = #
    equals = tk.Button(StentryPad, bg="#D7D7D9", text="=", padx=46, pady=10, command=Equals, activebackground="#D7D7D9")
    equals.grid(row=2, column=3, pady=1, padx=1, columnspan=2)

    # √ #
    Sqrt = tk.Button(StentryPad, bg="#5D8AA6", text="√", padx=19.48, pady=10, command=sqrt, activebackground="#5D8AA6")
    Sqrt.grid(row=3, column=3, pady=1, padx=1, columnspan=1)

    # ^ #
    Sqr = tk.Button(StentryPad, bg="#5D8AA6", text="^", padx=17, pady=10, command=sqr, activebackground="#5D8AA6")
    Sqr.grid(row=3, column=4, pady=1, padx=1, columnspan=1)

    #=========================CLEAR_BUTTONS=======================

    # COMPLETE_CLEAR #
    C = tk.Button(StentryPad, bg="#fc8700", text="C", padx=43.2, pady=33, command=CSt, activebackground="black", activeforeground="#fc8700")
    C.grid(row=0, column=5, rowspan=2, padx=1, pady=1)

    # MAIN_FIELD_CLEAR #
    CE = tk.Button(StentryPad, bg="#fc8700", text="CE", padx=40, pady=10, command=CESt, activebackground="black", activeforeground="#fc8700")
    CE.grid(row=2, column=5, padx=1, pady=1)

    # EXIT BUTTONS #
    AC= tk.Button(StentryPad, bg="#F24607", text="AC", padx=39.15, pady=10, command=ACSt, activebackground="black", activeforeground="#F24607")
    AC.grid(row=3, column=5, padx=1, pady=1)

    wrk = tk.Button(StentryPad, bg="cyan", text="https://youtube.com/duffyyt", font="roboto 10",fg="black", command=duffy)
    wrk.place(relheight=0.35, relwidth=0.8, relx=0.1, rely=0.6)

#SCIENTIFIC#

def scientific():

    global trig
    trig = 'rad'

    def Rad():
        global trig
        deg.config(fg="gray")
        rad.config(fg="black")
        trig = 'rad'       

    def Deg():
        global trig
        rad.config(fg="gray")
        deg.config(fg="black")
        trig = 'deg'
    
    def ACS():
        window.destroy()

    def CES():
        field.delete(0,END)

    def CS():
        field.delete(0,END)
        upperAns.delete(0,END)
        upperField.delete(0, END)

    def Sin():
        if trig == 'rad':
            x=float(field.get())
            siner = math.sin(x)
            field.delete(0, END)
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"sin" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
        if trig == 'deg':
            x=float(field.get())
            siner = math.sin(math.radians(x))
            field.delete(0, END)
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"sin" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
    
    def Cos():
        if trig == 'rad':
            x=float(field.get())
            siner = math.cos(x)
            field.delete(0, END)
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"cos" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
        if trig == 'deg':
            x=float(field.get())
            siner = math.cos(math.radians(x))
            field.delete(0, END)
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"cos" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")

    def Tan():
        if trig == 'rad':
            x=float(field.get())
            siner = math.tan(x)
            field.delete(0, END)
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"tan" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
        if trig == 'deg':
            x=float(field.get())
            siner = math.tan(math.radians(x))
            field.delete(0, END)
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"tan" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")

    def Csc():
        if trig == 'rad':
            x=float(field.get())
            c_siner = math.sin(x)
            siner = 1/c_siner
            field.delete(0, END)
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"Csc" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
        if trig == 'deg':
            x=float(field.get())
            c_siner = math.sin(math.radians(x))
            siner = 1/c_siner
            field.delete(0, END)
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"Csc" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")

    def Sec():
        if trig == 'rad':
            x=float(field.get())
            c_siner = math.cos(x)
            siner = 1/c_siner
            field.delete(0, END)
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"Sec" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
        if trig == 'deg':
            x=float(field.get())
            c_siner = math.cos(math.radians(x))
            siner = 1/c_siner
            field.delete(0, END)
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"sec" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")

    def Cot():
        if trig == 'rad':
            x=float(field.get())
            c_siner = math.tan(x)
            siner = 1/c_siner
            field.delete(0, END)
            upperField.delete(0, END)
            upperField.insert(0, siner)
            upperAns.delete(0, END),
            upperAns.insert(0,"Cot" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
        if trig == 'deg':
            x=float(field.get())
            c_siner = math.tan(math.radians(x))
            siner = 1/c_siner
            field.delete(0, END)
            upperField.delete(0, END)
            upperField.insert(0, siner  )
            upperAns.delete(0, END),
            upperAns.insert(0,"Cot" + "(" + str(x) + ")")
            upperOperator.delete(0, END)
            upperOperator.insert(0, "📐")
    
    def Pi():
        field.delete(0, END)
        field.insert(0, 2384626433832795)
        field.insert(0, 3.141592653589793)

    SentryPad = tk.LabelFrame(window, bg="black")
    SentryPad.place(relheight=0.65, relwidth=0.98, relx=0.01, rely=0.34)
    # 1 #
    num1 = tk.Button(SentryPad, bg="black", fg="white", text="1", pady=10, padx=20,command=num_1, activebackground="#262626", activeforeground="cyan")
    num1.grid(row=1, column=0, padx=1, pady=1)

    # 2 #
    num2 = tk.Button(SentryPad, bg="black", fg="white", text="2", pady=10, padx=20,command=num_2, activebackground="#262626", activeforeground="cyan")
    num2.grid(row=1, column=1, padx=1, pady=1)

    # 3 #
    num3 = tk.Button(SentryPad, bg="black", fg="white", text="3", pady=10, padx=20,command=num_3, activebackground="#262626", activeforeground="cyan")
    num3.grid(row=1, column=2, padx=1, pady=1)

    # 4 #
    num4 = tk.Button(SentryPad, bg="black", fg="white", text="4", pady=10, padx=20,command=num_4, activebackground="#262626", activeforeground="cyan")
    num4.grid(row=2, column=0, padx=1, pady=1)

    # 5 #
    num5 = tk.Button(SentryPad, bg="black", fg="white", text="5", pady=10, padx=20,command=num_5, activebackground="#262626", activeforeground="cyan")
    num5.grid(row=2, column=1, padx=1, pady=1)

    # 6 #
    num6 = tk.Button(SentryPad, bg="black", fg="white", text="6", pady=10, padx=20,command=num_6, activebackground="#262626", activeforeground="cyan")
    num6.grid(row=2, column=2, padx=1, pady=1)

    # 7 #
    num7 = tk.Button(SentryPad, bg="black", fg="white", text="7", pady=10, padx=20,command=num_7, activebackground="#262626", activeforeground="cyan")
    num7.grid(row=3, column=0, padx=1, pady=1)

    # 8 #
    num8 = tk.Button(SentryPad, bg="black", fg="white", text="8", pady=10, padx=20,command=num_8, activebackground="#262626", activeforeground="cyan")
    num8.grid(row=3, column=1, padx=1, pady=1)

    # 9 #
    num9 = tk.Button(SentryPad, bg="black", fg="white", text="9", pady=10, padx=20,command=num_9, activebackground="#262626", activeforeground="cyan")
    num9.grid(row=3, column=2, padx=1, pady=1)

    # 0 #
    num0 = tk.Button(SentryPad, bg="black", fg="white", text="0", pady=10, padx=20,command=num_0, activebackground="#262626", activeforeground="cyan")
    num0.grid(row=4, column=1, padx=1, pady=1,)

    # - #
    Negative = tk.Button(SentryPad, bg="#262626", fg="cyan", text="-", pady=10, padx=20,command=negative, activebackground="black", activeforeground="white")
    Negative.grid(row=4, column=0, padx=1, pady=1,)

    # . #
    decimal = tk.Button(SentryPad, bg="#262626", fg="cyan", text=".", pady=10, padx=21.499999999999998222,command=Decimal, activebackground="black", activeforeground="white")
    decimal.grid(row=4, column=2, padx=1, pady=1,)

    #========================OPERATOR_BUTTONS===========================

    # + #
    add = tk.Button(SentryPad, bg="#5D8AA6", text="+", padx=19.48, pady=10, command=Add, activebackground="#5D8AA6")
    add.grid(row=1, column=3, pady=1, padx=1,)

    # - #
    subtract = tk.Button(SentryPad, bg="#5D8AA6", text="-", padx=19.48, pady=10, command=Subtract, activebackground="#5D8AA6")
    subtract.grid(row=1, column=4, pady=1, padx=1,)

    # * #
    multiply = tk.Button(SentryPad, bg="#5D8AA6", text="x", padx=20, pady=10, command=Multiply, activebackground="#5D8AA6")
    multiply.grid(row=2, column=3, pady=1, padx=1,)

    # / #
    divide = tk.Button(SentryPad, bg="#5D8AA6", text="/", padx=19.48, pady=10, command=Divide, activebackground="#5D8AA6")
    divide.grid(row=2, column=4, pady=1, padx=1,)

    # = #
    equals = tk.Button(SentryPad, bg="#D7D7D9", text="=", padx=46, pady=10, command=Equals, activebackground="#D7D7D9")
    equals.grid(row=3, column=3, pady=1, padx=1, columnspan=2)

    # √ #
    Sqrt = tk.Button(SentryPad, bg="#5D8AA6", text="√", padx=19.48, pady=10, command=sqrt,activebackground="#5D8AA6")
    Sqrt.grid(row=4, column=3, pady=1, padx=1, columnspan=1)

    # ^ #
    Sqr = tk.Button(SentryPad, bg="#5D8AA6", text="^", padx=17, pady=10, command=sqr, activebackground="#5D8AA6")
    Sqr.grid(row=4, column=4, pady=1, padx=1, columnspan=1)

    #========================TRIGNOMETRY========================

    #sin#
    sin = tk.Button(SentryPad, bg="#C6FC00", text="sin", padx=15.45 , pady=10, command=Sin)
    sin.grid(row=0, column=0, padx=1, pady=1,)

    #cos#
    cos = tk.Button(SentryPad, bg="#B3D600", text="cos", padx=14 , pady=10, command=Cos)
    cos.grid(row=0, column=1, padx=1, pady=1,)

    #tan#
    tan = tk.Button(SentryPad, bg="#8AB000", text="tan", padx=14.45 , pady=10, command=Tan)
    tan.grid(row=0, column=2, padx=1, pady=1,)

    #cosec#
    csc = tk.Button(SentryPad, bg="#C6FC00", text="csc", padx=15 , pady=10, command=Csc)
    csc.grid(row=0, column=3, padx=1, pady=1,)

    #secent#
    sec = tk.Button(SentryPad, bg="#B3D600", text="sec", padx=13 , pady=10, command=Sec)
    sec.grid(row=0, column=4, padx=1, pady=1,)

    #cotangent#
    cot = tk.Button(SentryPad, bg="#8AB000", text="cot", padx=12.3 , pady=10, command=Cot)
    cot.grid(row=0, column=5, padx=1, pady=1,)

    #PI#
    pi = tk.Button(SentryPad, bg="#9D69F0", text="π", padx=16.5 , pady=10, command=Pi)
    pi.grid(row=0, column=6, padx=1, pady=1,)

    #RADIAN#
    rad = tk.Button(SentryPad, bg="#d4ff00", text="RAD", padx=10, pady=10, command=Rad)
    rad.grid(row=5, column=2, padx=1, pady=1,)

    #DEGREES#
    deg = tk.Button(SentryPad, bg="#d4ff00", text="DEG", padx=10, pady=10, command=Deg, fg="gray")
    deg.grid(row=5, column=3, padx=1, pady=1,)

    #=========================CLEAR_BUTTONS=======================

    # COMPLETE_CLEAR #
    C = tk.Button(SentryPad, bg="#fc8700", text="C", padx=43.2, pady=33, command=CS, activebackground="black", activeforeground="#fc8700")
    C.grid(row=1, column=5, rowspan=2, padx=1, pady=1, columnspan=2)

    # MAIN_FIELD_CLEAR #
    CE = tk.Button(SentryPad, bg="#fc8700", text="CE", padx=40, pady=10, command=CES, activebackground="black", activeforeground="#fc8700")
    CE.grid(row=3, column=5, padx=1, pady=1, columnspan=2)

    # EXIT BUTTONS #
    AC= tk.Button(SentryPad, bg="#F24607", text="AC", padx=39.15, pady=10, command=ACS, activebackground="black", activeforeground="#F24607")
    AC.grid(row=4, column=5, padx=1, pady=1, columnspan=2)

#WEIGHTS#

def weight():

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
        temp = entry1.get()
        entry1.delete(0,END)
        entry1.insert(0,str(temp) + str(1))
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

    def W_2():
        temp = entry1.get()
        entry1.delete(0,END)
        entry1.insert(0,str(temp) + str(2))
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

    def W_3():
        temp = entry1.get()
        entry1.delete(0,END)
        entry1.insert(0,str(temp) + str(3))
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

    def W_4():
        temp = entry1.get()
        entry1.delete(0,END)
        entry1.insert(0,str(temp) + str(4))
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

    def W_5():
        temp = entry1.get()
        entry1.delete(0,END)
        entry1.insert(0,str(temp) + str(5))
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

    def W_6():
        temp = entry1.get()
        entry1.delete(0,END)
        entry1.insert(0,str(temp) + str(6))
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

    def W_7():
        temp = entry1.get()
        entry1.delete(0,END)
        entry1.insert(0,str(temp) + str(7))
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

    def W_8():
        temp = entry1.get()
        entry1.delete(0,END)
        entry1.insert(0,str(temp) + str(8))
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

    def W_9():
        temp = entry1.get()
        entry1.delete(0,END)
        entry1.insert(0,str(temp) + str(9))
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

    def W_0():
        temp = entry1.get()
        entry1.delete(0,END)
        entry1.insert(0,str(temp) + str(0))
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
            
    def W_Decimal():
        temp = entry1.get()
        entry1.delete(0,END)
        entry1.insert(0,str(temp) + ".")
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

    def Copy1():
        window.clipboard_clear()
        window.clipboard_append(entry1.get())
    def Copy2():
        window.clipboard_clear()
        window.clipboard_append(entry2.get())
    def Paste1():
        entry1.insert(0, float(window.clipboard_get()))
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
        
    WentryPad = tk.LabelFrame(window, bg="black")
    WentryPad.place(relheight=0.65, relwidth=0.98, relx=0.01, rely=0.34)

    con = tk.Entry(WentryPad, bg="red", border=0, borderwidth=0, justify=CENTER, state=DISABLED)
    con.place(relheight=0.05, relwidth=0.2, relx=0.15, rely=0.34)
    con.config(state='normal')
    con.insert(0, "KilloGrams")
    con.config(state='disabled')

    con1 = tk.Entry(WentryPad, bg="red", border=0, borderwidth=0, justify=CENTER, state=DISABLED)
    con1.place(relheight=0.05, relwidth=0.2, relx=0.15, rely=0.47)
    con1.config(state='normal')
    con1.insert(0, "Grams")
    con1.config(state='disabled')

    con2 = tk.Entry(WentryPad, bg="white", border=0, borderwidth=0, justify=CENTER, state=DISABLED)
    con2.place(relheight=0.05, relwidth=0.05, relx=0.225, rely=0.405)
    con2.config(state='normal')
    con2.insert(0, "⬇")
    con2.config(state='disabled', takefocus=True)

    entry1 = tk.Entry(WentryPad, bg="black", fg = "white", borderwidth=0)
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

    entry2 = tk.Entry(WentryPad, bg="black", fg = "white", borderwidth=0)
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

    num1 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="1", command=W_1, activebackground="#262626", activeforeground="cyan")
    num1.place(relheight=0.17, relwidth=0.13, rely=0.01, relx=0.58)

    num2 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="2", command=W_2, activebackground="#262626", activeforeground="cyan")
    num2.place(relheight=0.17, relwidth=0.13, rely=0.01, relx=0.72)

    num3 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="3", command=W_3, activebackground="#262626", activeforeground="cyan")
    num3.place(relheight=0.17, relwidth=0.13, rely=0.01, relx=0.86)

    num4 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="4", command=W_4, activebackground="#262626", activeforeground="cyan")
    num4.place(relheight=0.17, relwidth=0.13, rely=0.19, relx=0.58)

    num5 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="5", command=W_5, activebackground="#262626", activeforeground="cyan")
    num5.place(relheight=0.17, relwidth=0.13, rely=0.19, relx=0.72)

    num6 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="6", command=W_6, activebackground="#262626", activeforeground="cyan")
    num6.place(relheight=0.17, relwidth=0.13, rely=0.19, relx=0.86)

    num7 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="7", command=W_7, activebackground="#262626", activeforeground="cyan")
    num7.place(relheight=0.17, relwidth=0.13, rely=0.37, relx=0.58)

    num8 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="8", command=W_8, activebackground="#262626", activeforeground="cyan")
    num8.place(relheight=0.17, relwidth=0.13, rely=0.37, relx=0.72)

    num9 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="9", command=W_9, activebackground="#262626", activeforeground="cyan")
    num9.place(relheight=0.17, relwidth=0.13, rely=0.37, relx=0.86)

    num0 = tk.Button(WentryPad, bg="black",fg="white", font="calibri 10", text="0", command=W_0, activebackground="#262626", activeforeground="cyan")
    num0.place(relheight=0.17, relwidth=0.13, rely=0.55, relx=0.72)

    decimal = tk.Button(WentryPad, bg="black", fg="cyan", text=".", command=W_Decimal, activebackground="black", activeforeground="white")
    decimal.place(relheight=0.17, relwidth=0.13, rely=0.55, relx=0.86)

    C = tk.Button(WentryPad, bg="#fc8700", font="calibri 10", text="C", command=CW, activebackground="black", activeforeground="#fc8700")
    C.place(relheight=0.17, relwidth=0.13, rely=0.55, relx=0.58)

    CE = tk.Button(WentryPad, bg="#fc8700", font="calibri 10", text="CE", command=CEW, activebackground="black", activeforeground="#fc8700")
    CE.place(relheight=0.17, relwidth=0.13, rely=0.73, relx=0.58)

    AC = tk.Button(WentryPad, bg="#F24607", font="calibri 10", text="AC",command=ACW, activebackground="black", activeforeground="#F24607")
    AC.place(relheight=0.17, relwidth=0.27, rely=0.73, relx=0.72)

#TIME#

def time():
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

    def CET():
        Tentry1.delete(0, END)

    def T_1():
        temp = Tentry1.get()
        Tentry1.delete(0,END)
        Tentry1.insert(0,str(temp) + str(1))
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

    def T_2():
        temp = Tentry1.get()
        Tentry1.delete(0,END)
        Tentry1.insert(0,str(temp) + str(2))
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

    def T_3():
        temp = Tentry1.get()
        Tentry1.delete(0,END)
        Tentry1.insert(0,str(temp) + str(3))
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

    def T_4():
        temp = Tentry1.get()
        Tentry1.delete(0,END)
        Tentry1.insert(0,str(temp) + str(4))
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

    def T_5():
        temp = Tentry1.get()
        Tentry1.delete(0,END)
        Tentry1.insert(0,str(temp) + str(5))
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

    def T_6():
        temp = Tentry1.get()
        Tentry1.delete(0,END)
        Tentry1.insert(0,str(temp) + str(6))
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

    def T_7():
        temp = Tentry1.get()
        Tentry1.delete(0,END)
        Tentry1.insert(0,str(temp) + str(7))
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

    def T_8():
        temp = Tentry1.get()
        Tentry1.delete(0,END)
        Tentry1.insert(0,str(temp) + str(8))
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

    def T_9():
        temp = Tentry1.get()
        Tentry1.delete(0,END)
        Tentry1.insert(0,str(temp) + str(9))
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

    def T_0():
        temp = Tentry1.get()
        Tentry1.delete(0,END)
        Tentry1.insert(0,str(temp) + str(0))
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
            
    def T_Decimal():
        temp = Tentry1.get()
        Tentry1.delete(0,END)
        Tentry1.insert(0,str(temp) + ".")
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

    def Copy1():
        window.clipboard_clear()
        window.clipboard_append(Tentry1.get())
    def Copy2():
        window.clipboard_clear()
        window.clipboard_append(Tentry2.get())
    def Paste1():
        Tentry1.insert(0, float(window.clipboard_get()))
        if Tonverter == 'ms':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) * 200
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) / 5
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) / 5000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) / 4.536e+6
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 'y':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'ms':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 142
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        #mg#
        if Tonverter == 's':
            if Tonverter2 == 's':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) / 200
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) / 1000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) / 1e+6
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) / 9.072e+8
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'y':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 's':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 28350
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'm':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 5
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) * 1000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) / 1000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) / 907185
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'y':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'm':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 28.35
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'h':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 5000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) / 1e+6
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) * 1000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) / 907
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'y':
                co = float(Tentry1.get()) * 35.274
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'h':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) * 2.205
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'd':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 4.536e+6
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) * 9.072e+8
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) * 907185
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) * 907
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'y':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'd':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) * 32000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'y':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 142
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) * 28350
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) * 28.35
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) / 35.274
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) / 32000
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'h':
                co = float(Tentry1.get())
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) / 16
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'y':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 16
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'c':
                co = float(Tentry1.get()) / 16
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'ms':
                co = float(Tentry1.get()) / 16
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 's':
                co = float(Tentry1.get()) / 16
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'm':
                co = float(Tentry1.get()) / 16
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'h':
                co = float(Tentry1.get()) / 16
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'd':
                co = float(Tentry1.get()) / 16
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        if Tonverter == 'c':
            if Tonverter2 == 'y':
                co = float(Tentry1.get()) / 16
                Tentry2.delete(0, END)
                Tentry2.insert(0,co)
        
    TentryPad = tk.LabelFrame(window, bg="black")
    TentryPad.place(relheight=0.65, relwidth=0.98, relx=0.01, rely=0.34)

    Tcon = tk.Entry(TentryPad, bg="red", border=0, borderwidth=0, justify=CENTER, state=DISABLED)
    Tcon.place(relheight=0.05, relwidth=0.2, relx=0.15, rely=0.34)
    Tcon.config(state='normal')
    Tcon.insert(0, "Minute")
    Tcon.config(state='disabled')

    Tcon1 = tk.Entry(TentryPad, bg="red", border=0, borderwidth=0, justify=CENTER, state=DISABLED)
    Tcon1.place(relheight=0.05, relwidth=0.2, relx=0.15, rely=0.47)
    Tcon1.config(state='normal')
    Tcon1.insert(0, "Seconds")
    Tcon1.config(state='disabled')

    Tcon2 = tk.Entry(TentryPad, bg="red", border=0, borderwidth=0, justify=CENTER, state=DISABLED)
    Tcon2.place(relheight=0.05, relwidth=0.05, relx=0.225, rely=0.405)
    Tcon2.config(state='normal')
    Tcon2.insert(0, "⬇")
    Tcon2.config(state='disabled')

    Tentry1 = tk.Entry(TentryPad, bg="black", fg = "white", borderwidth=0)
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

    Tentry2 = tk.Entry(TentryPad, bg="black", fg = "white", borderwidth=0)
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

    num1 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="1", command=T_1, activebackground="#262626", activeforeground="cyan")
    num1.place(relheight=0.17, relwidth=0.13, rely=0.01, relx=0.58)

    num2 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="2", command=T_2, activebackground="#262626", activeforeground="cyan")
    num2.place(relheight=0.17, relwidth=0.13, rely=0.01, relx=0.72)

    num3 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="3", command=T_3, activebackground="#262626", activeforeground="cyan")
    num3.place(relheight=0.17, relwidth=0.13, rely=0.01, relx=0.86)

    num4 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="4", command=T_4, activebackground="#262626", activeforeground="cyan")
    num4.place(relheight=0.17, relwidth=0.13, rely=0.19, relx=0.58)

    num5 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="5", command=T_5, activebackground="#262626", activeforeground="cyan")
    num5.place(relheight=0.17, relwidth=0.13, rely=0.19, relx=0.72)

    num6 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="6", command=T_6, activebackground="#262626", activeforeground="cyan")
    num6.place(relheight=0.17, relwidth=0.13, rely=0.19, relx=0.86)

    num7 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="7", command=T_7, activebackground="#262626", activeforeground="cyan")
    num7.place(relheight=0.17, relwidth=0.13, rely=0.37, relx=0.58)

    num8 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="8", command=T_8, activebackground="#262626", activeforeground="cyan")
    num8.place(relheight=0.17, relwidth=0.13, rely=0.37, relx=0.72)

    num9 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="9", command=T_9, activebackground="#262626", activeforeground="cyan")
    num9.place(relheight=0.17, relwidth=0.13, rely=0.37, relx=0.86)

    num0 = tk.Button(TentryPad, bg="black", fg="white", font="calibri 10", text="0", command=T_0, activebackground="#262626", activeforeground="cyan")
    num0.place(relheight=0.17, relwidth=0.13, rely=0.55, relx=0.72)

    decimal = tk.Button(TentryPad, bg="black", fg="cyan", text=".", command=T_Decimal, activebackground="#262626", activeforeground="white")
    decimal.place(relheight=0.17, relwidth=0.13, rely=0.55, relx=0.86)

    C = tk.Button(TentryPad, bg="#fc8700", font="calibri 10", text="C", command=CT, activebackground="black", activeforeground="#fc8700")
    C.place(relheight=0.17, relwidth=0.13, rely=0.55, relx=0.58)

    CE = tk.Button(TentryPad, bg="#fc8700", font="calibri 10", text="CE", command=CET, activebackground="black", activeforeground="#fc8700")
    CE.place(relheight=0.17, relwidth=0.13, rely=0.73, relx=0.58)

    AC = tk.Button(TentryPad, bg="#F24607", font="calibri 10", text="AC",command=ACT, activebackground="black", activeforeground="#F24607")
    AC.place(relheight=0.17, relwidth=0.27, rely=0.73, relx=0.72)

#HISTORY

def history():
    global counter
    global winCounter

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

        bb=0

        for meme in reversed(memory):
            if len(meme) < 15:
                mlist.insert(END,meme)
            else:
                pass
        counter +=1
    else:
        HentryPad.destroy()
        counter = 0

#=========MENU_BUTTONS==========

# STANDARD #                                                                                 
standard = tk.Button(menu, bg="#BF907E", text="Standard", command=standard,)                          
standard.place(relheight=0.94, relwidth=0.2, rely=0.02, relx=0.01)    

# SCIENTIFIC #                                                                                 
scientific = tk.Button(menu, bg="#BF907E", text="Scientific", command=scientific)                      
scientific.place(relheight=0.94, relwidth=0.2, rely=0.02, relx=0.22)                                           
                                
# WIEGHTS #                                                                                 
weight = tk.Button(menu, bg="#BF907E", text="    Weights   ", command=weight)                      
weight.place(relheight=0.94, relwidth=0.2, rely=0.02, relx=0.43)   

# TIME #                                                                                 
time = tk.Button(menu, bg="#BF907E", text="      Time      ", command=time)                      
time.place(relheight=0.94, relwidth=0.2, rely=0.02, relx=0.64)   

#HISTORY#

history = tk.Button(menu, bg="#d4ff00", text="HISTORY", command=history)
history.place(relheight=0.94, relwidth=0.143, rely=0.02, relx=0.85)   

#================MAINLOOP===================

tk.mainloop()
#===============File_open==================

with open('mem.txt', 'w+',encoding="utf-8")as f:
    for mem in memory:
        if mem=='':
            pass
        else:
            f.write(mem + ',')
            
#=============CREDITS===============#
# Made by THIRUCHLVAN (AKA) DUFFY
# MY YOUTUBE CHANNEL:- https://youtube.com/duffyyt