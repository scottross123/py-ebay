#!/bin/env python3

# https://docs.python.org/3/library/argparse.html

import argparse
import textwrap

from ebay import get_item_data, dump_to_csv

def main():
    parser = argparse.ArgumentParser(
        prog='py-ebay', 
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Careful not to overuse this and get your ip banned!',
        description=textwrap.dedent('''\
                py-ebay: Scrape item data from eBay search results and save to a CSV or database table
                ======================================================================================
        '''))

    parser.add_argument('search_terms', metavar='T', type=str, nargs='+', help='search terms for scrape ebay for (each search term is an HTTP request)')

    parser.add_argument('-n', '--page-number', type=int, nargs=1, default=1, help='How many pages to scrape')

    parser.add_argument('-o', '--output', type=str, nargs=1, default="", help='Dump output to csv file')

    args = parser.parse_args()
    data_table = get_item_data(args.search_terms, args.page_number[0])
    if args.output != "":
        dump_to_csv(data_table, args.output[0])
        
    print(args)

main()

