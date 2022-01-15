from textblob import TextBlob
import pandas as pd

def sentiment_calc(text):
    try:
        text = TextBlob(text)
        traducao = TextBlob(str(text.translate(to='en')))
        sentiment = traducao.sentiment.polarity
        print(text)
        print(sentiment)
        return text
    except:
        return None

        #print(archive)





df=pd.read_csv('./content/pastel/descricoes_pastel/Alessandra Santos Pastel.csv')

df['title_sentiment'] = df['Title'].apply(sentiment_calc)