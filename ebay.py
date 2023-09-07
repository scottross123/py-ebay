#!/bin/env python3
import requests
from bs4 import BeautifulSoup
import csv

search_terms = ["thinkpad laptop"]
page_number = 1

base_url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw={search_term}&_sacat=0&_pgn={page_number}'

output = open('output.csv', 'w', newline='')
writer = csv.writer(output)

for search_term in search_terms:
    for i in range(0, page_number):
        url = base_url.format(search_term=search_term.replace(" ", "+"), page_number=page_number)
        page = requests.get(url)
        data = page.text
        soup = BeautifulSoup(data, "html.parser")
        results = soup.find("ul", class_="srp-results")
        items = results.find_all("li", class_="s-item")

        for item in items:
            #title = item.find_all("div", class_="s-item__title")
            title_span = item.find("span", { "role": "heading" })
            price = item.find("span", class_="s-item__price")
            #seller_info = item.find("span", class_="s-item__seller-info-text").text.split()
    
            writer.writerow([search_term, title_span.text, price.text])

output.close()

