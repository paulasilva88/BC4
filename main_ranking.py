# Carregamento dos dados e criação da tabela de ranking a partir dos dados

# -> PARTE 1 => Carregamentos dos dados

# Importação de bibliotecas
import os # listagem dos arquivos das pastas
# import boto3
import pandas as pd

def upload(table): # Função criada para o Business Case 2, necessário adaptar para ler arquivos da pasta e não um arquivo por vez
    """
    It uploads the tables to AWS S3
    :param table: part of the table that identify it.
    :return: the table on AWS S3
    """
    # var
    s3 = boto3.client('s3')
    file = 'table_t' + table + '.parquet'

    #upload
    s3.upload_file(file, 'bc-dl-rd', file)
    return files + 1

# Função de criação dos campos da tabela
def header():
    header = ['Id', 'Nome']
    for i in range(10):
        header.append(f'ranking{i+1}')
    return header

# Função de leitura dos arquivos da pasta
def arquivos():
    arq = os.listdir(r"C:/Users/paula/Desktop/Scripts Python/BC4/Base/")
    '''for i in arq: 
        print (i)'''
    return arq

musicas = list(arquivos())

def processamentomusica(arq): # Funçãoi
    pass
    return("teste")



# Estrutura de leitura da letra da música
musica = f'lyrics\{musicas[0]}'
#print(musica)
arq = open(musica, 'rt')
letra = arq.read()
#print(letra)
arq.close()


def agrupar(letra):
    """
    FUnção para criação da tabela de ranking de palavras 
    :param letra: arquivo com uma string contendo a letra da música
    :return: uma lista com as palavras rankeadas por frequência, da mais frequente para a menos frequente
    """
    print(letra)

    letra = letra.replace(',', ' ').lower()
    tupla_letra = letra.split()

    # dicionario com palavras agrupadas
    dicio = {}
    for i in tupla_letra:
        try:
            dicio[i] +=1
        except:
            dicio[i] = 1

    # listagem e rankeamento das palavras
    lista_dicio = []
    lista_dicio = []
    lvolatil = [0,0]
    for i in dicio: 
        lvolatil[0] = dicio[i]
        lvolatil[1] =  i
        lista_dicio.append(lvolatil[:])
    lista_dicio.sort(reverse=True)
    #print(lista_dicio)
    return lista_dicio


# criação de linha da tabela de ranking de palavras, com id, nome da música e 20 palavras mais frequentes
group = agrupar(letra)
rank = [1, '3.txt']
for i in group:
    rank.append(i[1])
    if len(rank) ==20:
        break
# print(len(rank), rank)


# Criação do ranking de palavras no arquivo csv 
header = header()
with open('spamspam.csv', 'w') as f:
    header = str(header).replace("[", "")
    print((header).replace("]", ""), file = f)
    for i in range(1): # quando a tabela é 
        rank = str(rank).replace("[", "")
        print (rank.replace("]",""), file = f)