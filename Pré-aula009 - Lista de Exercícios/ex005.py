N = int(input("Digite o valor de N: "))
while N < 0 or N > 50:
    print("N deve estar entre 0 e 50!")
    N = int(input("Digite o valor de N: "))
    
i = 0
A = []
NEG = []
POS = []
while i < N:
    M = float(input("Digite o elemento {}: ".format(i+1)))
    A.append(M)
    if M<0:
        NEG.append(M)
    else:
        POS.append(M)
    i+=1
if N == 0:
    print("Não foram inseridos dados.")
else:
    print("A lista NEG possui {} elementos, seus valores são:\n{}".format(len(NEG), NEG))
    print("A lista POS possui {} elementos, seus valores são:\n{}".format(len(POS), POS))
print("\n\nIsso é tudo pessoal!")
