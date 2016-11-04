# Modules
from tkinter import *
import random
import datetime

# Nodig voor een afbeelding
from io import BytesIO
import pyqrcode
import urllib
import urllib.request
from PIL import Image, ImageTk # Installeer de module: Pillow

# functies van zelf gemaakte bestanden
import API
import sql
import common

root = Tk()
databaseNaam = 'Thuisbioscoop.db'
xmlNaam = 'films.xml'

nu = datetime.datetime.now()
global datum
datum = nu.strftime('%d-%m-%Y')

# Alle Menu's (GUI windows)
def showBerichtMenu(): # menu dat wordt gebruikt om de QR code, code na betaling of een ander bericht te weergeven
    global huidigMenu

    global berichtFrame
    berichtFrame = Frame(master=root)
    berichtFrame.pack(side=BOTTOM)

    global bovenberichtFrame
    bovenberichtFrame = Frame(master=root)
    bovenberichtFrame.pack(side=TOP)
    text = ''

    if berichtType == 'Code':
        text = 'Noteer deze code, U heeft deze zodadelijk nodig om in te loggen met uw gebruikersnaam\nUw code is: {}'.format(code)
        huidigMenu = 'Code'

        berichtButton = Button(master=berichtFrame,command=volgendMenu,text='Ga verder',height=3,width=20)
        berichtButton.pack(side=BOTTOM,pady=4,padx=25)

        bericht = Label(master=bovenberichtFrame,text=text,background='darkgrey',foreground='black',font=('Helvetica',10,'bold italic'),width=100,height=5)
        bericht.pack(side=BOTTOM)

        #QR code
        big_code = pyqrcode.create(str(code), error='L', version=5, mode='binary')
        big_code.png('code.png', scale=4, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])

        img = ImageTk.PhotoImage(Image.open("code.png"))
        qrcodeLabel = Label(master=berichtFrame, image = img)
        qrcodeLabel.pack(side = BOTTOM)

        root.mainloop()

    elif berichtType == 'Einde':
        huidigMenu = 'Einde'
        text = 'Uw film: {}\nStarttijd:{}\nDatum:{}\n\nBedankt voor het gebruiken van de filmbioscoop applicatie. Veel plezier met het kijken van uw film!'.format(filmNaamEnTijd[0],filmNaamEnTijd[1],filmNaamEnTijd[2])

        berichtButton = Button(master=berichtFrame,command=vorigMenu,text='Ga terug naar het begin menu',height=3,width=30,bg='darkorange')
        berichtButton.pack(side=BOTTOM,pady=4,padx=25)

    elif berichtType == 'Betalings Probleem':
        text = 'Er is iets misgegaan met de betaling, probeer het later opnieuw.'

    elif berichtType == 'Geclaimed':
        huidigMenu = 'Einde'
        text = 'U heeft succesvol deze film geclaimed! Wegens beveiligings redenen moet U opnieuw inloggen als U nog een film wilt claimed.'

        berichtButton = Button(master=berichtFrame,command=vorigMenu,text='Ga terug naar het begin menu',height=3,width=30,bg='darkorange')
        berichtButton.pack(side=BOTTOM,pady=4,padx=25)

    bericht = Label(master=bovenberichtFrame,text=text,background='darkgrey',foreground='black',font=('Helvetica',10,'bold italic'),width=100,height=5)
    bericht.pack(side=BOTTOM)

def hideBerichtMenu(): # verberg het TextMenu
    berichtFrame.destroy()
    bovenberichtFrame.destroy()

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
    global huidigMenu
    huidigMenu = 'Kaart Menu'

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

    extraInfoButton = Button(master=middenKaartFrame,command=extraInfo,text='Selecteer',height=3,width=30)
    extraInfoButton.pack(side=RIGHT,pady=4,padx=25)

    bestelKaartButton = Button(master=onderKaartFrame,command=bestelKaart,text='Bestel',height=3,width=30)
    bestelKaartButton.pack(side=LEFT,pady=4,padx=25)

    kaartIsBesteldButton = Button(master=onderKaartFrame,command=kaartIsBesteld,text='Ik heb al een kaartje',height=3,width=20)
    kaartIsBesteldButton.pack(side=RIGHT,pady=4,padx=25)

    terugButton = Button(master=onderKaartFrame,command=vorigMenu,text='Vorig menu',height=3,width=20)
    terugButton.pack(side=RIGHT,pady=4,padx=25)

    root.mainloop()

def hideKaartMenu(): # verberg het KaartMenu
    bovenKaartFrame.destroy()
    middenKaartFrame.destroy()
    onderKaartFrame.destroy()

