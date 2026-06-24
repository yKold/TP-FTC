# A ideia da leitura de arquivos é basicamente poder ler qualquer arquivo, e depois adaptar para o tipo de máquina desejada!
# O "ler_maquina" apenas lê as linhas iniciais que definem a máquina, como estados, estado inicial, final e outros, salvando em "descricao"
# Após isso, o "parse_cabecalho" vai colocar todos esses dados organizados em dicionários, para que você possa acessar rapidamente os estados, 
# estados iniciais, estodos finais e as linhas de transição.
# Após isso, basta chamar o "parser" da máquina desejada para configurar as transições de acordo com o tipo da máquina, dado que algumas possuem dados
# para escrita na fita, ou então para empilhar e etc...
import sys

def ler_maquina(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        linhas = [linha.rstrip('\n') for linha in arquivo]
    descricao = []
    i = 0

    while linhas[i] != "---":
        descricao.append(linhas[i])
        i += 1

    casos_teste = linhas[i+1:]
    return descricao, casos_teste

def cabecalho_afd(descricao):
    return {
        "estados": descricao[0].split()[1:],
        "inicial": descricao[1].split()[1:],
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

def cabecalho_apd(descricao):
    return {
        "estados": descricao[0].split()[1:],
        "pilha": list(descricao[1])[1:],
        "inicial": descricao[2].split()[1:],
        "finais": descricao[3].split()[1:],
        "linhas_transicao": descricao[4:]
    }

