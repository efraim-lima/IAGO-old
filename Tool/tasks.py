import layout
import yt_theme
import yt_channel
import yt_video
from multiprocessing import Process
from celery import Celery

app = Celery(
    broker = 'amqp://guest@localhost//'
)

@app.task
def take():
    word = layout.call()
    theme = yt_theme.theme(word)
take()
