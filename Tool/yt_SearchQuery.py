import datetime
import pandas as pd
import os.path
import re
import os.path
from bs4 import BeautifulSoup
import PySimpleGUI as sg
from time import sleep
from pandas.core.frame import DataFrame
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import config
import layout
from multiprocessing import Pool
from threading import Thread
import queue
from multiprocessing.dummy import Pool as ThreadPool
from queue import Empty, Queue


class IA5:
    def __init__(self):
        #global YT_Category
        #self.YT_Category = YT_Category
        YT_Cat = layout.sgLayout()
        self.YT_Category = str(YT_Cat)
        print(self.YT_Category)
        self.q = Queue()
        self.pool = ThreadPool(4)

    def SearchVideo(self):

            #global YT_Category, theme_in, videos_uni
            search_videos = []
            YT_Theme = self.YT_Category
            print(YT_Theme)


            global driver
            driver = config.webDriver()

            links = [
                f"https://www.youtube.com/results?search_query={YT_Theme}&sp=CAM%253D"
            ]

            pontuacao = ['(',')',';',':','[',']',',', '"', '|', '"', '/', '\\n']
            for link in links:
                driver.get(
                    link
                )

                driver.maximize_window() # For maximizing window
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);"
                    )
                driver.execute_script(
                    "window.scrollTo(0, window.scrollY + 2000)"
                    )

                config.inChrome()

                #for i in range(1,100):
                #    sg.one_line_progress_meter(
                #        'Channels', i+2, 100, 'Better Videos','Decrypting the better\n videos in the Channels'
                #        )
                #apenas um progress bar genérico (ainda não sei fazer um progress bar realmente útil)

                content = driver.page_source.encode(
                    'utf-8'
                ).strip()
                soup = BeautifulSoup(
                    content,
                    'lxml'
                )

                Titles = []
                titles_query = driver.find_elements_by_xpath(
                    '//*[@id="video-title"]/yt-formatted-string'
                )

                for titles_query in titles_query:
                    titles_query = titles_query.text
                    Titles.append(titles_query)
                
                theme_in = []
                for i in Titles:
                    theme_in.append(YT_Theme)

                Views = []
                views_query = driver.find_elements_by_xpath(
                    '//*[@id="metadata-line"]/span[1]'
                )
                for views_query in views_query:
                    views_query = views_query.text
                    Views.append(views_query)

                Ages = []
                ages_query = driver.find_elements_by_xpath(
                    '//*[@id="metadata-line"]/span[2]'
                )
                for ages_query in ages_query:
                    ages_query = ages_query.text
                    Ages.append(ages_query)

                Channels = []
                try:
                    channels_query = driver.find_elements_by_xpath(
                        '//*[@id="text"]/a'
                    )
                except:
                    channels_query = 'Unknown Channel'
                for channels_query in channels_query:
                    channels_query = channels_query.text
                    Channels.append(channels_query)

                CH_URLs = []
                ch_url_query = driver.find_elements_by_xpath(
                    '//*[@id="text"]/a'
                )
                for ch_url_query in ch_url_query:
                    CH_URLs.append(
                        '{}'.format(
                        ch_url_query.get_attribute('href')
                        )
                    )

                URLs = []
                url_query = driver.find_elements_by_xpath(
                    '//*[@id="video-title"]'
                )
                 # puxa o nome do canal
                for url_query in url_query:
                    URLs.append(
                        'https://www.youtube.com{}'.format(
                        url_query.get_attribute('href')
                        )
                    )

                today = datetime.date.today()
                today = str(today)

                for YT_Theme, titles_query, views_query, ages_query, channels_query, url_query, ch_url_query in zip(
                    theme_in,
                    Titles,
                    Views,
                    Ages,
                    Channels,
                    URLs,
                    CH_URLs
                ):#titles, views, URLs, tags, keywords
                    search_videos.append(
                        {
                            'Category':YT_Theme,
                            'Titles': titles_query,
                            'Video_URL': url_query,
                            'Channel_URL': ch_url_query,
                            'Date': ages_query,
                            f'View_{today}': views_query
                        }
                        )
                print(search_videos)

                df2 = pd.DataFrame(search_videos)
                print(df2)

                if not os.path.exists(f'{YT_Theme}/search_{YT_Theme}'):
                    os.mkdir(f'{YT_Theme}/search_{YT_Theme}')
                elif os.path.exists('{}/search_{}/search_{}.csv'.format(YT_Theme, YT_Theme, YT_Theme)):
                    try:
                        YT = pd.read_csv('{}/search_{}/search_{}.csv'.format(YT_Theme, YT_Theme, YT_Theme))
                        #df2 = df2.astype(str)
                        #YT = YT.astype(str)
                        #df2 = YT.merge(df2, how = 'outer')
                        #YT = pd.concat([YT, df2]).drop_duplicates().reset_index(drop=True)
                        YT = YT.astype(str) #tentando contornar erro que não permite o merge entre dataframes
                        df2 = df2.astype(str) #tentando contornar erro que não permite o merge entre dataframes
                        YT = pd.merge(
                            YT,
                            df2,
                            how='outer',

                            left_on=[
                                'Category',
                                'Ch_URL',
                                'Video_URL',
                                'Channel_URL',
                            ],
                            right_on=[
                                'Category',
                                'Ch_URL',
                                'Video_URL',
                                'Channel_URL',
                            ],
                            suffixes=(
                                '',
                                '_drop'
                            )
                        )
                        YT.drop([col for col in YT if 'drop' in col], axis=1, inplace=True)
                        YT = YT.drop_duplicates()
                        #YT.to_csv(f'{YT_Theme}/canais_{YT_Theme}'_data_leitura.csv')
                        YT.to_csv('{}/search_{}/search_{}.csv'.format(YT_Theme, YT_Theme, YT_Theme), index=False)
                        print('\n\nPesquisa já existe')
                        print(f'Aqui seria o YT.csv \n{YT}\n\n')
                    except:
                        print('No merge')
                        pass
                else:
                    #df2.to_csv(f'{YT_Theme}/canais_{YT_Theme}'_data_leitura.csv')
                    df2.to_csv('{}/search_{}/search_{}.csv'.format(YT_Theme, YT_Theme, YT_Theme), index=False)
                    #df2[f'Subs{today}'] = subscribers
                    #df2[f'View{today}'] = views
                    print('\n\nTema já existe\n Pesquisa não existe \n')
                    print(f'Resultado: \n\n\n {df2}\n\n')

                #df2.to_csv(f'{YT_Theme}/canais_{YT_Theme}/{CH}_df_l.csv')
                #print(f'\n\n {df2} \n\n')
            #self.links = df2['Video_URL']
            return #self.q.put(self.links)

            #print(canais_1)
            #print(YT_Theme)
IA5 = IA5()
IA5.SearchVideo()