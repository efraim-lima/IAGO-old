import re
import os
import os.path
from spacy.lang.pt.stop_words import STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer
import pt_core_news_sm
import pandas as pd
from unidecode import unidecode
from time import sleep

#python -m spacy download pt_core_news_sm

nlp = pt_core_news_sm.load()

pasta_mãe = os.listdir('./content')
#print( pasta_mãe )
YT_Theme = input('Qual tema voce tem interesse em analizar? \nR:  ')
archives = os.listdir(f'{YT_Theme}/descricoes_{YT_Theme}/')

def TextAnalyzer():
    for archive in archives:
        df=pd.read_csv(f'./content/{YT_Theme}/descricoes_{YT_Theme}/{archive}')
        df = df['Captions']
        print(df)

        links = []
        hashtags = []

        for item in df:

            text = str(item)
            doc = nlp(item)

            corpus = [sent.text.lower() for sent in doc.sents ]
            cv = CountVectorizer(stop_words=list(STOP_WORDS))
            cv_fit=cv.fit_transform(corpus)
            word_list = cv.get_feature_names();
            count_list = cv_fit.toarray().sum(axis=0)
            word_frequency = dict(zip(word_list,count_list))

            val=sorted(word_frequency.values())
            higher_word_frequencies = [word for word,freq in word_frequency.items() if freq in val[-3:]]
            #print("\nWords with higher frequencies: ", higher_word_frequencies)
            # gets relative frequency of words
            higher_frequency = val[-1]
            for word in word_frequency.keys():
                word_frequency[word] = (word_frequency[word]/higher_frequency)
            
            sentence_rank={}
            for sent in doc.sents:
                for word in sent :
                    if word.text.lower() in word_frequency.keys():
                        if sent in sentence_rank.keys():
                            sentence_rank[sent]+=word_frequency[word.text.lower()]
                        else:
                            sentence_rank[sent]=word_frequency[word.text.lower()]
            top_sentences=(sorted(sentence_rank.values())[::-1])
            top_sent=top_sentences[:3]

            summary=[]
            for sent,strength in sentence_rank.items():
                if strength in top_sent:
                    summary.append(sent)
                else:
                    continue
            for i in summary:
                print(i,end=" ")


TextAnalyzer()