import datetime

class SalesItem:
	def __init__(self, item):
		self.id = item.get('id')
		self.link = item.get('href')
		self.title = item.find('div', class_='li-title').text
		self.price = item.find('p', class_='list_price').text
		self.area = item.find('div', class_='cat_geo').p.text.strip()
		raw_date = item.find('div', class_='date_image').text.strip()
		self.date = parse_date(raw_date)

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
	if parts[0].startswith('tänään'):	
		today = datetime.date.today() - datetime.timedelta(days=1)
		year = today.year
		month = today.month
		day = today.day
		time = parts[1]
	elif parts[0].startswith('eilen'):
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


