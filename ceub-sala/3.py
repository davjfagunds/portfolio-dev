def conv(v1, v2):

    return (int(v1) * 60) + int(v2)

def conv2(v1, v2):
    print((v1*60) + v2)

if __name__ == "__main__":
    var1 = int(input("Horas: "))
    var2 = int(input("Minutos: "))

    print(f"Horas: {var1}, minutos: {var2} e Total: {conv(var1, var2)} minutos")

    conv2(var1, var2)