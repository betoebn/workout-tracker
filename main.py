import requests
import datetime as dt

# nutritionix credentials
APP_ID = " "
API_KEY = " "
ENDPOINT = "https://trackapi.nutritionix.com/"
EXERCISE_ENDPOINT = "/v2/natural/exercise"

# sheety credentials
SHEETY_ENDPOINT = " "

today = dt.datetime.today().strftime("%d/%m/%Y")
time = dt.datetime.today().strftime("%H:%M:%S")

exercise = input("What exercise you did?")

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

header1 = {
    # sheety credentials
    "Authorization": " ",
}

exercise_params = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 185,
    "age": 28
}

response = requests.post(url=f"{ENDPOINT}{EXERCISE_ENDPOINT}", json=exercise_params, headers=header)
result = response.json()


exercise = {
    "workout": {
        "date": today,
        "time": time,
        "exercise": result["exercises"][0]["name"].title(),
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"]
    }
}

response = requests.post(url=SHEETY_ENDPOINT, json=exercise, headers=header1)
print(response.text)
