import requests
from bs4 import BeautifulSoup as bs

DOMAIN = 'https://dota2.gamepedia.com'
URL = 'https://dota2.gamepedia.com/Category:Responses'
FILETYPE = ".mp3"
audio = []

def get_soup(url) :
	return bs(requests.get(url).text, 'html.parser')

groups = get_soup(URL).findAll('div', {"class", "mw-category-group"})

pages = []
for code in groups:
	for link in code.findAll('a'):
		pages.append(link.get('href'))

def get_audio(url):
	content_location = get_soup(url).find('div', {"class", "mw-parser-output"})
	audio_links = content_location.findAll('a')

	for link_loc in audio_links:
		if link_loc.has_attr('href'):
			link = link_loc.get('href')
			if FILETYPE in link:
				audio.append(link)

# get_audio(DOMAIN + pages[0])


