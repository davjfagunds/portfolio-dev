def valor_absoluto(numero):
    if numero < 0:
        numero =  numero * -1
    return numero

if __name__ == '__main__':
    n = int(input("Digite um Valor:"))

    print(f"O valor absoluto de {n} é {valor_absoluto(n)}")
