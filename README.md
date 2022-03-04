# Processamento-De-Linguagem-Natural-Text_Processing
Esse projeto tem as seguintes funções a serem realizadas nos arquivos de texto: 

1. Tokenização.

• Saída esperada: Uma lista que contém strings representando os tokens extraídos.

2. Normalização e Limpeza.

(a) Lower casing (conversão de todos os caracteres para minúsculo);
(b) Remoção de pontuações e outros caracteres especiais;
(c) Remoção de stopwords;
• São consideradas as stopwords da língua inglesa;
(d) Remoção das palavras mais frequentes;
• Implementação da remoção das n palavras mais frequentes ou a remoção das palavras que ocorreram mais que n vezes, sendo n um argumento para a função.
(e) Remoção das palavras mais raras;
• Implementação da remoção das n palavras menos frequentes ou a remoção das palavras que ocorreram menos que n vezes, sendo n um argumento para a função.
• Saída esperada: Uma string contendo o texto limpo ou uma lista de strings contendo o texto tokenizado após o processo de limpeza.

3. Lematização.

• Aplicação de um método de lematização em uma lista de tokens;

• Considerando uma lista tokens da língua inglesa;

• Saída esperada: Uma lista dos tokens após o processo de lematização.

4. Stemming.

• Aplicação de um método de stemming em uma lista de tokens;

• Considerando uma lista tokens da língua inglesa;

• Saída esperada: Uma lista dos tokens após o processo de stemming.

5. Representação vetorial de textos.

• Considerando um Corpus de textos, no projeto há a conversão de cada texto para um vetor de números.

A função extrai o vocabulário do Corpus e gerar vetores (com o tamanho do vocabulário) que representam cada
texto considerando as seguintes abordagens:

(a) Binária, onde cada posição dos vetores deve indicar se uma palavra ocorreu ou não em um texto;

(b) Contagem, onde cada posição dos vetores deve indicar o número de vezes que uma palavra ocorreu no texto;

(c) Frequência de termos, onde cada posição dos vetores deve indicar a frequência de cada palavra no texto;

• Frequência dos termos = (Número de vezes que a palavra ocorreu no texto/Número de palavras no texto).

(d) Term Frequency-Inverse Document Frequency, onde cada posição dos vetores indica o valor de TF-IDF da
palavra no texto.

• TF-IDF = (Frequência dos termos) * log(número de documentos/número de textos que a palavra ocorreu).

• Saída esperada: Um vetor de vetores para cada abordagem.


Sendo assim,

O trabalho conta com 2 pastas, uma pasta é a de Entrada e a outra é a de Saída. Para cada
função usamos os mesmos arquivos de entrada e geramos saídas diferentes, cada função
tem saídas diferentes para cada um dos livros utilizados como Entrada.

Dentro da Pasta Entrada temos os 7 livros utilizados como base de dados para as funções,
além de mais 3 arquivos que foram utilizados como auxiliares(Stemming, Lemanization e
Stopwords). o Stemming é um arquivo contendo diversas palavras utilizadas na função
Stemming para buscarmos nos livros, já no arquivo Lemanization temos uma lista de
palavras que usamos para fazer a função do Lemanization e por último temos o arquivo
Stopwords que contém uma lista de Stopwords utilizadas para fazer a função de retirada de
Stopwords, é válido lembrar que assim como os livros utilizados são em português tanto o
Stemming, Lemanization e Stopwords utilizadas também foram da língua portuguesa.

No arquivo de Saída temos todas as funções da Atividade, a cada função nova executada
foi gerado 7 saídas diferentes dos livros utilizados na Entrada, para melhor verificação dos
processos, com o decorrer das funções até o final vemos que as últimas funções contém
todas as funcionalidades completas, como tokenização, normalização de texto, remoção de
stopWords, ou seja, os arquivos de saídas vão aglutinando funções anteriores, sendo assim
o último arquivo de saída da última Tarefa já possuí o pré-processamento completo.

O código da main está todo comentado para facilitar o entendimento, as funções estão
todas no começo do arquivo, na main está alguns comentários sobre possíveis chamadas
da função, para melhor entendimento deve-se ler os comentários da main.

Esse projeto teve como contribuidor Júlio Cabral
