# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:46:26 2017

@author: kishi
"""


from selenium import webdriver
from bs4 import BeautifulSoup
import time



path_to_chromedriver ="C:\\Users\\kishi\\Downloads\\chromedriver_win32\\chromedriver"            #enter path of chromedriver
browser = webdriver.Chrome(executable_path = path_to_chromedriver)


url =  "https://weibo.com/nike?is_hot=1"

#this function is to handle dynamic page content loading - using Selenium
def tweet_scroller(url):

    browser.get(url)
    
    #define initial page height for 'while' loop
    lastHeight = browser.execute_script("return document.body.scrollHeight")
    
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #define how many seconds to wait while dynamic page content loads
        time.sleep(3)
        newHeight = browser.execute_script("return document.body.scrollHeight")
        
        if newHeight == lastHeight:
            break
        else:
            lastHeight = newHeight
            
    html = browser.page_source

    return html


    
#function to handle/parse HTML and extract data - using BeautifulSoup    
def scrapper(url):
    
     
    #set to global in case you want to play around with the HTML later   
    global soup    
    
    #call dynamic page scroll function here
    soup = BeautifulSoup(tweet_scroller(url), "html.parser")
    
    i=soup.select("div.WB_text")
    print(i) 
    
    
#main
if __name__ == "__main__":
    scrapper(url)