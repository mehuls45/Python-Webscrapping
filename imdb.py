from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os

MovieList = []

class Movie:

	def __init__(self):
		self.title = ''
		self.rating = ''
		self.link = ''

url = 'https://www.imdb.com/chart/top?ref_=tt_mv_close'

driver = webdriver.PhantomJS(r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get(url)
html_doc = driver.page_source

soup = BeautifulSoup(html_doc, 'lxml')
tbody = soup.find('tbody', class_='lister-list')
tr = tbody.find_all('tr')
for t in tr:
	title = t.find('td', class_='titleColumn').find('a')
	link = title['href']
	rating = t.find('td', class_='ratingColumn').find('strong').text
	movie = Movie()
	movie.title = title.text
	movie.rating = rating
	movie.link = link
	MovieList.append(movie)

baseurl = 'https://www.imdb.com'

if not os.path.exists('imdb_posters'):
	os.makedirs('imdb_posters')

for m in MovieList:

	driver.get(baseurl + m.link)
	html_doc = driver.page_source

	soup = BeautifulSoup(html_doc, 'lxml')
	img = soup.find('div', class_='poster').find('a').find('img')['src']

	f = open('imdb_posters\{0}.jpg'.format(m.title),'wb')
	f.write(requests.get(img).content)
	print(m.title)

f.close()
driver.quit()
