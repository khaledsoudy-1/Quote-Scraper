import requests
from bs4 import BeautifulSoup


def get_quotes():
    url = 'https://quotes.toscrape.com/'
    
    # Make a GET request
    response = requests.get(url)
    
    # Make a soup object
    soup = BeautifulSoup(response.content, 'lxml')
    
    # Find and extract the first quote.
    quote = soup.find('span', class_='text').text
    print(quote)
    
    # Find and extract the author's name of the first quote
    author = soup.find('small', class_='author').text
    print(author)


if __name__ == '__main__':
    get_quotes()

# OUTPUT:
# “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
# Albert Einstein
