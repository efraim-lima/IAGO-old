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
                f"https://www.google.com/search?q={YT_Theme}"
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


                cite = driver.find_elements_by_tag_name(
                    'cite'
                )
                for cite in cite:
                    cite = cite.text
                    print(cite)

                Titles = []
                titles_query = driver.find_elements_by_xpath(
                    '//div/div/div/div/div/a/h3'
                )

                for titles_query in titles_query:
                    titles_query = titles_query.text
                    Titles.append(titles_query)
                    print(f'Olha o 1 \n\n{titles_query}')

                links_query = driver.find_elements_by_xpath(
                    "//div[@id='rso']/div/div/div/div/a/h3"
                )

                for links_query in links_query:
                    Titles.append(links_query.get_attribute('href'))
                    print(f'Olha o 2 \n\n{links_query}')

                theme_in = []
                for i in Titles:
                    theme_in.append(YT_Theme)
                
                today = datetime.date.today()
                today = str(today)

                for YT_Theme, titles_query, in zip(
                    theme_in,
                    Titles

                ):#titles, views, URLs, tags, keywords
                    search_videos.append(
                        {
                            'Category':YT_Theme,
                            'Titles': titles_query
                        }
                        )

                df2 = pd.DataFrame(search_videos)
                print(df2)

                if not os.path.exists(f'{YT_Theme}/google_{YT_Theme}'):
                    os.mkdir(f'{YT_Theme}/google_{YT_Theme}')
                elif os.path.exists('{}/google_{}/google_{}.csv'.format(YT_Theme, YT_Theme, YT_Theme)):
                    try:
                        YT = pd.read_csv('{}/google_{}/google_{}.csv'.format(YT_Theme, YT_Theme, YT_Theme))
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
                        YT.to_csv('{}/google_{}/google_{}.csv'.format(YT_Theme, YT_Theme, YT_Theme), index=False)
                        print('\n\nPesquisa já existe')
                        print(f'Aqui seria o YT.csv \n{YT}\n\n')
                    except:
                        print('No merge')
                        pass
                else:
                    #df2.to_csv(f'{YT_Theme}/canais_{YT_Theme}'_data_leitura.csv')
                    df2.to_csv('{}/google_{}/google_{}.csv'.format(YT_Theme, YT_Theme, YT_Theme), index=False)
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