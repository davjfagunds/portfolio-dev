lista = []
while True:
    valor =  int(input("Digite um valor: "))
    if valor == 0:
        break
    lista.append(valor)

print(lista)
for valor in lista:

    print(f"{valor} = {lista.index(valor)}")


lista.sort()

menor = lista[0]
maior = lista[-1]

print(f"O maior valor è {maior} e o menor valor é {menor}")