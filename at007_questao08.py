import re
from collections import Counter

falhas = []
with open("sistema.log") as f:
    for linha in f:
        if "Failed password" in linha:
            match = re.search(r'Failed password for (\w+)', linha)
            if match:
                falhas.append(match.group(1))

c = Counter(falhas)
for usuario, qtd in c.items():
    if qtd > 1:
        print(f"{usuario}: {qtd} vezes")
# at007_questao08.py - Usuarios que falharam login mais de uma vez
from collections import Counter
falhas = []
with open("sistema.log") as f:
    for linha in f:
        if "Failed password" in linha:
            match = re.search(r'Failed password for (\w+)', linha)
            if match:
                falhas.append(match.group(1))
c = Counter(falhas)
for usuario, qtd in c.items():
    if qtd > 1:
        print(f"{usuario}: {qtd} vezes")
