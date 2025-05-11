"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
n_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    n_float = float(n_str)
    print('FLOAT:', n_float)
    print(f'O dobro de {n_str} é {n_float * 2:.2f}')
except:
    print('Isso não é um número')
