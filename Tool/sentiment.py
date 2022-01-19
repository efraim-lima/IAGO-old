import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import nltk
import base_texto
import base_teste
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
import datetime
import saving

nltk.download('stopwords')
nltk.download('rslp')
nltk.download('punkt')
nltk.download('wordnet')

texto = pd.read_csv('./Tool/Tweets_Mg.csv', encoding='UTF-8')
texto = texto.drop_duplicates()
exemplo_base = pd.DataFrame(texto)

# print(f'''
      
#       Base do conhecimento
#       {exemplo_base}
      
      
#       ''')


#exemplo_base = pd.DataFrame(base_texto.base)
exemplo_base.columns = ['Frase', 'Sentimento']
exemplo_base_teste = pd.DataFrame(base_texto.base)
exemplo_base_teste.columns = ['Frase', 'Sentimento']
tweets = texto['Frase']
classes = texto['Sentimento']

print((exemplo_base.Sentimento.value_counts() / exemplo_base.shape[0])*100)

lista_stop = nltk.corpus.stopwords.words('portuguese')
np.transpose(lista_stop)
#lista_stop.append('palavra')


###################################### Stopwords ######################################

def RemoveStopWords(instancia):
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))


###################################### Stemmeer ######################################

def Stemming(instancia):
    stemmer = nltk.stem.RSLPStemmer()
    palavras = []
    for w in instancia.split():
        palavras.append(stemmer.stem(w))
    return (" ".join(palavras))

##################################### Limpeza ######################################

def Limpeza_dados(instancia):
    # remove links, pontos, virgulas,ponto e virgulas dos tweets
    instancia = re.sub(r"http\S+", "", instancia).lower().replace('.','').replace(';','').replace('-','').replace(':','').replace(')','')
    return (instancia)
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

def Lemmatization(instancia):
  palavras = []
  for w in instancia.split():
    palavras.append(wordnet_lemmatizer.lemmatize(w))
  return (" ".join(palavras))

##################################### preprocessing ######################################

def Preprocessing(instancia):
    stemmer = nltk.stem.RSLPStemmer()
    instancia = re.sub(r"http\S+", "", instancia).lower().replace('.','').replace(';','').replace('-','').replace(':','').replace(')','')
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [stemmer.stem(i) for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))

# Aplica a função em todos os dados:
tweets = [Preprocessing(i) for i in tweets]
print(tweets)

frase = 'A live do @blogminerando é show! :) :-) ;) =D'
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
word_tokenize(frase)
tweet_tokenizer = TweetTokenizer()
print(tweet_tokenizer.tokenize(frase))

#vectorizer = CountVectorizer(analyzer="word", tokenizer=tweet_tokenizer.tokenize)
vectorizer = CountVectorizer(analyzer="word", tokenizer=tweet_tokenizer.tokenize, max_features=1000)   #<-- bases muito grandes

freq_tweets = vectorizer.fit_transform(tweets)
print(type(freq_tweets))
print(freq_tweets.shape)

########################################### Treino do Modelo ###############################################################

modelo = MultinomialNB()
modelo.fit(freq_tweets,classes)
freq_tweets.A


# defina instâncias de teste dentro de uma lista
testes = pd.read_csv('./Arthur Aguiar 2022-01-17 23:33:10.277352/Arthur Aguiar 2022-01-17 23:33:10.277352.csv', on_bad_lines='skip')
testes = testes['Tweet']

testes = [Preprocessing(i) for i in testes]

# Transforma os dados de teste em vetores de palavras.
freq_testes = vectorizer.transform(testes)

whatSays = []
# Fazendo a classificação com o modelo treinado.
for t, c in zip (testes,modelo.predict(freq_testes)):
  whatSays.append({
    'Tweet':t,
    'SentimentML':c
  })
  
  now = datetime.datetime.now()
  name = f'SentimentAnalisysBBB{now}'
  df = pd.DataFrame(whatSays)
  saving.tweet(name, df)
  print (f'\n\n{df}\n\n')
  
  print (t +", "+ c)

# Probabilidades de cada classe
print (modelo.classes_)
modelo.predict_proba(freq_testes).round(2)


######################################### Tags de Negações ##############################################################

def marque_negacao(texto):
    negacoes = ['não','not']
    negacao_detectada = False
    resultado = []
    palavras = texto.split()
    for p in palavras:
        p = p.lower()
        if negacao_detectada == True:
            p = p + '_NEG'
        if p in negacoes:
            negacao_detectada = True
        resultado.append(p)
    return (" ".join(resultado))


from sklearn.pipeline import Pipeline

pipeline_simples = Pipeline([
  ('counts', CountVectorizer()),
  ('classifier', MultinomialNB())
])

pipeline_negacoes = Pipeline([
  ('counts', CountVectorizer(tokenizer=lambda text: marque_negacao(text))),
  ('classifier', MultinomialNB())
])

pipeline_simples.fit(tweets,classes)
pipeline_simples.steps
pipeline_negacoes.fit(tweets,classes)
pipeline_negacoes.steps

pipeline_svm_simples = Pipeline([
  ('counts', CountVectorizer()),
  ('classifier', svm.SVC(kernel='linear'))
])

pipeline_svm_negacoes = Pipeline([
  ('counts', CountVectorizer(tokenizer=lambda text: marque_negacao(text))),
  ('classifier', svm.SVC(kernel='linear'))
])

resultados = cross_val_predict(pipeline_simples, tweets, classes, cv=10)
metrics.accuracy_score(classes,resultados)

sentimento=['Positivo','Negativo','Neutro']
print (metrics.classification_report(classes,resultados)) #removi sentimento

Tabii = pd.crosstab(classes, resultados, rownames=['Real'], colnames=['Predito'], margins=True)
print(Tabii)

def Metricas(modelo, tweets, classes):
  resultados = cross_val_predict(modelo, tweets, classes, cv=10)
  return 'Acurácia do modelo: {}'.format(metrics.accuracy_score(classes,resultados))

# naive bayes simples
Metricas(pipeline_simples,tweets,classes)

# naive bayes com tag de negacoes
Metricas(pipeline_negacoes,tweets,classes)

# svm linear simples
Metricas(pipeline_svm_simples,tweets,classes)

# svm linear com tag de negacoes
Metricas(pipeline_svm_negacoes,tweets,classes)

######################################## modelo com tag de negações ############################################################

resultados = cross_val_predict(pipeline_negacoes, tweets, classes, cv=10)
metrics.accuracy_score(classes,resultados)

sentimento=['Positivo','Negativo','Neutro']
print (metrics.classification_report(classes,resultados)) #removi sentimento


###################################### Matriz de Confusão ###########################################################

matrix = pd.crosstab(classes, resultados, rownames=['Real'], colnames=['Predito'], margins=True)
print(matrix)

# Bigrams
vectorizer = CountVectorizer(ngram_range=(2,2))
freq_tweets = vectorizer.fit_transform(tweets)
modelo = MultinomialNB()
modelo.fit(freq_tweets,classes)

resultados = cross_val_predict(modelo, freq_tweets, classes, cv=10)
metrics.accuracy_score(classes,resultados)
sentimento=['Positivo','Negativo','Neutro']
metricas = metrics.classification_report(classes,resultados) #removi sentimento
print(metricas)