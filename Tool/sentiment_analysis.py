from googletrans import Translator
from deep_translator import GoogleTranslator
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import pandas as pd
import emojis
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import textblob.exceptions

nltk.download('vader_lexicon')
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
                Analyzer = SentimentIntensityAnalyzer()
                polarity = Analyzer.polarity_scores(sentence)
                try:
                    traducao = TextBlob(sentence, analyzer=NaiveBayesAnalyzer())
                    traducao2   = TextBlob(traducao2)
                except textblob.exceptions.TranslatorError:
                    word=" "  #replace word with space
                    txt=txt+word
                except textblob.exceptions.NotTranslated:
                    txt=txt+word+" "
                else:
                    txt=txt+traducao2+" "
                sentiment = traducao.sentiment
                sentiment2 = traducao2.sentiment.polarity
        print(polarity)
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