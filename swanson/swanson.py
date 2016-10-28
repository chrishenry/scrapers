#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

base_url = "http://www.tvfanatic.com/quotes/characters/ron-swanson/"

r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')

def get_quotes_from_page(soup_obj):
    quotes = soup_obj.select('blockquote p')

    for quote in quotes:
        print quote.get_text().strip()

get_quotes_from_page(soup)


page = 2
while r.status_code == 200:
    url = "{0}page-{1}.html".format(base_url, page)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    get_quotes_from_page(soup)

    page = page + 1
