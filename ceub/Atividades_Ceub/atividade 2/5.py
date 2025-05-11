a = float(input("Digite o valor da reta a: "))
b = float(input("Digite o valor da reta b: "))
c = float(input("Digite o valor da reta c: "))

if ((a + b) <= c) or ((c + b) <= a) or ((c + a) <= b):
    print("Não é um triângulo")

elif (a != b and c) and (b != c and a) and ( c != a and b):
    print("È um triângulo escaleno")

elif a == b == c:
    print("È um triângulo equilátero")

elif a == b or a == c or b == c:
    print("È uma triângulo isósceles")
