
from bs4 import BeautifulSoup as soup
import pandas
pandas.set_option('display.max_colwidth', 500)
import time
import requests
import random

#basepage = requests.get("https://finance.yahoo.com")#www.marketwatch.com/");#insert website in quotes here http://quotes.toscrape.com/)
## check for response 200
#if basepage.status_code != 200:
#    quit
#    #exit program
#
##scrub = soup(basepage.content)
##print(basepage.headers)
#test = "https://finance.yahoo.com/quote/NEE/history"#?period1=1606780800&period2=1614470400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
##0 = December 31 1969 Unix (epoch) timestamp
#
#base = "https://finance.yahoo.com/quote/"
#id2p1 = "/history?period1="
#p2 = "&period2="
#end = "&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
#
#tp1 = requests.get("https://finance.yahoo.com/quote/NEE/key-statistics", params={'p':'NEE'})
#print(tp1.status_code)
#
#tp2 = requests.get("https://en.wikipedia.org/w/index.php", params={'title':'Dog', 'action':'history'})
#print(tp2.status_code)
#
#tp3 = requests.get("https://www.marketwatch.com/investing/stock/nee/charts", params={'mod':'mw_quote_tab'})
#print(tp3.status_code)
#
#tp4 = requests.get("https://finance.yahoo.com/quote/AAPL/history?period1=345423600&period2=1495922400&interval=1d&filter=history&frequency=1d")
#print(tp4.status_code)
#
#testpage = requests.get(test)#, params={'period1':1606780800, 'period2':1614470400, 'interval':'1d', 'filter':'history', 'frequency':'1d', 'includeAdjustedClose':True})
#print(testpage.status_code)
##print(testpage.headers)
#
##scrub = soup(testpage.content)
##print(scrub)
##tstart = scrub.find("tbody",{"data-reactid":"50"})
##rows = tstart.find_all_next("tr")
##print(t)