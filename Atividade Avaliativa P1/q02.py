print("Gustavo Pereira da Silva")
print("Vinicius Corrêa Carvalho")
print("Questão 02\n")

LMin = int(input("Digite o valor mínimo: "))
while LMin <= 0:
    print("O valor mínimo deve ser maior que 0!")
    LMin = int(input("Digite o valor mínimo: "))

LMax = int(input("Digite o valor máximo: "))
while LMax <= LMin:
    print("O valor máximo deve ser maior que o mínimo!")
    LMax = int(input("Digite o valor máximo: "))

X = int(input("Digite o valor de X: "))
while X == 0:
    print("O valor de X deve ser DIFERENTE de 0!")
    X = int(input("Digite o valor de X: "))

L = []
soma = 0
media = 0

N = int(input("\nDigite um valor para a lista: "))
while N != 0:
    achou = False
    if N >= LMin and N <= LMax:
        if N % X == 0:
            i = 0
            while i < len(L):
                if N == L[i]:
                    achou = True
                i += 1
                
            if achou:
                print("O valor já está na lista.")
            else:
                L.append(N)
                soma += N
                media = soma / len(L)
                
        else:
            print("O valor não é divisível por {}!".format(X))
    else:
        print("O valor não está dentro do intervalo fornecido.")

    N = int(input("Digite um valor para a lista: "))
    
print("\nA lista é:\n{}".format(L))
print("A lista tem {} elemento(s), a soma é: {} e a média é: {}.".format(len(L), soma, media))
print("\n\n Fim do programa!")
