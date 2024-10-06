import requests
from bs4 import BeautifulSoup


def fetch_page_content(page_url):
    """Fetch the content of a web page."""
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }
    
    try:
        # Make a GET request to the specified URL.
        response = requests.get(page_url, headers=headers, timeout=10)
        response.raise_for_status()  # Raises an error for non-successful requests
        
        return response.content  # Return page content if successful
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.ConnectionError:
        print("Connection error occurred. Please check your internet connection.")
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
    
    return None  # Explicitly return None if an error occurs


def extract_quotes_and_authors(page_content):
    """Extract quotes and their authors from the page content."""
    
    # Make a soup object
    soup = BeautifulSoup(page_content, 'lxml')
    
    # Find all quotes
    quotes = soup.find_all('span', class_='text')
    
    # Find author's names
    authors = soup.find_all('small', class_='author')
    
    quotes_and_authors = zip(quotes, authors)  # Use zip to combine iterables
    return quotes_and_authors


def get_number_of_pages():
    """Get the number of pages to scrape from the user."""
    
    while True:
        try:
            # Get user input for number of pages to scrape
            num_of_pages = int(input("How many pages would you like to scrape? "))
            return num_of_pages
        
        except ValueError:
            print("Invalid input, please enter a valid number.\n")
            continue


def scrape_quotes():
    """Main function to scrape quotes from the specified number of pages."""
    
    pages = get_number_of_pages()
    
    # Get the file name from user
    file_name = input("\nEnter the name of the file to save the data: ")
    
    # Get the data for each page
    for current_page_num in range(1, pages + 1):
        page_url = f'https://quotes.toscrape.com/page/{current_page_num}'
        
        print(f"Scraping page {current_page_num}...")         # Feedback on progress
        
        # Get the page content
        page_content = fetch_page_content(page_url)
        
        # Check if page content was fetched successfully
        if page_content:
            # Parse or scrape the content
            quotes_and_authors = extract_quotes_and_authors(page_content)
            
            # Save all quotes along their author's name to a text file
            with open(f"{file_name}.txt", "a") as f:         # Use "a" to append to the file
                
                for quote, author in quotes_and_authors:
                    f.write(f"{quote.text}\n- {author.text}\n\n")
        
    print(f"\nSaving data to {file_name}.txt ...")


if __name__ == '__main__':
    scrape_quotes()
