v1 = int(input("Digite um valor: "))
v2 = int(input("Digite um valor: "))
v3 = int(input("Digite um valor: "))

if v1 > v2 and v3:
    print(f"O maior valor è {v1}")

elif v2 > v3 and v1:
    print(f"O maior valor è {v2}")

elif v3 > v2 and v1:
    print(f"O maior valor è {v3}")

else:
    print("dois ou mais valores são iguais")
