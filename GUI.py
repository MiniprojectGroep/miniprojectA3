from tkinter import *
import math
import login

login.login() # Test

global root
root = Tk()

def showBeginMenu():
    global linkerBeginFrame
    linkerBeginFrame = Frame(master=root)
    linkerBeginFrame.pack(side=LEFT)

    global rechterBeginFrame
    rechterBeginFrame = Frame(master=root)
    rechterBeginFrame.pack(side=RIGHT)

    global beginLabel
    beginLabel = Label(master=rechterBeginFrame,text='Bent U een gebruiker of bent U een aanbieder?',background='darkgrey',foreground='blue',font=('Helvetica',10,'bold italic'),width=100,height=10)
    beginLabel.pack()

    global beginAanbiederButton
    buttonAanbiederButton = Button(master=linkerBeginFrame,command=aanbieder_menu,text='Aanbieder',height=3,width=20)
    buttonAanbiederButton.pack(side=LEFT,pady=4,padx=25)

    global beginGebruikerButton
    beginGebruikerButton = Button(master=linkerBeginFrame,command=gebruiker_menu,text='Gebruiker',height=3,width=20)
    beginGebruikerButton.pack(side=RIGHT,pady=4,padx=25)

    root.mainloop()

def hideBeginMenu():
    linkerBeginFrame.destroy()
    rechterBeginFrame.destroy()
    beginLabel.destroy()

def loginMenu():
    pass

def aanbieder_menu():
    #frame.pack_forget() kan een memory leak veroorzaken, probeer deze te vermijden!
    hideBeginMenu()
    global keuze
    keuze = 'aanbieder'

def gebruiker_menu():
    hideBeginMenu()
    global keuze
    keuze = 'gebruiker'

# start de GUI
showBeginMenu()
