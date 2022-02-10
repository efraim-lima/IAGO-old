import datetime
import pandas as pd
import os.path
from bs4 import BeautifulSoup
import config
from selenium.webdriver.common.by import By
from googlesearch import search


def search(theme):
    driver = config.webDriver()
    driver.get(f'https://www.google.com/search?q={theme}')
    
    quantity = driver.find_element(
        By.XPATH,
        '//*[@id="result-stats"]'
    ).text
    quantity = float(quantity.split('Aproximadamente ')[1]
                        .split(' resultados')[0]
                        .replace('.',''))
    pages = quantity/10
    url_page = driver.find_element(
        By.XPATH,
        '//*[@id="xjs"]/table/tbody/tr/td[3]/a'
    ).get_attribute('href')
    
    
    actually_page = 0
    start = 10
    
    listNotice = []
    listLink = []
    
    while actually_page <= 10:
        if not actually_page == 0:
            url_page = url_page.replace(
                'start=%s' % start,
                'start=%s' % (start+10)
                )
            start + 10
        actually_page += 1
        driver.get(url_page)
        
        notices = driver.find_elements(
            By.ID,
            'search'
            #'//div[@class="v7W49e"]'
        )
        
        for item in notices:
            item = item.text
            
            i = 0
            
    
            textos = driver.find_elements(
                By.TAG_NAME,
                'h3'
            )
            
            for testo in textos:
                testo = testo.text

                listNotice.append(testo)
            
            linkNotices = driver.find_elements(
                By.TAG_NAME,
                'a'
            )
            for linkt in linkNotices:
                noticesLink = linkt.get_attribute('href')
                linkt = linkt.text
                
                listLink.append(noticesLink)
            
            i+=1
    
    dfList = []
    
    for notice, link in zip(listNotice, listLink):
        dfList.append({
            'Noticias': notice,
            'URL': link
        })
    
    df = pd.DataFrame(dfList)
    df = df.to_json()
    print (df)
    config.quit()
    
    return df