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

    str = response.text
 # In de API wordt er soms (1-11-2016 en 2-11-2016) een ' ; ' in het XML geleverd, als deze niet verwijdert wordt dan kan dit ervoor zorgen dat het XML bestand onleesbaar wordt
    str = str.replace('&','')
    str = str.replace(';','')
    with open(file,'w')as filmsXML:
        try:
            filmsXML.write(str)
        except:
            print('Error in de API')
