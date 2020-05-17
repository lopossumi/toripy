import requests
import datetime
from bs4 import BeautifulSoup
months = {
	'tam': 1,
	'hel': 2,
	'maa': 3,
	'huh': 4,
	'tou': 5,
	'kes': 6,
	'hei': 7,
	'elo': 8,
	'syy': 9,
	'lok': 10,
	'mar': 11,
	'jou': 12
}

def parse_date(text):
	parts = text.split()
	if raw_date.startswith('tänään'):	
		today = datetime.date.today() - datetime.timedelta(days=1)
		year = today.year
		month = today.month
		day = today.day
		time = parts[1]
	elif raw_date.startswith('eilen'):
		yesterday = datetime.date.today() - datetime.timedelta(days=1)
		year = yesterday.year
		month = yesterday.month
		day = yesterday.day
		time = parts[1]
	else:
		year = datetime.date.today().year
		month = months[parts[1]]
		day = int(parts[0])
		time = parts[2]
	hour = int(time.split(':')[0])
	minute = int(time.split(':')[1])
	return datetime.datetime(year, month, day, hour, minute)

class SalesItem:
	def __init__(self, title, price, area, link, date):
		self.title = title
		self.price = price
		self.area = area
		self.link = link
		self.date = date

keyword = 'äänikortti'
url = f'https://www.tori.fi/koko_suomi?q={keyword}&cg=0&w=3&xtatc=INT-166'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

dict = {}
items = soup.find_all('a', class_='item_row_flex')
for item in items:
	id = item.get('id')
	
	link = item.get('href')
	title = item.find('div', class_='li-title').text
	price = item.find('p', class_='list_price').text
	area = item.find('div', class_='cat_geo').p.text.strip()
	raw_date = item.find('div', class_='date_image').text.strip()
	date = parse_date(raw_date)

	#print(f'{id} {title} ({area}) {price} {date}')
	dict[id] = SalesItem(title, price, area, link, date)
	next

print(dict)