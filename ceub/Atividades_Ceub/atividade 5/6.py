num = int(input("Digite um numero: "))
qtd = int(input("Digite a qtd de vezes a ser multiplicado: "))
print("Tabuada até 10")

for x in range(0, qtd, 1):
    vl = (x+1)*num
    print(f"{x+1} x {num} = {vl}")