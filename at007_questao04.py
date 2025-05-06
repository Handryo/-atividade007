# at007_questao04.py - Filtrar falhas de login
with open("sistema.log") as f:
    for linha in f:
        if "Failed password" in linha:
            print(linha.strip())
