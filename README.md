

# Business Case 4 - Rankeamento de músicas

*Estagiária: Paula Silva*

    O projeto não está pronto, pois tive muita dificuldade em aplicar a estrutura nas tecnologias solicitadas: hadoop e Spark. Implementei todas as etapas em Python, de modo que o processo fique mais claro, e seja possível migrar e traduzir os comandos para a tecnologia mais adequada posteriormente.

A dificuldade em Hadoop surgiu pois não pude praticar a teoria aprendida do curso, já que não existe mais a possibilidade de usar a máquina virtual Cloudera, e o Spark até aprendi bem a executar os comandos básicos, mas não consegui pensar em como aplicar os comandos aprendidos na criação do ranking a partir dos arquivos com as letras das músicas.

Pelas características dos dados, é mais interessante criar um Data Lake, em que os dados de entrada são as letras das músicas brutas, e essas são carregadas antes de passar por qualquer tipo de processamento.
Os dois requisitos funcionais principais da aplicação, que estão atrelados diretamente ao usuário são:
1.  Inserção de novos arquivos no bucket; 
2.  Busca baseada em trechos de músicas;

## Carregamento dos dados 
---

Uma forma simples de fazer o carregamento das músicas em um bucket é através do código usado no Business Case 2, que carregava os dados de uma pasta em um bucket no AWS S3. Observações: 
- Porém, no caso das tabelas do BC 2, eu usei um meio mais simples, de leitura de arquivos, e isso só foi possível porque os dados seguiam um padrão, o que não ocorre nesse caso. Então eu implementaria apenas uma correção na entrada de dados para que o código lesse e carregasse todos os arquivos de uma pasta, ao invés de um arquivo por vez.
- O código pode ser inserido em uma função lambda da AWS ou pode ser feito no AWS Glue, juntamente com o tratamento dos dados. Ele está disponível no arquivo main.ranking, mas não foi adpatado ainda.


A busca se divide em duas tarefas principais:
  - Criar uma tabela com o ranking de palavras de cada música;
  - Percorrer a tabela criada, selecionando as 10 músicas que possuem maior grau de correspondência com o trecho buscado


## Tabela de Rankeamento de palavras
---
>Primeiramente é criado o cabeçalho com o id, o nome da tabela e mais 20 colunas, com nomes r1, r2, ..., r20, que conterão as palavras mais frequentes.

E após o carregamento das letras das músicas no Data Lake, é preciso criar o rankeamento das palavras mais frequentes de cada música. 
- Primeiro, ao ser processada, cada música deve receber o tratamento de limpeza, que será feito pelo código Python disponível no Anexo II. Para além disso, é interessante inserir palavras que podem ser removidas como conectivos(preposições e conjunções)
- Depois da limpeza, a música será processada de modo a construir uma tabela, ou várias tabelas, com cada linha correpondendo a uma música.  
- A tabela é feita em um arquivo csv, com os dados de cada linha separados por vírgula. Basicamente, a ideia é realizar o processamento, criação do ranking e inserção da linha no arquivo por música através de uma função que será iterada ao final do código.
- Toda a parte do carregamento dos dados e processamento estão no arquivo main_ranking.
- Exemplo de resultado esperado para a tabela de ranking de palavras:
> 'Id', 'Nome', 'ranking1', 'ranking2', 'ranking3', 'ranking4', 'ranking5', 'ranking6', 'ranking7', 'ranking8', 'ranking9', 'ranking10'
> 
> 1, '3.txt', 'i', 'to', 'the', 'you', "don't", "i'm", 'this', 'never', 'a', 'time', 'that', "it's", 'am', 'who', 'was', 'understand', 'then', 'same'

> 1, '3.txt', 'i', 'to', 'the', 'you', "don't", "i'm", 'this', 'never', 'a', 'time', 'that', "it's", 'am', 'who', 'was', 'understand', 'then', 'same' 

## A Busca 
---
> Não consegui implementar a busca por questões de tempo e dificuldade em utilizar o Databricks Community.

A entrada da busca é o trecho da música desejada, em arquivo .txt e o objetivo é mostrar um novo ranking contendo as 10 músicas que mais correspondem ao que está presente no arquivo de texto. 

- A busca consiste em fazer o mesmo processo de limpeza que as letras das músicas passaram, de modo a se obter as palavras-chave que serão utilizadas para a busca.

- Será criada uma nova tabela com as colunas: id, nome_musica pontuacao, e uma variável temporária contador.
- Cada palavra-chave do trecho de busca deve ser comparada com cada uma das palavras contidas em cada linha da tabela de ranking de palavras, exceto as colunas de "ID" e "nome_musica", que são colunas de referência. 
- Caso a palavra corresponda à uma coluna específica, é somado à variável contador o valor da linha correspondente daquela palavra à coluna "pontuação". Após comparar todas as palavras da busca à linha da música, será adicionado à tabela de ranking de músicas os valores do id e nome, além do valor do contador, na coluna de pontuação. 

> Cada coluna do ranking de palavras tem um valor específico.Assim, mesmo que uma palavra tenha mais palavras menos frequentes no trecho de busca, ela não será rankeada à frequente de uma música que tem menos palavras correspondentes, mas com maior frequencia. O valor de cada coluna é dado pelo seu índice, sendo a 1º palavra mais frequente em uma música, na coluna r1, tem valor 2, a 2º valor 4 e assim por diante, cada coluna valendo o valor de 2 elevado ao índice menos 1. Desse modo, a coluna r1 tem valor igual a 1, a r2, 4 e a r20 524288. 
>
> Fórmula:  v =  2^(i-1)


 Esquema de valores por coluna:

| r1 | r2| r3 | ... |r20|

| 1  | 2 | 4  | ... | 524288|


- Depois que todas as linhas tenham recebido sua pontuação, basta ordenar a tabela pela coluna de pontuação, na ordem crescente, e selecionar os primeiros 10 valores.

O código que já foi implementado está disponível em main_busca.py
