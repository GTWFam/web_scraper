import requests
from bs4 import BeautifulSoup as bs

DOMAIN = 'https://dota2.gamepedia.com'
URL = 'https://dota2.gamepedia.com/Category:Responses'
FILETYPE = ".mp3"

# Function to get the html of a page using the url
def get_soup(url) :
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
		if len(aName.contents) > 1:
			if "Link▶️" in aName.text:
				aText = aName.text.replace("Link▶️", "")
				file_names.append(aText)

	# print(len(file_links))
	# print(len(file_names))
	

groups = get_soup(URL).findAll('div', {"class", "mw-category-group"})

pages = []
for code in groups:
	for link in code.findAll('a'):
		pages.append(link.get('href'))

# for aPage in pages:
# 	file_links = []
# 	file_names = []
# 	get_audio(DOMAIN + aPage)

# 	i = 0
# 	while i < len(file_links):
# 		with open("\Abadon\" + file_names[i] + FILETYPE, 'wb') as file:
# 		response = requests.get(DOMAIN + file_links[i])
# 		file.write(response.content)
# 		i += 1



print(pages[0])
file_links = []
file_names = []
get_audio(DOMAIN + pages[0])

with open(file_names[0] + FILETYPE, "wb") as file:
	response = requests.get(file_links[0])
	file.write(response.content)





