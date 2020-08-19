import requests
from bs4 import BeautifulSoup as bs

DOMAIN = 'https://dota2.gamepedia.com'
URL = 'https://dota2.gamepedia.com/Category:Responses'
FILETYPE = ".mp3"
pages = []

def get_soup(url) :
	return bs(requests.get(url).text, 'html.parser')

groups = get_soup(URL).findAll('div', {"class", "mw-category-group"})

for code in groups:
	for link in code.findAll('a'):
		pages.append(link.get('href'))

print(pages)