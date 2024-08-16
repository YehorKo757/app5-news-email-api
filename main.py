import requests
from send_email import send_email

topic = "tesla"

api_key = "fab5482fd45f4ef1bcedbb1aad04c5ba"
url = (f"https://newsapi.org/v2/everything?"
       f"q={topic}&"
       f"from=2024-07-16&"
       f"sortBy=publishedAt&"
       f"apiKey={api_key}&"
       f"language=en")

# Make a request
request = requests.get(url)

# Gat a dictionary with data
content = request.json()

# Access the article title and description
body = "Subject: Today's news" + "\n"
for article in content["articles"][:20]:
    if (article["title"] and article["description"]
            and article["url"] is not None):
        body = (body + article["title"]
                + "\n" + article["description"]
                + "\n" + article["url"] + 2*"\n")

body = body.encode("utf-8")
send_email(message=body)
