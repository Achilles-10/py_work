from urllib.request import urlopen
from bs4 import BeautifulSoup
from getTitle import getTitle

title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
	print("Title couldn't be found")
else:
	print(title)
