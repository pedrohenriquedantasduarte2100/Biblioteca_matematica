print("----- Sistema de Log Natural -----")
print("")

x = float(input("Digite um número maior que 0: "))

while x <= 0:
    print("Número inválido!")
    x = float(input("Digite um número maior que 0: "))

arredondamento = int(input("Digite o máximo de repeticões que deseja (ideal, 20): "))

soma = 0
n = 0

while n <= arredondamento:
    termo = (1 / (2*n + 1)) * (((x - 1) / (x + 1)) ** (2*n + 1))
    soma = soma + termo
    n = n + 1

resultado = 2 * soma

print("")
print(f"ln({x}) ≈ {resultado}")