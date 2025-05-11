nota = 0
ap = 0
rep = 0
ct = 0

while True:
    nota = float(input("Escreva a nota: "))
    if nota == 0:
        break
    ct += 1

    if nota >= 5:
        ap += 1
    if nota < 5:
        rep += 1

print(f"Alunos (A)provados: {ap}")
print(f"Alunos (R)eprovados: {rep}")
print(f"Qtd de alunos que fizeram aprova: {ct}")