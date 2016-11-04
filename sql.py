def isDatabaseConnection(databasename):
    import sqlite3
    try:
        connect = sqlite3.connect(databasename)
        return True
    except:
        return False

def startDatabase(databasename):
    import sqlite3
    if isDatabaseConnection(databasename) == True:
        connect = sqlite3.connect(databasename)
        c = connect.cursor()
        # Create table

        c.execute('''CREATE TABLE IF NOT EXISTS accounts
                         (gebruikersnaam text, email text, wachtwoord text, filmnaam text, filmstarttijd text, type text, datum text)''')

        c.execute('''CREATE TABLE IF NOT EXISTS films
                        (filmnaam text, aanbiedersnaam text, filmstarttijd text, filmdatum text, aantal_bezoekers int)''')

def isLoginCorrect(gebruikersnaam, wachtwoord,type):
    import sqlite3
    database = 'Thuisbioscoop.db'
    if isDatabaseConnection(database) == True:
        connect = sqlite3.connect(database)
        c = connect.cursor()
        gegevens = [gebruikersnaam, wachtwoord,type]

        c.execute('''SELECT * FROM accounts WHERE gebruikersnaam = ? AND wachtwoord = ? AND type = ?''',gegevens)
        resultaten = c.fetchall()

        # controleer of gebruikersnaam EN wachtwoord overeenkomen met de opgegeven data, eigenlijk overbodig maar dubbel check
        for resultaat in resultaten:

            if resultaat[0] == gebruikersnaam and resultaat[2] == wachtwoord:
                connect.close()
                # data van gebruikersnaam en wachtwoord wissen ivm security redenen

                return True
        return False

def isFilmInDatabase(film):
    import sqlite3
    database = 'Thuisbioscoop.db'
    if isDatabaseConnection(database) == True:
        connect = sqlite3.connect(database)
        c = connect.cursor()
        gegevens = [film]

        c.execute('''SELECT filmnaam FROM films WHERE filmnaam = ? ''',gegevens)
        resultaten = c.fetchall()

        for resultaat in resultaten:
            if resultaat[0] == film:
                connect.close()
                return True
        return False

def createFilmsTableData(lst):
    import sqlite3
    database = 'Thuisbioscoop.db'
    if isDatabaseConnection(database) == True:
        connect = sqlite3.connect(database)
        c = connect.cursor()
        for films in lst:
            if isFilmInDatabase(films[0]) == False:
                c.execute('INSERT INTO films VALUES (?,?,?,?,?)', films)
        connect.commit()
        return True

def getGebruikerFilmEnTijd(gebruikersnaam,wachtwoord):
    import sqlite3
    database = 'Thuisbioscoop.db'
    if isDatabaseConnection(database) == True:
        connect = sqlite3.connect(database)
        c = connect.cursor()
        gegevens = [gebruikersnaam, wachtwoord]

        c.execute('''SELECT gebruikersnaam,wachtwoord,filmnaam,filmstarttijd,datum FROM accounts WHERE gebruikersnaam = ? AND wachtwoord = ?''',gegevens)
        resultaten = c.fetchall()

        # controleer of gebruikersnaam EN wachtwoord overeenkomen met de opgegeven data
        for resultaat in resultaten:

            if resultaat[0] == gebruikersnaam and resultaat[1] == wachtwoord:
                connect.close()
                lst = []
                lst.append(resultaat[2])
                lst.append(resultaat[3])
                lst.append(resultaat[4])
                return lst
    return False

def isCodeUnique(code):
    import sqlite3
    database = 'Thuisbioscoop.db'
    if isDatabaseConnection(database) == True:
        connect = sqlite3.connect(database)
        c = connect.cursor()
        gegevens = [code]

        c.execute('''SELECT wachtwoord FROM accounts WHERE wachtwoord = ?''',gegevens)
        resultaten = c.fetchall()

        # controleer of gebruikersnaam EN wachtwoord overeenkomen met de opgegeven data
        for resultaat in resultaten:
            if resultaat == code:
                connect.close()
                return False
        return True
    return False

def registreerGebruiker(lst):
        import sqlite3
        database = 'Thuisbioscoop.db'
        if isDatabaseConnection(database) == True:
            connect = sqlite3.connect(database)
            c = connect.cursor()
            c.execute('INSERT INTO accounts VALUES (?,?,?,?,?,?,?)', lst)
            connect.commit()
            aantal_bezoekers = getAantalBezoekers(str(lst[3]),str(lst[6]))
            setAantalBezoekers(str(lst[3]),str(lst[6]),aantal_bezoekers) #veroorzaakt een error waardoor je de error krijgt "database is locked", ivm met tijd gebrek geen fix meer kunnen vinden
            connect.close()
            return True
        else:
            return False