def showBetalingsMenu(): # In dit menu moet de bezoeker zijn naam, email invullen en daarna betalen. Suggestie: misschien leuk om ook iets van een prijs te gebruiken, en dat de prijs wordt gebaseerd op de IMDB rating (2 * IMDB rating = prijs). Verder eventueel nog zaken zoals: weekend korting, kinder/senior korting. Maar dat hangt af of we tijd overhouden of niet.
    global huidigMenu
    huidigMenu = 'Betalings Menu'

    global bovenBetalingsFrame
    bovenBetalingsFrame = Frame(master=root)
    bovenBetalingsFrame.pack(side=TOP)

    global onderBetalingsFrame
    onderBetalingsFrame = Frame(master=root)
    onderBetalingsFrame.pack(side=BOTTOM)

    emailBetalingsFrame = Frame(master=bovenBetalingsFrame)
    emailBetalingsFrame.pack(side=BOTTOM)

    gebruikersnaamBetalingsFrame = Frame(master=onderBetalingsFrame)
    gebruikersnaamBetalingsFrame.pack(side=TOP)

    text = 'Uw gekozen film: {}\n IMDB rating: {}\n Wij baseren onze prijs op de IMDB rating, ( IMDB rating * 2) = €{}'.format(filmtitel,imdbRating,prijs)
    betalingsLabel = Label(master=bovenBetalingsFrame,text=text,background='darkgrey',foreground='black',font=('Helvetica',10,'bold italic'),width=70,height=5)
    betalingsLabel.pack()

    gebruikersnaamLabel = Label(master=gebruikersnaamBetalingsFrame, text="Gebruikersnaam")
    gebruikersnaamLabel.pack(side=LEFT)

    global gebruikersnaamEntry
    gebruikersnaamEntry = Entry(master=gebruikersnaamBetalingsFrame, bd=5)
    gebruikersnaamEntry.pack(side = RIGHT)

    emailLabel = Label(master=emailBetalingsFrame, text="E-mail")
    emailLabel.pack(side=LEFT)

    global emailEntry
    emailEntry = Entry(master=emailBetalingsFrame, bd=5)
    emailEntry.pack(side = RIGHT)

    betaalBetalingsButton = Button(master=onderBetalingsFrame,command=registeerGebruiker,text='Betaal',height=3,width=20,bg='darkgreen')
    betaalBetalingsButton.pack(side=LEFT,pady=4,padx=25)

    terugButton = Button(master=onderBetalingsFrame,command=vorigMenu,text='Vorig Menu',height=3,width=20)
    terugButton.pack(side=RIGHT,pady=4,padx=25)

def hideBetalingsMenu(): # verberg het betalings menu
    bovenBetalingsFrame.destroy()
    onderBetalingsFrame.destroy()

def showLoginMenu(): # in dit menu moet de bezoeker inloggen met zijn naam en code. De aanbieder kan hier inloggen met zijn wachtwoord en gebruikersnaam. (Via SQLite3)
    global huidigMenu
    huidigMenu = 'Gebruikers Inlog Menu'

    global bovenLoginFrame
    bovenLoginFrame = Frame(master=root)
    bovenLoginFrame.pack(side=TOP)

    middenLoginFrame = Frame(master=bovenLoginFrame)
    middenLoginFrame.pack(side=BOTTOM)

    gebruikersnaamLoginFrame = Frame(master=middenLoginFrame)
    gebruikersnaamLoginFrame.pack(side=TOP)

    codeLoginFrame = Frame(master=middenLoginFrame)
    codeLoginFrame.pack(side=BOTTOM)

    global onderLoginFrame
    onderLoginFrame = Frame(master=root)
    onderLoginFrame.pack(side=BOTTOM)

    global informatieLoginLabel
    informatieLoginLabel = Label(master=bovenLoginFrame,text='Vul uw gebruikersnaam en code in.',background='darkgrey',foreground='black',font=('Helvetica',10,'bold italic'),width=60,height=5)
    informatieLoginLabel.pack(side=TOP)

    global gebruikersnaamLoginEntry
    gebruikersnaamLoginEntry = Entry(master=gebruikersnaamLoginFrame, bd=5)
    gebruikersnaamLoginEntry.pack(side = RIGHT)

    gebruikersnaamLabel = Label(master=gebruikersnaamLoginFrame, text="Gebruikersnaam")
    gebruikersnaamLabel.pack(side=LEFT)

    codeLabel = Label(master=codeLoginFrame, text="Code")
    codeLabel.pack(side=LEFT)

    global codeLoginEntry
    codeLoginEntry = Entry(master=codeLoginFrame,bd=5)
    codeLoginEntry.pack(side = RIGHT)

    inlogButton = Button(master=onderLoginFrame,command=loginGebruiker,text='Login',height=3,width=20)
    inlogButton.pack(side=LEFT,pady=4,padx=25)

    terugButton = Button(master=onderLoginFrame,command=vorigMenu,text='Vorig Menu',height=3,width=20)
    terugButton.pack(side=RIGHT,pady=4,padx=25)

    if keuze == 'aanbieder':
        huidigMenu = 'Aanbieders Inlog Menu'
        codeLabel['text'] = 'Wachtwoord'
        informatieLoginLabel['text'] = 'Welkom film aanbieder,\nvul uw wachtwoord en gebruikersnaam in om verder te gaan.'
        informatieLoginLabel['width'] = 60
        inlogButton['command'] = loginAanbieder

