
from leituraDeMaquina import parse_cabecalho_turing

# parse_all() == parse_mt()

def verifica_palavra_all(maquina, palavra):

    estado_atual = maquina["inicial"]
    fita = list("<" + palavra + ">")
    cabeca = 1
    aceita = False
    
    while True:
        if cabeca < 0 or cabeca >= len(fita):
            aceita = False
            break

        simbolo_lido = fita[cabeca]
        chave = (estado_atual, simbolo_lido)

        # print(simbolo_lido)
        if chave not in maquina["transicoes"]:
            break

        prox_estado, simbolo_escrito, direcao = (
            maquina["transicoes"][chave][0]
        )

        fita[cabeca] = simbolo_escrito
        estado_atual = prox_estado

        if direcao == "D":
            cabeca += 1
        elif direcao == "E":
            cabeca -= 1
        else:
            break

        if estado_atual in maquina["finais"]:
            aceita = True
            break

    resultado = ''.join(fita)
    if aceita:
        print("OK", resultado)
    else:
        print("X", resultado)