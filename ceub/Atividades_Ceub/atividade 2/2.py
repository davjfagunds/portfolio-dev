v1 = int(input("Digite um valor: "))
v2 = int(input("Digite um valor: "))
v3 = int(input("Digite um valor: "))

if v1 > v2:
    if v1 > v3:
        print(f"O maior valor é {v1}")
elif v2 > v1:
    if v2 > v3:
        print(f"O maior valor é {v2}")
    elif v2 < v3:
        print(f"o maior valor é {v3}")
else:
    print("dois ou mais valores são iguais")
