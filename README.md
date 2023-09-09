# eBay Web Scrapper

Simple Python script to scrape data from eBay search results

## Usage

Give `main.py` executable permissions and run `./main.py --help` for usage details.

```
usage: py-ebay [-h] [-n PAGE_NUMBER] [-o OUTPUT] T [T ...]

py-ebay: Scrape item data from eBay search results and save to a CSV or database table
======================================================================================

positional arguments:
  T                     search terms for scrape ebay for (each search term is an HTTP request)

  options:
    -h, --help              show this help message and exit
    -n PAGE_NUMBER, --page-number PAGE_NUMBER 
                            How many pages to scrape
    -o OUTPUT, --output OUTPUT  
                            Dump output to csv file

Careful not to overuse this and get your ip banned!
```

## Dependencies

- BeauitfulSoup4

