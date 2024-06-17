import csv
import requests
from bs4 import BeautifulSoup
import time

def scrape_country_info(url):
    page = requests.get(url)
    time.sleep(3)  # Adding a delay to avoid overwhelming the server
    soup = BeautifulSoup(page.text, 'html.parser')
    art = soup.find(class_='infobox ib-country vcard')
    art_objects = art.find_all('tr')

    country_info = {
        'Country': None,
        'Capital': None,
        'Native Languages': None,
        'Area': None,
        'Population': None,
        'GDP': None
    }

    for obj in art_objects:
        key = obj.find('th')
        value = obj.find('td')
        if key and value:
            key_text = key.get_text(strip=True)
            value_text = value.get_text(strip=True)
            if key_text == 'Official languages':
                value_text = ', '.join([lang.get_text(strip=True) for lang in value.find_all('a')])
            country_info[key_text] = value_text

    return country_info

countries = {
    "Canada": "https://en.wikipedia.org/wiki/Canada",
    "China": "https://en.wikipedia.org/wiki/China",
    "US": "https://en.wikipedia.org/wiki/United_States",
    "Korea": "https://en.wikipedia.org/wiki/Korea",
    "UK": "https://en.wikipedia.org/wiki/United_Kingdom",
    "France": "https://en.wikipedia.org/wiki/France",
    "Turkey": "https://en.wikipedia.org/wiki/Turkey",
    "Italy": "https://en.wikipedia.org/wiki/Italy"
}

country_info_list = [scrape_country_info(url) for url in countries.values()]

with open('countries_info.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Country', 'Capital', 'Native Languages', 'Area', 'Population', 'GDP'])
    
    writer.writeheader()
    
    writer.writerows(country_info_list)

print("CSV file has been generated successfully.")
