n = int(input("Digite um valor inteiro: "))
lista = []
while n > 0:
    lista.append(n)
    n = int(input("Digite um valor inteiro: "))
if len(lista) == 0:
    print("Não foram inseridos dados na lista.")
else:
    print("Os dados inseridos na lista foram: \n{}".format(lista))
