# -*- coding: utf-8 -*-
import sys
import re

regex = r"[-'a-zA-ZÀ-ÖØ-öø-ÿ0-9]+"

def Tokenizacao(entrada, saida):
    #Lendo Arquivo
    arquivoAberto = open(entrada, encoding="utf8")
    texto = arquivoAberto.read()
    ##Criando um arquivo com a saida
    arquivo = open(saida, "a")
    ##Mandando cada Token para uma linha diferente
    palavras = re.findall(regex, texto)
    for p in palavras:
        arquivo.write(p + "\n")
    arquivoAberto.close()
    arquivo.close()
 
def LowerCasing(entrada, saida): 
    arquivoAberto = open(entrada)##, encoding="utf8")
    texto = arquivoAberto.read()
    ##Criando um arquivo com a saida
    arquivo = open(saida, "a")

    ##Aplicando o Lowercasing em cada linha do arquivo de entrada e jogando para um arquivo de saída
    for linha in texto: 
        aux = linha.lower()
        arquivo.write(aux)
    arquivoAberto.close()
    arquivo.close()

    
def removePontuacoesCaracteresEspeciais(entrada, saida): 
    arquivoAberto = open(entrada)
    texto = arquivoAberto.readlines()
    ##Criando um arquivo com a saida
    arquivo = open(saida, "a")
    ##Aplicando a remoção de pontuações e caracteres especiais em cada linha do arquivo de entrada e jogando para um arquivo de saída
    for linha in texto: 
        aux = re.sub('\W+','', linha)
        ##aux = (aux + "\n")
        arquivo.write(aux+"\n")

    arquivoAberto.close()
    arquivo.close()

def removeStopwords(entrada, stopwords, saida): 
    
    arquivoStopwords = open(stopwords)
    stopWordsarq = arquivoStopwords.readlines()
    stopWords = list()
    stopWords = stopWordsarq
    ##Criando uma lista do arquivo Stopwords

    arquivoAberto = open(entrada)
    textoarq = arquivoAberto.readlines()
    texto = list()
    texto = textoarq
    ##Criando uma lista do arquivo de entrada

    
    arquivo = open(saida, "a")
    
    for txt in texto: 
        ##em cada elemento da lista do texto de entrada eu vou comparar com todas as stopwords e se for diferente eu mando para um arquivo de saída, tendo assim no fim um arquivo do texto sem as stopWords
        if(txt not in stopWords): 
            arquivo.write(txt)


def removeMaisFrequentes(entrada, saida, frequencia): 
    arquivoAberto = open(entrada)
    texto = arquivoAberto.read()
    
    palavras = re.findall(regex, texto)
    calculaFrequencias = dict([])
    ##Criando um dicionário com as frequências das Palavras

    for pl in palavras: 
        if pl not in calculaFrequencias: 
            calculaFrequencias[pl] = 0
        calculaFrequencias[pl]+=1 
    ##Calculando as frequências de cada palavras

    ##Gerando um dicionário só com as palavras que tem a frequência menor que o usuário deu como entrada
    dicionarioFinal = { key: calculaFrequencias[key] for key in calculaFrequencias if calculaFrequencias[key] < frequencia }
    ##print(dicionarioFinal)

    arquivo = open(saida, "a")
   
    #Enviando para um arquivo de saída
    for i in dicionarioFinal: 
        arquivo.write(i+"\n")

def removeMaisRaras(entrada, saida, frequencia): 
    arquivoAberto = open(entrada)
    texto = arquivoAberto.read()
    
    palavras = re.findall(regex, texto)
    calculaFrequencias = dict([])
    ##Criando um dicionário com as frequências das Palavras

    for pl in palavras: 
        if pl not in calculaFrequencias: 
            calculaFrequencias[pl] = 0
        calculaFrequencias[pl]+=1 
    ##Calculando as frequências de cada palavras

    ##Gerando um dicionário com as palavras que tem a frequência maior que o usuário deu como entrada
    ##ou seja as palavras mais raras não vão aparecer
    dicionarioFinal = { key: calculaFrequencias[key] for key in calculaFrequencias if calculaFrequencias[key] > frequencia }
    ##print(dicionarioFinal)

    arquivo = open(saida, "a")
   
    #Enviando para um arquivo de saída
    for i in dicionarioFinal: 
        arquivo.write(i+"\n")

def Lemanization(entrada, saida, lista): 
    arquivoLemanization = open(lista)
    lemanizationArq = arquivoLemanization.readlines()
    palavrasLemanization = list()
    palavrasLemanization = lemanizationArq


    arquivoAberto = open(entrada)
    textoarq = arquivoAberto.readlines()
    texto = list()
    texto = textoarq
    ##Criando uma lista do arquivo de entrada

    arquivo = open(saida, "a")

    ##fazendo o Lemanization e mandando para um arquivo de saida
    for txt in texto: 
        aux = 1
        for lem in palavrasLemanization: 
            if(txt.find(lem)!=-1 and aux==1): 
                arquivo.write(lem)
                aux = 0
        if (aux==1): 
            arquivo.write(txt)


def Stemming(entrada, saida, lista): 
    arquivoStemming = open(lista)
    stemmingArq = arquivoStemming.readlines()
    palavrasStemming = list()
    palavrasStemming = stemmingArq


    arquivoAberto = open(entrada)
    textoarq = arquivoAberto.readlines()
    texto = list()
    texto = textoarq
    ##Criando uma lista do arquivo de entrada

    arquivo = open(saida, "a")

    ##fazendo o Stemming e mandando para um arquivo de saida
    for txt in texto: 
        aux = 1
        for stem in palavrasStemming: 
            if(txt.find(stem)!=-1 and aux==1): 
                arquivo.write(stem)
                aux = 0
        if (aux==1): 
            arquivo.write(txt)



if __name__ == '__main__':
    
    ##Insira o nome do arquivo de entrada para fazer a Tokenização
    nomeArquivo = "Saídas\Tarefa 2 - Normalização e Limpeza\C - Remoção de Stopwords\Ernesto de Tal - Machado de Assis.txt"
    stopWords = "Entradas\Stopwords.txt"
    listaDePalavrasLemanization = "Entradas\Lemanization.txt"
    listaDePalavrasStemming = "Entradas\Stemming.txt"
    ##INsira o nome do arquivo de saída que será criado
    nomeArquivoSaida = "Saídas\Tarefa 4 - Stemming\Ernesto de Tal - Machado de Assis.txt"

    ##Utilizando a função de Tokenização
    ##Tokenizacao(nomeArquivo, nomeArquivoSaida)
    
    ##Utilizando a função LowerCasing
    ##LowerCasing(nomeArquivo, nomeArquivoSaida)

    ##Utilizando a função de Remoção de Pontuações e outros caracteres especiais
    ##removePontuacoesCaracteresEspeciais(nomeArquivo, nomeArquivoSaida)    

    #Utilizando a função de Remover Stopwords
    ##removeStopwords(nomeArquivo, stopWords, nomeArquivoSaida)

    ##Utilizando a função que Remove as palavras mais Frequentes
    ##removeMaisFrequentes(nomeArquivo, nomeArquivoSaida, 5)

    ##Utilizando a função que remove as palavras mais Raras
    ##removeMaisRaras(nomeArquivo,nomeArquivoSaida, 10)

    ##Utilizando a função Lemmanization
    ##Lemanization(nomeArquivo, nomeArquivoSaida, listaDePalavrasLemanization)

    ##Utilizando a função Stemming
    Stemming(nomeArquivo, nomeArquivoSaida, listaDePalavrasStemming)



    

   


