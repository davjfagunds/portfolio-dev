#Problema: Verificar se um número é par ou ímpa

#elabore um programa em Python que recebe um número inteiro como parâmetro e 
#retorna um texto informando se ele é "Par" ou "Ímpar"

def impar_ou_par(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
if __name__ == '__main__':
    num = int(input("Digite um numero: "))
    resultado = impar_ou_par(num)

    print("Seu numero é",resultado)
