def soma(v1, v2):
    som = v1 + v2
    print("A Soma é igual a ", som)

def subtracao(v1, v2):
    sub = v1 - v2
    print("A subtração é igual a ", sub)

def multiplicacao(v1, v2):
    multi = v1 * v2
    print("A multiplicação é igual a ", multi)

def divisao(v1, v2):
    div = v1 / v2
    print("A divisão é igual a ", div)

if __name__ == '__main__':
    v1 = int(input("Digite um Valor:"))
    op = input("Escolha uma operação [+, -, *, /]: ")
    v2 = int(input("Digite outro Valor:"))

    if op == "+":
        print(soma(v1, v2))
    if op == "-":
        print(subtracao(v1, v2))
    if op == "*":
        print(multiplicacao(v1, v2))
    if op == "/":
        print(divisao(v1, v2))