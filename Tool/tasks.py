#from celery.app import autoretry
import layout
from celery import Celery
import yt_theme
import yt_channel
import yt_video

# word = layout.call()
# yt = yt_theme.theme()

app = Celery(
    broker = 'amqp://guest@localhost//'
)

@app.task(
    bind=True,
    max_retry=3,
    default_retry_delay=2,
    autoretry_for=(TypeError, Exception)
          )
def take(self):
    self.request.retries
    word = layout.call()
    try:
        theme, df = yt_theme.theme(word)
    except:    
        self.retry()
    return theme, df
theme, df = take()

@app.task(
    bind=True,
    max_retry=3,
    default_retry_delay=2,
    #TimeoutException = 'selenium.common.exceptions.TimeoutException: Message: Connection refused (os error 111)',
    autoretry_for=(TypeError, Exception), 
    #
          )
def take_theme(self, theme, df):
    theme1, df1, ch = yt_channel.channel(theme, df)
    self.retry()
take_theme(theme, df)
