import requests
from send_email import send_email

api_key = "fab5482fd45f4ef1bcedbb1aad04c5ba"
url = f"https://newsapi.org/v2/everything?q=tesla&from\
=2024-07-16&sortBy=publishedAt&apiKey={api_key}"

# Make a request
request = requests.get(url)

# Gat a dictionary with data
content = request.json()

# Access the article title and description
body = ""
for article in content["articles"]:
    if article["title"] and article["description"] is not None:
        body = body + article["title"] \
           + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
