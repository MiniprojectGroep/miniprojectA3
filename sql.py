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
                         (gebruikersnaam text, email text, wachtwoord text, filmnaam text, filmstarttijd text, type text)''')

        c.execute('''CREATE TABLE IF NOT EXISTS films
                        (filmnaam text, aanbiedersnaam text, filmstarttijd text, aantal_bezoekers int)''')

def isLoginCorrect(gebruikersnaam, wachtwoord):
    import sqlite3
    database = 'Thuisbioscoop.db'
    if isDatabaseConnection(database) == True:
        connect = sqlite3.connect(database)
        c = connect.cursor()
        gegevens = [gebruikersnaam, wachtwoord]

        c.execute('''SELECT * FROM accounts WHERE gebruikersnaam = ? AND wachtwoord = ?''',gegevens)
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

        # controleer of gebruikersnaam EN wachtwoord overeenkomen met de opgegeven data, eigenlijk overbodig maar dubbel check
        for resultaat in resultaten:
            if resultaat[0] == film:
                connect.close()
                # data van gebruikersnaam en wachtwoord wissen ivm security redenen
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
                c.execute('INSERT INTO films VALUES (?,?,?,?)', films)
        connect.commit()
        return True

def getGebruikerFilmEnTijd(gebruikersnaam,wachtwoord):
    import sqlite3
    database = 'Thuisbioscoop.db'
    if isDatabaseConnection(database) == True:
        connect = sqlite3.connect(database)
        c = connect.cursor()
        gegevens = [gebruikersnaam, wachtwoord]

        c.execute('''SELECT gebruikersnaam,wachtwoord,filmnaam,filmstarttijd FROM accounts WHERE gebruikersnaam = ? AND wachtwoord = ?''',gegevens)
        resultaten = c.fetchall()

        # controleer of gebruikersnaam EN wachtwoord overeenkomen met de opgegeven data
        for resultaat in resultaten:

            if resultaat[0] == gebruikersnaam and resultaat[1] == wachtwoord:
                connect.close()
                lst = []
                lst.append(resultaat[2])
                lst.append(resultaat[3])
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
    #try:
        import sqlite3
        database = 'Thuisbioscoop.db'
        if isDatabaseConnection(database) == True:
            connect = sqlite3.connect(database)
            c = connect.cursor()
            c.execute('INSERT INTO accounts VALUES (?,?,?,?,?,?)', lst)
            connect.commit()
            connect.close()
            return True
        else:
            return False
    #except:
        #return False

def registeerAanbieders():
    aanbieders = [
        ['Nick','nick@hotmail.nl','kaasbroodje13','','','aanbieder'],
        ['Piet Jan', 'pietjan@gmail.com','arash','','','aanbieder'],
        ['Nathan', 'nathan@gmail.com','pizzaburger','','','aanbieder'],
        ['Jeroen','jeroen@hotmail.nl','computerlaptop','','','aanbieder']
    ]
    import sqlite3
    database = 'Thuisbioscoop.db'
    if isDatabaseConnection(database) == True:
        connect = sqlite3.connect(database)
        c = connect.cursor()
        print(aanbieders)
        for aanbieder in aanbieders:
            print(aanbieder)
            if isAanbiederInDatabase(aanbieder[0]) == False:
                c.execute('INSERT INTO accounts VALUES (?,?,?,?,?,?)', aanbieder)
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
