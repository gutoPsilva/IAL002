A = []
B = []
i = 0
print("Digite os valores da Lista 1")
while i < 10:
    n = int(input("Digite o elemento {}: ".format(i+1)))
    A.append(n)
    i+=1

i = 0 # reiniciar
print("Digite os valores da Lista 2")
while i < 10:
    m = int(input("Digite o elemento {}: ".format(i+1)))
    B.append(m)
    i+=1
C = A+B
print(C)
