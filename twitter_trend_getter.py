# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:34:51 2019

@author: nekot
"""

import requests
from bs4 import BeautifulSoup
import re

#初回のみ
target_url = "https://twittrend.jp/time/1118370/2019111018/"
#Requestsを使って、webから取得
r = requests.get(target_url)
#要素を抽出
soup = BeautifulSoup(r.text, 'lxml')
#soup.find_allを用いてリンク先が「news.yahoo.co.jp/pickup」の項目を全て取得
elems = soup.find_all(href=re.compile("twitter.com/search"))
for e in elems:
    print(e.getText())