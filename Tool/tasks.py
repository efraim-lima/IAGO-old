# from celery.app import autoretry
# sudo apt-get install rabbitmq-server
# sudo apt install redis-server
from celery import Celery
import yt_theme
import yt_channel
import twitter
import trends
import saving
import google
from celery.contrib import rdb
# import yt_video

#name = layout.call()
# yt = yt_theme.theme()

app = Celery(
    'tasks',
    broker = 'redis://localhost:6379/0'
    # broker = 'pyamqp://guest@localhost//',
    # backend = 'amqp://guest@localhost//'
)

@app.task(
    name="Getting Theme",
    bind=True,
    retry_backoff = 2,
    autoretry_for=(TypeError, Exception)
          )
def themeGe(self, name, *args, **kwargs):
    self.request.retries
    # name = layout.call()
    try:
        df = yt_theme.theme(name)
    except:    
        self.retry()
    # rdb.set_trace()
    return df




@app.task(
    name='Getting Google',
    bind=True,
    retry_backoff = 2,
    autoretry_for=(TypeError, Exception)
          )
def google(self,theme, *args, **kwargs):
    self.request.retries
    #name = layout.call()
    try:
        searchDf = google.search(theme)
    except:    
        self.retry()
    # rdb.set_trace()
    return searchDf


@app.task(
    bind=True,
    retry_backoff = 2,
    autoretry_for=(TypeError, Exception)
    )
def tweet(self, theme, *args, **kwargs):
    ttDf = twitter.tweet_anal(theme)
    self.retry()
    return ttDf

@app.task(
    bind=True,
    retry_backoff = 2,
    autoretry_for=(TypeError, Exception)
    )
def trending(self, theme, *args, **kwargs):
    dataset = trends.trends(theme)
    self.retry()
    # rdb.set_trace()
    return dataset


@app.task(
    bind=True,
    retry_backoff = 2,
    #TimeoutException = 'selenium.common.exceptions.TimeoutException: Message: Connection refused (os error 111)',
    autoretry_for=(TypeError, Exception)
    )
def channelYt(self, df, *args, **kwargs):
    theme1, chDf, ch = yt_channel.channel(df)
    self.retry()
    # rdb.set_trace()
    return chDf


@app.task(
    bind=True,
    retry_backoff = 2,
    #TimeoutException = 'selenium.common.exceptions.TimeoutException: Message: Connection refused (os error 111)',
    autoretry_for=(TypeError, Exception)
    )
def saving(self, theme, df, ttDf, dataset, *args, **kwargs):
    
    saving.theme(theme, df)
    self.retry()
    # rdb.set_trace()

@app.task(
    bind=True,
    retry_backoff = 2,
    #TimeoutException = 'selenium.common.exceptions.TimeoutException: Message: Connection refused (os error 111)',
    autoretry_for=(TypeError, Exception)
    )
def saving_tweet(self, theme, df, ttDf, dataset, *args, **kwargs):
    df = df.reset_index(drop=True)
    df2 = ttDf.reset_index(drop=True)
    df = df.join(df2)
    df = df.join(dataset)
    df = df.loc[:,~df.columns.duplicated()]
    saving.theme(theme, df)
    self.retry()
    # rdb.set_trace()



