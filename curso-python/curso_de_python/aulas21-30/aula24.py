# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3
#  D a v i
# -4-3-2-1

nome = 'Davi'
print('Davi'[2])

seu_nome = input('Seu nome -->')
sua_letra = input('Uma letra -->')

if sua_letra in seu_nome:
    print(f'({sua_letra}) esta em {seu_nome}')

else:
    print(f'({sua_letra}) não esta em {seu_nome}')