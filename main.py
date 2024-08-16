import requests

api_key = "fab5482fd45f4ef1bcedbb1aad04c5ba"
url = f"https://newsapi.org/v2/everything?q=tesla&from\
=2024-07-16&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["description"])
