from MT import parse_mt, verifica_palavra as VPMT
from ALL import verifica_palavra_all as VPALL

import leituraDeMaquina as lm

print("Máquina de Turing")
descricao, casos_testes = lm.ler_maquina("mt")
MT = parse_mt(descricao)
for caso in casos_testes:
    VPMT(MT, caso)
print("")

print("Autômato Linearmente Limitado")
descricao, casos_testes = lm.ler_maquina("all")
ALL = parse_mt(descricao)
for caso in casos_testes:
    VPALL(ALL, caso)

    

# tipo = input("Digite o tipo da máquina")
# if tipo == "AFD":
#     maquina = lm.parse_afd(descricao)

# elif tipo == "AFN":
#     maquina = lm.parse_afn(descricao)

# elif tipo == "APD":
#     maquina = lm.parse_apd(descricao)

# elif tipo == "MT":
#     maquina = lm.parse_mt(descricao)