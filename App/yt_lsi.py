import re
import nltk
import nltk.corpus
import pandas as pd
import os
import os.path
from collections import Counter
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from unidecode import unidecode
from nltk import ngrams, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from time import sleep
from textblob import TextBlob
import urlmarker



#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('rslp')
pasta_mãe = os.listdir('.')
#print( pasta_mãe )
YT_Theme = input('Qual tema voce tem interesse em analizar? \nR:  ')
archives = os.listdir(f'{YT_Theme}/descricoes_{YT_Theme}/')
#print (archives)

#sleep(4)

def TextAnalyzer():
    for archive in archives:
        start = timer()

        #print(archive)

        df=pd.read_csv(f'C:/Users/efrai/Desktop/YT/{YT_Theme}/descricoes_{YT_Theme}/{archive}')

        df[['polarity', 'subjectivity']] = df['Title'].apply(lambda Text: pd.Series(TextBlob(Text).sentiment))
        #print(df)
        #pop = sb.pairplot(df)

        links = []
        hashtags = []

        for item in df:
            item = item.split()
            for i in item:
                if i.isdigit() == True:
                    print(i)
                    sleep(2)
                if i == 'www':
                    links.append(item)
                    print(item)
                    sleep(2)
                if item == '#':
                    hashtags.append(item)
                    print(item)
                    sleep(2)

            df_title = df['Title']
            df_desc = df['Description']
            df_capt = df['Captions']
            df_tags = df['Tags']

            #for x in df_title:
            #    if x.isdigit():
            #        pass
            #    else:
            #        x.lower()
            #        re.sub('[0-9]|,|\.|/|$|\(|\)|-|\+|:|•', '', x)
            #        unidecode(x)
            #   print(df_title)

            try:
                df_ = df_title.apply(lambda x : x.lower())
                url = df_.apply(lambda x : re.findall(urlmarker.URL_REGEX,f'{x}'))
                print(url)
                print(df_)
                df_ = df_.apply(lambda x: re.sub('[0-9]|,|\.|/|$|\(|\)|-|\+|:|•?', '', x))
                df_ = df_.apply(lambda x: unidecode(x))
                print(df_desc)
                df_b = df_desc.apply(lambda x: str(x))
                url = df_b.apply(lambda x : re.findall(urlmarker.URL_REGEX,f'{x}'))
                print(url)
                df_b = df_b.apply(lambda x : x.lower())
                
                df_b = df_b.apply(lambda x: re.sub('[0-9]|,|\.|/|$|\(|\)|-|\+|:|•?', '', x))
                df_b = df_b.apply(lambda x: unidecode(x))
            except:
                print('error')
            finally:
                pass

        #########################################################
        #stemmer = nltk.stem.RSLPStemmer()
        #df_ = df_.apply(lambda x: stemmer.stem(x))
        #df_b = df_b.apply(lambda x: stemmer.stem(x))
        #########################################################

        stopwords = nltk.corpus.stopwords.words('portuguese')
        stopwords = stopwords.extend(["nao"])
        stop_words = ["de","a","o","que","e","do","da","em","um","para","é","com","não","uma","os","no","se","na","por","mais","as","dos","mas","foi","ao","ele","das","tem","à","seu","sua","ou","ser","quando","muito","há","nos","já","está","eu","também","só","pelo","pela","até","isso","ela","entre","era","depois","sem","mesmo","aos","ter","seus","quem","nas","me","esse","eles","estão","você","tinha","foram","essa","num","nem","suas","meu","às","minha","têm","numa","pelos","elas","havia","seja","qual","será","nós","tenho","lhe","deles","essas","esses","pelas","este","fosse","dele","tu","te","vocês","vos","lhes","meus","minhas","teu","tua","teus","tuas","nosso","nossa","nossos","nossas","dela","delas","esta","estes","estas","aquele","aquela","aqueles","aquelas","isto","aquilo","estou","está","estamos","estão","estive","esteve","estivemos","estiveram","estava","estávamos","estavam","estivera","estivéramos","esteja","estejamos","estejam","estivesse","estivéssemos","estivessem","estiver","estiverem","hei","havemos","hão","houve","ha","há","houvemos","houveram","houvera","hajamos","hajam","houvéssemos","houver","houvermos","houverem","houverei","houveremos","houverão","houveria","houveríamos","houveriam","sou","somos","são","era","éramos","eram","fui","foi","fomos","foram","fora","fôramos","seja","sejamos","sejam","fosse","fôssemos","fossem","for","formos","forem","serei","será","seremos","serão","seria","seríamos","seriam","tenho","tem","temos","tém","tinha","tínhamos","tinham","tive","teve","tivemos","tiveram","tivera","tivéramos","tenha","tenhamos","tenham","tivesse","tivéssemos","tivessem","tiver","tivermos","tiverem","terei","terá","teremos","terão","teria","teríamos","teriam"]
        vec = TfidfVectorizer(stop_words=stopwords)
        pontuacao = ['(',')',';',':','[',']',',', '"', '|', '-', '[', ']', '_', ' ', '?', '!', '?!', '!?', '.', ',', '>', '<', '"', "'", ",", '\\n']
        pd.options.display.max_colwidth = 5000


        #vec.fit(df_.values)
        #features = vec.transform(df_.values)
        #vec.fit(df_b.values)
        #features_b = vec.transform(df_b.values)

        #stemmer = PorterStemmer()
        #def tokenizer(df_, df_b):
        #    return [stemmer.stem(w) for w in df_.split()] and [stemmer.stem(w) for w in df_b.split()]

        #tfidf = TfidfVectorizer(tokenizer='lemmatize', stop_words=stopwords)
        #X = pd.DataFrame(tfidf.fit_transform(df_).toarray(),
        #                index=df_, columns=tfidf.get_feature_names())
        #c = cluster.AffinityPropagation()
        #pred = c.fit_predict(X)
        #print(pred)

        #X, y = make_blobs(n_samples=10, centers=3, n_features=2, random_state=0)

        #for cluster in range(2,30):
            #cls = MiniBatchKMeans(n_clusters=cluster, random_state=random_state)
            #cls = MiniBatchKMeans(n_clusters=cluster)
            #cls.fit(features.reshape(-1,1))
            #cls.fit(features_b.reshape(-1,1))
            # predict cluster labels for new dataset
            #cls.predict(features)
            #print (features)
            # to get cluster labels for the dataset used while
            # # training the model (used for models that does not
            # # support prediction on new dataset).
            #cls.labels_
            #print(cls)
            #clusterer = KMeans(n_clusters=cluster, random_state=10)
            #cluster_labels = clusterer.fit_predict(features)

        unique_titles = []
        titles_list = []
        unique_description = []
        description_list = []

        for row in df_:
            #print(row)
            df_ = str(row)
            df_1 = df_.lower()
            df_1 = df_1.split()

            all_words = ''

            nltk_tokens = word_tokenize(str(df_1))

            #nltk_tokens = word_tokenize(df_2)
            #print(list(bigrams(nltk_tokens)))
            #print(list(trigrams(nltk_tokens)))

            n_gram = 5
            n_gram_dic = dict(Counter(ngrams(all_words.split(), n_gram)))
            #print(n_gram_dic)


            keywords1 = [i for i in df_1 if not i in stop_words and not i in pontuacao]

            for i in keywords1:
                if i not in unique_titles:
                    unique_titles.append(i)
                else:
                    pass

        for word_t in unique_titles:
            word_frequency = keywords1.count(word_t)
            #print(f'{word_t} = {word_frequency}')
                    #listas = (f'Title: {word_t} = {word_frequency}')
                    #print(listas)

            for i in zip(word_t, str(word_frequency)):
                titles_list.append({'T Words': word_t, 'Count': word_frequency})

        df_t = pd.DataFrame(titles_list)


        for row in df_b:
            #pd.options.display.max_colwidth = 5000
            df_ = str(row)
            df_2 = df_.lower()
            df_2 = df_2.split()

            nltk_tokens = word_tokenize(str(df_2))
            #print(list(bigrams(nltk_tokens)))
            #print(list(trigrams(nltk_tokens)))

            n_gram = 5
            n_gram_dic = dict(Counter(ngrams(all_words.split(), n_gram)))
            #print(n_gram_dic)


            keywords1 = [i for i in df_2 if not i in stop_words and not i in pontuacao]

            for i in keywords1:
                if i not in unique_description:
                    unique_description.append(i)
                else:
                    pass
        for word_d in unique_description:
            word_frequency = keywords1.count(word_d)
            #print(f'{word_d} = {word_frequency}')
                    #listas = (f'Title: {word_t} = {word_frequency}')
                    #print(listas)

            for i in zip(word_d, str(word_frequency)):
                description_list.append({'d Words': word_d, 'Count': word_frequency})

        df_d = pd.DataFrame(description_list)
        print(df_t)
        print(df_d)

        def links_loop():
                for i in df_1:
                    loop = next(df_1.iteritems[i+1])
                    if loop == False:
                        links_loop.exit()
                    elif loop == True:
                        exec(function)
        end = timer()
        print(end - start)


