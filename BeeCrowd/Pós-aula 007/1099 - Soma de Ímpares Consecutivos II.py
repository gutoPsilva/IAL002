n = int(input())
while n > 0:
    soma = 0 # zera a soma para cada nova saída
    linha = input().split()
    X = int(linha[0])
    Y = int(linha[1])
    menor = min(X, Y) # menor elemento
    maior = max(X, Y) # maior elemento
    if maior%2 == 1:  # se o maior elemento for ímpar
        maior-=1 # desconsidere o primeiro, pois é impar e é o digitado
        while maior>menor: # enquanto for maior
            if maior%2 != 0: # se o atual maior for ímpar
                soma +=maior # some o atual ao total
            maior-=1 # tire 1 para ter o fechamento do laço
        print(soma)
    else: # se nao for ímpar, faça o mesmo processo sem desconsiderar o primeiro
        while maior>menor:
            if maior%2 != 0:
                soma += maior
            maior-=1
        print(soma)
    n-=1
