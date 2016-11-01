from tkinter import *
import math
root = Tk()

'''
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
'''
def beginMenu():

    # Maak 4 globale frames
    global linkerFrame
    linkerFrame = Frame(master=root)
    linkerFrame.pack(side=LEFT)

    global rechterframe
    rechterFrame = Frame(master=root)
    rechterFrame.pack(side=RIGHT)

    global bovenFrame
    bovenFrame = Frame(master=root)
    bovenFrame.pack(side=TOP)

    global benedenFrame
    benedenFrame = Frame(master=root)
    benedenFrame.pack(side=BOTTOM)

    global keuzeFrame
    keuzeFrame = Frame(master=root)
    keuzeFrame.pack(side=LEFT)

    global rechterLabelFrame
    rechterLabelFrame = LabelFrame(rechterFrame, text="Main Window")
    rechterLabelFrame.pack(fill="both", expand="yes")

    global keuzeLabel
    keuzeLabel = Label(master=rechterLabelFrame,text='Bent U een gebruiker of bent U een aanbieder?',background='darkgrey',foreground='blue',font=('Helvetica',10,'bold italic'),width=100,height=10)
    keuzeLabel.pack()

    createButton_aanbieder()
    createButton_gebruiker()

    root.mainloop()

def loginMenu():
    pass

def createButton_aanbieder():
    global button_aanbieder
    button_aanbieder = Button(master=keuzeFrame,command=aanbieder_menu,text='Aanbieder',height=3,width=20)
    button_aanbieder.pack(side=LEFT,pady=4,padx=25)

def createButton_gebruiker():
    global button_gebruiker
    button_gebruiker = Button(master=keuzeFrame,command=gebruiker_menu,text='Gebruiker',height=3,width=20)
    button_gebruiker.pack(side=RIGHT,pady=4,padx=25)

def aanbieder_menu():
    #keuzeframe.pack_forget() kan een memory leak veroorzaken
    keuzeFrame.destroy()

def gebruiker_menu():
    keuzeFrame.destroy()


def beginMenu():

    # Maak 4 globale frames
    global linkerFrame
    linkerFrame = Frame(master=root)
    linkerFrame.pack(side=LEFT)

    global rechterframe
    rechterFrame = Frame(master=root)
    rechterFrame.pack(side=RIGHT)

    global bovenFrame
    bovenFrame = Frame(master=root)
    bovenFrame.pack(side=TOP)

    global benedenFrame
    benedenFrame = Frame(master=root)
    benedenFrame.pack(side=BOTTOM)

    global keuzeFrame
    keuzeFrame = Frame(master=root)
    keuzeFrame.pack(side=LEFT)

    global rechterLabelFrame
    rechterLabelFrame = LabelFrame(rechterFrame, text="Main Window")
    rechterLabelFrame.pack(fill="both", expand="yes")

    global keuzeLabel
    keuzeLabel = Label(master=rechterLabelFrame,text='Bent U een gebruiker of bent U een aanbieder?',background='darkgrey',foreground='blue',font=('Helvetica',10,'bold italic'),width=100,height=10)
    keuzeLabel.pack()

    createButton_aanbieder()
    createButton_gebruiker()

    root.mainloop()

beginMenu()
