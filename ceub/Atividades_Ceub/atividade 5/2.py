vl_inicial = int(input("Digite o valor inicial: "))
vl_final = int(input("Digite o valor final: "))
print("")
print("Fahreinheit | Celsius")

if vl_inicial < vl_final:
    for x in range(vl_inicial, vl_final + 1 , 1):
        print(f"{x} ºF | {(x - 32)*5/9:.3f}")

if vl_inicial > vl_final:
    for x in range(vl_inicial, vl_final - 1, -1):
        print(f"{x} ºF | {(x - 32)*5/9:.3f}")