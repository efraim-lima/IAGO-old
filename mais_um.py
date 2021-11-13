import datetime
import pandas as pd
import numpy as np
import os.path
import re, sys
from selenium import webdriver
import os.path
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import PySimpleGUI as sg
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm
from time import sleep


#python -m venv __YT__
#### para acionar o virtual env
#__YT__\Scripts\activate.bat
#### para ativar o virtual env
#sg.change_look_and_feel('DarkEmber')
#### deixei pra ter referência de temas, já que ao usar este o Terminal me retorna todos nomes existentes
sg.change_look_and_feel('SystemDefaultForReal')
#### tema que estou usando
sg.popup_ok("Hello!! \nI'm IAGO  \nAn Artificial Inteligence that helps You \nto find your content for videos!!!") 
####janela de popup

#desenhando o layout simples

layout= [[sg.Text(
                    "\nFirst I need your help... \nWhats your maint theme or niche?"
                    ),
            sg.Input()
            ],#[sg.Button('Iniciar Análise')],
            [sg.Submit(),
            sg.Cancel()
            ]
        ]

janela = sg.Window('IA5').layout(layout) #### abre a janela de acordo com o Layout acima especificado
event, values = janela.read()
YT_Category = values[0].lower() #### captura o texto dentro da caixa de Texto
#print = sg.Print
print(YT_Category)
janela.close()


#YT_Category = input(f'tema: ')
#Confirmation = input(
#    '\n\n Obrigado, primeiro vamos analisar a quantidade de concorrentes que você possui. \nA analise a seguir vai abrir um navegador do Chrome, depois disso pode voltar para essa tela que o robô faz tudo isso.\nQuer fazer essa analise agora? [S/N] \nR: ')

#if YT_Category and Confirmation == 's' or 'S' or 'Sim' or 'sim':
#    print('\n\n\n Aguarde...\n\n\n')
#elif YT_Category and Confirmation == 'n' or 'N' or 'No' or 'Not' or 'não' or 'Não':
#    print('Poutz, que pena, mas o programa vai rodar por default...depois arrumo isso, ta bem?')
#    quit()
#else:
#    print('Não entendi, sou meio limitado, poderia me dizer se quer Sim ou não?  ')




