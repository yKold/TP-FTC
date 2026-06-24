from MT import parse_mt, verifica_palavra
import leituraDeMaquina as lm

descricao, casos_testes = lm.ler_maquina()
MT = parse_mt(descricao)
verifica_palavra(MT, casos_testes[1])

# tipo = input("Digite o tipo da máquina")
# if tipo == "AFD":
#     maquina = lm.parse_afd(descricao)

# elif tipo == "AFN":
#     maquina = lm.parse_afn(descricao)

# elif tipo == "APD":
#     maquina = lm.parse_apd(descricao)

# elif tipo == "MT":
#     maquina = lm.parse_mt(descricao)