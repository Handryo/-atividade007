# at007_questao10.py - Contar conexoes SSH por IP
import re

from collections import Counter
ips = []
with open("sistema.log") as f:
    for linha in f:
        if "sshd" in linha:
            match = re.search(r'from ([\d.]+)', linha)
            if match:
                ips.append(match.group(1))
contagem = Counter(ips)
for ip, qtd in contagem.most_common():
    print(f"{ip}: {qtd}")
