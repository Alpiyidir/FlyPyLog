import sqlite3
import csv

connection = sqlite3.connect('airportinfo.db')

c = connection.cursor()

with open("finalcombineddatawithltfm.csv") as data:
    reader = csv.DictReader(data)
    for a in reader:
        airportCode = a["airportCode"]
        airportName = a["airportName"]
        cityName = a["cityName"]
        countryName = a["countryName"]
        countryCode = a["countryCode"]
        latitude = a["latitude"]
        longitude = a["longitude"]
        c.execute("INSERT INTO airports VALUES (?,?,?,?,?,?,?)", (airportCode, airportName, cityName, countryName, countryCode, latitude, longitude))

connection.commit()

connection.close()
