from bs4 import BeautifulSoup
from urllib.request import urlopen
def results():
	shipUrl="https://www.mohfw.gov.in/"
	shipPage = urlopen(shipUrl)
	l=[]
	soup = BeautifulSoup(shipPage,'lxml')
	data = soup.find_all("div", { "class" : "site-stats-count" })
	for line in data:
		sd=line.find_all('strong')
	for val in sd:
		l.append(val.text)
	return l
