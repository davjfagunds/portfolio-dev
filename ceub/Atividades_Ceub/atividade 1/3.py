import math

print("Primeiro ponto:")
x1 = int(input("Digite o x:"))
y1 = int(input("Digite o y:"))

print("Segundo ponto:")
x2 = int(input("Digite o x:"))
y2 = int(input("Digite o y:"))

distancia = math.sqrt(((x2 - x1)**2)+((y2 - y1)**2))

print("A distancia entre os pontos é", distancia)