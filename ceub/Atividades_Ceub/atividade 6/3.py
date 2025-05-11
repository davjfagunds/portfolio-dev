def calcular_soma(v1, v2, v3):
    soma = v1 + v2 + v3
    return soma

if __name__ == '__main__':
    valor1 = int(input("Digite o valor número 1: "))
    valor2 = int(input("Digite o valor número 2: "))
    valor3 = int(input("Digite o valor número 3: "))

    resultado = calcular_soma(valor1, valor2, valor3)
    print("A soma dos números é", resultado)