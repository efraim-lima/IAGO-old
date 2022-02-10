import pandas as pd
import config
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
#opencv-python
#tesseract

# YT_Category = layout.sgLayout()
# links = [
#     f'https://www.youtube.com/results?search_query={YT_Category}&sp=CAASAhAC',
#     f'https://www.youtube.com/results?search_query={YT_Category}&sp=CAISAhAC'
    
# ]
# quant = len(links)
# i = 0

def theme(link):
        YT_Category = link
        print(f'OLHA O Nome do tema!!!!\n\n\n{link}\n\n\n')
        driver = config.webDriver()
        driver.get(
            f'https://www.youtube.com/results?search_query={link}&sp=CAASAhAC'
        )

        config.inChrome()

        theme_in = []
        tweets = []

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
            tweet_path = f'./content/{YT_Category}/tweets/{YT_Category}.csv'
            tweets.append(tweet_path)
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
            
        config.quit()

        theme_data = []
        for YT_Category, name, subscribers, videos, URL, tweet_path in zip(
            theme_in,
            channel_name,
            channel_subs,
            channel_videos,
            channel_URL,
            tweets
        ):
            theme_data.append(
                {
                'Category':YT_Category,
                'Channel': name,
                'Inscritos':subscribers,
                'Videos': videos,
                'Ch_URL': URL,
                'Tweets_Path': tweet_path
            }
            )

        df = pd.DataFrame(theme_data)
        df = df.to_json()
        
        driver.quit()

        return df