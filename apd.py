import sys
import leituraDeMaquina
#def ler_maquina_APD_terminal():
#   q = input("Q: ")
#   g = input("G: ")
#   i = input("I: ")
#   f = input("F: ")
#    linhas = [q, g, i, f]
#    linhas += [linha.rstrip('\n') for linha in sys.stdin]
#   descricao = []
#    k = 0
#   while linhas[k] != "---":
#        descricao.append(linhas[k])
#        k += 1
#    casos_teste = linhas[k+1:];
#    return descricao, casos_teste
#usa ctrl+z para parar a leitura 🥶🤟

def configuracao_apd(descricao):
    maquina = leituraDeMaquina.cabecalho_apd(descricao)
    if "\\" in maquina["pilha"]:
        print("ERRO: o simbolo '\\' e reservado para lambda "
            "e nao pode estar no alfabeto da pilha.")
        sys.exit(1)


    if "pilha" not in maquina:
        raise KeyError("Campo 'pilha' não encontrado na descrição.")

    transicoes = {}
    apn = False
    alfabeto = set()

    for linha in maquina["linhas_transicao"]:
        origem, resto = linha.split(" -> ")
        destino, operacoes = resto.split(" | ")
        
        for numero_linha, linha in enumerate(linhas_transicao, start=1):

            origem, resto = linha.split(" -> ")
            destino, operacoes = resto.split(" | ")

        for op in operacoes.split():
        
            entrada, pilha = op.split(",")
            if entrada != "\\":
    alfabeto.add(entrada)
            desempilha, empilha = pilha.split("/")
            chave = (origem, entrada, desempilha)

            if chave not in transicoes:
                transicoes[chave] = []

            if len(transicoes[chave]) > 0:
                apn = True
                #print para verificar não determinismo
                #print("\nAPN DETECTADO TRANSIÇÃO")

            transicoes[chave].append((destino, empilha))
            if entrada == "\\":
                apn = True

    maquina["transicoes"] = transicoes
maquina["alfabeto"] = {"a", "b", "c"}
    if len(maquina["inicial"]) > 1:
        apn = True
        #print para verificar não determinismo
        #print("\nAPN DETECTADO MÚLTIPLOS INICIAIS")

    return maquina

def executar_apd(maquina, palavra):
    for simbolo in palavra:
    if simbolo not in maquina["alfabeto"]:
        return "X"
    configuracoes = []
for estado in maquina["inicial"]:
        configuracoes.append((estado, [], 0))


    while configuracoes:
          try:
        estado, pilha, i = configuracoes.pop()
except ValueError:
            raise RuntimeError(
                "Configuração interna corrompida."
            )
        assinatura = (estado, tuple(pilha), i)

        if assinatura in visitados:
            continue

        visitados.add(assinatura)

        # condição de aceitação
        if i == len(palavra) and len(pilha) == 0:
            return "OK"

        simbolo_entrada = palavra[i] if i < len(palavra) else "\\"
        topo = pilha[-1] if pilha else "\\"
        transicoes_possiveis = []

        # consome símbolo
        chave = (estado, simbolo_entrada, topo)
try:
        if simbolo_entrada != "\\" and chave in maquina["transicoes"]:
            for destino, empilha in maquina["transicoes"][chave]:
                transicoes_possiveis.append((destino, empilha, True))
except Exception as erro:
            raise RuntimeError(
                f"Erro ao processar transições: {erro}"
            ) from erro
        # lambda
        chave = (estado, "\\", topo)

        if chave in maquina["transicoes"]:
            for destino, empilha in maquina["transicoes"][chave]:
                transicoes_possiveis.append((destino, empilha, False))
                except Exception as erro:
            raise RuntimeError(
                f"Erro ao processar transições: {erro}"
            ) from erro

        # expande todos os caminhos
        for prox_estado, empilha, consumiu in transicoes_possiveis:
            nova_pilha = pilha.copy()
            try:
            if topo != "\\":
                nova_pilha.pop()

            if empilha != "\\":
                for simbolo in reversed(empilha):
                    nova_pilha.append(simbolo)
                    except Exception as erro:
                raise RuntimeError(
                    f"Erro ao manipular pilha: {erro}"
                ) from erro

            novo_i = i
            if consumiu:
                novo_i += 1

            configuracoes.append((prox_estado,nova_pilha,novo_i))
    return "X"
