#manipulando arquivos com funções 


def multiplicacao():
    mult = 10*2
    file = 'arquivo.txt'

    #formas de abertura de arquivo 

    #open 
    #arquivo_leitura = open(file, "r") #open somente para leitura 

    #abertura para escrita 
    arquivo_escrita = open(file, "w")
    arquivo_escrita.write(f'O resultado da multiplicação é {mult}')
    arquivo_escrita.close()

    #leitura 
    arquivo_leitura = open(file, "r") #open somente para leitura 
    leitura = arquivo_leitura.read()
    print(leitura)
    arquivo_leitura.close()


    #abertura de arquivos binários 
    #arquivo_binario = open(file, "wb")

multiplicacao()