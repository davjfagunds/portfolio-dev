def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def main():
    num1 = float(input("Digite o primeiro número: "))
    opcao = input("Escolha a operação (soma[+] ou subtrai[-]): ")
    num2 = float(input("Digite o segundo número: "))
    
    
    if opcao == '+':
        print("Soma:", soma(num1, num2))
    elif opcao == '-':
        print("Subtração:", subtrai(num1, num2))
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()