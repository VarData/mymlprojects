from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import urllib.request
import os
import codecs

# def make_soup(url):
#     thepage=urllib.request.urlopen(url)
#     soupdata=BeautifulSoup(thepage, "html.parser")
#     return soupdata

wiki = "https://en.wikipedia.org/wiki/Sixteenth_Legislative_Assembly_of_Uttar_Pradesh"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urr.Request(wiki,headers=header)
page = urr.urlopen(req)
soup = BeautifulSoup(page, "lxml")

soup= make_soup("https://en.wikipedia.org/wiki/Sixteenth_Legislative_Assembly_of_Uttar_Pradesh")

albumdatasaved="#,Assembly,Name,Party,Reserved,ID,District,LS,Comments"
# find all table ,get the first
table = soup.find_all('table', class_="wikitable")[4] # Only use the first table
# iter over it
for record in table.findAll('tr'):
    albumdata=""
    for data in record.findAll('td'):
        albumdata=albumdata+","+data.text
    albumdatasaved=albumdatasaved+"\n"+albumdata[1:]

print(albumdatasaved)
