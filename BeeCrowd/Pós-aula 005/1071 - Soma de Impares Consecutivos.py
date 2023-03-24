X = int(input())
Y = int(input())
soma = 0
if X%2==1:
    while X > Y:
        X-=1 # tirar 1 no início, para NÃO contar o primeiro ímpar que é o digitado.
        if X%2 != 0:
            soma += X
else:
    while X > Y:
        if X%2 != 0:
            soma += X
        X-=1 # tirar 1 no fim, já que o primeiro impar NÃO é o digitado
print(soma)
