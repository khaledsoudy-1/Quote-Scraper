import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

# Make a GET request
response = requests.get(url)

# Check response status code
print(response.status_code)          # OUTPUT: 200

# Display the result
print(response.text)