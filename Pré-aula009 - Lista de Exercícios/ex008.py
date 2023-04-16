LMin = int(input("Digite o Mínimo: "))
LMax = int(input("Digite o Máximo: "))

if LMin > LMax:
    X = LMin
    LMin = LMax
    LMax = X
    print("Mínimo maior que Máximo, o valor de ambos foi invertido para o prosseguimento do programa.")

i = 0
A = []
R = []
m = int(input("Digite o valor de N: "))
while i < m: 
    N = int(input("Digite o elemento {}: ".format(i+1)))
    if N >= LMin and N <= LMax:
        A.append(N)
    else:
        R.append(N)
    i+=1

print("A lista de valores ACEITOS possui {} elementos e seus valores são: \n{}".format(len(A), A))
print("A lista de valores REJEITADOS possui {} elementos e seus valores são: \n{}".format(len(R), R))

print("\n\nIsso é tudo pessoal!")
