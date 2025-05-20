def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

if __name__ == '__main__':
    print("Cálculo de Fatorial")
    numero = int(input("Digite um número inteiro: "))

    print(f"O fatorial de {numero}! é {fatorial(numero)}")

