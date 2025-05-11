v1 = float(input("Digite um valor: "))
op = input("Escolha um operador lógico(+,-,*,/):" )
v2 = float(input("Digite um valor: "))


if op == "+":
    print("R = ", v1 + v2)
elif op == "-":
    print("R = ", v1 - v2)
elif op == "*":
    print("R = ", v1*v2)
elif op == "/":
    print("R = ", v1/v2)

else:
    print("Você errou em algum lugar")