print("Somas dos numeros(impares e multiplos de 3) interios de um a quinhentos")
soma = 0

for x in range(1, 501, 1):

    if x%2 != 0 and x%3 == 0:  
        soma = x + soma
print(f"A soma é {soma}")

        