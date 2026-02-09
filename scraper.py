import requests
from bs4 import BeautifulSoup


def scrape_quotes():
    url = "https://quotes.toscrape.com"

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("span", class_="text")

        print("\n--- Quotes ---")
        for quote in quotes[:5]:
            print(quote.text)

    except Exception as e:
        print("Scraping failed:", e)
