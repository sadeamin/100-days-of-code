import requests
from requests import api
from twilio.rest import Client

account_sid = "ACd06fb7ca26f0747854632a9545ed1ab5"
auth_token = "ef067d6d51f4c3ee00864fcb880b28e4"

api_key = "6594bfd4614f272daf00e27a4bed9e86"

"""
"lat": 46.947975,
"lon": 7.447447,

"""

parameter = {
    "lat": 23.684994,
    "lon": 90.356331,
    "appid" : api_key, 
    "exclude" : "current,minutely,daily"
    
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=parameter)
response.raise_for_status()
data = response.json()
weather_data = data["hourly"][:12]



is_raining = False

for data in weather_data:
    condition_code = data['weather'][0]['id']
    if int(condition_code) < 700:
        is_raining = True
        
if is_raining:
    client = Client(account_sid, auth_token)

    message = client.messages.create(body="It's going to rain today. Remember to bring an Umbrella", from_='+15752686391', to='+880 1749-319102')

    print(message.status)

print(is_raining)
     
     