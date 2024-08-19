import requests
from send_email import send_email

api_key = "d5eb6598980047fea683defa2a9bd864"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-07-19" \
      "&sortBy=publishedAt&" \
      "apiKey=d5eb6598980047fea683defa2a9bd864"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description

body = ""
for article in content["articles"]:
      if article["title"] is not None and article["description"] is not None:
            body = body + article["title"] + "\n" + article["description"] + 2*"\n"


# Email the content
body = body.encode("utf-8")
send_email(message=body)