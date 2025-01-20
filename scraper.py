# scraper.py
# Scrape arrivals table from DCA website (https://www.flyreagan.com/arrivals-and-departures)
# Departures are behind a toggle button, so need to figure out how to access those later
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import requests

url = "https://www.flyreagan.com/arrivals-and-departures"
browser = webdriver.Chrome()

browser.get(url)
time.sleep(3)
html = browser.page_source
soup = BeautifulSoup(html, "lxml")

print("Length of Tables: " + str(len(soup.find_all("table"))))

browser.close()
browser.quit() 

# TODO: refresh rather than restart browser for subsequent loads
# driver.navigate().refresh();
#
# OR to use the F5 approach to (maybe) save a full reload -- depends on if site takes a If-Modified-Since request 
#
# Actions actions = new Actions(driver);
# actions.keyDown(Keys.CONTROL).sendKeys(Keys.F5).perform();


response = requests.post("https://www.flyreagan.com/arrivals-and-departures/json", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "if-modified-since": "Mon, 20 Jan 2025 00:29:58 GMT",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest"
  },
  "referrer": "https://www.flyreagan.com/arrivals-and-departures",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "",
  "method": "GET",
  "mode": "cors",
  "credentials": "include"
});

if response.status_code == 200:
    print(response.text)
else:
    print("An error occurred:", response.status_code)