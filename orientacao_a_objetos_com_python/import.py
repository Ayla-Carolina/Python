'''forma 1 de importar um módulo de outro arquivo e utilizar suas funções
import funcoes_do_log

funcoes_do_log.imprimir_no_log(f'Bem vinda, {funcoes_do_log.nome_de_usuario}!')
'''

'''
#forma 2 - não é boa prática
#pode gerar conflitos por trazer tudo do outro arquivo
from funcoes_do_log import *

imprimir_no_log(f'Bem vinda, {nome_de_usuario}!')
'''

#import específico, boa prática; importa só o necessário
from funcoes_do_log import nome_de_usuario, imprimir_no_log

imprimir_no_log(f'Bem vinda, {nome_de_usuario}!')

#módulo do python 
from datetime import datetime
agora = datetime.now()
print(agora)