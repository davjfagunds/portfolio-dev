valor = 0
ct1 = 0
ct2 = 0
mediaP = 0
mediaI = 0
somaP = 0
somaI = 0
valorP = 0
valorI = 0

while True:
    valor = int(input("Digite um valor: "))

    if valor == 0:
        break

    if valor % 2 == 0:
        valorP = valor
        ct1 += 1 
        somaP += valorP
        mediaP = somaP/ct1

    if valor % 2 != 0:
        valorI = valor
        ct2 += 1 
        somaI += valorI
        mediaI = somaI/ct2

print(f"Media PAR: {mediaP} ")
print(f"Media IMPAR: {mediaI} ")