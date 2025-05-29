lista = []
while True:
    valor = int(input("Digite o Valor: "))
    if valor == 0:
        break
    if (valor % 2) == 0:
        lista.append(valor)
    
    
print(lista)
for valor in lista:
    print(valor)

print(f"A media é {sum(lista)/len(lista):.2f}, e a Quantidade é {len(lista)}, A soma das notas é {sum(lista)}")
