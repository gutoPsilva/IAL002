N = int(input("Digite o Nº de termos: "))
P = int(input("Digite o primeiro termo: "))
R = int(input("Digite a razão: "))
cont = 1
soma = P # soma já recebe valor do primeiro termo, para que no while, some a partir do segundo termo. Ou exiba o único termo existente.
print(P)
while cont<N:
    cont+=1
    P = P * R
    soma += P
    print(P)
print('A soma dos termos é = %d' %soma)
