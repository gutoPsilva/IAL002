N = int(input("Digite o valor de N: "))
while N < 0 or N > 50:
    print("O valor de N deve estar entre 0 e 50!")
    N = int(input("Digite o valor de N: "))
    
L = []
i = 0
while i < N:
    m = float(input("Digite o elemento {}: ".format(i+1)))
    L.append(m)
    i+=1

if N == 0:
    print("Dados não foram inseridos.")
else:
    for elemento in L:
        print(elemento)

print("\n\nIsso é tudo pessoal!")