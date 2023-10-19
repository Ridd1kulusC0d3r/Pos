import requests
import json

url = "https://api.imagga.com/v2/tags"

querystring = {"image_url":"https://jpimg.com.br/uploads/2021/03/sao-paulo.jpg"}

headers = {
    'accept': "application/json",
    'authorization': "Basic YWNjXzk0ZWIyY2U5MTc5ZmIxMTpjMjIxOWE1ZDk5YTlkMjJkZjkwM2UzOGU1MzM5ODQ2Yg=="
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text.encode("ascii"))



for i in range(5):
    tag = data["result"]["tags"][i]["tag"]["en"]
    print(tag)
