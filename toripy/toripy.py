import requests
from SalesItem import SalesItem
from bs4 import BeautifulSoup

keyword = 'dsl modeemi'
url = f'https://www.tori.fi/koko_suomi?q={keyword}&cg=0&w=3&xtatc=INT-166'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

salesItems = {}
items = soup.find_all('a', class_='item_row_flex')
for item in items:
	salesItem = SalesItem(item)
	salesItems[salesItem.id] = salesItem
	next

print(salesItems)