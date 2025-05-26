import requests
from bs4 import BeautifulSoup

class WebScraper:
    def scrape_text(self, url: str) -> str:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

        text = soup.get_text()
        
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\\n'.join(chunk for chunk in chunks if chunk)
        
        return text

if __name__ == '__main__':
    scraper = WebScraper()
    text = scraper.scrape_text("https://www.independent.co.uk/travel/news-and-advice/newark-airport-flight-prices-controller-shortages-b2755374.html")
    print(text)