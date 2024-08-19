import requests
import smtplib

api_key = "d5eb6598980047fea683defa2a9bd864"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-07-19" \
      "&sortBy=publishedAt&" \
      "apiKey=d5eb6598980047fea683defa2a9bd864"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
      print(content["title"])
      print(content["description"])

# Email the content