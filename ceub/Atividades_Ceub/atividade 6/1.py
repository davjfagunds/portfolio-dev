def mostra_valor(msg, num):
    print(f"Parâmetro recebido: {msg}, {num}")

if __name__ == '__main__':
    msg = input("Escreva uma str: ")
    num = int(input("Escreva um número: "))
    mostra_valor(msg, num)
