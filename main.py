import leituraDeMaquina

descricao, testes = ler_maquina()

if tipo == "AFD":
    maquina = parse_afd(descricao)

elif tipo == "AFN":
    maquina = parse_afn(descricao)

elif tipo == "APD":
    maquina = parse_apd(descricao)

elif tipo == "MT":
    maquina = parse_mt(descricao)