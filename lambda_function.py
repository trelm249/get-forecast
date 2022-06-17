import json, requests, datetime, boto3

#Gulfport, MS
city_id = ["4428667"]

#api_key 
with open('api.key', 'r') as file:
    api_key = file.read().replace('\n', '')

# sns topic target
with open('topic.target', 'r') as file:
   topic_raw = file.read().replace('/n', '')

topic_target = topic_raw.strip()

def lambda_handler(event, context):
  def get_date(timezone):
      tz = datetime.timezone(datetime.timedelta(seconds=int(timezone)))
      return datetime.datetime.fromtimestamp(element["dt"], tz = tz).strftime("%Y.%m.%d-%H:%M:%S") #strftime is just for visually formatting the datetime object

  for city in city_id:
      url = "https://api.openweathermap.org/data/2.5/forecast?id=%s&appid=%s&units=imperial&cnt=8" % (city, api_key)
      response  = requests.get(url)
      data = json.loads(response.text)
      for element in data["list"]:
        format_time = f"{get_date(data['city']['timezone'])}"
        element.update({'dt_txt': format_time})
      msg_data = json.dumps(data["list"], indent=4)
      client = boto3.client('sns')
      reponse = client.publish (
        TopicArn = topic_target,
        Subject = 'Daily Forecast',
        Message = msg_data
        )
