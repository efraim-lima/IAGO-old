import pandas as pd
import config
import layout
import processing
import saving
from selenium.webdriver.common.by import By

#sudo apt-get install pyhton3
#sudo apt install python3-virtualenv
#virtualenv iago
#source iago/bin/activate
#sudo pip install
#sudo apt-get install python3-tk
#bs4
#selenium
#webdriver-manager
#PySimpleGUI
#lxml

def theme():
    YT_Category = layout.sgLayout()
    urls = [
        f'https://www.youtube.com/results?search_query={YT_Category}'
    ]
    # browser = webdriver.Chrome('C:/Users/efrai/Downloads/chromedriver88_win32/chromedriver.exe') #precisa ser onde está instalado o Chromedriver

    driver = config.webDriver()
    #By = config.modBy()

    for url in urls:
        driver.get(
            '{}&sp=CAASAhAC'.format(url)
        )

        config.inChrome()

        theme_in = []

        channel_name = []
        names = driver.find_elements(
            By.CSS_SELECTOR,
            '#channel-title'
        )  # puxa o nome do canal

        for names in names:
            names = names.find_element(
                By.CSS_SELECTOR,
                '#text'
            )
            names = names.text
            YT_Category = YT_Category
            theme_in.append(YT_Category)
            name = channel_name.append(processing.processing(names))

        channel_subs = []
        subscribers = driver.find_elements(
            By.XPATH, 
            '//*[@id="subscribers"]'
        )
        for subscribers in subscribers:
            v = subscribers.text
            subscribers = channel_subs.append(processing.processing(v))

        channel_videos = []
        video_count = driver.find_elements(
            By.XPATH,
            '//*[@id="video-count"]'
            )
        for video_count in video_count:
            v = video_count.text
            videos = channel_videos.append(processing.processing(v))

        channel_URL = []
        channel_urls = driver.find_elements(
            By.XPATH,
            '//*[@id="main-link"]'
        )
        for channel_urls in channel_urls:
            channel_URL.append(
                (
                channel_urls.get_attribute('href')
                )
            )

        theme_data = []
        for YT_Category, name, subscribers, videos, URL in zip(
            theme_in,
            channel_name,
            channel_subs,
            channel_videos,
            channel_URL
        ):
            theme_data.append(
                {
                'Category':YT_Category,
                'Channel': name,
                'Inscritos':subscribers,
                'Videos': videos,
                'Ch_URL': URL
            }
            )

        #for i in tqdm(urls):

        df = pd.DataFrame(theme_data)

        saving.save_theme(YT_Category, df)
        return YT_Category, df

