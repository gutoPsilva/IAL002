# Solução Nº1 receber dados linha por linha
lista = []
nmr = 0
while len(lista) < 10:
    n = int(input("Digite o elemento da posição {}: ".format(nmr+1)))
    lista.append(n)
    nmr += 1

i = -1 # index do último elemento
while i > -11: # até chegar no index do primeiro elemento
    print(lista[i])
    i -= 1

# Solução Nº2 receber dados numa linha e exibir numa linha
m = input("Digite 10 elementos separados por espaço: ")
lista1 = m.split()
while len(lista1) != 10:
    print("Você errou na digitação! Siga estritamente o que lhe foi pedido!")
    m = input("Digite 10 elementos separados por espaço: ")
    lista1 = m.split()
lista1.reverse()
print(lista1)

print("\n\nIsso é tudo pessoal.")
