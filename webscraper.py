#!/usr/bin/env python
# coding: utf-8

# In[51]:


import requests # for making standard html requests
import pandas as pd
import time
import os
import json # for parsing data

from bs4 import BeautifulSoup # magical tool for parsing html data
from pandas import DataFrame as df # premier library for data organization
from selenium import webdriver


# In[52]:


names = []
amounts = []
#locations = []
prices = []


# In[55]:


def appendAll(soup):
    for a in soup.findAll('div', attrs={'class':'sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item s-asin sg-col-4-of-28 sg-col-4-of-16 AdHolder sg-col sg-col-4-of-20 sg-col-4-of-32'}):
        name = a.find('h2', attrs={'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-4'}).find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
        amount = a.find('span', attrs={'class':'a-icon-alt'})
        #location=a.find('div', attrs={'class':'location'})
        price=a.find('span', attrs={'class':'a-price-whole'}) #.findChildren()[1]
        names.append(name.text)
        amounts.append(amount.text)
        #locations.append(location.text)
        prices.append(price.text)


# In[56]:


url = "https://www.amazon.de/s?k=chopsticks&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=5DL4OFCO5ID0&sprefix=chopst%2Caps%2C164&ref=nb_sb_ss_i_1_6"
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path="/Users/jiazheng/TUM/Self learning/Python course/Webscraper/chromedriver")
driver.get(url)
time.sleep(3)
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')
appendAll(soup)


# In[65]:


df = pd.DataFrame({'Product Name':names,'Sold amounts':amounts,'Prices':prices}) 
df.to_csv('amazon.csv', index=False, encoding='utf-8')


# In[ ]:




