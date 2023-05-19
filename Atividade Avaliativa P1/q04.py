print("Gustavo Pereira da Silva")
print("Vinicius Corrêa Carvalho")
print("Questão 04\n")

N = int(input("Digite o valor de N: "))
if N < 5 or N > 49 or N%2 == 0:
    print("O número {} é inválido".format(N))
else:
    i = 1
    espacamento = N / 2 - 0.5
    print()
    while i <= N:
        print(' ' * int(espacamento) + '*' * i)
        espacamento -= 1
        i+=2
    print(' ' * int(N / 2 - 0.5) + '|')
    print(' ' * int(N / 2 - 1) + '---')

print("\n\nFim do Programa.")
