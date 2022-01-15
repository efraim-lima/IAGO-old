from deep_translator import GoogleTranslator
from textblob import TextBlob
import pandas as pd
import emojis
import nltk

def sentiment(text, *args, **kwargs):
        print(f"""
              Tweet:
              {text}
              
              """)
        try:
            emoji = emojis.get(text)
        except:
            emoji = "null"
        text = TextBlob(text)
        #phrase = nltk.tokenize.sent_tokenize(text)
        #translator=Translator()
        traducao = GoogleTranslator(source='auto', target='en').translate(text)
        traducao = traducao.text
        sentiment = traducao.sentiment.polarity
        print(text)
        print(sentiment)
        return sentiment, traducao, emoji


        #print(archive)





df=pd.read_csv('./content/pastel/descricoes_pastel/Alessandra Santos Pastel.csv')

df['title_sentiment'] = df['Title'].apply(sentiment)