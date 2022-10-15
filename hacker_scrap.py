import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://news.ycombinator.com/"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')


hacker_item = soup.find('span',class_ = 'pagetop').text

print(hacker_item)

hacker_found = {}

for index, item in enumerate(hacker_found):
       try:
           title = item.find("div", class_ = "item-info").find("a").text
           link = item.find("div", class_ = "item-info").find("a").text
           points = item.find(class_ = "price-current").strong.text
           comments = item.find("div", class_ = "item-info").find("a").text
           author = item.find("div", class_ = "item-info").find("a").text
           rank = item.find(class_ = "price-current").strong.text
           
       except:
        pass

movies = hacker_found()
movies.to_csv('movies.csv',index=None)