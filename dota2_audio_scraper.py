import requests
import os
from mutagen.id3 import ID3 as id3
from bs4 import BeautifulSoup as bs

from mutagen.id3 import ID3NoHeaderError, TIT3

DOMAIN = 'https://dota2.gamepedia.com'
URL = 'https://dota2.gamepedia.com/Category:Responses'
FILETYPE = ".mp3"
PARENT_DIR = "/Users/hoangphanpham/Documents/Projects/Application/dota_audio_files"

# Function to get the html of a page using the url
def get_soup(url):
	return bs(requests.get(url).text, 'html.parser')

# Function to get the file links and file names
def get_audio(url):
	
	content_location = get_soup(url).find('div', {"class", "mw-parser-output"})
	
	audio_links = content_location.findAll('a')
	for link_loc in audio_links:
		if link_loc.has_attr('href'):
			link = link_loc.get('href')
			if FILETYPE in link:
				file_links.append(link)

	names = content_location.findAll('li')
	for aName in names:
		if "Link▶️ Link▶️ Link▶️ Link▶️" in aName.text:
			aText = aName.text.replace("Link▶️ Link▶️ Link▶️ Link▶️", "")
			file_names.append(aText)
			file_names.append(aText + " 2")
			file_names.append(aText + " 3")
			file_names.append(aText + " 4")
		elif "Link▶️ Link▶️ Link▶️" in aName.text:
			aText = aName.text.replace("Link▶️ Link▶️ Link▶️", "")
			file_names.append(aText)
			file_names.append(aText + " 2")
			file_names.append(aText + " 3")
		elif "Link▶️ Link▶️" in aName.text:
			aText = aName.text.replace("Link▶️ Link▶️", "")
			file_names.append(aText)
			file_names.append(aText + "2")
		elif "Link▶️" in aName.text:
			aText = aName.text.replace("Link▶️", "")
			file_names.append(aText)

# Renaming the pages to create Directories
def rename(page):
	page = page.strip()
	page = page.replace("/", "")
	page = page.replace("Responses", "")
	page = page.replace("%27", "'")
	page = page.replace("%26", "&")
	page = page.replace('.', '')
	page = page.replace(':', '')
	page = page.strip()
	page = page.replace(' ', '_')
	return page

def check(n):
	i = 2
	if not n in checkArray:
		checkArray.append(n)
		return n
	else:
		while i <= 10:
			if not n + ' (' + str(i) + ')' in checkArray:
				n = n + ' (' + str(i) + ')'
				checkArray.append(n)
				return n
			i += 1

groups = get_soup(URL).findAll('div', {"class", "mw-category-group"})

# Responeses pages 
pages = []
for code in groups:
	for link in code.findAll('a'):
		pages.append(link.get('href'))

# 166
for aPage in pages[0:167]:
	i = 0
	file_links = []
	file_names = []
	checkArray = []

	
	get_audio(DOMAIN + aPage)

	directory = rename(aPage)
	print(directory)
	path = os.path.join(PARENT_DIR, directory)
	os.mkdir(path)

	with open('heros.txt', 'a') as file:
		file.write(directory + '\n')
	
	while i < len(file_links):
		n = file_names[i]
		n = rename(n)
		if len(n) > 20:
			n = n[0:30]

		n = check(n )

		with open(directory + '_list.txt', 'a') as file:
			file.write(n + '\n')

		with open(os.path.join(path, n) + FILETYPE, 'wb') as file:
			response = requests.get(file_links[i])
			file.write(response.content)
		
		with open(os.path.join(path, n) + ".txt", 'w') as file:
			file.write(file_names[i])

		i += 1



