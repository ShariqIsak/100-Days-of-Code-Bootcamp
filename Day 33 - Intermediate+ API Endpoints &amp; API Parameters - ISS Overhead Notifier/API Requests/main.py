import requests
from datetime import datetime
import smtplib

MYLAT = -1.441680
MYLNG = 36.680770

my_email = "engineeringsolutionke@gmail.com"
password = "sqhbyioviculeayu"

parameters = {
    'lat': -1.441680,
    'lng': 36.680770,
    'formatted': 0,
}

data = requests.get(url="http://api.open-notify.org/iss-now.json")
data.raise_for_status()

longitude = float(data.json()["iss_position"]['longitude'])
latitude = float(data.json()["iss_position"]['latitude'])

print(longitude)
print(latitude)
print(MYLAT)
print(MYLNG)

# get sunrise and sunset times
data2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
data2.raise_for_status()
sunrise = data2.json()["results"]["sunrise"]
sunset = data2.json()["results"]["sunset"]
sunriseHour = int((sunrise.split("T")[1].split(":"))[0])
sunsetHour = int((sunset.split("T")[1].split(":"))[0])
print(sunsetHour)
print(sunriseHour)
hourNow = datetime.now().hour
print(hourNow)

# compare ISS possition to my location and alert by email
# if it is at night then
# compare location vs my location in to see if its withing +- 5 of my coordinates
# then send email


if sunsetHour < hourNow or hourNow < sunriseHour:
    if MYLNG - 5 < longitude < MYLNG + 5:
        if MYLAT - 5 < latitude < MYLAT + 5:
            print("ISS above you")
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=my_email,
                    msg=f"Subject: ISS Above!\n\n Look up!")
