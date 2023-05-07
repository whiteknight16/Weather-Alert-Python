import address
import requests
from twilio.rest import Client
import os
api_key=(os.environ['API_KEY'])
end_point=os.environ["END_POINT"]
account_sid=os.environ["ACCOUNT_SID"]
auth_token=os.environ["AUTH_TOKEN"]
[lat,lng]=address.get_loc()
weather_params={
    "key":api_key,
    "q":f"{lat},{lng}",
    
}
data=requests.get(end_point,params=weather_params)
data.raise_for_status()
will_it_rain=data.json()["forecast"]["forecastday"][0]["day"]['daily_chance_of_rain']
max_temp=data.json()["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
min_temp=data.json()["forecast"]["forecastday"][0]["day"]["mintemp_c"]
avg_temp=data.json()["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
if will_it_rain==0:
    rain="It will not rain"
else:
    rain="It will rain"

client = Client(account_sid, auth_token)
message = client.messages.create(
    body=f"Today's weather update\nMAX TEMPERATURE: {max_temp}\nMIN TEMPERATURE: {min_temp}\nAVERAGE TEMPERATURE: {avg_temp}\n{rain}",
    from_="+13203226214",
    to='+917007157057'
)

print(message.status)