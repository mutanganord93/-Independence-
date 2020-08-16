from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import csv


def scraper(url):
	myURL = []
	for i in range(len(url)):
		val = urlopen(url[i])
		bs = BeautifulSoup(val,'html.parser')
		table = bs.find('table',{'class':'wikitable sortable'})
		rows = table.find_all('tr')
		

		if i == 0:
			for row in rows:
				v = ''
				cells = row.find_all('td')
				for i in range(1,len(cells)):
					if i is not None:
						st = f"{cells[i].text.strip(), }"
						v += st
					else:
						myURL.append('None')
				myURL.append(v)


		else:
			for row in rows:
				v = ''
				cells = row.find_all('td')
				for i in range(0,len(cells)):
					if i is not None:
						st = f"{cells[i].text.strip(), }"
						v += st
					else:
						myURL.append('None')
				myURL.append(v)

	return myURL


url = ['https://en.wikipedia.org/wiki/Decolonisation_of_Africa','https://en.wikipedia.org/wiki/Decolonization_of_Asia','https://en.wikipedia.org/wiki/Decolonization_of_the_Americas#Timeline','https://en.wikipedia.org/wiki/Decolonisation_of_Oceania']
arr = scraper(url)
file = open("countries.txt","w")
for v in range(len(arr)):
	file.write(arr[v]+'\n')
file.close()
print('Done')
	