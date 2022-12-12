import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

# Nutritionix Authentication App id and app key
APP_ID = ""
APP_KEY = ""
SHEETY_API = ""

#Sheety username and password

USERNAME = ""
PASSWORD = ""



exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers={
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json"
}

answer = input("Describe your activity today \n")
parameters = {
    "query": answer
}

response = requests.post(exercise_endpoint,json=parameters ,headers=headers)
data = response.json()

today_date = datetime.now().strftime("%d-%m-%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheets_inputs={
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_API, json=sheets_inputs, auth=(USERNAME, PASSWORD))
    print(sheet_response.text)

    basic = HTTPBasicAuth(username=USERNAME, password=PASSWORD)

    sheet_response1 = requests.get(SHEETY_API, auth=basic)
    #print(sheet_response1)




