

# Entrada do valor de busca
import os

def entrada():
    trecho = open(r'busca.txt', 'rt')
    trecho = trecho.read()
    print(trecho)
    return trecho