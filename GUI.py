# Modules
from tkinter import *
import math
import sqlite3

# Nodig voor een afbeelding
from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk
# http://stackoverflow.com/questions/18562771/how-to-display-a-png-file-from-a-webpage-on-a-tk-label-in-python

# Bestandsnamen
import sql
import API
import common

root = Tk()
databaseNaam = 'Thuisbioscoop.db'
xmlNaam = 'films.xml'

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
    global bovenKaartFrame
    bovenKaartFrame = Frame(master=root)
    bovenKaartFrame.pack(side=TOP)

    global middenKaartFrame
    middenKaartFrame = Frame(master=bovenKaartFrame)
    middenKaartFrame.pack(side=BOTTOM)

    global onderKaartFrame
    onderKaartFrame = Frame(master=root)
    onderKaartFrame.pack(side=BOTTOM)

    global kaartLabel
    kaartLabel = Label(master=bovenKaartFrame,text='Voor vandaag zijn er de volgende films op televisie',background='darkgrey',foreground='blue',font=('Helvetica',10,'bold italic'),width=50,height=10)
    kaartLabel.pack(side=RIGHT)

    global filmAfbeelding
    filmAfbeelding = Label(master=bovenKaartFrame,image=None,background='black',width=20,height=10)
    filmAfbeelding.pack( fill = Y)

    scrollbar = Scrollbar(master=middenKaartFrame)
    scrollbar.pack( side = LEFT, fill=Y )

    global filmListbox
    filmListbox = Listbox(master=middenKaartFrame, selectmode=SINGLE,width=50, yscrollcommand=scrollbar.set)
    global filmLijst
    filmLijst = common.getFilms(xmlNaam)

    for film in filmLijst:
        filmListbox.insert(film[5], '{}'.format(film[0]))

    filmListbox.pack(side = LEFT)
    scrollbar.config( command = filmListbox.yview )

    extraInfoButton = Button(master=middenKaartFrame,command=extraInfo,text='Meer informatie',height=3,width=30)
    extraInfoButton.pack(side=RIGHT,pady=4,padx=25)

    bestelKaartButton = Button(master=onderKaartFrame,command=bestelKaart,text='Bestel',height=3,width=30)
    bestelKaartButton.pack(side=LEFT,pady=4,padx=25)

    kaartIsBesteldButton = Button(master=onderKaartFrame,command=kaartIsBesteld,text='Ik heb al een kaartje',height=3,width=20)
    kaartIsBesteldButton.pack(side=RIGHT,pady=4,padx=25)

    terug = Button(master=onderKaartFrame,command=kaartIsBesteld,text='Vorig menu',height=3,width=20)
    terug.pack(side=RIGHT,pady=4,padx=25)

    root.mainloop()

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

def bestelKaart():
    pass

def kaartIsBesteld():
    pass

def extraInfo():
    tuple_getal = str(filmListbox.curselection())
    film = tuple_getal[1]
    film = int(film)
    text = 'Titel: {} \nGenre: {}\n Jaar: {}\nIMDB rating: {}'.format(filmLijst[film][0],filmLijst[film][1],filmLijst[film][2],filmLijst[film][3])
    kaartLabel['text'] = text

    # Nodig om een afbeelding via URL weer te geven
    url = filmLijst[film][4]
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()
    im = Image.open(BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)

    # Afbeelding moet een resize krijgen, deze methode zorgt er alleen voor dat de lengte en de breedte past. Afbeelding kan dus niet volledig worden weergegeven.

    filmAfbeelding['image'] = image
    filmAfbeelding['height'] = 150
    filmAfbeelding['width'] = 200
    root.mainloop()

def terug():
    pass

# start de GUI
API.getAPIDataToXML()
sql.startDatabase(databaseNaam)

showBeginMenu()