def hideLoginMenu(): # verberg het login menu
    bovenLoginFrame.destroy()
    onderLoginFrame.destroy()

def showAanbiedersMenu(): #speciaal menu voor de aanbieder, hierkan hij een overzicht zien van alle films die niet worden aangeboden door een andere aanbieder, overzicht van alle films, overzicht val alle bezoekers die bij deze aanbieder zitten, aanmeldcode controleren
    # Inhoud afhankelijk van de resultaten die teamlid 4 (Nathan) moet inleveren
    global huidigMenu
    huidigMenu = 'Aanbieders Menu'

    global aanbiederFrame
    aanbiederFrame = Frame(master=root)
    aanbiederFrame.pack()

    global aanbiederLabel
    aanbiederLabel = Label(master=aanbiederFrame,text='De volgende films zijn beschikbaar',background='darkgrey',foreground='black',font=('Helvetica',10,'bold italic'),width=100,height=5)

    global filmsZonderAanbiederButton
    filmsZonderAanbiederButton = Button(master=aanbiederFrame,command=filmsZonderAanbieder,text='Films zonder aanbieder',height=3,width=30)
    filmsZonderAanbiederButton.pack()

    global claimFilmButton
    claimFilmButton = Button(master=aanbiederFrame,command=claimFilm,text='Claim deze film',height=3,width=30)

    global terugButton
    terugButton = Button(master=aanbiederFrame,command=vorigMenu,text='Ga terug')
    terugButton.pack(side=RIGHT)

    scrollbar = Scrollbar(master=aanbiederFrame)
    scrollbar.pack( side = LEFT, fill=Y )

    global filmZonderAanbiederListBox
    filmZonderAanbiederListBox = Listbox(master=aanbiederFrame, selectmode=SINGLE,width=50, yscrollcommand=scrollbar.set)
    global filmZonderAanbiederLijst
    filmZonderAanbiederLijst = sql.getFilmsZonderAanbieder()

    for film in filmZonderAanbiederLijst:
        filmZonderAanbiederListBox.insert(film[0],film[1])
    scrollbar.config( command = filmZonderAanbiederListBox.yview )


def filmsZonderAanbieder(): # Een lijst met alle films de géén aanbieder is
    claimFilmButton.pack(side=RIGHT,pady=4,padx=25)
    filmsZonderAanbiederButton.destroy()
    filmZonderAanbiederListBox.pack(side = LEFT)
    aanbiederLabel.pack(side=TOP)

def claimFilm(): # Een aanbieder aan een film koppelen
    gebruikersnaam = aanbieder_gebruikersnaam
    tuple_getal = str(filmZonderAanbiederListBox.curselection())
    tuple_getal = tuple_getal.replace('(','')
    tuple_getal = tuple_getal.replace(')','')
    tuple_getal = tuple_getal.replace(',','')
    film_int = int(tuple_getal)
    filmnaam = filmZonderAanbiederLijst[film_int][1].replace("'","")
    sql.claimFilm(gebruikersnaam,filmnaam)
    hideAanbiedersMenu()
    global berichtType
    berichtType = 'Geclaimed'
    showBerichtMenu()

def hideAanbiedersMenu(): # verberg het AanbiedersMenu
    aanbiederFrame.destroy()

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
    hideKaartMenu()
    showBetalingsMenu()

def kaartIsBesteld():
    hideKaartMenu()
    showLoginMenu()

