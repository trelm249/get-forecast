import json, requests, datetime

#Gulfport, MS; Longview, TX; Waveland, MS; Norfolk, MS; SD
city_id = ["4428667", "4707814", "4450411", "4776222", "5391811"]
#api_key = "SuperSecretKey" # open weather api key, should be protected
with open('api.key', 'r') as file:
    api_key = file.read().replace('\n', '')


def get_date(timezone):
    tz = datetime.timezone(datetime.timedelta(seconds=int(timezone)))
    return datetime.datetime.fromtimestamp(element["dt"], tz = tz).strftime("%Y.%m.%d-%H:%M:%S") #strftime is just for visually formatting the datetime object

for city in city_id:
    # Grab a 24 hours worth of weather forecast in 3 hour increments
    url = "https://api.openweathermap.org/data/2.5/forecast?id=%s&appid=%s&units=imperial&cnt=8" % (city, api_key)
    response  = requests.get(url)
    data = json.loads(response.text)
    for element in data["list"]:
     weather_info = {'city.id': f"{data['city']['id']}",
                     'time': f"{get_date(data['city']['timezone'])}",
                     'city': f"{data['city']['name']}",
                     'temperature': f"{element['main']['temp']}",
                     'heat.index': f"{element['main']['feels_like']}",
                     'condition': f"{element['weather'][0]['main']}",
                     'wind': f"{element['wind']['speed']}",
                     'pressure': f"{element['main']['pressure']}",
                     'humidity': f"{element['main']['humidity']}"
                     }
     print(weather_info)
    print()
