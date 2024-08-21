import requests
from send_email import send_email

# Choose news topic
topic = "tesla"

# API Key and URL
api_key = "d5eb6598980047fea683defa2a9bd864"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&from=2024-07-19" \
      "&sortBy=publishedAt&" \
      "apiKey=d5eb6598980047fea683defa2a9bd864" \
      "&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description

body = ""

for article in content["articles"][0:10]:
      if article["title"] is not None and article["description"] is not None:
            body = "Subject: Today's News" \
            + "\n" + body + article["title"] + "\n" \
            + article["description"] + "\n" + article["url] + 2*"\n"


# Email the content
body = body.encode("utf-8")
send_email(message=body)