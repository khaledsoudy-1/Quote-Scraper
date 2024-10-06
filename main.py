import requests
from bs4 import BeautifulSoup


def get_quotes():
    try:
        url = 'https://quotes.toscrape.com/'
        
        # Make a GET request
        response = requests.get(url)
        
        response.raise_for_status()  # Handles non-successful requests
        
        # Make a soup object
        soup = BeautifulSoup(response.content, 'lxml')
        
        # Find all quotes
        quotes = soup.find_all('span', class_='text')
        
        # Find author's names
        authors = soup.find_all('small', class_='author')
        
        # Print all quotes along their author's name
        for quote, author in zip(quotes, authors):
            print(f"{quote.text}\n- {author.text}\n\n")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")


if __name__ == '__main__':
    get_quotes()
