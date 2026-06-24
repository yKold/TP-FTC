# A ideia da leitura de arquivos é basicamente poder ler qualquer arquivo, e depois adaptar para o tipo de máquina desejada!
# O "ler_maquina" apenas lê as linhas iniciais que definem a máquina, como estados, estado inicial, final e outros, salvando em "descricao"
# Após isso, o "parse_cabecalho" vai colocar todos esses dados organizados em dicionários, para que você possa acessar rapidamente os estados, 
# estados iniciais, estodos finais e as linhas de transição.
# Após isso, basta chamar o "parser" da máquina desejada para configurar as transições de acordo com o tipo da máquina, dado que algumas possuem dados
# para escrita na fita, ou então para empilhar e etc...

# import sys 

def ler_maquina(arquivo_lido):
    # linhas = [linha.rstrip('\n') for linha in sys.stdin]

    with open(arquivo_lido+".txt", "r", encoding="utf-8") as arquivo:
        linhas = [linha.rstrip('\n') for linha in arquivo]

    descricao = []
    i = 0

    while linhas[i] != "---":
        descricao.append(linhas[i])
        i += 1

    casos_teste = linhas[i+1:]

    return descricao, casos_teste

def parse_cabecalho(descricao):
    return {
        "estados": descricao[0].split()[1:],
        "inicial": descricao[1].split()[1],
        "finais": descricao[2].split()[1:],
        "linhas_transicao": descricao[3:]
    }

def parse_cabecalho_turing(descricao):
    return {
        "estados": descricao[0].split()[1:],
        "estados_escrita": descricao[1].split()[1:],
        "inicial": descricao[2].split()[1],
        "finais": descricao[3].split()[1:],
        "linhas_transicao": descricao[4:]
    }

def parse_afd(descricao):
    maquina = parse_cabecalho(descricao)

    transicoes = {}

    for linha in maquina["linhas_transicao"]:
        origem, resto = linha.split(" -> ")
        destino, simbolos = resto.split(" | ")

        for simbolo in simbolos.split():
            transicoes[(origem, simbolo)] = destino

    maquina["transicoes"] = transicoes

    return maquina

def parse_afn(descricao):
    maquina = parse_cabecalho(descricao)

    transicoes = {}

    for linha in maquina["linhas_transicao"]:
        origem, resto = linha.split(" -> ")
        destino, simbolos = resto.split(" | ")

        for simbolo in simbolos.split():

            chave = (origem, simbolo)

            if chave not in transicoes:
                transicoes[chave] = []

            transicoes[chave].append(destino)

    maquina["transicoes"] = transicoes

    return maquina

def parse_apd(descricao):
    maquina = parse_cabecalho(descricao)

    transicoes = {}

    for linha in maquina["linhas_transicao"]:

        esquerda, direita = linha.split(" -> ")

        estado, simbolo, topo = esquerda.split()

        prox_estado, empilha = direita.split()

        chave = (estado, simbolo, topo)

        if chave not in transicoes:
            transicoes[chave] = []

        transicoes[chave].append(
            (prox_estado, empilha)
        )

    maquina["transicoes"] = transicoes

    return maquina

