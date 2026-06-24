import leituraDeMaquina

def configuracao_afd(descricao):
    maquina = leituraDeMaquina.cabecalho_afd(descricao)
    transicoes = {}
    afn = False

    for linha in maquina["linhas_transicao"]:
        origem, resto = linha.split(" -> ")
        destino, simbolos = resto.split(" | ")

        for simbolo in simbolos.split():
            chave = (origem, simbolo)
            if chave not in transicoes:
                transicoes[chave] = set()

            if len(transicoes[chave]) > 0 and destino not in transicoes[chave]:
                afn = True
                #prints utilizados para debug de reconhecimento de não determinismo
                #print("\nAFN DETECTADO NA TRANSIÇÃO")

            transicoes[chave].add(destino)

    maquina["transicoes"] = transicoes

    iniciais_raw = maquina["inicial"]

    if isinstance(iniciais_raw, str):
        maquina["iniciais"] = set(iniciais_raw.split())
    else:
        maquina["iniciais"] = set(iniciais_raw)

    if len(maquina["iniciais"]) > 1:
        afn = True
        #prints utilizados para debug de reconhecimento de não determinismo
        #print("\nAFN DETECTADO MULTIPLOS ESTADOS INICIAIS")

    for (estado, simbolo), destinos in transicoes.items():
        if simbolo == "\\" and len(destinos) > 0:
            afn = True
            #prints utilizados para debug de reconhecimento de não determinismo
            #print("\nAFN DETECTADO TRANSICAO COM LAMBDA")
    
    for (estado, simbolo), destinos in transicoes.items():
    if simbolo == "\\" and len(destinos) > 0:
        afn = True

# Alfabeto da linguagem
maquina["alfabeto"] = {"p", "q", "d"}

return maquina

    return maquina


def fecho_lambda(maquina, estados):
    resultado = set(estados)
    pilha = list(estados)

    while pilha:
        estado = pilha.pop()
        chave = (estado, "\\")

        if chave in maquina["transicoes"]:
            for destino in maquina["transicoes"][chave]:
                if destino not in resultado:
                    resultado.add(destino)
                    pilha.append(destino)

    return resultado


def identifica_palavra_afd(maquina, palavra):
    def identifica_palavra_afd(maquina, palavra):

    for simbolo in palavra:
        if simbolo not in maquina["alfabeto"]:
            return "X"

    estados_atuais = fecho_lambda(maquina, maquina["iniciais"])
    estados_atuais = fecho_lambda(maquina, maquina["iniciais"])

    for simbolo in palavra:
        novos_estados = set()

        for estado in estados_atuais:
            chave = (estado, simbolo)

            if chave in maquina["transicoes"]:
                novos_estados.update(maquina["transicoes"][chave])
        
        if not novos_estados:
            return "X"

        estados_atuais = fecho_lambda(maquina, novos_estados)

    if estados_atuais.intersection(maquina["finais"]):
        return "OK"

    return "X"

def faz_testes(maquina, testes):
    resultados = []

    for palavra in testes:
        resultado = identifica_palavra_afd(maquina, palavra)
        resultados.append(resultado)

    return resultados
