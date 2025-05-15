def maior(v1, v2):
    if v1 > v2:
        return v1
    else:
        return v2

def menor(v1, v2):
    if v1 < v2:
        return v1
    else:
        return v2
    
if __name__ == "__main__":
    v1 = int(input("Digite o primeiro número: "))
    v2 = int(input("Digite o segundo número: "))

    print("Maior número:", maior(v1, v2))
    print("Menor número:", menor(v1, v2))