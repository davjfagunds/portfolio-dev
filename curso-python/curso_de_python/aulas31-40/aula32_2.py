hora = input('Digite o horário atual: ')

try: 
    int(hora)
    hora_int = int(hora)

    dia = hora_int >= 0 and hora_int <= 11
    tarde = hora_int >= 12 and hora_int <= 17
    noite = hora_int >= 18 and hora_int <= 23

    if hora_int:

        if dia:
            print('Bom dia!')
        if tarde:
            print('Boa tarde!')
        if noite:
            print('Boa noite!')



except:
    print('Coloque apenas o número desejado!')