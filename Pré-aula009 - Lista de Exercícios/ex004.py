from random import randint
N = int(input("Digite o valor de N: "))
while N < 0 or N > 50:
    print("N deve estar entre 0 e 50!")
    N = int(input("Digite o valor de N: "))

L = []
i = 0
while i < N:
    m = randint(0, 1000)
    L.append(m)
    i += 1

if N == 0:
    print("Não foram inseridos dados.")
else:
    print(L)
print("\n\nIsso é tudo pessoal!")
