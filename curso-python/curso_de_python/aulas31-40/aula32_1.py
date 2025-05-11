valor = input("Digite um número inteiro:")

if valor.isdigit():

    if (int(valor) % 2) == 0:
        print(f"{valor} é par")

    if (int(valor) % 2) != 0:
        print(f"{valor} é ímpar")

else:
    print("Coloque um número inteiro")
