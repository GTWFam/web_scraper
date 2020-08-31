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
		if "Link▶️ Link▶️ Link▶️" in aName.text:
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

	# print(len(file_links))
	# print(len(file_names))

# Renaming the pages to create Directories
def rename(page):
	page = page.replace("/", "")
	page = page.replace("Responses", "")
	page = page.replace("%27", "'")
	page = page.replace("%26", "&")
	page = page.replace("_", " ")
	return page

groups = get_soup(URL).findAll('div', {"class", "mw-category-group"})

# Responeses pages 
pages = []
for code in groups:
	for link in code.findAll('a'):
		pages.append(link.get('href'))

# for aPage in pages:
# 	i = 0
# 	file_links = []
# 	file_names = []

# 	print(aPage)
# 	get_audio(DOMAIN + aPage)

# 	directory = rename(aPage)
# 	path = os.path.join(PARENT_DIR, directory)
# 	os.mkdir(path)

	
# 	while i < len(file_links):
# 		n = file_names[i]
# 		if len(n) > 20:
# 			n = n[0:10]

# 		with open(os.path.join(path, n) + FILETYPE, 'wb') as file:
# 			response = requests.get(file_links[i])
# 			file.write(response.content)
		
# 		with open(os.path.join(path, n) + ".txt", 'w') as file:
# 			file.write(file_names[i])

# 		i += 1
# 162
for aPage in pages[0:14]:
	i = 0
	file_links = []
	file_names = []

	print(aPage)
	get_audio(DOMAIN + aPage)

	directory = rename(aPage)
	path = os.path.join(PARENT_DIR, directory)
	os.mkdir(path)

	with open('heros.txt', 'a') as file:
		file.write(directory + '\n')
	
	while i < len(file_links):
		n = file_names[i]
		n = n.replace("/", "|")
		if len(n) > 20:
			n = n[0:10]

		with open(os.path.join(path, n) + FILETYPE, 'wb') as file:
			response = requests.get(file_links[i])
			file.write(response.content)
		
		with open(os.path.join(path, n) + ".txt", 'w') as file:
			file.write(file_names[i])

		i += 1

# To Debug
# aPage = rename(pages[2])

# print(aPage)

# path = os.path.join(PARENT_DIR, aPage)
# os.mkdir(path)

# file_links = []
# file_names = []
# get_audio(DOMAIN + pages[2])

# n = file_names[72]
# if len(n) > 255:
# 	n = n[0:10]

# with open(os.path.join(path, n) + FILETYPE, "wb") as file:
# 	response = requests.get(file_links[72])
# 	file.write(response.content)

# with open(os.path.join(path, n) + ".txt", "w") as file:
# 	file.write(file_names[72])




