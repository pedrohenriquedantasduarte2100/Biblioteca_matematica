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