# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:34:51 2019

@author: nekot
"""

import requests
from bs4 import BeautifulSoup
import re
import datetime

def createTrendList(datetime):
    target_url = "https://twittrend.jp/time/1118370/" + datetime.strftime('%Y%m%d%H') + "/"
    r = requests.get(target_url)
    soup = BeautifulSoup(r.text, 'lxml')
    elems = soup.find_all(href=re.compile("twitter.com/search"))
    list = []
    for e in elems:
        list.append(e.text)
    return list


startDate = datetime.datetime(2019,11,4,0)
endDate = datetime.datetime(2019,11,9,0)

trendLists = []

if(startDate <= endDate):
    dt = startDate
    while dt <= endDate:
        print(dt)
        trendLists.append( createTrendList(dt))
        dt += datetime.timedelta(hours=2)
else:
    print("end date is before start date")


with open("result.csv","w", encoding='utf-8') as f:
    for i in range(50):
        for j in range(len(trendLists)):
            f.write(trendLists[j][i])
            f.write(",")
        f.write("\n")