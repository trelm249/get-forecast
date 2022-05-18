import json, requests, datetime

#Gulfport, MS; Longview, TX; Waveland, MS; Norfolk, MS; SD 
city_id = ["4428667", "4707814", "4450411", "4776222", "5391811"]

with open('api.key', 'r') as file:
    api_key = file.read().replace('\n', '')


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
