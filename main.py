import leituraDeMaquina
import afd

descricao, testes = leituraDeMaquina.ler_maquina("entrada.txt")

tipo = input("Digite maquina: ")

if tipo == "AFD":
    maquina = afd.configuracao_afd(descricao)
    resultados = afd.faz_testes(maquina, testes)

elif tipo == "AFN":
    maquina = leituraDeMaquina.parse_afn(descricao)

elif tipo == "APD":
    maquina = leituraDeMaquina.parse_apd(descricao)

elif tipo == "MT":
    maquina = leituraDeMaquina.parse_mt(descricao)