class IA5:
    def theme(self):
        yt_dados = {}
        dados_no = 0
    urls = [
        f'https://www.youtube.com/results?search_query={YT_Category}'
    ]
    # browser = webdriver.Chrome('C:/Users/efrai/Downloads/chromedriver88_win32/chromedriver.exe') #precisa ser onde está instalado o Chromedriver
    chrome_options = Options()
    #chrome_options.add_argument(
    #    "-headless"
    #)
    browser = Chrome
    driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            options = chrome_options
    )

    for url in urls:
        driver.get(
            '{}&sp=CAASAhAC'.format(url)
        )

        parent_handle = driver.window_handles[0]

        for i in range(len(urls)):
            sg.one_line_progress_meter(
                'Theme Analysis',
                i+1,
                100,
                'Better Channels',
                'Decrypting Channels\n and Data'
            )

        driver.maximize_window() # For maximizing window
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        driver.execute_script(
            "window.scrollTo(0, window.scrollY + 5000)"
        )
        driver.delete_all_cookies()

        content = driver.page_source.encode(
            'utf-8'
        ).strip()
        soup = BeautifulSoup(
            content, 
            'lxml'
        )
        # print (driver) #para ver qual o driver utilizado
        # print (content) #mostra o java script do site
        # executar um python main.py
        # exec. pip install chromedriver

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        driver.execute_script(
            "window.scrollTo(0, window.scrollY + 2000)"
        )
        driver.delete_all_cookies()
        

        theme_in = []
        channel_name = []

        names = driver.find_elements_by_xpath(
            '//*[@id="text"]'
        )
        # puxa o nome do canal

        #names = soup.find_all(
        #    'div',
        #    id='text-container'
        #)  # puxa o nome do canal
        for names in names:
            names = names.text
            names = re.sub(
                '[0-9]|,|\.|/|$|\(|\)|-|\+|:|•\\n',
                ' ',
                names
            )
            channel_name.append(names)
        
        theme_in.append(YT_Category)

        channel_subs = []
        subscribers = soup.find_all(
            'span', 
            id='subscribers'
        )  # puxa o nome do canal
        for subscribers in subscribers:
            v = subscribers.text

            if ' mil inscritos'  in v:
                vi = re.sub(r',', '', v) and re.sub(r' mil inscritos', '00', v)
            elif 'mi de inscritos' in v:
                vi = re.sub(r',', '', v) and re.sub(r' mi de inscritos', '00000', v)
            else:
                vi = re.sub(r' mil inscritos', '000', v)

            vie = re.sub(r' mil inscritos', '00', v)
            vie = re.sub(r' mi de inscritos', '0000', vi)
            view = re.sub(r' inscritos', '', vie)
            view = re.sub(r' inscrito', '', view)
            view = re.sub(r'Um inscrito', '1', view)
            channel_subs.append(view)

        channel_videos = []
        video_count = soup.find_all(
            'span', 
            id='video-count'
        )  # puxa o nome do canal
        for video_count in video_count:
            v = video_count.text

            if ','  in v:
                vi = re.sub(r',', '.', v) and re.sub(r' mil vídeos', '00', v)
            else:
                vi = re.sub(r' mil vídeos', '000', v)
            vie = re.sub(r' mi de vídeos', '00000', vi)
            vie = re.sub(r' vídeos', '', vie)
            view = re.sub(r'Um vídeo', '1', vie)

            channel_videos.append(view)

        channel_URL = []
        channel_urls = soup.find_all(
            'a',
            id = 'main-link',
            class_='channel-link yt-simple-endpoint style-scope ytd-channel-renderer'
        )  # puxa o nome do canal
        for channel_urls in channel_urls:
            channel_URL.append(
                'https://www.youtube.com{}'.format(
                channel_urls.get('href')
                )
            )

        theme_data = []
        for YT_Category, names, subscribers, videos, URL in zip(
            theme_in,
            channel_name,
            channel_subs,
            channel_videos,
            channel_URL
        ):
            theme_data.append(
                {
                'Category':YT_Category,
                'Channel': names,
                'Inscritos':subscribers,
                'Videos': videos,
                'Ch_URL': URL
            }
            )

        #for i in tqdm(urls):
        #    k=0
        #    while k<i:
        #        k += 1

        df1 = pd.DataFrame(theme_data)


        if not os.path.exists(f'{YT_Category}'):
            os.mkdir(f'{YT_Category}')
            #df1.to_csv(f'{YT_Category}/{YT_Category}_data_leitura.csv')
            df1.to_csv(
                f'{YT_Category}/{YT_Category}.csv',
                index=False
            )

            print(f'\n\n{df1}\n\n')
        elif os.path.exists(f'{YT_Category}') and not os.path.exists(f'{YT_Category}/{YT_Category}.csv'):
            #YT.to_csv(f'{YT_Category}/{YT_Category}_data_leitura.csv')
            df1.to_csv(
                f'{YT_Category}/{YT_Category}.csv',
                index=False
            )
            print('\n\nTema já existe\n Resumo não existe \n\n')

            print(f'\n\n{df1}\n\n')
        else:
            YT = pd.read_csv(f'{YT_Category}/{YT_Category}.csv')
            for row in YT:
                if row == row in df1:
                    pass
                else:
                    YT.loc(row)
            #df1 = pd.concat([YT, df1], ignore_index = False, sort=False, join = "outer")
            #YT.to_csv(f'{YT_Category}/{YT_Category}_data_leitura.csv')
            YT.to_csv(
                f'{YT_Category}/{YT_Category}.csv', 
                index=False
            )
            print('\nTema já existe')
            print(f'\n{YT}\n\n')

