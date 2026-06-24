import ap
import af
import leituraDeMaquina
from MT import parse_mt, verifica_palavra as VPMT
from ALL import verifica_palavra_all as VPALL

arquivo = input("Digite o nome do arquivo de entrada: ")
descricao, testes = leituraDeMaquina.ler_maquina(arquivo)

tipo = input("Digite maquina: ")

if tipo == "AFD":
    maquina = af.configuracao_afd(descricao)
    resultados = af.faz_testes(maquina, testes)
    for i in range(len(resultados)):
        print(resultados[i])

elif tipo == "APD":
    maquina = ap.configuracao_apd(descricao)
    for palavra in testes:
        resultado = ap.executar_apd(maquina, palavra)
        print(resultado)

elif tipo == "MT":
    descricao, casos_testes = leituraDeMaquina.ler_maquina(arquivo)
    MT = parse_mt(descricao)
    for caso in casos_testes:
        VPMT(MT, caso)

elif tipo == "ALL":
    descricao, casos_testes = leituraDeMaquina.ler_maquina(arquivo)
    ALL = parse_mt(descricao)
    for caso in casos_testes:
        VPALL(ALL, caso)
