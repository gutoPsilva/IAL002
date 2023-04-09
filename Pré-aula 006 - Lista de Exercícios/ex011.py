arq = open("ex011-saida008.txt", "w")
N = int(input("Digite um inteiro: "))
if N == 2:
    print("{} é primo".format(N))
elif N % 2 == 0:
    print("{} não é primo".format(N))
else:
    raiz = N ** 0.5
    resto = 1
    i = 3
    while i <= raiz and resto != 0:
        resto = N % i
        i = i + 2
    if resto != 0:
        print("{} é primo".format(N))
        arq.write("{} é primo".format(N)) # escrever se o N é primo
    else:
        print("{} não é primo".format(N))
        arq.write("{} não é primo".format(N)) # escrever se o N ñ é primo
arq.close()
print("\n\nFim do programa")
