
# Calculadora de Número Inteiro (DIFERENCA = A*B - C*D)

try:
    A = int(input().strip())
    B = int(input().strip())
    C = int(input().strip())
    D = int(input().strip())
except Exception:
    raise SystemExit("Erro: digite quatro números inteiros, um por linha.")

DIFERENCA = A * B - C * D
print(f"DIFERENCA = {DIFERENCA}")
