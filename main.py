import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameter = {
    "lat": 5.603717,
    "lon": -0.186964,
    "appid": api_key,
    "cnt": 4,
}

r = requests.get(OWM_Endpoint , params=parameter)
r.raise_for_status()
weather_data = r.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True
        break

msg= "It will rain today, take an umbrella with you."
if will_rain:
    client = Client(account_sid, auth_token)
    sms_message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☂️",
        from_= "+14058745904",
        to= "+2347072850274"
    )
    print(sms_message.status)

    whatsapp_message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an umbrella ☂️",
        to="whatsapp:+2347072850274"
    )
    print(whatsapp_message.status)