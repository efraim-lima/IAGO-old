import pandas as pd
import config
import processing
import datetime

# print('\n\nTemas disponíveis: \n \n')
# arquivos = os.listdir('.')
# print( arquivos )
# YT_Theme = input('\n\n\nQual tema você precisa analisar?    \nR: ')

# print('\n\nCanais disponíveis: \n \n')
# canais_1 = os.listdir(f'{YT_Theme}/canais_{YT_Theme}/')
# print(canais_1)


def video_details(df, name, CH, *args, **kwargs):
    driver = config.webDriver()
    for item in df:
        print(name)
        print(df)
       
        print(links)
        #ch_name = df['Nome'][1].split('\n')


        ch_dados = {}
        dados_no = 0
        #browser = webdriver.Chrome('C:/Users/efrai/Downloads/chromedriver88_win32/chromedriver.exe') #precisa ser onde está instalado o Chromedriver
        videos = []
        for links in links:
            links = df['Video_URL']
            driver.get(
                f'{links}'
            ) ## estudando 
            config.pauseVideo()
            
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
                ' visualização',''
                )
            vie = vie.replace(
                '.', ''
            )
            view = vie.replace(
                ' visualizações', ''
            ) #soup.find('span', {'class':'view-count style-scope ytd-video-view-count-renderer'})
            views.append(view)
            #print(views)

            captions = []
            try:
                driver.find_element_by_xpath(
                    "//div[3]/div/ytd-menu-renderer/yt-icon-button/button/yt-icon" #este caminho está TOTALMENTE certo
                    ).click()
                icon = driver.find_element_by_xpath(
                    "/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-menu-popup-renderer/tp-yt-paper-listbox"
                    )
                icon = icon.find_element_by_xpath(
                    "//yt-formatted-string[contains(text(),'Abrir transcrição')]"
                ).click()

                #ESPERANDO APARECER A JANELA DE LEGENDA
                #box = WebDriverWait(driver, 2).until(
                #EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/ytd-transcript-body-renderer')))
                sleep(1)
                transcriptions = driver.find_element_by_xpath(
                    '//*[@id="body"]/ytd-transcript-body-renderer'
                )
                captions.append(transcriptions.text)
            except:
                captions.append('No captions')

            comments = []
            driver.maximize_window() # For maximizing window
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
                )
            driver.execute_script(
                "window.scrollTo(0, window.scrollY + 500)"
                )
            driver.implicitly_wait(5)
            try:
                comment = driver.find_element_by_css_selector(
                    'ytd-comments div h2 yt-formatted-string > span'
                    ).text
            except Exception as error:
                #print(f'O Erro encontrado foi {error.__cause__}')
                comment = '0'
            finally:
                pass

            comment = comment.replace(
                '.', ''
            )
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

            thumb = driver.find_element_by_xpath('//*[@id="watch7-content"]/link[2]').get_attribute("href")
            print(f'\n\nOlha a Thumb aqui!!\n\n{thumb}')
            path = "{}.jpg".format(title)
            urllib.request.urlretrieve(thumb, path)


            descriptions = []
            description = driver.find_element_by_xpath(
                '//*[@id="description"]/yt-formatted-string'
            ).text
            #for items in description:
            descriptions.append(description)
            #print(f'Descr.: {description}')

            #icon = driver.find_element_by_css_selector('div.style-scope.ytd-app:nth-child(12) ytd-page-manager.style-scope.ytd-app:nth-child(4) ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div.style-scope.ytd-watch-flexy:nth-child(8) div.style-scope.ytd-watch-flexy:nth-child(1) div.style-scope.ytd-watch-flexy div.style-scope.ytd-watch-flexy:nth-child(11) div.style-scope.ytd-watch-flexy ytd-video-primary-info-renderer.style-scope.ytd-watch-flexy div.style-scope.ytd-video-primary-info-renderer:nth-child(3) div.style-scope.ytd-video-primary-info-renderer:nth-child(6) div.style-scope.ytd-video-primary-info-renderer:nth-child(4) div.style-scope.ytd-video-primary-info-renderer:nth-child(1) ytd-menu-renderer.style-scope.ytd-video-primary-info-renderer yt-icon-button.dropdown-trigger.style-scope.ytd-menu-renderer button.style-scope.yt-icon-button > yt-icon.style-scope.ytd-menu-renderer')
            #icon.click()
            #try:
            #    views = soup.findAll('s%pan', class_='view-count style-scope ytd-video-view-count-renderer')
            #    print(views)
            #except:

            #final = video_titles.append([video_views, video_urls])
            #print(final)
            #videos = []

            keywords = []
            key = driver.find_element_by_xpath(
                '/html/head/meta[5]'
            ).get_attribute(
                'content'
            )
            keywords.append(key)
            #print(keywords)

            for title, views, comments, likes, descriptions, transcriptions, keywords in zip(
                title, views, comments, likes, descriptions, captions, keywords
            ):
                videos.append(
                    {
                    'Title': title,
                    'Views': views,
                    'Comments': comment,
                    'Likes': likes,
                    'Description': descriptions,
                    'Captions': transcriptions,
                    'Tags': keywords
                    }
                    )

            df2 = pd.DataFrame(videos)
            print(f'\n\n {df2} \n\n')

            if not os.path.exists(f'{YT_Theme}/descricoes_{YT_Theme}'):
                os.mkdir(f'{YT_Theme}/descricoes_{YT_Theme}')
            else:
                print('\n Canal já existe \n')

            df2 = pd.DataFrame(videos)
            pontuacao = ['(',')',';',':','[',']',',', '"', '|', '"']
            for i in name:
                if i in pontuacao in name:
                    name.replace(i in pontuacao, ' ')
            
            df2.to_csv(f'{YT_Theme}/descricoes_{YT_Theme}/{name}', index=False)
            #df2.to_csv(f'{YT_Theme}/descricoes_{YT_Theme}/{Canal}_df_l.csv')
            print(f'\n\n {df2} \n\n')

        driver.quit()