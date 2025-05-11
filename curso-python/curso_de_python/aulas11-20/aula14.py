# Formatação de strings com o metódo format
a = 'A'
b = 'B'
c = 1.5
string = 'a={nome1} b={nome2} c={nome3}'
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))