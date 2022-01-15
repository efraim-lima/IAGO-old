import datetime
from TwitterSearch import *
import pandas as pd
import sentiment_analysis
import json
import saving


# consumer_key = 'dG9VUEhTZUJyNkJaNDhUUlZxWjQ6MTpjaQ'
# consumer_secret = 'T7m6PAOycOvgq_TuDcZ60SholK3Q0MhqMaPFFLaTYIY_Gk8Qs2'
# access_token = '226815872-bx8C7lUGS95xTqmPE2IpAmB1xk6T0lhNguUO09zx'
# access_token_secret = 'VYbxiUfpTRrGUs88RKImJ2xGcduy6tqGMb5sKpLWFjKBG'

consumer_key = 'LqztBo1V1vc0naC5Dam9rtYqU'
consumer_secret = 'ERePUqG3c5qgJDkh4Bfy3tlYkiF0DIiImZjBYgBfBWFuhwsg6C'
access_token = '226815872-rWfczDtae2MtXb2xcEyGJGHxmnF2PyGuFJsG5tcg'
access_token_secret = 'PsbJWgfeEuVutQUGgcXUvWoCoYKdJ6hfoU9YKyBplBKHx'

from TwitterSearch import *
def tweet_anal():
    try:

        ts = TwitterSearch(
            consumer_key = consumer_key,
            consumer_secret = consumer_secret,
            access_token = access_token,
            access_token_secret = access_token_secret
        )
        now = datetime.datetime.now()
        name = 'Arthur Aguiar {now}'
        arroba = 'Aguiarthur'
        tso = TwitterSearchOrder()
        tso.set_keywords([f'{name}', f'@{arroba}'], or_operator = True)
        tso.set_language('pt')
        tso.set_since(datetime.date.today()) #(datetime.date(2021,12,1))
        tso.set_until(datetime.date.today())
        # tso.set_result_type('mixed') #{mixed, recent, popular}
        # tso.set_positive_attitude_filter() #atitudes positivas --- opcional
        # tso.set_negative_attitude_filter() #atitudes negativas --- opcional
        # tso.set_question_filter() # resultados que contem perguntas
        
        ListaFull = []
        User = []
        Posts = []
        Translate = []
        whatFeels = []
        Tweets = []
        Emoji = []
        
        i = 0
        for tweet in ts.search_tweets_iterable(tso):
            #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
            #text = ('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ))
            user = tweet['user']['screen_name']
            print(f'''
                  
                  User:
                  {user}
                  
                  ''')
            text = tweet['text']
            date = tweet['created_at']
            source = tweet['source']
            photo_profile = tweet['user']['profile_image_url']
            sentiment, translate, emoji = sentiment_analysis.sentiment(text)
            i = i+1
            #print(type(sentiment))
            User.append(user)
            Tweets.append(text)
            Translate.append(translate)
            whatFeels.append(sentiment)
            Emoji.append(emoji)
            i+=1
            
            if i > 10000:
                break
            
        for user, text in zip(
            User, Tweets
        ):
            Posts.append({
                'User': user,
                'Tweet': text,
                'Date': date
                })
        df = pd.DataFrame(Posts)
        saving.tweet(name, df)
        
        print (df)
        return df
            #dataframe = dataframe.append(text)
            #print(text)
            
    except TwitterSearchException as e:
        print(e)
tweet_anal()