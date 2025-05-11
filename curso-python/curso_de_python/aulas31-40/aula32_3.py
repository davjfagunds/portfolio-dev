nome = input("Qual seu primeiro nome?")

if len(nome) <= 4:
    print("seu nome é curto")

elif len(nome) == 5 or len(nome) == 6:
    print("Seu nome é normal")

if len(nome) > 6:
    print("Seu nome é muito grande")