def getAPIDataToXML():
    import requests
    import datetime

    private_key = ('lo1wkfqu66uwntl7nkvim1b2b8yoqdz6')
    file = 'films.xml'
    nu = datetime.datetime.now()
    datum = nu.strftime('%d-%m-%Y')

    # methode 0 = alle films, method 1 = filmtips, method 2 = film van de dag
    methode = 0
    link = 'http://api.filmtotaal.nl/filmsoptv.xml?apikey={}&dag={}&sorteer={}'.format(private_key,datum,methode)

    response = requests.get(link)

    string = response.text
 # In de API wordt er soms (1-11-2016 en 2-11-2016) een ' ; ' ,of er zit een encoding fout in het bestand, in het XML geleverd, als deze niet verwijdert of aangepast worden dan kan dit ervoor zorgen dat het XML bestand onleesbaar wordt
    string = string.replace('&eacute;', 'é') # &eacure; staat voor ' é '
    string = string.replace('&euml;','ë') # &euml; staat voor ' ë '
    string = string.replace('<?xml version="1.0" encoding="iso-8859-1"?>','<?xml version="1.0" encoding="UTF-8"?>' ) # zorgt ook voor en error??
    string = string.replace(';','') # Haal onbekende encodingselementen weg zodat het XML kan blijven functioneren
    string = string.replace('&','')
    string = string.replace('','') # Haal onbekende  tekensweg
    new_str = str(string)
    with open(file,'w')as filmsXML:
        try:
            filmsXML.write(new_str)
        except:
            print('Error in de API')
