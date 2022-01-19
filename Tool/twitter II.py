import tweepy
import pandas as pd
import sentiment_analysis
import datetime
import saving
import nltk
import sentiment


# consumer_key = 'dG9VUEhTZUJyNkJaNDhUUlZxWjQ6MTpjaQ'
# consumer_secret = 'T7m6PAOycOvgq_TuDcZ60SholK3Q0MhqMaPFFLaTYIY_Gk8Qs2'
# access_token = '226815872-bx8C7lUGS95xTqmPE2IpAmB1xk6T0lhNguUO09zx'
# access_token_secret = 'VYbxiUfpTRrGUs88RKImJ2xGcduy6tqGMb5sKpLWFjKBG'



nltk.download('punkt')

consumer_key = 'LqztBo1V1vc0naC5Dam9rtYqU'
consumer_secret = 'ERePUqG3c5qgJDkh4Bfy3tlYkiF0DIiImZjBYgBfBWFuhwsg6C'
access_token = '226815872-rWfczDtae2MtXb2xcEyGJGHxmnF2PyGuFJsG5tcg'
access_token_secret = 'PsbJWgfeEuVutQUGgcXUvWoCoYKdJ6hfoU9YKyBplBKHx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
print("foi")

def get_tweets(q):
    print("foi")
    date = datetime.date.today()
    
    print('########################## O que dizem sobre ######################################')
    data = datetime.date.today()
    
    now = datetime.datetime.now()
    
    #until=datetime.date.today()
    posts = api.search_tweets(q={q}, lang = 'en', count=50000)
    
    whatSays = []
    Translate = []
    whatFeels = []
    whatFeels2 = []
    Emoji = []
    Tweets = []
    i=1  
    for tweet in posts[0:500]:
        tweet = tweet.text
        print(f'''
              
              Tweet
              {tweet}
              
              ''')
        sentiment, sentiment2, translate, emoji = sentiment_analysis.sentiment(tweet)
        #print(sentiment)
        i = i+1
    Tweets.append(tweet)
    Translate.append(translate)
    whatFeels.append(sentiment)
    whatFeels2.append(sentiment2)
    Emoji.append(emoji)
        
    for tweet, sentiment, sentiment2, translate, emoji in zip(
        Tweets, whatFeels, whatFeels2, Translate, Emoji
    ):
        whatSays.append({
            'Tweet': tweet,
            'Translate': translate,
            'Emoji': emoji,
            'Sentiment': sentiment,
            'Sentiment2': sentiment2
        })
    
    name = f'Arthur {now}'
    df = pd.DataFrame(whatSays)
    df2 = df['Tweet']
    sentiment.fillings(df2)
    saving.tweet(name, df)
    print (f'\n\n{df}\n\n')
    return df
    
# def get_profile(profile):
    
#     print('########################## perfil do AA ######################################')
    
#     posts = api.user_timeline(screen_name=profile, count = 1000,tweet_mode="extended")
    
#     Posts = []
#     Translate = []
#     whatFeels = []
#     Tweets = []
#     i=1
#     for tweet in posts[0:50]:
#         tweet = tweet.full_text
#         #sentiment, translate = sentiment_analysis.sentiment(tweet)
#         i = i+1
#         Tweets.append(tweet)
#         #Translate.append(translate)
#         #whatFeels.append(sentiment)
        
#     for tweet in zip(
#         Tweets
#     ):
#         Posts.append({
#             'Tweet': tweet,
#         })
#     df = pd.DataFrame(Posts)
#     print (df)
#     return df

# get_profile("Arthur Aguiar")
get_tweets("Arthur Aguiar")