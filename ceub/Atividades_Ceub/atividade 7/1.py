def positivo_nulo_negativo(num):
    if num > 0:
        print("Valor Positivo")
    elif num == 0:
        print("Valor Nulo")
    elif num < 0:
        print("Valor Negativo")
    else:
        print("Digite um numero")

if __name__ == '__main__':
    n = int(input("Digite um valor: "))
    print(positivo_nulo_negativo(n))