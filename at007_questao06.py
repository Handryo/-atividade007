# at007_questao06.py - Usuarios que usaram sudo
import re
usuarios = set()
with open("sistema.log") as f:
    for linha in f:
        if "sudo" in linha:
            match = re.search(r'sudo\[\d+\]: (\w+)', linha)
            if match:
                usuarios.add(match.group(1))
for u in usuarios:
    print(u)
