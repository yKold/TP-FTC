import apd
import afd
import leituraDeMaquina

arquivo = input("Digite o nome do arquivo de entrada: ")
arquivo_completo = "./TP-FTC/testes/" + arquivo
descricao, testes = leituraDeMaquina.ler_maquina(arquivo_completo)

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
    maquina = leituraDeMaquina.parse_mt(descricao)