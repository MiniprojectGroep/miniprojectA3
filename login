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




'''c.executemany('INSERT INTO accounts VALUES (?,?,?)', iets)'''


gebruikersnaam = input('gebruikersnaam')
wachtwoord = input('wachtwoord')
gegevens = [wachtwoord, gebruikersnaam]

c.execute('''SELECT * FROM accounts WHERE wachtwoord = ? AND gebruikersnaam = ?''',gegevens)
rows = c.fetchall()

for row in rows:
    print(row)

'''Save (commit) the changes
connect.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
connect.close()'''

