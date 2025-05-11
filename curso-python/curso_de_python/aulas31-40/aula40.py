"""Calculadora com while """
while True:
    n_1 = input("Digite um numero: ")
    operador = input("Digite um operador (+-/*): ")
    n_2 = input("Digite um numero: ")

    n_validos = None

    n_1float = 0
    n_2float = 0

    try:
        n_1float = float(n_1)
        n_2float = float(n_2)
        n_validos = True
    except:
        ...

    if n_validos is None:
        print("Um dos números é inválido")
        continue

    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("{Operador inválido}")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue


    #######
    
    print("Confira o resultado abaixo: ")
    if operador == '+':
        print(n_1float + n_2float)
    elif operador == '-':
        print(n_1float - n_2float)
    elif operador == '/':
        print(round(n_1float / n_2float, 2))
    elif operador == '*':
        print(round(n_1float * n_2float, 2))
    else:
        ...
    

    sair = input("Quer sair? [s]im: ").lower().startswith("s")

    if sair:
        break