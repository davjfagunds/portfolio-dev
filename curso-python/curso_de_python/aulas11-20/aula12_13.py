0# Calculo do IMC (Exercício)
# Formula do IMC = peso / (altura x altura)
# Com algumas f-Strings

nome = 'Davi Fagundes'
altura = 1.87
peso = 72
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura'

print(nome,'Pesa', peso, 'quilos', 'e seu IMC é')
print(f'{imc:.2f}')

print(linha_1)