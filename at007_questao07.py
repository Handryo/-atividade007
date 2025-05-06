# at007_questao07.py - Ordenar logs por data/hora
from datetime import datetime
with open("sistema.log") as f:
    linhas = f.readlines()
linhas.sort(key=lambda l: datetime.strptime(" ".join(l.split()[:3]), "%b %d %H:%M:%S"))
for linha in linhas:
    print(linha.strip())
