# at007_questao01.py - Contar linhas do log
with open("sistema.log", "r") as f:
    linhas = f.readlines()
    print(f"Total de linhas no log: {len(linhas)}")
