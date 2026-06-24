from leituraDeMaquina import parse_cabecalho_turing
def parse_mt(descricao):
    maquina = parse_cabecalho_turing(descricao)

    transicoes = {}

    for linha in maquina["linhas_transicao"]:

        estado_atual, direita = linha.split(" -> ")

        # prox_estado, simbolo_escrito, direcao = direita.split()
        prox_estado, resto = direita.split(" | ")
        leitura_na_fita, escrita_na_fita, direcao = resto[0], resto[2], resto[3]

        chave = (estado_atual, leitura_na_fita)

        if chave not in transicoes:
            transicoes[chave] = []

        transicoes[chave].append(
            (
                prox_estado,
                escrita_na_fita,
                direcao
            )
        )

    maquina["transicoes"] = transicoes
    # print(maquina)
    return maquina

def verifica_palavra(maquina, palavra):
    fita = list(palavra + "_")  # branco no final
    cabeca = 0
    estado_atual = maquina["inicial"]

    while True:

        print("EA:", estado_atual, " Fita:", ''.join(fita), " Cabeca:", cabeca)

        simbolo_lido = fita[cabeca]

        if (estado_atual, simbolo_lido) not in maquina["transicoes"]:
            break

        transicao = maquina["transicoes"][(estado_atual, simbolo_lido)][0]

        novo_estado, simbolo_escrito, direcao = transicao

        # escreve na fita
        fita[cabeca] = simbolo_escrito

        estado_atual = novo_estado

        # movimenta cabeça
        if direcao == "D":
            cabeca += 1
        elif direcao == "E":
            cabeca -= 1

        if cabeca < 0:
            fita.insert(0, "_")
            cabeca = 0

        if estado_atual in maquina["finais"]:
            break

    if estado_atual in maquina["finais"]:
        print("ACEITA:", ''.join(fita))
    else:
        print("OK:", ''.join(fita))
    # print("EA:", estado_atual, " EF:", escrita_fita, " D:", direcao)
