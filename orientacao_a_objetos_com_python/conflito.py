from funcoes_do_log import *

imprimir_no_log(f'Bem vinda, {nome_de_usuario}!')
print()

def imprimir_no_log(texto):
    print(texto)

imprimir_no_log(f'Bem vinda, {nome_de_usuario}!')

#gerando conflitos, conferindo a má prática quando importa-se tudo de um módulo já existente 

