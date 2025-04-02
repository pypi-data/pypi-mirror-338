import os

import requests


class AssetExtractor:
    def __init__(self, api_key):
        self.api_key = api_key

    def import_listings(self):
        url = f"https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={self.api_key}"
        response = requests.get(url)

        data = response.text.split('\n')
        rows = [row.split(',') for row in data[1:] if row]

        nyse_listings = [row for row in rows if len(row) > 1 and row[2] == 'NYSE']

        return nyse_listings
