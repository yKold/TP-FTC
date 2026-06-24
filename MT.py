from leituraDeMaquina import parse_cabecalho_turing

def parse_mt(descricao):
    maquina = parse_cabecalho_turing(descricao)
    transicoes = {}

    for linha in maquina["linhas_transicao"]:
        estado_atual, direita = linha.split(" -> ")
        prox_estado, resto = direita.split(" | ")
        lista_transicoes = resto.split()
        
        for transicao in lista_transicoes:

            leitura = transicao[0]
            escrita = transicao[2]
            direcao = transicao[3]

            chave = (estado_atual, leitura)

            if chave not in transicoes:
                transicoes[chave] = []

            transicoes[chave].append(
                (
                    prox_estado,
                    escrita,
                    direcao
                )
            )

    maquina["transicoes"] = transicoes
    return maquina

def verifica_palavra(maquina, palavra):
    estado_atual = maquina["inicial"]
    fita = list(palavra)

    if len(fita) == 0:
        fita.append("_")

    cabeca = 0

    while True:
        if cabeca >= len(fita):
            fita.append("_")

        if cabeca < 0:
            fita.insert(0, "_")
            cabeca = 0

        simbolo_lido = fita[cabeca]
        chave = (estado_atual, simbolo_lido)

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
            print("Direção inválida:", direcao)
            break

        if estado_atual in maquina["finais"]:
            break

    resultado_fita = ''.join(fita).rstrip('_')

    if estado_atual in maquina["finais"]:
        print("OK", resultado_fita)
    else:
        print("X", resultado_fita)
