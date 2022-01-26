import datetime
import pandas as pd
import os.path
from bs4 import BeautifulSoup
import config
from selenium.webdriver.common.by import By
from googlesearch import search





def SearchContent(theme):
        driver = config.webDriver()
        driver.get(f'https://www.google.com/search?q={theme}')
        
        quantity = driver.find_element(
            By.XPATH,
            '//*[@id="result-stats"]'
        ).text
        quantity = float(quantity.split('Aproximadamente ')[1].split(' resultados')[0].replace('.',''))
        pages = quantity/10
        url_page = driver.find_element(
            By.XPATH,
            '//*[@id="xjs"]/table/tbody/tr/td[3]/a'
        ).get_attribute('href')
        
        print(url_page)
        
        actually_page = 0
        start = 10
        
        listNotice = []
        listLink = []
        
        while actually_page <= 10:
            if not actually_page == 0:
                url_page = url_page.replace('start=%s' % start,'start=%s' % (start+10))
                start + 10
            actually_page += 1
            driver.get(url_page)
            notices = driver.find_elements(
                By.XPATH,
                '//div[@class="g"]'
            )
            
            print(notices)
            
            for notice in notices:
                linkNotice = driver.find_element(
                    By.TAG_NAME,
                    'a'
                )
                for linkNotice in linkNotice:
                     texto = driver.find_element(
                        By.TAG_NAME,
                        'h3'
                    )
                noticesLink = linkNotice.get_attribute('href')
                listNotice.append(texto.text)
                listLink.append(noticesLink)
                print(notices, noticesLink)
        
        dfList = []
        
        for notice, link in zip(listNotice, listLink):
            dfList.append({
                'Noticias': notice,
                'URL': link
            })
        
        df = pd.DataFrame(dfList)
        print (df)
        
        return df, theme
        

SearchContent('pastel de frango')