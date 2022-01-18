import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import nltk
import base_texto
import base_teste


texto = pd.read_csv('./Tool/Tweets_Mg.csv')
exemplo_base = pd.DataFrame(texto)
print(f'''
      
      Base do conhecimento
      {exemplo_base}
      
      
      ''')
#exemplo_base = pd.DataFrame(base_texto.base)
exemplo_base.columns = ['Frase', 'Sentimento']
exemplo_base_teste = pd.DataFrame(base_texto.base)
exemplo_base_teste.columns = ['Frase', 'Sentimento']
# print("Tamanho da base de Treinamento {}".format(exemplo_base.shape[0]))
# print(exemplo_base.Sentimento.value_counts())
print((exemplo_base.Sentimento.value_counts() / exemplo_base.shape[0])*100)

lista_stop = nltk.corpus.stopwords.words('portuguese')
np.transpose(lista_stop)
#lista_stop.append('palavra')

def removeStopWords(texto):
    frases = []
    for (palavras, sentimento) in texto:
        semStop = [p for p  in palavras.split() if p not in lista_stop]
        frases.append((semStop, sentimento))
    return frasesgit 

def aplica_Stemmer(texto):
    stemmer = nltk.stem.RSLPStemmer()
    frases_sem_Stemming = []
    for (palavras, sentimento) in texto:
        com_Stemming = [str(stemmer.stem(p)) for p in palavras.split() if p in lista_stop]
        frases_sem_Stemming.append((com_Stemming, sentimento))
    return frases_sem_Stemming

frases_com_Stem_treinamento = aplica_Stemmer(texto)
print(pd.DataFrame(frases_com_Stem_treinamento, columns=['Frase', 'Sentimento']).sample(10))
frases_com_Stem_teste = aplica_Stemmer(base_texto.base)
print(pd.DataFrame(frases_com_Stem_treinamento, columns=['Frase', 'Sentimento']).sample(10))

def busca_Palavras(frases):
    todas_Palavras = []
    for (palavras, sentimento) in frases:
        todas_Palavras.extend(palavras)
    return todas_Palavras

palavras_treinamento = busca_Palavras(frases_com_Stem_treinamento)
palavras_teste = busca_Palavras(frases_com_Stem_teste)
print("Quantidade de palavras na basae de Treinamento {}".format(pd.DataFrame(palavras_treinamento).count()))
print("Quantidade de palavras na basae de Teste {}".format(pd.DataFrame(palavras_teste).count()))

def busca_frequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras

frequencia_treinamento = busca_frequencia(palavras_treinamento)
frequencia_teste = busca_frequencia(palavras_teste)
print(frequencia_treinamento.most_common(10))

def busca_palavras_unicas(frequencia):
    freq = frequencia.keys()
    return freq

palavras_unicas_treinamento = busca_palavras_unicas(frequencia_treinamento)
palavras_unicas_teste = busca_palavras_unicas(frequencia_teste)

def extrator_palavras(documento):
    doc = set(documento)
    características = {}
    for palavras in palavras_unicas_treinamento:
        características['%s' % palavras] = (palavras in doc)
    return características

def extrator_palavras_teste(documento):
    doc = set(documento)
    características = {}
    for palavras in palavras_unicas_teste:
        características['%s' % palavras] = (palavras in doc)
    return características

base_completa_treinamento = nltk.classify.apply_features(extrator_palavras, frases_com_Stem_treinamento)
base_completa_teste = nltk.classify.apply_features(extrator_palavras, frases_com_Stem_teste)

classificador = nltk.NaiveBayesClassifier.train(base_completa_treinamento)
print(classificador.labels())
print(classificador.show_most_informative_features(10))
print(nltk.classify.accuracy(classificador, base_completa_teste))

################# matriz de confusão #############################

erros = []
for (frase, classe) in base_completa_teste:
    resultado = classificador.classify(frase)
    if resultado != classe:
        erros.append((classe, resultado))
        
from nltk.metrics import ConfusionMatrix

esperado = []
previsto = []
for (frase, classe) in base_completa_teste:
    resultado = classificador.classify(frase)
    previsto.append(resultado)
    esperado.append(classe)
    
matriz = ConfusionMatrix(esperado, previsto)
print(matriz)

##################################################################