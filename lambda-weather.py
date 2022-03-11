import json, requests, datetime

#gulfport 
city_id = ["4428667", "4707814"] # Gulfport, MS and Longview, TX
api_key = "SuperSecretKey" # open weather api key, should be protected


def get_date(timezone):
    tz = datetime.timezone(datetime.timedelta(seconds=int(timezone)))
    return datetime.datetime.now(tz = tz).strftime("%Y.%m.%d-%H:%M:%S") #strftime is just for visually formatting the datetime object

for city in city_id:
    url = "https://api.openweathermap.org/data/2.5/weather?id=%s&appid=%s&units=imperial" % (city, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    weather_info = {'current.temperature': f"{data['main']['temp']}",
                    'state': f"{data['weather'][0]['main']}",
                    'city': f"{data['name']}",
                    'local.time': f"{get_date(data['timezone'])}",
                    'city.id': f"{data['id']}"
                    }
    print(weather_info)
