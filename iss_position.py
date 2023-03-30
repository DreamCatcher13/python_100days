import requests, smtplib
from datetime import datetime
import pytz 

MY_LAT = 48.62
MY_LONG = 22.287


def if_above():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()

    long, lat = float(data['iss_position']['longitude']), float(data['iss_position']['latitude'])
    position = (long, lat)

    return (position[0]-5 < MY_LONG < position[0]+5 and position[1]-5 < MY_LAT< position[1]+5)

def is_night():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()

    sunrise_hour = int(sun_response.json()['results']['sunrise'].split("T")[1].split(":")[0])
    sunset_hour = int(sun_response.json()['results']['sunset'].split("T")[1].split(":")[0])
    time_now = datetime.now(pytz.timezone('UTC')) # import pytz to set timezone for datetime 
    
    return (sunset_hour < time_now.hour < 24 or 0 < time_now.hour < sunrise_hour)
    
if if_above() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # secure connection
        connection.login(user="email", password="password")
        connection.sendmail(from_addr="email", 
                            to_addrs="email2", 
                            msg=f"Subject:ISS is here\n\nGo stare at the sky"
                            )
else:
    print("ISS is not over your head")
            
"""
while True:
    time.sleep(60)
    if if_above() and is_night(): ...
"""


