soma = 0
ct = 0
media = 0

for x in range(2, 21, 2):
    print(x)
    ct += 1
    soma += x

media = soma/ct
print("soma: ", soma)
print("Media:", media)
