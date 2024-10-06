# 📚 Quotes Scraper
## 📖 Description
A powerful and user-friendly Python-based web scraper designed to extract quotes and their authors from quotes.toscrape.com. This project allows you to collect inspirational quotes and save them to a text file with just a few simple steps!

## ✨ Features
- Scrape multiple pages of quotes automatically
- Error handling for network issues
- User-friendly command-line interface
- Custom file naming for output
- Progress feedback during scraping
- Robust HTTP request handling with retry mechanism
- Clean and organized output format

## 🚀 How to Use
1. **Set up your environment**:  
   Make sure you have Python installed on your system.

2. **Install dependencies**:  
   Run the following command to install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Scraper**:  
   Execute the script:
   ```bash
   python main.py
   ```
   Follow the prompts to:
   - Enter the number of pages you want to scrape
   - Specify the output file name

## 💻 Code Highlights
### Fetch Page Content
```python
def fetch_page_content(page_url):
    """Fetch the content of a web page with proper headers and error handling."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        response = requests.get(page_url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    return None
```

### Extract Quotes and Authors
```python
def extract_quotes_and_authors(page_content):
    """Parse HTML content to extract quotes and their authors."""
    soup = BeautifulSoup(page_content, 'lxml')
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    return zip(quotes, authors)
```

## 🛠️ Potential Enhancements
- Add support for different quote websites
- Implement data export to different formats (CSV, JSON)
- Add search functionality within saved quotes
- Create a web interface using Flask
- Add tags and categories extraction
- Implement concurrent scraping for faster execution
- Add option to filter quotes by author

## 👨‍💻 Author
Khaled Soudy

## 📦 Dependencies
The project relies on the following Python packages:
- beautifulsoup4==4.12.3
- requests==2.32.3
- lxml==5.3.0
- And other supporting packages listed in `requirements.txt`

## 🧱 Project Structure
```
quotes-scraper/
├── main.py          # Main script with scraping logic
├── requirements.txt # Project dependencies
├── .gitignore      # Git ignore file
└── README.md       # Project documentation
```

## 🤝 Contributing
Contributions are welcome! Feel free to submit pull requests or open issues to improve the project.

## 📄 License
This project is open source and available under the MIT License.

## ⚠️ Disclaimer
Please ensure you follow the target website's robots.txt and terms of service when using this scraper. Be respectful of the website's resources and implement appropriate delays between requests if needed.

## 📞 Support
If you encounter any issues or have questions, please open an issue in the GitHub repository.

---
Happy quote collecting! 📝✨