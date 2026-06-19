import leituraDeMaquina

def configuracao_afd(descricao):
    maquina = leituraDeMaquina.parse_cabecalho(descricao)

    transicoes = {}

    for linha in maquina["linhas_transicao"]:
        origem, resto = linha.split(" -> ")
        destino, simbolos = resto.split(" | ")

        for simbolo in simbolos.split():
            transicoes[(origem, simbolo)] = destino

    del maquina["estados"]
    del maquina["linhas_transicao"]

    maquina["transicoes"] = transicoes

    return maquina

def identifica_palavra_afd(maquina, palavra):

    #Tratamento de palavra vazia
    if len(palavra) == 0:
        if maquina["inicial"] in maquina["finais"]:
            return "OK"
        else:
            raise "X"
    
    #Coloca a máquina no estado inicial
    novoestado = maquina["inicial"]

    #Percorre a máquina consumindo a palavra inteira
    for i in range(len(palavra)):
        k = (novoestado, palavra[i])
        novoestado = maquina["transicoes"][k]

    #Determina se a palavra é aceita ou não pensando que
    #Se o estado em que a máquina parou depois de consumir a palavra é final, a palavra é aceita
    if novoestado in maquina["finais"]:
        return "OK"
    return "X"

def faz_testes(maquina, testes):
    resultados = []
    
    for palavra in testes:
        resultados.append(identifica_palavra_afd(maquina, palavra))
    
    return resultados