def extraInfo():
    tuple_getal = str(filmListbox.curselection())
    tuple_getal = tuple_getal.replace('(','')
    tuple_getal = tuple_getal.replace(')','')
    tuple_getal = tuple_getal.replace(',','')
    film = int(tuple_getal)

    global prijs
    prijs = (float(filmLijst[film][3]) * 2)
    global filmtitel
    filmtitel = filmLijst[film][0]
    global imdbRating
    imdbRating = filmLijst[film][3]
    global filmStartTijd
    filmStartTijd = filmLijst[film][7]

    aantal_bezoekers = sql.getAantalBezoekers(filmLijst[film][0],datum)
    aanbieder = sql.getFilmAanbieder(filmLijst[film][0],datum)

    if aanbieder == "''":
        aanbieder = 'onbekend'

    # lst[x][0] = titel, lst[x][1] = genre, lst[x][2] = jaar, lst[x][3] = imdb_rating, lst[x][4] = afbeelding_URL, lst[x][5] = film_nummer (Wordt gebruikt voor ListBox), lst[x][6] = Zender, lst[x][7] = start tijd, lst[x][8] = eindtijd
    text = 'Titel: {} \nGenre: {}\n Jaar: {}\nIMDB rating: {}\n Al {} bezoekers gingen U voor!\n Prijs: €{}\n Duur: {} - {}\n\n Deze film wordt U aangeboden door: {}'.format(filmLijst[film][0],filmLijst[film][1],filmLijst[film][2],filmLijst[film][3],aantal_bezoekers,prijs,filmLijst[film][7], filmLijst[film][8],aanbieder)
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

def registeerGebruiker():
    lst = []

    gebruikersnaam = gebruikersnaamEntry.get()
    email = emailEntry.get()
    global code

    while True:
        code = random.randint(100000,999999) # random string
        if sql.isCodeUnique(code) == True:
            break

    lst.append(gebruikersnaam)
    lst.append(email)
    lst.append(code)
    lst.append(filmtitel)
    lst.append(filmStartTijd)
    lst.append(keuze)
    lst.append(datum)

    if gebruikersnaam == '' or email == '':
        print('U moet een gebruikersnaam of email invullen!') # label van maken
    else:
        if sql.registreerGebruiker(lst) == True:
            hideBetalingsMenu()
            global berichtType
            berichtType = 'Code'
            showBerichtMenu()
        else:
            print('bericht dat het niet gelukt is (kan alleen voorkomen als de gebruiker niet genoeg geld op zijn rekening heeft')

    lst = [] #verwijder data uit de list

def loginGebruiker():
    gebruikersnaam = gebruikersnaamLoginEntry.get()
    wachtwoord = codeLoginEntry.get()

    if sql.isLoginCorrect(gebruikersnaam, wachtwoord,keuze) == True:
        global filmNaamEnTijd
        filmNaamEnTijd = sql.getGebruikerFilmEnTijd(gebruikersnaam,wachtwoord)

        global berichtType
        berichtType = 'Einde'
        hideLoginMenu()
        showBerichtMenu()
    else:
        informatieLoginLabel['text'] = 'De opgegeven gebruikersnaam en/of wachtwoord is/zijn onjuist.\nProbeer het opnieuw'
        informatieLoginLabel['foreground'] = 'red'

def loginAanbieder():
    global aanbieder_gebruikersnaam
    gebruikersnaam = gebruikersnaamLoginEntry.get()
    aanbieder_gebruikersnaam = gebruikersnaam
    wachtwoord = codeLoginEntry.get()

    if sql.isLoginCorrect(gebruikersnaam, wachtwoord,keuze) == True:
        hideLoginMenu()
        showAanbiedersMenu()
    else:
        informatieLoginLabel['text'] = 'De opgegeven gebruikersnaam en/of wachtwoord is/zijn onjuist.\nProbeer het opnieuw'
        informatieLoginLabel['foreground'] = 'red'

    # if sql.login == True

def vorigMenu(): # 1 functie voor alle "Terug" of "Vorige Menu" knoppen
    if huidigMenu == 'Kaart Menu':
        hideKaartMenu()
        showBeginMenu()
    elif huidigMenu == 'Betalings Menu':
        hideBetalingsMenu()
        showKaartMenu()
    elif huidigMenu == 'Gebruikers Inlog Menu':
        hideLoginMenu()
        showKaartMenu()
    elif huidigMenu == 'Aanbieders Inlog Menu':
        hideLoginMenu()
        showBeginMenu()
    elif huidigMenu == 'Aanbieders Menu':
        hideAanbiedersMenu()
        showBeginMenu()
    elif huidigMenu == 'Einde':
        hideBerichtMenu()
        showBeginMenu()

def volgendMenu(): # Zelfde structuur als vorige knop, wegens tijd gebrek niet volledig kunnen implementeren
    if huidigMenu == 'Code':
        hideBerichtMenu()
        showLoginMenu()

# start de GUI

API.getAPIDataToXML()
sql.startDatabase('Thuisbioscoop.db')
sql.registeerAanbieders()
sql.createFilmsTableData(common.getFilmTableDataList('films.xml'))
sql.getFilmsZonderAanbieder()

showBeginMenu()
