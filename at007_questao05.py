# at007_questao05.py - Contar logins bem-sucedidos e falhados
sucesso = falha = 0
with open("sistema.log") as f:
    for linha in f:
        if "Accepted password" in linha:
            sucesso += 1
        elif "Failed password" in linha:
            falha += 1
print(f"Logins bem-sucedidos: {sucesso}")
print(f"Logins falhados: {falha}")
