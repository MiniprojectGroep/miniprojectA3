# Alle algemene functies

# Krijg een lijst met alle films van vandaag
def getFilms(bestand):
    import xmltodict
    import datetime

    datetime.datetime.fromtimestamp(int("1284101485")).strftime('%Y-%m-%d %H:%M:%S')


    def processXML(filename):
        with open(filename) as myXMLFile:
            filecontentstring = myXMLFile.read()
            xmldictionary = xmltodict.parse(filecontentstring)
            return xmldictionary

    filmdict = processXML(bestand)
    films = filmdict["filmsoptv"]["film"]

    # lst[x][0] = titel, lst[x][1] = genre, lst[x][2] = jaar, lst[x][3] = imdb_rating, lst[x][4] = afbeelding_URL, lst[x][5] = film_nummer (Wordt gebruikt voor ListBox), lst[x][6] = Zender, lst[x][7] = start tijd, lst[x][8] = eindtijd

    lst = []
    film_nummer = 1
    for film in films:
        temp_list = []
        temp_list.append(str(film['titel']))
        temp_list.append(str(film['genre']))
        temp_list.append(str(film['jaar']))
        temp_list.append(str(film['imdb_rating']))
        temp_list.append(str(film['cover']))
        temp_list.append(film_nummer)
        temp_list.append(str(film['zender']))

        starttijd = str(datetime.datetime.fromtimestamp(int(film['starttijd'])).strftime('%H:%M'))
        eindtijd = str(datetime.datetime.fromtimestamp(int(film['eindtijd'])).strftime('%H:%M'))

        temp_list.append(str(starttijd))
        temp_list.append(str(eindtijd))
        lst.append(temp_list)
        film_nummer += 1

    return lst

def getFilmsNames(bestand):
    import xmltodict
    import datetime

    def processXML(filename):
        with open(filename) as myXMLFile:
            filecontentstring = myXMLFile.read()
            xmldictionary = xmltodict.parse(filecontentstring)
            return xmldictionary

    filmdict = processXML(bestand)
    films = filmdict["filmsoptv"]["film"]

    # lst[x][0] = titel, lst[x][1] = genre, lst[x][2] = jaar, lst[x][3] = imdb_rating, lst[x][4] = afbeelding_URL, lst[x][5] = film_nummer (Wordt gebruikt voor ListBox), lst[x][6] = Zender, lst[x][7] = start tijd, lst[x][8] = eindtijd

    lst = []
    film_nummer = 1
    for film in films:
        temp_list = []
        temp_list.append(str(film['titel']))
        temp_list.append(film_nummer)
        lst.append(temp_list)
        film_nummer += 1

    return lst

def getFilmTableDataList(bestand):
    import xmltodict
    import datetime

    def processXML(filename):
        with open(filename) as myXMLFile:
            filecontentstring = myXMLFile.read()
            xmldictionary = xmltodict.parse(filecontentstring)
            return xmldictionary

    filmdict = processXML(bestand)
    films = filmdict["filmsoptv"]["film"]

    # lst[x][0] = titel, lst[x][1] = Aanbieder, lst[x][2] = start tijd, lst[x][3] = filmdatum lst[x][4] = aantal_bezoekers
    lst = []
    for film in films:
        temp_list = []
        starttijd = str(datetime.datetime.fromtimestamp(int(film['starttijd'])).strftime('%H:%M'))
        vandaag = datetime.datetime.now()
        datum = vandaag.strftime('%d-%m-%Y')

        temp_list.append(str(film['titel']))
        temp_list.append('')
        temp_list.append(starttijd)
        temp_list.append(datum)
        temp_list.append(0)
        lst.append(temp_list)

    return lst
