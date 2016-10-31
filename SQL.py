import sqlite3
database = 'Thuisbioscoop.db'

try:
    connect = sqlite3.connect(database)
except:
    print('Error, kon niet verbinden met de database: {}'.format(database))

c = connect.cursor()
tabel = 'accounts'

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS accounts
             (gebruikersnaam text, wachtwoord text, type text)''')

'''
iets = [('2006-03-28', 'Woerden', 'Harmelen', 45.00),
             ('2006-04-05', 'Woerden', 'Amsterdam Centraal', 72.00),
             ('2006-04-06', 'Woerden', 'Utrecht Centraal', 53.00),
            ]
c.executemany('INSERT INTO treinen VALUES (?,?,?,?)', iets)
'''

gebruiker = ''
wachtwoord = ''
gegevens = [gebruiker,wachtwoord]

# c.execute('''SELECT * FROM treinen WHERE beginstation = ? AND eindstation = ?''',gegevens)
# rows = c.fetchall()

# for row in rows:
#    print(row)

# Save (commit) the changes
connect.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
connect.close()
