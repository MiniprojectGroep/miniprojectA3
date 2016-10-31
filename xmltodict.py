import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

filmdict = processXML("films.xml")
films = filmdict["films"]["film"]

for film in films:
    print(film["film"])
