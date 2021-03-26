import sqlite3
from math import radians, cos, sin, asin, sqrt, atan2, pi

conn = sqlite3.connect('airportinfo.db')

conn.row_factory = sqlite3.Row

c = conn.cursor()

def getUsefulInfoFromAirportCode(airportCode):
    c.execute("SELECT airportname, cityName, countryName, countryCode, latitude, longitude FROM airports WHERE airportCode = ?", [airportCode])

    return c.fetchall()[0]
def getDistanceBetweenTwoAirports(firstAirportCode, secondAirportCode):
    c.execute("SELECT latitude,longitude FROM airports WHERE airportCode= ?", [firstAirportCode])

    tmp = c.fetchall()

    try:
        tmp[0]
    except IndexError:
        return -1

    lat1 = float(tmp[0]["latitude"])
    lon1 = float(tmp[0]["longitude"])

    c.execute("SELECT latitude,longitude FROM airports WHERE airportCode= ?", [secondAirportCode])

    tmp = c.fetchall()

    try:
        tmp[0]
    except IndexError:
        return -1

    lat2 = float(tmp[0]["latitude"])
    lon2 = float(tmp[0]["longitude"])

    R = 6372.8

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    C = 2 * asin(sqrt(a))

    return R * C
