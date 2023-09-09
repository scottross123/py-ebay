import requests
from bs4 import BeautifulSoup
import csv

def dump_to_csv(table: [[str]], filename: str):
    output = open('{}.csv'.format(filename), 'w', newline='')
    writer = csv.writer(output)
    writer.writerows(table)
    output.close()

def get_item_data(search_terms: [str], page_number: int):
    """
    Scrape data from ebay search results and put into multi-dimensional array

    search_terms: string array of terms to search
    page_number: int for how many pages to scrape results from

    return: table/2d array where each row is an item
    """

    base_url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw={search_term}&_sacat=0&_pgn={page_number}'

    table =  []

    for search_term in search_terms:
        for i in range(0, page_number):
            url = base_url.format(search_term=search_term.replace(" ", "+"), page_number=page_number)
            page = requests.get(url)
            data = page.text
            soup = BeautifulSoup(data, "html.parser")            
 
            results = soup.find("ul", class_="srp-results")
            items = results.find_all("li", class_="s-item")            


            for item in items:
                id = item.get('id')
                title = item.find("span", { "role": "heading" }).text.replace(';', "")
                price = item.find("span", class_="s-item__price").text
                seller_info = item.find("span", class_="s-item__seller-info-text")
                link = item.find("a", class_="s-item__link").get("href")

                if seller_info == None:
                    continue

                seller_split = seller_info.text.split()
                seller_name = seller_split[0]
                seller_reviews = seller_split[1].replace("(", "").replace(")", "").replace('"', "")
                seller_ratings = seller_split[2]

        
                table.append([id.replace("item", ""), search_term, title, price, seller_name, seller_reviews, seller_ratings, link])
    return table

