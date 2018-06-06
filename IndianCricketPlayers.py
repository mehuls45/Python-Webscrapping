from selenium import webdriver
from bs4 import BeautifulSoup
import time

class Player():

	def __init__(self):
		self.name = ''
		self.link = ''

driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url = 'http://www.espncricinfo.com/india/content/player/country.html?country=6'

all_players = []

driver.get(url)
html_doc = driver.page_source
soup = BeautifulSoup(html_doc, 'lxml')
players = soup.find_all('table', class_='playersTable')
for player in players:
	tbody = player.find_all('tbody')
	tr = []
	tr = tbody[0].find_all('tr')
	bigr = []
	r = []
	for td in tr:

		r = td.find_all('td')
		
		for td in r:
			a = td.find('a')
			play = Player()
			play.name = a.text
			play.link = a['href']
			all_players.append(play)

for p in all_players:
	print('Name: ' + p.name)

	detailed_url = 'http://www.espncricinfo.com/'+p.link

	driver.get(detailed_url)
	html_doc = driver.page_source
	soup = BeautifulSoup(html_doc, 'lxml')
	details = soup.find_all('p', class_='ciPlayerinformationtxt')
	for d in details:
		print(d.find('b').text + ": " + d.find('span').text)
	print()
				