#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################
        #df1 = pd.DataFrame(theme_data)
        #links = df1['Ch_URL']
        #ch_name = df1['Channel'][1].split('\n')
        #YT_Theme = YT_Category

        #def canais_dados(self):
        #    ch_dados = {}
        #    dados_no = 0
        #    #browser = webdriver.Chrome('C:/Users/efrai/Downloads/chromedriver88_win32/chromedriver.exe') #precisa ser onde está instalado o Chromedriver

        pontuacao = ['(',')',';',':','[',']',',', '"', '|', '"', '/', '\\n']
        for URL in channel_URL:
            driver.get(
                '{}/videos?view=0&sort=p&flow=grid'.format(URL)
            )
            if(URL!=len(channel_URL)-1):
                driver.execute_script("window.open('');")
                chwd = driver.window_handles
                driver.switch_to.window(chwd[-1])
            content = driver.page_source.encode ('utf-8').strip()
            soup = BeautifulSoup (
                content,
                'lxml'
            )
            driver.delete_all_cookies()

            Links = []
            Links.append(i in URL)

            #for i in range(1,100):
            #    sg.one_line_progress_meter(
            #        'Channels', i+2, 100, 'Better Videos','Decrypting the better\n videos in the Channels'
            #        ) #apenas um progress bar genérico (ainda não sei fazer um progress bar realmente útil)


            CH = driver.find_element_by_xpath(
                "//div[@id='inner-header-container']//div[@id='meta']//ytd-channel-name[@id='channel-name']//div[@id='container']//div[@id='text-container']//yt-formatted-string[@id='text']"
                ).text
            print(f'\n{CH}\n')
            CH = re.sub('[0-9]|,|\.|/|$|\(|\)|-|\+|:|•\\n', ' ', CH)
            pontuacao = ['(',')',';',':','[',']',',', '"', '|', '"','/', '\\n']
            for i in CH:
                if i in pontuacao:
                    CH = CH.replace(i, '-')
                else:
                    pass
            subscribers = driver.find_element_by_xpath(
                "//yt-formatted-string[@id='subscriber-count']"
                ).text
            subscribers = re.sub(' mil inscritos', ' ', subscribers)
            subscribers = re.sub(' mi de inscritos', ' ', subscribers)
            subscribers = re.sub(' inscritos', ' ', subscribers)

            print (subscribers)

            video_titles = []
            titles = soup.findAll('a', id='video-title')
            for titles in titles:
                video_titles.append(titles.get('title'))
            #video_titles = pd.DataFrame({'Title':video_titles})
            #print(video_titles)

            video_views = []
            views = driver.find_elements_by_xpath('//*[@id="metadata-line"]/span[1]')
            for views in views:
                v = views.text

                if ','  in v:
                    vi = re.sub(r',', '', v) and re.sub(r' mil visualizações', '00', v)
                elif ',' + 'mi de visualizações' in v:
                    vi = re.sub(r',', '', v) and re.sub(r' mi de visualizações', '00000', v)
                else:
                    vi = re.sub(r' mil visualizações', '000', v)
                vie = re.sub(r' mi de visualizações', '00000', vi)
                view = re.sub(r' visualizações', '', vie)
                video_views.append(view)

            video_date = []
            dates = driver.find_elements_by_xpath('//*[@id="metadata-line"]/span[2]')
            for dates in dates:
                d = dates.text
                video_date.append(d)

            #video_views = pd.DataFrame(video_views)

            video_urls = []
            URLs = soup.findAll(
                'a', 
                id='video-title'
            )
            for URLs in URLs:
                video_urls.append(
                    'https://www.youtube.com{}'.format(
                    URLs.get('href')
                )
                )

            today = datetime.date.today()
            today = str(today)

            channels = []
            for YT_Category, titles, views, dates, urls in zip(
                theme_in,
                video_titles,
                video_views,
                video_date,
                video_urls
            ):#titles, views, URLs, tags, keywords
                channels.append(
                    {
                        'Category':YT_Category,
                        'Channel': CH,
                        'Ch_URL': links,
                        'Titles': titles,
                        'Video_URL': urls,
                        'Videos': videos,
                        'Date': dates,
                        f'View_{today}': views,
                        f'Subs_{today}': subscribers
                    }
                    )
            #print(channels)

            df2 = pd.DataFrame(channels)
            print(df2)

            if not os.path.exists(f'{YT_Theme}/canais_{YT_Theme}'):
                os.mkdir(f'{YT_Theme}/canais_{YT_Theme}')
            elif os.path.exists(f'{YT_Theme}/canais_{YT_Theme}/{CH}.csv'):
                try:
                    YT = pd.read_csv(f'{YT_Theme}/canais_{YT_Theme}/{CH}.csv')
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
                            'Channel',
                            'Ch_URL',
                            'Video_URL',
                            'Videos',
                            'Date'
                        ],
                        right_on=[
                            'Category',
                            'Channel',
                            'Ch_URL',
                            'Video_URL',
                            'Videos',
                            'Date'
                        ],
                        suffixes=(
                            '',
                            '_drop'
                        )
                    )
                    YT.drop([col for col in YT if 'drop' in col], axis=1, inplace=True)
                    YT = YT.drop_duplicates()
                    #YT.to_csv(f'{YT_Theme}/canais_{YT_Theme}'_data_leitura.csv')
                    YT.to_csv(f'{YT_Theme}/canais_{YT_Theme}/{CH}.csv', index=False)
                    print('\n\nCanal já existe')
                    print(f'\n{YT}\n\n')
                except:
                    os.path.exists(f'{YT_Theme}/canais_{YT_Theme}/{CH}.csv')
                    next
            else:
                #df2.to_csv(f'{YT_Theme}/canais_{YT_Theme}'_data_leitura.csv')
                df2.to_csv(f'{YT_Theme}/canais_{YT_Theme}/{CH}.csv', index=False)
                #df2[f'Subs{today}'] = subscribers
                #df2[f'View{today}'] = views
                print('\n\nTema já existe\n Canal não existe \n')
                print(f'{df2}\n\n')

            #df2.to_csv(f'{YT_Theme}/canais_{YT_Theme}/{CH}_df_l.csv')
            #print(f'\n\n {df2} \n\n')

        canais_1 = os.listdir(f'{YT_Theme}/canais_{YT_Theme}/')
        #print(canais_1)
        #print(YT_Theme)


        for name in canais_1:
            #print(name)
            #Channel_Name = input('\n\n\nQual canal você precisa analisar o texto?   \nR: ')

            try:
                df = pd.read_csv(f'{YT_Theme}/canais_{YT_Theme}/{name}')
                links = df['Video_URL']
            except(EmptyDataError):
                df.iteritems()
            finally:
                df = pd.read_csv(f'{YT_Theme}/canais_{YT_Theme}/{name}')
                links = df['Video_URL']

            #browser = webdriver.Chrome('C:/Users/efrai/Downloads/chromedriver88_win32/chromedriver.exe') #precisa ser onde está instalado o Chromedriver

            videos = []
            for links in links:

                driver.get(f'{links}') ## estudando
                content = driver.page_source.encode ('utf-8').strip()
                soup = BeautifulSoup (content, 'lxml')

                for i in range(1,100):
                    sg.one_line_progress_meter(
                        'Videos',
                        i+6,
                        100,
                        'Better Videos',
                        'Decrypting the metadata\n of each video'
                    )

                title = []
                try:
                    ti =  driver.find_element_by_xpath(
                        '//[@id="container"]/h1/yt-formatted-string'
                        ).text
                    title.append(ti)
                    #print(title)
                except:
                    driver.implicitly_wait(1)
                    ti = driver.find_element_by_css_selector(
                        ".title > .ytd-video-primary-info-renderer"
                        ).text
                    title.append(ti)
                finally:
                    pass

                views = []
                vi = driver.find_element_by_xpath(
                    "//div[@id='count']/ytd-video-view-count-renderer/span"
                    ).text
                vie = vi.replace(
                    ' visualização', 
                    ''
                    )
                vie = vie.replace('.', '')
                view = vie.replace(' visualizações', '') #soup.find('span', {'class':'view-count style-scope ytd-video-view-count-renderer'})
                views.append(view)
                #print(views)

                comments = []
                driver.maximize_window() # For maximizing window
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);"
                    )
                driver.execute_script(
                    "window.scrollTo(0, window.scrollY + 500)"
                    )
                driver.implicitly_wait(5)
                driver.delete_all_cookies()

                try:
                    comment = driver.find_element_by_css_selector(
                        'ytd-comments div h2 yt-formatted-string > span'
                        ).text
                except Exception as error:
                    #print(f'O Erro encontrado foi {error.__cause__}')
                    comment = '0'
                finally:
                    pass

                comment = comment.replace('.', '')
                comments.append(comment)

                #print(comments)


                likes = []
                try:
                    like = soup.find(
                        'yt-formatted-string', 
                        id = 'text', 
                        class_='style-scope ytd-toggle-button-renderer style-text'
                        )
                    likes.append(like.text)
                    #print(likes)
                except:
                    like = driver.find_element_by_css_selector(
                        'ytd-menu-renderer div ytd-toggle-button-renderer a yt-formatted-string'
                        )
                    likes.append(like.text)
                else:
                    like = driver.find_element_by_css_selector(
                        '.ytd-video-primary-info-renderer > #top-level-buttons-computed > .style-scope:nth-child(1) #button > #button > .style-scope'
                        )
                    likes.append(like.text)


                descriptions = []
                description = driver.find_element_by_xpath(
                    '//*[@id="description"]/yt-formatted-string'
                ).text
                #for items in description:
                descriptions.append(description)

                keywords = []
                key = driver.find_element_by_xpath(
                    '/html/head/meta[5]'
                ).get_attribute(
                    'content'
                )
                keywords.append(key)
                #print(keywords)

                for title, views, comments, likes, descriptions, keywords in zip(
                    title,
                    views,
                    comments,
                    likes,
                    descriptions,
                    keywords
                ):
                    videos.append(
                        {
                        'Title': title,
                        'Views': views,
                        'Comments': comment,
                        'Likes': likes,
                        'Description': descriptions,
                        'Tags': keywords
                    }
                    )

                df2 = pd.DataFrame(videos)
                print(f'\n\n {df2} \n\n')


            #for title, views, comments, likes, descriptions, keywords in zip(title, views, comments, likes, descriptions, keywords):
            #    videos.append({'Title': title, 'Views': views, 'Comments': comment, 'Likes': likes, 'Description': descriptions, 'Tags': keywords})

            if not os.path.exists(f'{YT_Theme}/descricoes_{YT_Theme}'):
                os.mkdir(f'{YT_Theme}/descricoes_{YT_Theme}')
            else:
                print('')

            df2 = pd.DataFrame(videos)
            pontuacao = ['(',')',';',':','[',']',',', '"', '|', '"', '/', '\\n']

            name = re.sub(
                '[0-9]|,|\.|/|$|\(|\)|-|\+|:|•',
                ' ',

                name
            )
            for i in name:
                if i in name in pontuacao:
                    name.replace(i in pontuacao, '')

            df2.to_csv(f'{YT_Theme}/descricoes_{YT_Theme}/{name}.csv', index=False)
            #df2.to_csv(f'{YT_Theme}/descricoes_{YT_Theme}/{Canal}_df_l.csv')
            print(f'\n\n {df2} \n\n')


        theme_full = []
        for YT_Theme, subscribers, URL, title, date, views, comments, likes, descriptions, keywords in zip(
            YT_Theme,
            channel_URL,
            subscribers,
            title,
            video_date,
            views,
            comments,
            likes,
            descriptions,
            keywords

            ):
            theme_full.append(
                {
                'Theme': YT_Theme,
                'URL': URL,
                'Subscribers': subscribers,
                'Title': title,
                'Date':video_date,
                'Views': views,
                'Comments': comments,
                'Likes': likes,
                'Description': descriptions,
                'Tags': keywords
                }
            )
        #print(theme_full)

        if not os.path.exists(f'{YT_Theme}/series_{YT_Theme}'):
            os.mkdir(f'{YT_Theme}/series_{YT_Theme}')
        else:
            pass

        df_series = pd.DataFrame(theme_full)
        pontuacao = ['(',')',';',':','[',']',',', '"', '|', '"', '/', '\\n']

        name = re.sub('[0-9]|,|\.|/|$|\(|\)|-|\+|:|•', ' ', name)
        for i in name:
            if i in name in pontuacao:
                name.replace(i in pontuacao, ' ')

        df_series.to_csv(f'{YT_Theme}/series_{YT_Theme}/{name}.csv', index=False)
        #df2.to_csv(f'{YT_Theme}/descricoes_{YT_Theme}/{Canal}_df_l.csv')
        print(f'\n\n {df_series} \n\n')

        #for i in range(1,100):
        #   sg.one_line_progress_meter('Saving', i+6, 100, 'Saving Data','Saving the data in \n X:/ folder')

    driver.quit()
    theme()
