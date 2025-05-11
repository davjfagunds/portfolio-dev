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

if entrada == 'E' or entrada =='e':
    print('Entrando...')
    senha_digitada = input('Senha: ')

elif entrada == 'S' or entrada =='s':
    print('Lamentamos sua saída :(')

if (entrada == 'E' or entrada =='e') and senha_digitada == senha_permitida:
    print('Bem-vindo de volta!!  :)')

elif (entrada == 'E' or entrada == 'e') and senha_digitada != senha_permitida:
    print("Senha Incorreta")
