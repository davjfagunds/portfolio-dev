# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
entrada = input('[E]ntrar [S]air: ')
senha_permitida = '123'

if entrada == 'E':
    
    print('Entrando...')
    senha_digitada = input('Senha: ')

elif entrada == 'S':
    print('Lamentamos sua saída :(')

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Bem-vindo de volta!!  :)')

elif entrada == 'E' and senha_digitada != senha_permitida:
    print("Senha Incorreta")

