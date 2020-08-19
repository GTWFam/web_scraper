import requests
from bs4 import BeautifulSoup as bs

DOMAIN = 'https://dota2.gamepedia.com'
URL = 'https://dota2.gamepedia.com/Category:Responses'
FILETYPE = ".mp3"


def get_soup(url) :
	return bs(requests.get(url).text, 'html.parser')

groups = get_soup(URL).findAll('div', {"class", "mw-category-group"})

pages = []
for code in groups:
	for link in code.findAll('a'):
		pages.append(link.get('href'))

def get_audio(url):

	file_links = []
	file_names = []

	content_location = get_soup(url).find('div', {"class", "mw-parser-output"})
	
	audio_links = content_location.findAll('a')
	for link_loc in audio_links:
		if link_loc.has_attr('href'):
			link = link_loc.get('href')
			if FILETYPE in link:
				file_links.append(link)

	names = content_location.findAll('li')
	for aName in names:
		if len(aName.contents) > 1:
			if len(aName.contents) == 2:
				file_names.append(aName.contents[1])

			if len(aName.contents) == 4:
				file_names.append(aName.contents[3])

			if len(aName.contents) == 6:
				file_names.append(aName.contents[5])

	print(len(file_links))
	print(len(file_names))
	

get_audio(DOMAIN + pages[0])


