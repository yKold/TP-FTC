import AP
import AF
import leituraDeMaquina
from MT import parse_mt, verifica_palavra as VPMT
from ALL import verifica_palavra_all as VPALL

arquivo = input("Digite o nome do arquivo de entrada: ")
tipo, alfabeto, descricao, testes = leituraDeMaquina.ler_maquina(arquivo)

if tipo == "AF":
    alfabeto += "\\"
    maquina = AF.configuracao_af(descricao, alfabeto)
    if maquina != {}:
        for caso in testes:
            AF.identifica_palavra_af(maquina, caso)

elif tipo == "AP":
    alfabeto += "\\"
    maquina = AP.configuracao_ap(descricao, alfabeto)
    if maquina != {}:
        for caso in testes:
            AP.executar_ap(maquina, caso)

elif tipo == "MT":
    alfabeto += "_<"
    maquina = parse_mt(descricao, alfabeto)
    if maquina != {}:
        for caso in testes:
            VPMT(maquina, caso)

elif tipo == "ALL":
    alfabeto += "_<>"
    maquina = parse_mt(descricao, alfabeto)
    if maquina != {}:
        for caso in testes:
            VPALL(maquina, caso)