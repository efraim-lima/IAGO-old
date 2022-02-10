from tasks import take, take_theme, search, take_tweet, trending, saving
import layout 
from celery import chain

class Theme:
    theme = layout.call()
Theme()
def running():
    # c = chain(
    #     take.s(Theme.theme),
    #     take_theme.s()
    # )
    theme = Theme.theme
    df = take(theme)    
    # df = df.get(df)
    # df = df['Ch_URL']
    
    print(f'''
          
          
          
          DF
          {df}
          
          
          ''')
    
    
    searchDf = search.delay(theme)
    ttDf = take_tweet.delay(theme)
    dataset = trending.delay(theme)
    
    # for row in df:
    chDf = take_theme.delay(df)
        
    saving.delay(theme, df, ttDf, dataset)
running()