import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

filmdict = processXML("films.xml")
films = filmdict["filmsoptv"]["film"]

lst = []
for film in films:
    lst.append(film['titel'])
    
print(lst)
