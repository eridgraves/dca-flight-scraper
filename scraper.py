# scraper.py
# Scrape arrivals table from DCA website (https://www.flyreagan.com/arrivals-and-departures)
# Departures are behind a toggle button, so need to figure out how to access those later
import urllib3
from bs4 import BeautifulSoup

#create instance to extract from website
http = urllib3.PoolManager()

# Declare a variable containing the URL is going to be scrapped 
URL = 'https://www.flyreagan.com/arrivals-and-departures/'

#Extract the data from the website
r = http.request('GET', URL)

print("Info returned: " + str(r.info()))
print("Data returned: " + str(r.data))

#create a map of the site into beautiful soup framework
soup = BeautifulSoup(r.data, 'html.parser')

print("[1]***** **")
[ print( item.prettify() ) for item in soup.find_all('table') ]