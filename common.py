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
    
    lst = []
    for film in films:
        lst.append(film['titel'])
    print(lst)
