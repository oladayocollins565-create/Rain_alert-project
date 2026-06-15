import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameter = {
    "lat": 7.484120,
    "lon": 4.556276,
    "appid": api_key,
    "units": "metric",
    "cnt": 4,
}

response = requests.get(OWM_Endpoint , params=parameter)
response.raise_for_status()
weather_data = response.json()

will_rain = False

first_forecast = weather_data["list"][0]

temperature = first_forecast["main"]["temp"]
weather_condition = first_forecast["weather"][0]["description"].title()


for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if condition_code < 700:
        will_rain = True
        break

if will_rain:
    message_body =(
        f"🌦 Weather Update\n\n"
        f"Condition: {weather_condition}\n"
        f"Temperature: {temperature}°C\n"
        f"Rain Expected: Yes ☂️\n\n"
        f"It's going to rain today. Remember to bring an umbrella ☂️"
    )
else:
    message_body =(
        f"☀️ Weather Update\n\n"
        f"Condition: {weather_condition}\n"
        f"Temperature: {temperature}°C\n"
        f"Rain Expected: No\n\n"
        f"It seem there will not be rain today, Enjoy your day!"
    )

client = Client(account_sid, auth_token)

numbers = [
    "whatsapp:+2347072850274",
    "whatsapp:+2347078699595",
    "whatsapp:+2349136779676"
]

for number in numbers:
    whatsapp_message = client.messages.create(
        from_="whatsapp:+14155238886",
        body=message_body,
        to=number
    )
    print(whatsapp_message.status)
