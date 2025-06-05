"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

lista.append(50) # adiciona 50 no final da lista
lista.pop() # remove o último elemento da lista
lista.append(60)
lista.append(70)
lista.insert(2,'X')# insere um valor na lista em um indice
ultimo_valor = lista.pop(3)

print(lista, 'Removido,', ultimo_valor)
print()
for item in lista:
    print(item)

print(60 in lista)

print(lista.index(20)) #mostra o indice do numero na lista

lista[0] = "nome"

print(lista)
print(lista.count(70))