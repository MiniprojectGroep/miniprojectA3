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
                         (gebruikersnaam text UNIQUE, emails text, wachtwoord text, type text)''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS aanbieders
                         (aanbieder text UNIQUE, wachtwoord text, type text)''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS films
                        (filmnaam text UNIQUE, aanbieder text, aantal_bezoekers int)''')

def isLoginCorrect():
    import sqlite3
    database = 'Thuisbioscoop.db'
    if isDatabaseConnection(database) == True:
        connect = sqlite3.connect(database)
        c = connect.cursor()
        global gebruikersnaam
        gebruikersnaam = input('gebruikersnaam') # Wordt later entry.get()
        global wachtwoord
        wachtwoord = input('wachtwoord') # Wordt later entry.get()
        gegevens = [gebruikersnaam, wachtwoord]

        c.execute('''SELECT * FROM accounts WHERE gebruikersnaam = ? AND wachtwoord = ?''',gegevens)
        resultaten = c.fetchall()

        # controleer of gebruikersnaam EN wachtwoord overeenkomen met de opgegeven data, eigenlijk overbodig maar dubbel check
        for resultaat in resultaten:
            if resultaat[0] == gebruikersnaam and resultaat[1] == wachtwoord:
                connect.close()
                # data van gebruikersnaam en wachtwoord wissen ivm security redenen
                gebruikersnaam = None
                wachtwoord = None

                return True
        return False
