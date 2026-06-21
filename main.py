import apd
import afd
import leituraDeMaquina

descricao, testes = leituraDeMaquina.ler_maquina("entrada.txt")

tipo = input("Digite maquina: ")

if tipo == "AFD":
    maquina = afd.configuracao_afd(descricao)
    resultados = afd.faz_testes(maquina, testes)

elif tipo == "AFN":
    maquina = leituraDeMaquina.parse_afn(descricao)

elif tipo == "APD":
    maquina = apd.configuracao_apd(descricao)
    for palavra in testes:
        resultado = apd.executar_apd(maquina, palavra)
        print(resultado)

elif tipo == "MT":
    maquina = leituraDeMaquina.parse_mt(descricao)