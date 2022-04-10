import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

baseurl = 'https://www.thewhiskyexchange.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

productlinks = []
    
for x in range(1,6):
    r = requests.get(f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={x}&psize=24&sort=pasc')
    soup = BeautifulSoup(r.content, 'lxml')
    productlist = soup.findAll('li',class_='product-grid__item')
    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])
            
# testlink = 'https://www.thewhiskyexchange.com/p/29388/suntory-hibiki-harmony'

whiskylist = []
for link in productlinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    name = soup.find('h1',class_='product-main__name')
    price = soup.find('p',class_='product-action__price')
    try:
        rating = soup.find('div',class_='review-overview')
    except:
        rating = 'no rating'
        
    whisky = {
            'name': name,
            'rating':rating,
            'price':price
        }
    
    whiskylist.append(whisky)
    print('Saving: ', whisky)

df = pd.DataFrame(whiskylist)
print(df.head(15))