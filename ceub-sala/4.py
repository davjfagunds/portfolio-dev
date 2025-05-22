lista = []
lista_10 = []
x = 0
while True:
    var = int(input("Digite um numero: "))
    lista.append(var)
    if var == 0:
        break

print(lista)
for item in lista:
    print(item)
print()
print(f"Quantidade: {len(lista)}")
print(f"Soma dos valores: {sum(lista)}")
print(f"O maior valor é {max(lista)}")
print(f"O maior valor é {min(lista)}")

if 10 in lista:
    print(f"Pesquisa: (10) está na posiçao: {lista.index(10)}")

a = sorted(lista)

print(f"Ordem crescente da lista: {a}")

lista.insert(1,30)
print(lista)

b = list(reversed(lista))

print(f"Ordem decrescente da lista: {b}")
if 0 in lista:
    lista.remove(0)
media = sum(lista)/(len(lista))
print(f"{media:.3f}")

for item in lista:
    
    if item > 10:
        lista_10.append(item)
print(f"O numeros maiores que 10 é {lista_10}")

por = ((len(lista_10)*100)/(len(lista)))
print(f"A porcentagem dos numeros maiores que dez da lista é: {por}")




    

    