from leituraDeMaquina import ler_maquina ,parse_afd, parse_afn, parse_mt
from apd import executar_apd,ler_maquina_APD_terminal, configuracao_apd, ler_maquina_APD_arquivo
#pra executar so lançar um type entrada.txt | python main.py no terminal ou trocar aqui pra terminal
descricao, testes = ler_maquina_APD_arquivo()

tipo = "APD"

if tipo == "AFD":
    maquina = parse_afd(descricao)

elif tipo == "AFN":
    maquina = parse_afn(descricao)

elif tipo == "APD":
    maquina = configuracao_apd(descricao)
    for palavra in testes:
        resultado = executar_apd(maquina, palavra)
        print(resultado)

elif tipo == "MT":
    maquina = parse_mt(descricao)