print("Gustavo Pereira da Silva")
print("Vinicius Corrêa Carvalho")
print("Questão 01\n")


Valor = int(input("Digite a quantidade de segundos: "))
Z = Valor % 60
Y = Valor // 60
X = Y // 60

if Y >= 60:
    Y = Y % 60
print("{} horas, {} minutos, {} segundos".format(X, Y, Z))


print("\n\nFim do Programa")
