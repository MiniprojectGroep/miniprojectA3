# Lijst van alle algemene functies

# Krijg een lijst met alle films van vandaag
def getFilms(bestand):
    import xmltodict

    def processXML(filename):
        with open(filename) as myXMLFile:
            filecontentstring = myXMLFile.read()
            xmldictionary = xmltodict.parse(filecontentstring)
            return xmldictionary

    filmdict = processXML(bestand)
    films = filmdict["filmsoptv"]["film"]

    # lst[x][0] = titel, lst[x][1] = genre, lst[x][2] = jaar, lst[x][3] = imdb_rating, lst[x][4] = afbeelding_URL

    lst = []
    for film in films:
        temp_list = []
        temp_list.append(str(film['titel']))
        temp_list.append(str(film['genre']))
        temp_list.append(str(film['jaar']))
        temp_list.append(str(film['imdb_rating']))
        temp_list.append(str(film['cover']))
        lst.append(temp_list)

    for item in lst:
        print(item[4])
    return lst
