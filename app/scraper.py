from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self) -> None:
        nat_cir_url = 'https://www.tabroom.com/index/index.mhtml'
        self.nat_cir_html = requests.get(nat_cir_url).text

    
    def tournament_name_fetcher(self):
        soup = BeautifulSoup(self.nat_cir_html, "lxml")

def main():
    nat_cir_url = 'https://www.tabroom.com/index/index.mhtml'
    html_response = requests.get(url = nat_cir_url)
    with open("sample.html", "w", encoding = "utf-8") as html_file:
        html_file.write(html_response.text)

if __name__ == "__main__":
    main()

