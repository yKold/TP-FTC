import sys

def ler_maquina_APD_terminal():
    q = input("Q: ")
    g = input("G: ")
    i = input("I: ")
    f = input("F: ")
    linhas = [q, g, i, f]
    linhas += [linha.rstrip('\n') for linha in sys.stdin]
    descricao = []
    k = 0

    while linhas[k] != "---":
        descricao.append(linhas[k])
        k += 1
    casos_teste = linhas[k+1:];
    return descricao, casos_teste
#usa ctrl+z para parar a leitura 🥶🤟

def ler_maquina_APD_arquivo():
    linhas = [linha.rstrip('\n') for linha in sys.stdin]

    descricao = []
    k = 0

    while linhas[k] != "---":
        descricao.append(linhas[k])
        k += 1

    casos_teste = linhas[k+1:]
    return descricao, casos_teste

def cabecalho_apd(descricao):
    return {
        "estados": descricao[0].split(),
        "pilha": list(descricao[1]),
        "inicial": descricao[2],
        "finais": descricao[3].split(),
        "linhas_transicao": descricao[4:]
    }

#funçao que pega e transforma em um dicionario onde tem (estado att, simbolo, topo pilha): (proximo estado, empilhar)
def configuracao_apd(descricao):
    maquina = cabecalho_apd(descricao)
    transicoes = {}
    for linha in maquina["linhas_transicao"]:
        origem, resto = linha.split(" -> ")
        destino, operacoes = resto.split(" | ")
        for op in operacoes.split():
            entrada, pilha = op.split(",")
            desempilha, empilha = pilha.split("/")
            chave = (origem, entrada, desempilha)
            transicoes[chave] = (destino, empilha)
        maquina["transicoes"] = transicoes
    return maquina

#consome as entradas verificando se existem transiçoes e se n tiver da break e n reconhece, desempilha com pop e empilha com reversec
def executar_apd(maquina, palavra):
    estado = maquina["inicial"]
    pilha = []
    i = 0
    while True:
        simbolo_entrada = palavra[i] if i < len(palavra) else "\\"
        topo = pilha[-1] if pilha else "\\"
        transicao = None
        consumiu = False
        chave = (estado, simbolo_entrada, topo)
        if (simbolo_entrada != "\\" and chave in maquina["transicoes"]):
            transicao = maquina["transicoes"][chave]
            consumiu = True
        else:
            chave = (estado, "\\", topo)
            if chave in maquina["transicoes"]:
                transicao = maquina["transicoes"][chave]
        if transicao is None:
            break
        if consumiu:
            i += 1
        prox_estado, empilha = transicao
        if topo != "\\":
            pilha.pop()
        if empilha != "\\":
            for simbolo in reversed(empilha):
                pilha.append(simbolo)
        estado = prox_estado
    if(i == len(palavra) and len(pilha) == 0):
        return "OK"
    else:
        return "X"