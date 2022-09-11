import sqlite3

conn = sqlite3.connect('airportinfo.db')



c = conn.cursor()

test = "LTAF"

c.execute("SELECT * FROM airports WHERE airportCode= ?", [test])

print(c.fetchall()[0]["cityName"])

