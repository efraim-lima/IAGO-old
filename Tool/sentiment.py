import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import nltk

base = [('Essa capinha de celular é muito boa', 'alegria'),
        ('Gostei muito desta capinha de celular', 'alegria'),
        ('Capinha maravilhosa', 'alegria'),
        ('Que capinha bonita', 'alegria'),
        ('Abaixo do esperado', 'raiva'),
        ('Não gostei', 'raiva'),
        ('Desbotou na primeira semana', 'raiva'),
        ('Olha só essa capinha! ', 'alegria'),
        ('Material de baixa resistência', 'raiva'),
        ('Custo benefício excelente', 'alegria'),
        ('A foto é diferente do produto', 'raiva')] 


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')
stopwords=nltk.corpus.stopwords.words('portuguese')

def fazstemmer(texto):
    stemmer = nltk.stem.RSLPStemmer()
    frasessstemming = []
    for (palavras, emocao) in texto:
        comstemming = [str(stemmer.stem(p))
                       for p in palavras.split() if p not in stopwords]
        frasessstemming.append((comstemming, emocao))
    return frasessstemming 

frasescomstemming = fazstemmer(base)
#print(frasescomstemming)

def buscapalavras(frases):
    todaspalavras = []
    for (palavras, emocao) in frases:
        todaspalavras.extend(palavras)
        frequencia = buscafrequencia(palavras)
        def buscafrequencia(palavras):
            palavras = nltk.FreqDist(palavras)
            return palavras
        frequencia = buscafrequencia(palavras)
        def busca_palavrasunicas(frequencia):
            freq = frequencia.keys()
            return freq
        frasescomstemming = fazstemmer(base)
        print(frasescomstemming)

        palavrasunicas = busca_palavrasunicas(frequencia)
        print(palavrasunicas)
        print(frequencia) 
    return todaspalavras
 


###############################################################################################