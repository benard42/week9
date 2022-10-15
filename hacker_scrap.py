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
           title = item.find("div", class_ = "title").text
           link = item.find("div", class_ = "titleline").href
           points = item.find(class_ = "subline").strong.text
           comments = item.find("href", href = "item?id=33189724").href
           author = item.find("div", class_ = "hnuser").find("a").text
           rank = item.find('div', class_ = "votearrow").strong.text
           
       except:
        pass
        hacker_found[index+1] = {'title':title, 'link':link, 'points':points, 'comments':comments, 'points':points, 'rank':rank}

hacker = hacker_found()
hacker.to_csv('hacker.csv',index=None)