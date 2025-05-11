print("Para calcular seu peso ideal responda: ")
altura = float(input("Qual sua altura: "))
print("Digite [1] para Homem e [2] para Mulher !!")
sx = int(input("Você é Homem ou Mulher?: "))

if sx == 1:
    h = ((72.2)*altura)-58
    print(f'Seu peso ideal é {h:.0f}Kg')

elif sx == 2:
    m = ((62.1)*altura)-44.7
    print(f'Seu peso ideal é {m:.0f}Kg')

else:
    print("gay")