sg.popup_ok(
    'Your datasets are in Instalation File'
)


# ----compilando----

# cd C:\Users\efrai\Downloads\auto-py-to-exe-master\auto-py-to-exe-master
# pip install eel
# python run.py

# folder: folder: C:\Users\efrai\Desktop\YT\dist

# pyinstaller --onefile --noconsole  C:\Users\efrai\Desktop\YT\__YT__\__API__\yt_full.py
# pyinstaller --noconfirm --onedir --noconsole --windowed --icon "C:/Users/efrai/Documents/ASTRO/ASTRO-Group.ico" --name "IA5" --upx-dir "C:/Users/efrai/Documents/ASTRO" --add-data "C:/Users/efrai/Downloads/chromedriver_win32_3/chromedriver.exe;." --add-binary "C:/Users/efrai/Downloads/chromedriver_win32_3/chromedriver.exe;."  "C:/Users/efrai/Desktop/YT/__YT__/__API__/yt_full.py"
#pyuic5 -x login.ui -o login.py  ####for PyQt archive in folder
#pyrcc5 -o files-rc.py filerc.qrc ####for archives in PyQt


#a = Analysis(['yt_full.py'],
#             pathex=['path\\to\\my\\script'],
#             binaries=[ ('path\\to\\my\\chromedriver.exe', '.\\selenium\\webdriver') ],
#             datas=None)