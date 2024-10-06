import requests
from bs4 import BeautifulSoup


def get_quotes():
    url = 'https://quotes.toscrape.com/'
    
    # Make a GET request
    response = requests.get(url)
    
    # Make a soup object
    soup = BeautifulSoup(response.content, 'lxml')
    
    # Find all quotes
    quotes = soup.find_all('span', class_='text')
    
    # Find author's names
    authors = soup.find_all('small', class_='author')
    
    # Print all quotes along their author's name
    for quote, author in zip(quotes, authors):
        print(f"{quote.text}\n- {author.text}\n\n")


if __name__ == '__main__':
    get_quotes()
