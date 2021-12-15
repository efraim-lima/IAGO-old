import layout
from celery import Celery
import yt_theme
import yt_channel
import yt_video

app = Celery(
    broker = 'amqp://guest@localhost//'
)

@app.task
def take():
    word = layout.call()
    theme = yt_theme.theme(word)
take()
