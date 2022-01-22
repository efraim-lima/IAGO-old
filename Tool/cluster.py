import nltk

frases = "Esta é a primeira frase, a frase 1. Depois temos a segunda frase, a frase 2. E agora a terceira."
palavras = nltk.word_tokenize(frases)
palavras = [palavras.lower() for palavras in palavras if palavras.isalpha()]
palavras_frequentes = nltk.FreqDist(palavras)

for key in palavras_frequentes:
    print(key + ' - ' + str(palavras_frequentes[key]))