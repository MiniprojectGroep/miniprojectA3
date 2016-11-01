def login():
    import sqlite3
    database = 'Thuisbioscoop.db'

    try:
        connect = sqlite3.connect(database)
        c = connect.cursor()
        tabel = 'accounts'

        # Create table
        c.execute('''CREATE TABLE IF NOT EXISTS accounts
                     (gebruikersnaam text, wachtwoord text, type text)''')
        '''c.executemany('INSERT INTO accounts VALUES (?,?,?)', iets)'''

        gebruikersnaam = input('gebruikersnaam') # Wordt later entry.get()
        wachtwoord = input('wachtwoord') # Wordt later entry.get()
        gegevens = [gebruikersnaam, wachtwoord]

        c.execute('''SELECT * FROM accounts WHERE gebruikersnaam = ? AND wachtwoord = ?''',gegevens)
        resultaten = c.fetchall()

        # controleer of gebruikersnaam EN wachtwoord overeenkomen met de opgegeven data, eigenlijk overbodig maar dubbel check
        for resultaat in resultaten:
            if resultaat[0] == gebruikersnaam and resultaat[1] == wachtwoord:
                connect.close()
                
                # data van gebruikersnaam en wachtwoord wissen ivm security redenen
                gebruikersnaam = nil
                wachtwoord = nil
                
                return True
        
        return False
        '''Save (commit) the changes
        connect.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        connect.close()'''
    except:
        print ('Error, kon niet verbinden met de database: {}'.format(database))
        return False