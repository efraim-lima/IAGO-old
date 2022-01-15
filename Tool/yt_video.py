import pandas as pd
import config
import datetime
import processing
import saving
from time import sleep
import urllib
from selenium.webdriver.common.by import By

# print('\n\nTemas disponíveis: \n \n')
# arquivos = os.listdir('.')
# print( arquivos )
# YT_Theme = input('\n\n\nQual tema você precisa analisar?    \nR: ')

# print('\n\nCanais disponíveis: \n \n')
# canais_1 = os.listdir(f'{YT_Theme}/canais_{YT_Theme}/')
# print(canais_1)

#theme--->tema
#CH--->canal

def video(theme, df, channel, *args, **kwargs):
    print(f'OLHA o DF \n\n\n\n\n{df}')
    videos = []
    links = df['Video_URL']
    print(links)
    while True:
        for link in links:
            driver = config.webDriver()
            print(theme)
            #ch_theme = df['Nome'][1].split('\n')     
            driver.get(
                f'{link}'
            ) ## estudando 
            config.pauseVideo()
            
            titles = []
            try:
                title =  driver.find_element(
                    By.XPATH,
                    '//[@id="container"]/h1/yt-formatted-string'
                    ).text
            except:
                driver.implicitly_wait(1)
                title = driver.find_element(
                    By.CSS_SELECTOR,
                    ".title > .ytd-video-primary-info-renderer"
                    ).text
            finally:
                pass
            
            titles.append(title)

            views = []
            vi = driver.find_element(
                By.XPATH,
                "//div[@id='count']/ytd-video-view-count-renderer/span"
                )
            vi = vi.text
            view = processing.processing(vi)
            views.append(view)
            #print(views)

            captions = []
            try:
                driver.find_element(
                    By.XPATH,
                    "//div[3]/div/ytd-menu-renderer/yt-icon-button/button/yt-icon" #este caminho está TOTALMENTE certo
                    ).click()
                icon = driver.find_element(
                    By.XPATH,
                    "/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-menu-popup-renderer/tp-yt-paper-listbox" #Seria o ícone do elemento acima do botão
                    #"/html[1]/body[1]/ytd-app[1]/ytd-popup-container[1]/tp-yt-iron-dropdown[1]/div[1]/ytd-menu-popup-renderer[1]/tp-yt-paper-listbox[1]/ytd-menu-service-item-renderer[2]/tp-yt-paper-item[1]"
                    )
                try:
                    icon = icon.find_element(
                        By.XPATH,
                        "//yt-formatted-string[contains(text(),'Abrir transcrição')]" #aqui sim é a parte do botão
                    ).click()
                except:
                    icon = icon.find_element(
                    By.XPATH,
                        "//yt-formatted-string[contains(text(),'Open transcript')]" #aqui sim é a parte do botão
                    ).click()
                    
                new_icon = driver.find_element(
                    By.XPATH,
                    "//ytd-menu-renderer[@class='style-scope ytd-engagement-panel-title-header-renderer']//yt-icon-button[@id='button']//button[@id='button']//yt-icon[@class='style-scope ytd-menu-renderer']"
                ).click()
                
                new_icon = driver.find_element(
                    By.XPATH,
                    "//tp-yt-paper-item[@class='style-scope ytd-menu-service-item-renderer']"
                )
                
                new_icon = new_icon.find_element(
                    By.XPATH,
                    "//yt-formatted-string[@class='style-scope ytd-menu-service-item-renderer']"
                ).click()

                #ESPERANDO APARECER A JANELA DE LEGENDA
                #box = WebDriverWait(driver, 2).until(
                #EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/ytd-transcript-body-renderer')))
                sleep(1)
                transcriptions = driver.find_element(
                    By.XPATH,
                    '//*[@id="body"]/ytd-transcript-body-renderer'
                )
                transcriptions = transcriptions.text
                transcriptions = processing.processing2(transcriptions)
                captions.append(transcriptions)
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
            driver.implicitly_wait(1)
            try:
                comment = driver.find_element(
                    By.CSS_SELECTOR,
                    'ytd-comments div h2 yt-formatted-string > span'
                    )
            except Exception as error:
                #print(f'O Erro encontrado foi {error.__cause__}')
                comment = '0'
            finally:
                pass
            
            try:
                comment = comment.text
            except:
                pass
            comment = processing.processing2(comment)
            comments.append(comment)

            #print(comments)


            likes = []
            try:
                like = driver.find_element(
                    By.CSS_SELECTOR,
                    'div.style-scope.ytd-app:nth-child(13) ytd-page-manager.style-scope.ytd-app:nth-child(4) ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div.style-scope.ytd-watch-flexy:nth-child(8) div.style-scope.ytd-watch-flexy:nth-child(1) div.style-scope.ytd-watch-flexy div.style-scope.ytd-watch-flexy:nth-child(11) div.style-scope.ytd-watch-flexy ytd-video-primary-info-renderer.style-scope.ytd-watch-flexy div.style-scope.ytd-video-primary-info-renderer div.style-scope.ytd-video-primary-info-renderer:nth-child(6) div.style-scope.ytd-video-primary-info-renderer:nth-child(4) div.style-scope.ytd-video-primary-info-renderer:nth-child(1) ytd-menu-renderer.style-scope.ytd-video-primary-info-renderer div.top-level-buttons.style-scope.ytd-menu-renderer > ytd-toggle-button-renderer.style-scope.ytd-menu-renderer.force-icon-button.style-text:nth-child(2)'
                    )
                #print(likes)
            except:
                like = driver.find_element(
                    By.CSS_SELECTOR,
                    'ytd-menu-renderer div ytd-toggle-button-renderer a yt-formatted-string'
                    )
            else:
                like = driver.find_element(
                    By.CSS_SELECTOR,
                    '.ytd-video-primary-info-renderer > #top-level-buttons-computed > .style-scope:nth-child(1) #button > #button > .style-scope'
                )
            
            like = like.text
            like = processing.processing(like)
            likes.append(like)

            thumbs = []
            thumb = driver.find_element(
                By.XPATH,
                '//*[@id="watch7-content"]/link[2]').get_attribute("href")
            print(f'\n\nOlha a Thumb aqui!!\n\n{thumb}')
            path = f"../../content/{theme}/{channel}/{title}.jpg"
            thumbs.append(path)
            saving.thumbnail(theme, channel, title, thumb)
            


            descriptions = []
            description = driver.find_element(
                By.XPATH,
                '//*[@id="description"]/yt-formatted-string'
            )
            
            description = description.text
            #for items in description:
            descriptions.append(description)
            #print(f'Descr.: {description}')

            #icon = driver.find_element(
            # By.CSS_SELECTOR,'div.style-scope.ytd-app:nth-child(12) ytd-page-manager.style-scope.ytd-app:nth-child(4) ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div.style-scope.ytd-watch-flexy:nth-child(8) div.style-scope.ytd-watch-flexy:nth-child(1) div.style-scope.ytd-watch-flexy div.style-scope.ytd-watch-flexy:nth-child(11) div.style-scope.ytd-watch-flexy ytd-video-primary-info-renderer.style-scope.ytd-watch-flexy div.style-scope.ytd-video-primary-info-renderer:nth-child(3) div.style-scope.ytd-video-primary-info-renderer:nth-child(6) div.style-scope.ytd-video-primary-info-renderer:nth-child(4) div.style-scope.ytd-video-primary-info-renderer:nth-child(1) ytd-menu-renderer.style-scope.ytd-video-primary-info-renderer yt-icon-button.dropdown-trigger.style-scope.ytd-menu-renderer button.style-scope.yt-icon-button > yt-icon.style-scope.ytd-menu-renderer')
            #icon.click()
            #try:
            #    views = soup.findAll('s%pan', class_='view-count style-scope ytd-video-view-count-renderer')
            #    print(views)
            #except:

            #final = video_titles.append([video_views, video_urls])
            #print(final)
            #videos = []

            keywords = []
            key = driver.find_element(
                By.XPATH,
                '/html/head/meta[5]'
            ).get_attribute(
                'content'
            )
            keywords.append(key)
            #print(keywords)
            
            channels = []
            channels.append(channel)
            
            themes = []
            themes.append(theme)
            
            previa = []
            
            driver.close()
            
            for theme, title, channel, view, comments, like, descriptions, transcriptions, key, path in zip(
                themes, titles, channels, views, comments, likes, descriptions, captions, keywords, thumbs
            ):
                videos.append(
                    {
                    'Theme': theme,
                    'Title': title,
                    'Channel': channel,
                    'Views': view,
                    'Comments': comment,
                    'Likes': like,
                    'Description': description,
                    'Captions': transcriptions,
                    'Tags': key,
                    'Thumbs':path
                    })
                previa.append(
                    {
                    'Theme': theme,
                    'Title': title,
                    'Channel': channel,
                    'Views': view,
                    'Comments': comment,
                    'Likes': like,
                    'Description': description,
                    'Captions': transcriptions,
                    'Tags': key,
                    'Thumbs':path
                    })
                
            print(previa)
        driver.quit()
        df = pd.DataFrame(videos)
        print(f'\n\n {df} \n\n')
        
        saving.video(theme, df, channel)
        return theme, df, channel

df1 = pd.read_csv("/home/efraim/Documentos/IAGO/IAGO/content/pastel/canais_pastel/Alessandra Santos Pastel.csv")
#df1 = df1['Video_URL']
channel1 = 'Alessandra Santos Pastel'
thee = 'pastel'
video(thee, df1, channel1)