import requests
from datetime import datetime
import smtplib
import decimal
MY_LAT = 26.238947 # Your latitude
MY_LONG = 73.024307 # Your longitude

MY_EMAIL = "abc@gmail.com"    #your gmail will come here
MY_PASSWORD = "fkjgef"  #Your password will come here

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour


#If the ISS is close to my current position
# and it is currently dark

if((iss_latitude >= 21 and iss_latitude <= 31) and (iss_longitude>=68 and iss_longitude<=78) and
        (current_hour<=sunrise and current_hour>=sunset)):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="def@gmail.com",
                            msg="Subject:LOOK UP\n\n LOOK UP. ISS is above you in the sky")

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



