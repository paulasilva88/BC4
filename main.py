# Esse código tem basicamante dois requisitos funcionais:
#       - Insere no Bucket S3 os dados que estão na pasta C:\Users\paula\Desktop\Scripts Python\BC4\Base.
#       - Busca as músicas que têm mais correspondência com o trecho inserido pelo usuário


# Importação de bibliotecas

# import main_busca, main_ranking
# Menu do usuário

def sair():
    return("Programa finalizado com sucesso")

def menu ():
    entrada = int(input("----- MENU INICIAL ----- \n\
1 - Adicionar uma nova música e carregar tabela de rankings \n\
2 - Buscar or um trecho de música \n\
0 - Sair\n\
Digite o que que deseja fazer: "))
    if entrada == 1:
        # main.ranking.upload()
        # main.ranking.processamentomusica()
        menu()
    if entrada == 2:
        # main_busca.entrada()
        menu()
    else:
        print(sair())

menu()

