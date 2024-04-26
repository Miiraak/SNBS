import requests
from bs4 import BeautifulSoup

f = open("scrapper_output.txt", "a")

for i in ["https://webscraper.io/test-sites/e-commerce/allinone", "https://webscraper.io/test-sites/e-commerce/static",
          "https://webscraper.io/test-sites/e-commerce/ajax", "https://webscraper.io/test-sites/e-commerce/more",
          "https://webscraper.io/test-sites/e-commerce/scroll", "https://webscraper.io/test-sites/tables"]:

    url = i
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()

        if text is not None:
            f.write(text)
        else:
            print("No element find with ID 'text'", url)
    else:
        print("Request failed. Status :", response.status_code)

f.close()
