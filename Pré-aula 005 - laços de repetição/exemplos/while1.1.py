P = int(input("Digite o primeiro termo: "))
R = int(input("Digite a razão: "))
Q = int(input("Quantidade de elementos: "))
cont = 0
total = 0
while cont<Q:
    print('Termo ', cont+1, 'da PA = ', P)
    total += P
    P += R
    cont += 1
print('Soma dos termos:' , total)
