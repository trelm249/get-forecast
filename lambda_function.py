import json, requests, datetime, boto3

city_id = ["4428667"] # city id from open weather map

# api key for open weather map in file
with open('api.key', 'r') as file:
    api_key = file.read().replace('\n', '')

# arn for sns topic in file
with open('topic.target', 'r') as file:
   topic_raw = file.read().replace('/n', '')

topic_target = topic_raw.strip()
print(topic_target)

def lambda_handler(event, context):
  for city in city_id:
      url = "https://api.openweathermap.org/data/2.5/forecast?id=%s&appid=%s&units=imperial&cnt=8" % (city, api_key)
      response  = requests.get(url)
      data = json.loads(response.text)
      msg_data = json.dumps(data["list"], indent=4)
      client = boto3.client('sns')
      reponse = client.publish (
        TopicArn = topic_target,
        Subject = 'Daily Forecast',
        Message = msg_data
        )
