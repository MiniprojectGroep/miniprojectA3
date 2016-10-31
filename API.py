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

with open(file,'w')as myXMLFile:
    myXMLFile.write(response.text)
