from googletrans import Translator
from deep_translator import GoogleTranslator
from textblob import TextBlob
import pandas as pd
import emojis
import nltk

nltk.download('averaged_perceptron_tagger')
nltk.download('brown')

def sentiment(text, *args, **kwargs):
        try:
            emoji = emojis.get(text)
        except:
            emoji = "null"
        translator=Translator()
        traducao = translator.translate(text, dest='en')
        traducao = traducao.text
        traducao2 = str(traducao)
        x = nltk.tokenize.sent_tokenize(traducao)
        for sentence in x:
            #print(sentence)
            traducao = GoogleTranslator(source='auto', target='en').translate(traducao)
       
        traducao = TextBlob(sentence)
        traducao2 = TextBlob(traducao2)
        sentiment = traducao.sentiment.polarity
        # print(text)
        # print(sentiment)
        sentiment2 = traducao2.sentiment.polarity
        return sentiment, sentiment2, traducao, emoji
        #print(archive)





# df=pd.read_csv('./content/pastel/descricoes_pastel/Alessandra Santos Pastel.csv')

# df['title_sentiment'] = df['Title'].apply(sentiment)