TextAnalyzer()

#Aqui fiz uma segunda maneira de analise de texto usando nltk, mas apenas para confirmação do anterior.
#class __init__:
#    def TextNatural():
#        for archive in archives:
#            stop_words = ["de","a","o","que","e","do","da","em","um","para","é","com","não","uma","os","no","se","na","por","mais","as","dos","como","mas","foi","ao","ele","das","tem","à","seu","sua","ou","ser","quando","muito","há","nos","já","está","eu","também","só","pelo","pela","até","isso","ela","entre","era","depois","sem","mesmo","aos","ter","seus","quem","nas","me","esse","eles","estão","você","tinha","foram","essa","num","nem","suas","meu","às","minha","têm","numa","pelos","elas","havia","seja","qual","será","nós","tenho","lhe","deles","essas","esses","pelas","este","fosse","dele","tu","te","vocês","vos","lhes","meus","minhas","teu","tua","teus","tuas","nosso","nossa","nossos","nossas","dela","delas","esta","estes","estas","aquele","aquela","aqueles","aquelas","isto","aquilo","estou","está","estamos","estão","estive","esteve","estivemos","estiveram","estava","estávamos","estavam","estivera","estivéramos","esteja","estejamos","estejam","estivesse","estivéssemos","estivessem","estiver","estiverem","hei","havemos","hão","houve","ha","há","houvemos","houveram","houvera","hajamos","hajam","houvéssemos","houver","houvermos","houverem","houverei","houveremos","houverão","houveria","houveríamos","houveriam","sou","somos","são","era","éramos","eram","fui","foi","fomos","foram","fora","fôramos","seja","sejamos","sejam","fosse","fôssemos","fossem","for","formos","forem","serei","será","seremos","serão","seria","seríamos","seriam","tenho","tem","temos","tém","tinha","tínhamos","tinham","tive","teve","tivemos","tiveram","tivera","tivéramos","tenha","tenhamos","tenham","tivesse","tivéssemos","tivessem","tiver","tivermos","tiverem","terei","terá","teremos","terão","teria","teríamos","teriam"]
#            pontuacao = ['(',')',';',':','[',']',',', '"', '|', '-', '[', ']', '_', ' ', '?', '!', '?!', '!?', '.', ',', '>', '<', '"', "'", ",", '\\n']
#            pd.options.display.max_colwidth = 5000
#            df=pd.read_csv(f'C:/Users/efrai/Desktop/YT/{YT_Theme}/descricoes_{YT_Theme}/{archive}')
#            #print(df)
#            df_1 = df['Title'].to_string().lower()
#            #print(df_1)
#
#            words1 = df_1.split()
#            keywords1 = [i for i in words1 if not i in stop_words and not i in pontuacao]
#            for word in words1:
#                token = word_tokenize(word)
#                fdist = FreqDist(token)
#                fdist1 = fdist.most_common(20)
#                print(fdist1)
#                pst = PorterStemmer()
#                #pst.stem(i in i)
#                #for word in arquivos:
#                #    print(word+ ":" +pst.stem(word))
#
#            df_2 = df['Description'].to_string().lower()
#            #print(df_2)
#            words2 = df_2.split()
#            keywords2 = [i for i in words2 if not i in stop_words and not i in pontuacao]
#            for word in keywords2:
#                token = word_tokenize(word)
#                fdist = FreqDist(token)
#                fdist1 = fdist.most_common(200)
#                print(fdist1)
#                pst = PorterStemmer()
#                #pst.stem(i in i)
#                #for word in arquivos:
#                #    print(word+ ":" +pst.stem(word))
#    TextNatural()




#stop_words = nltk.corpus.stopwords.words('portuguese')
#keywords = [i for i in text if not i in stop_words and not i in pontuacao]
#print(keywords)
#tamanho = len(keywords)
#print(f'Quantidade de Palavras Deste Canal: \n\n{tamanho}\n\n')
#texto_final = " ".join(s for s in keywords)