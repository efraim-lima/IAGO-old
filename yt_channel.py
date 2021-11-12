import pandas as pd
import config
import processing
import datetime

def channel(name, df, *args, **kwargs):
    #if not os.path.exists(f'{name}/{name}.csv'):
    #    import yt_theme
    #    yt_theme(name)
    #else:
    #    arquivos = os.listdir('.')
    #    print( arquivos )
    #    name = input('\n\n\nQual o seu tema de interesse?   \nR: ')
    #
    #    df = pd.read_csv('{}/{}.csv'.format(name, name))
    #    print(df)
    #    links = df['Ch_URL']
    #    print(links)

    
    YT_Theme = name

    #pd.read_csv(f'{YT_Theme}/{YT_Theme}.csv')
    links = df['Ch_URL']

    driver = config.webDriver()

    pontuacao = ['(',')',';',':','[',']',',', '"', '|', '"', '/', '\\n']
    for links in links:
        driver.get(
            '{}/videos?view=0&sort=p&flow=grid'.format(links)
        )

        config.inChrome()

        theme_in = []
        for i in links:
            theme_in.append(YT_Category)
        Links = []
        Links.append(links)

        #for i in range(1,100):
        #    sg.one_line_progress_meter(
        #        'Channels', i+2, 100, 'Better Videos','Decrypting the better\n videos in the Channels'
        #        ) #apenas um progress bar genérico (ainda não sei fazer um progress bar realmente útil)

        content = driver.page_source.encode(
            'utf-8'
        ).strip()

        CH = driver.find_element_by_xpath(
            "//div[@id='inner-header-container']//div[@id='meta']//ytd-channel-name[@id='channel-name']//div[@id='container']//div[@id='text-container']//yt-formatted-string[@id='text']"
            ).text
        #print(f'\n{CH}\n')
        CH = processing.processing(CH)
        
        subscribers = driver.find_element_by_xpath(
            "//yt-formatted-string[@id='subscriber-count']"
            ).text
        subscribers = processing.processing(subscribers)
        #channel_videos.append(subscribers)

        video_titles = []
        titles = driver.find_elements_by_css_selector(
            '#video-title'
        )
        for titles in titles:
            video_titles.append(titles.get('title'))
        #video_titles = pd.DataFrame({'Title':video_titles})
        #print(video_titles)

        video_views = []
        views = driver.find_elements_by_xpath('//*[@id="metadata-line"]/span[1]')    
        v = views.text
        view = processing.processing(v)
        video_views.append(view)

        video_date = []
        dates = driver.find_elements_by_xpath('//*[@id="metadata-line"]/span[2]')
        for dates in dates:
            d = dates.text
            video_date.append(d)

        #video_views = pd.DataFrame(video_views)

        video_urls = []
        URLs = driver.find_elements_by_css_selector(
            '#video-title'
        )
        for URLs in URLs:
            video_urls.append(
                (
                URLs.get_attribute('href')
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
                    #'Videos': videos_uni,
                    'Date': dates,
                    f'View_{today}': views,
                    f'Subs_{today}': subscribers
                }
                )
        #print(channels)

        df2 = pd.DataFrame(channels)
        

        return df2, YT_Category, CH


        #print(canais_1)
        #print(YT_Theme)