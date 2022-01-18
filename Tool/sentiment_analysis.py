from googletrans import Translator
from deep_translator import GoogleTranslator
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import pandas as pd
import emojis
import nltk

nltk.download('averaged_perceptron_tagger')
nltk.download('brown')

def sentiment(text):
        #text = "isso é muito ruim, ruim demais"
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
            traducao = GoogleTranslator(source='auto', target='en').translate(traducao)
       
        traducao = TextBlob(sentence, analyzer=NaiveBayesAnalyzer)
        traducao2   = TextBlob(traducao2)
        sentiment = traducao.sentiment.polarity
        sentiment2 = traducao2.sentiment.polarity
        print(sentence)
        print(traducao)
        print(text)
        print(sentiment)
        print(sentiment2)
        return sentiment, sentiment2, traducao, emoji
        #print(archive)
#sentiment()




# df=pd.read_csv('./content/pastel/descricoes_pastel/Alessandra Santos Pastel.csv')

# df['title_sentiment'] = df['Title'].apply(sentiment)