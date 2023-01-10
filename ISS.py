#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""

import requests
import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

#SOLUTION TO PART 2 - listing location
    lon= resp["iss_position"]["longitude"]
    lat= resp["iss_position"]["latitude"]

#TIME
    ts= resp["timestamp"]
    ts = datetime.datetime.fromtimestamp(ts)

#LOCATION BY CITY AND COUNTRY
    locator_resp= rg.search((lat, lon))

    city= locator_resp[0]["name"]

    country= locator_resp[0]["cc"]

#OUTPUT
    print(f"""
    CURRENT LOCATION OF THE ISS: 
    Lon: {lon}
    Lat: {lat}
    City/Country: {city}, {country}
    Timestamp: {ts}
    """)

if __name__ == "__main__":

    main()

