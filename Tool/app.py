from tasks import themeGe, channelYt, google, tweet, trending, saving
import layout 
from celery import chain

class Theme:
    nam = layout.call()
Theme()

def running():
    nam = Theme.nam
    print (f'''
        
        
        STARTED:
        {nam}
        
        
        ''')

    df = themeGe(nam)    
    print (f'''
    
    
    DF:
    {df}
    
    
    ''')

    
    # search = google.delay(nam)
running()