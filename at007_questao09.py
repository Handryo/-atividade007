# at007_questao09.py - Comandos executados via sudo
import re

with open("sistema.log") as f:
    for linha in f:
        if "sudo" in linha:
            match = re.search(r'COMMAND=(.*)', linha)
            if match:
                print(match.group(1))
