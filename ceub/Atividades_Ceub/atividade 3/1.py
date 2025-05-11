ct = 0
ct_20 = 0
soma = 0

while True:
    valor = int(input("Escreva um Valor: "))
    if valor == 0:
        break

    ct += 1
    soma += valor 
    media = soma/ct

    if valor > 20:
        ct_20 += 1


print(f"Quantidade: {ct} Soma: {soma}, Media: {media}, qtd de valores maiores que 20: {ct_20}")