"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 

"""

variavel = 'AAA'
print(f'{variavel: >9}')
print(f'{variavel: ^10}')
print(f'{variavel: ^20}')
print(f'{1000.212122332423:0=+10,.2f}')
print(f'O hexadecimal de 1000 é {1000:X}')