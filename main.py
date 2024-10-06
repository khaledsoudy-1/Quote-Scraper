import requests
from bs4 import BeautifulSoup


def fetch_page_content(page_url):
    try:
        # Make a GET request
        response = requests.get(page_url)
        response.raise_for_status()  # Handles non-successful requests
        
        return response.content  # return page content
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
        return None


def extract_quotes_and_authors(page_content):
    # Make a soup object
    soup = BeautifulSoup(page_content, 'lxml')
    
    # Find all quotes
    quotes = soup.find_all('span', class_='text')
    
    # Find author's names
    authors = soup.find_all('small', class_='author')
    
    quotes_and_authors = zip(quotes, authors)  # Use zip to combine iterables
    return quotes_and_authors


def scrape_quotes():
    # Get user input for number of pages to scrape
    pages = int(input("How many pages would you like to scrape? "))
    
    # Get the data for each page
    for current_page_num in range(1, pages + 1):
        page_url = f'https://quotes.toscrape.com/page/{current_page_num}'
        
        # Get the page content
        page_content = fetch_page_content(page_url)
        
        # Parse or scrape the content
        quotes_and_authors = extract_quotes_and_authors(page_content)
        
        # Print all quotes along their author's name
        for quote, author in quotes_and_authors:
            print(f"{quote.text}\n- {author.text}\n\n")


if __name__ == '__main__':
    scrape_quotes()
