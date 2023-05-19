A = []
B = []
i = 0
print("Digite os valores da Lista A")
while i < 10:
    n = int(input("Digite o elemento {}: ".format(i+1)))
    A.append(n)
    i+=1

i = 0 # reiniciar
print("\n\nDigite os valores da Lista B")
while i < 10:
    m = int(input("Digite o elemento {}: ".format(i+1)))
    B.append(m)
    i+=1
    
C = A+B
print(C)

print("\n\nIsso é tudo pessoal!")
