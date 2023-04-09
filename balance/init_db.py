import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO crypto ( dateoftrans, timeoftrans, from_currency, from_quantity, to_concurrency, to_quantity) VALUES (?,?,?,?,?,?)",
            ('01/04/2023', '23:04:12', 'EUR','100','BTC','1'),
            )

cur.execute("INSERT INTO crypto (dateoftrans, timeoftrans, from_currency, from_quantity, to_concurrency, to_quantity) VALUES (?,?,?,?,?,?)",
            ('02/04/2023', '23:04:12', 'EUR','1000','BTC','2'),
            )

connection.commit()
connection.close()
