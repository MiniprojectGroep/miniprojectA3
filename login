def login():
    import sqlite3
    database = 'Thuisbioscoop.db'

    try:
        connect = sqlite3.connect(database)
        c = connect.cursor()
        # Create table
        c.execute('''CREATE TABLE IF NOT EXISTS accounts
                     (gebruikersnaam text, emails text, wachtwoord text, type text)''')

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

    except:
        print ('Error, kon niet verbinden met de database: {}'.format(database))
        return False
