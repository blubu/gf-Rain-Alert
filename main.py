
import requests
from msg import s_name, s_quote
from twilio.rest import Client

# constants
OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
apikey = {API_KEY}
house = ({LAT}, {LON})

# setting twilio
account_sid = {SID}
auth_token = {TOKEN}
client = Client(account_sid, auth_token)


# check weather function
def check_weather(place):
    # parameters
    is_rainy = False
    m_sent = False
    weather_parameters = {
        "lat": place[0],
        "lon": place[1],
        "appid": apikey
    }

    # api request
    r = requests.get(url=OWM_endpoint, params=weather_parameters)

    # data
    data = r.json()["weather"]
    print(data)

    # checking for rain
    for i in data:
        if i["id"] < 600:
            is_rainy = True
            m_sent = True
            forecast = i["main"]
            break

    # send message to friend
    if is_rainy:
        message = client.messages.create(
                    body=f"\n{s_quote}Please consider taking an umbrella. [Forecast : {forecast}]\nLove you {s_name}",
                    from_={SENDER_NUM},
                    to={RECEIVER_NUM}
                    )

        print(message.status)

    # send info to user about the weather and the status of rain alert
    message = client.messages.create(
        body=f"\nForecast : {data[0]['main']}\nMessage sent : {m_sent}",
        from_={SENDER_NUM},
        to={USER_NUM}
    )

    print(message.status)


check_weather(house)
