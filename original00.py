#https://www.slickcharts.com/sp500   -    use at home to solve
# https://www.stockmonitor.com/sp500-stocks/     -    anotha source

# google.com/search?q=(ticker)+(google)+(finance)    -  Does google search for "(ticker) google finance" and can get the first link and open that seperately to get info

import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import chromedriver_autoinstaller
from openpyxl.utils import get_column_letter



#chromedriver_autoinstaller.install()

options = Options()

options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
driver = webdriver.Chrome(chrome_options = options, executable_path=r'C:/Users/aykhan/Desktop/chromedriver_win32/chromedriver.exe')

#driver = webdriver.Chrome()

names = []  # name of companies
abbreviated = []   # company name abbreviated
value = []   # current value
change = []  # numerical change
PCTchange = []   # change in value today
# will hold names of companies respective to sector
sectors = []




driver.get("https://www.slickcharts.com/sp500")
content = driver.page_source


soup = BeautifulSoup(content, features = "html.parser")

a = soup.find('tbody')
# used to order companies by their sector
for b in a.find_all('tr'):

    temp = []
    for c in b.find_all('td'):
        temp.append(c)
    abbrev = temp[2].text
    if '.' in abbrev:
        abbrev = abbrev.replace('.', '-')
    name = temp[1].text


    abbreviated.append(abbrev)
    names.append(name)

abbreviated.pop()
names.pop()

driver.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")

soup = BeautifulSoup(driver.page_source, features = "html.parser")

tempSector = {}

c = soup.find('tbody')

for a in c.find_all('tr'):

    temp = a.find_all('td')

    tempAbbrev = temp[0].text.strip()
    if '.' in tempAbbrev:
        tempAbbrev = tempAbbrev.replace('.', '-')

    tempSector[tempAbbrev] = temp[3].text


for a in abbreviated:
    sectors.append(tempSector[a])


marketCap = []

for a in abbreviated:

    driver.get('https://finance.yahoo.com/quote/{}?p={}'.format(a, a))
    content2 = driver.page_source

    soup = BeautifulSoup(content2, features = 'html.parser')

    b = soup.find('div', attrs = {'class' : 'D(ib) Mend(20px)'})



    val = b.find('fin-streamer')

    c = b.find_all('span' , attrs = {'class' : ['C($positiveColor)', 'C($negativeColor)']})



    value.append(val.text)

    if len(c) == 0:
        change.append('0.00')
        PCTchange.append('0.00%')
    else:
        change.append(c[0].text)
        PCTchange.append(c[1].text)

    marketCap.append(soup.find('td', attrs = {'class' : 'Ta(end) Fw(600) Lh(14px)', 'data-test' : 'MARKET_CAP-value'}).text)



df = pd.DataFrame({'Company Name': names, 'Ticker' : abbreviated, 'Sector' : sectors, 'Value' : value, 'Change' : change, 'Percent Change' : PCTchange, 'Market Cap' : marketCap})

with pd.ExcelWriter("stock.xlsx", engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df.to_excel(writer, sheet_name = 'stocks', index = False, encoding = 'utf-8')
