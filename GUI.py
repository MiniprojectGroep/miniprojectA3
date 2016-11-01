from tkinter import *
import math
import login

global root
root = Tk()

# Alle Menu's (GUI windows)
def showTextMenu(text): # menu dat wordt gebruikt om de QR code, code na betaling of een ander bericht te weergeven
    pass

def hideTextMenu(): # verberg het TextMenu
    pass

def showBeginMenu(): # het begin menu waar de gebruiker kan kiezen of het een bezoeker (gebruiker) of een aanbieder is
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

def hideBeginMenu(): # verberg het BeginMenu
    linkerBeginFrame.destroy()
    rechterBeginFrame.destroy()
    beginLabel.destroy()

def showKaartMenu(): # In dit menu moet de bezoeker een film kiezen. De bezoeker kan kiezen of hij een kaartje wilt kopen, of dat hij al in bezit is van een kaartje.
    pass

def hideKaartMenu(): # verberg het KaartMenu
    pass

def showBetalingsMenu(): # In dit menu moet de bezoeker zijn naam, email invullen en daarna betalen. Suggestie: misschien leuk om ook iets van een prijs te gebruiken, en dat de prijs wordt gebaseerd op de IMDB rating (2 * IMDB rating = prijs). Verder eventueel nog zaken zoals: weekend korting, kinder/senior korting. Maar dat hangt af of we tijd overhouden of niet.
    pass

def hideBetalingsMenu(): # verberg het betalings menu
    pass

def showLoginMenu(): # in dit menu moet de bezoeker inloggen met zijn naam en code. De aanbieder kan hier inloggen met zijn wachtwoord en gebruikersnaam. (Via SQLite3)
    pass

def hideLoginMenu(): # verberg het login menu
    pass

def showAanbiedersMenu(): #speciaal menu voor de aanbieder, hierkan hij een overzicht zien van alle films die niet worden aangeboden door een andere aanbieder, overzicht van alle films, overzicht val alle bezoekers die bij deze aanbieder zitten, aanmeldcode controleren
    pass

def hideAanbiedersMenu(): # verberg het AanbiedersMenu
    pass

# functies voor knoppen (buttons)
def aanbieder_menu(): # Wordt gebruikt om de keuze te onthouden en naar het volgende menu te gaan
    #frame.pack_forget() kan een memory leak veroorzaken, probeer deze te vermijden!
    hideBeginMenu()
    global keuze
    keuze = 'aanbieder'
    showLoginMenu()

def gebruiker_menu(): # Zie aanbieder_menu
    hideBeginMenu()
    global keuze
    keuze = 'gebruiker'
    showKaartMenu()

# start de GUI
showBeginMenu()
