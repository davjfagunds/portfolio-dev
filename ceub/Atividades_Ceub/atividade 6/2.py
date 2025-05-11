def cal_idade(valor):
    idade = 2025 - valor
    return idade

if __name__ == '__main__':
    var = int(input("Em que ano você nasceu? "))
    valor_retorno = cal_idade(var)

    print("Sua idade é ",valor_retorno)