
import os
import pandas as pd
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import nltk
from sklearn.metrics import silhouette_samples, silhouette_score, v_measure_score
from sklearn.datasets import load_files
import re
from unidecode import unidecode
from mpl_toolkits import mplot3d
import seaborn as sns


pasta_mãe = os.listdir('.')
print( pasta_mãe )
YT_Theme = input('Qual tema voce tem interesse em analizar? \nR:  ')
archives = os.listdir(f'{YT_Theme}/descricoes_{YT_Theme}/')

#print (archives)

#sleep(4)

def TextAnalyzer():
    for archive in archives:
        df=pd.read_csv(f'C:/Users/efrai/Desktop/YT/{YT_Theme}/descricoes_{YT_Theme}/{archive}')
        df_ = df['Title'].apply(lambda x: x.lower())
        df_ = df_.apply(lambda x: re.sub('[0-9]|,|\.|/|$|\(|\)|-|\+|:|•', ' ', x))
        df_ = df_.apply(lambda x: unidecode(x))
        df_b = df['Description'].apply(lambda x: x.lower())
        df_b = df_b.apply(lambda x: re.sub('[0-9]|,|\.|/|$|\(|\)|-|\+|:|•', ' ', x))
        df_b = df_b.apply(lambda x: unidecode(x))

        stemmer = nltk.stem.RSLPStemmer()

        df_ = df_.apply(lambda x: stemmer.stem(x))
        df_b = df_b.apply(lambda x: stemmer.stem(x))

        print(df)
        df.info()
        print(df_)
        print(df_b)
        df_.info()

        knn = sns.pairplot(df)
        print(knn)
        knn.show()
        kmeans = sns.pairplot(df)
        print(kmeans)
        sb.plt.show(kmeans)

TextAnalyzer()