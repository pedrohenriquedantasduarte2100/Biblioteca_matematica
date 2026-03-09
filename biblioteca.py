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
#SENO do ANGULO
# solicitando o valor do angulo
anguloRecebido = float(input("Digite o ângulo em graus: "))

# armazenando o valor de pi (ate 15 casas)
pi = 3.141592653589793

# a quantidade de tentativas para nao deixar infinito, no caso 10
k = 10

# funcao para calcular o radiano pois a formula de taylor trabalha
def radiano(angulo):
    rad = angulo * pi / 180
    return rad

radianoConvertido = radiano(anguloRecebido)

# funcao da formula de taylor
def funcao_taylor(rad, k):
    sin = 0

    for pedaco in range(k):
        fatorialAtual = 2 * pedaco + 1

        fatorialCalc = 1
        for i in range(1, fatorialAtual + 1):
            fatorialCalc *= i

        formula = (((-1) ** pedaco) * (rad ** (2 * pedaco + 1))) / fatorialCalc
        sin += formula

    return sin
    # sin eh o valor do angulo

resultado = funcao_taylor(radianoConvertido, k)
print(f'O seno do angulo {anguloRecebido} = {resultado:.6f}')

# Pedro 
#funçao exponencial


def exponencial (x, termos=50):
    print("-- funçao de exponencial iniciada")
    termo_atual = 1.0
    resultado = 1
    
    for i in range (1, termos):
        termo_atual = termo_atual * x / i
        resultado += termo_atual
        
    return resultado

x = float(input("digite seu numero: "))

print(exponencial(x))
