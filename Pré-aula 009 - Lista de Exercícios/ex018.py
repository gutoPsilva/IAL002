Min = int(input("Digite o mínimo: "))
Max = int(input("Digite o máximo: "))
while Max < Min:
    print("O máximo deve ser maior!")
    Min = int(input("Digite o mínimo: "))
    Max = int(input("Digite o máximo: "))
L = []
ini = True
while Min < Max: # inclui o minimo e o máximo
    if ini and Min % 7 == 0:
        Min+=1 # não considerar o primeiro valor se for 0
        ini = False
    if Min%7 == 0:
        L.append(Min)
    Min+=1
print("Divisíveis por 7 ENTRE os dois valores: \n{}".format(L))

print("\n\nIsso é tudo pessoal!")
