import requests
from bs4 import BeautifulSoup as bs

domain = 'https://dota2.gamepedia.com'
my_url = 'https://dota2.gamepedia.com/Category:Responses'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"mw-category-group"})