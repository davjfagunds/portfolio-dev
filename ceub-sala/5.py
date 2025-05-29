lista = []
while True:
    valor = int(input("Digite um valor: "))
    if valor == -1:
        break
    lista.append(valor)

print(f"A media é {sum(lista)/len(lista):.2f}, e a Quantidade é {len(lista)}, A soma das notas é {sum(lista)}")