def registeerAanbieders(): # Eenmalig, hoeft eigenlijk zelden gebruikt te worden aangezien aanbieders hetzelfde blijven
    aanbieders = [
        ['Nick','nick@hotmail.nl','kaasbroodje13','','','aanbieder','04-11-2016'],
        ['Piet Jan', 'pietjan@gmail.com','arash','','','aanbieder','04-11-2016'],
        ['Nathan', 'nathan@gmail.com','pizzaburger','','','aanbieder','04-11-2016'],
        ['Jeroen','jeroen@hotmail.nl','computerlaptop','','','aanbieder','04-11-2016']
    ]
    import sqlite3
    database = 'Thuisbioscoop.db'
    if isDatabaseConnection(database) == True:
        connect = sqlite3.connect(database)
        c = connect.cursor()
        for aanbieder in aanbieders:
            if isAanbiederInDatabase(aanbieder[0]) == False:
                c.execute('INSERT INTO accounts VALUES (?,?,?,?,?,?,?)', aanbieder)
        connect.commit()
        return True
    return False

def isAanbiederInDatabase(aanbieder):
    import sqlite3
    database = 'Thuisbioscoop.db'
    if isDatabaseConnection(database) == True:
        connect = sqlite3.connect(database)
        c = connect.cursor()
        gegevens = [aanbieder]

        c.execute('''SELECT gebruikersnaam FROM accounts WHERE gebruikersnaam = ? AND type == 'aanbieder' ''',gegevens)
        resultaten = c.fetchall()

        for resultaat in resultaten:
            if resultaat[0] == aanbieder:
                return True
        return False

def getAantalBezoekers(filmnaam,datum):
    import sqlite3
    database = 'Thuisbioscoop.db'
    if isDatabaseConnection(database) == True:
        connect = sqlite3.connect(database,timeout=10)
        c = connect.cursor()
        gegevens = [filmnaam,datum]
        c.execute('''SELECT aantal_bezoekers FROM films WHERE filmnaam = ? AND filmdatum = ?''',gegevens)
        resultaten = c.fetchall()

        # controleer of gebruikersnaam EN wachtwoord overeenkomen met de opgegeven data
        for resultaat in resultaten:
            aantal_bezoekers = str(resultaat)
            aantal_bezoekers = aantal_bezoekers.replace('(','')
            aantal_bezoekers = aantal_bezoekers.replace(')','')
            aantal_bezoekers = aantal_bezoekers.replace(',','')
            aantal_bezoekers = int(aantal_bezoekers)
            return aantal_bezoekers

def getFilmAanbieder(filmnaam,datum):
    import sqlite3
    database = 'Thuisbioscoop.db'
    if isDatabaseConnection(database) == True:
        connect = sqlite3.connect(database,timeout=10)
        c = connect.cursor()
        gegevens = [filmnaam,datum]
        c.execute('''SELECT aanbiedersnaam FROM films WHERE filmnaam = ? AND filmdatum = ?''',gegevens)
        resultaten = c.fetchall()

        # controleer of gebruikersnaam EN wachtwoord overeenkomen met de opgegeven data
        for resultaat in resultaten:
            aanbieder = str(resultaat)
            aanbieder = aanbieder.replace('(','')
            aanbieder = aanbieder.replace(')','')
            aanbieder = aanbieder.replace(',','')
            return aanbieder

def setAantalBezoekers(filmnaam,datum,aantal_bezoekers_int):
    import sqlite3
    database = 'Thuisbioscoop.db'
    if isDatabaseConnection(database) == True:
        connect = sqlite3.connect(database)
        c = connect.cursor()
        aantal_bezoekers_int += 1
        c.execute('''UPDATE films SET aantal_bezoekers = (?) WHERE filmnaam = (?) AND filmdatum = (?)''',(aantal_bezoekers_int, filmnaam, datum))
        connect.commit()
        connect.close()

def getFilmsZonderAanbieder():
    import sqlite3
    database = 'Thuisbioscoop.db'
    if isDatabaseConnection(database) == True:
        connect = sqlite3.connect(database,timeout=10)
        c = connect.cursor()
        c.execute('''SELECT filmnaam FROM films WHERE aanbiedersnaam = '' ''')
        resultaten = c.fetchall()

        lst = []
        i = 0
        for resultaat in resultaten:
            temp_lst = []
            resultaat = str(resultaat)
            resultaat = resultaat.replace('(','')
            resultaat = resultaat.replace(')','')
            resultaat = resultaat.replace(',','')
            temp_lst.append(i)
            temp_lst.append(resultaat)
            lst.append(temp_lst)

            i += 1
        return lst

def claimFilm(gebruikersnaam, filmnaam):
    import sqlite3
    database = 'Thuisbioscoop.db'
    if isDatabaseConnection(database) == True:
        connect = sqlite3.connect(database)
        c = connect.cursor()
        c.execute('''UPDATE films SET aanbiedersnaam = (?) WHERE filmnaam = (?)''',(gebruikersnaam, filmnaam))
        connect.commit()
        connect.close()
