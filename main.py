import apd
import afd
import leituraDeMaquina
from MT import parse_mt, verifica_palavra as VPMT
from ALL import verifica_palavra_all as VPALL

arquivo = input("Digite o nome do arquivo de entrada: ")
descricao, testes = leituraDeMaquina.ler_maquina(arquivo)

tipo = input("Digite maquina: ")

if tipo == "AFD":
    maquina = afd.configuracao_afd(descricao)
    resultados = afd.faz_testes(maquina, testes)
    for i in range(len(resultados)):
        print(resultados[i])

elif tipo == "APD":
    maquina = apd.configuracao_apd(descricao)
    for palavra in testes:
        resultado = apd.executar_apd(maquina, palavra)
        print(resultado)

elif tipo == "MT":
    descricao, casos_testes = leituraDeMaquina.ler_maquina(arquivo)
    MT = parse_mt(descricao)
    for caso in casos_testes:
        VPMT(MT, caso)
    print("")

elif tipo == "ALL":
    descricao, casos_testes = leituraDeMaquina.ler_maquina(arquivo)
    print(descricao)
    ALL = parse_mt(descricao)
    for caso in casos_testes:
        VPALL(ALL, caso)
