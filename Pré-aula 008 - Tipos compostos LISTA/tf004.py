#  Solução Nº1, inserir dados linha a linha
print("Solução Nº1\n")
lista1 = []
lista2 = []
nmr = 0
print("Primeira Lista!\n")
while len(lista1) < 10:
    n = int(input("Digite o inteiro de posição {}: ".format(nmr+1)))
    lista1.append(n)
    nmr += 1
print("\nSegunda lista! \n")
nmr = 0 # reiniciarr o contador
while len(lista2) < 10:
    m = int(input("Digite o inteiro de posição {}: ".format(nmr+1)))
    lista2.append(m)
    nmr += 1
print("\nAs duas listas juntas formam: \n{}".format(lista1 + lista2))


# solução Nº2, inserir dados numa linha só
# PROVÁVEL DO USUÁRIO SER TEIMOSO E COLOCAR LETRAS AO INVÉS DE NÚMEROS --> erro
print("\n\nSolução Nº2\n")
n = input("Digite 10 inteiros separados por espaço: ")
Lista1 = n.split()
while len(Lista1) != 10:
    print("Você errou na digitação! Siga estritamente o que lhe foi pedido!")
    n = input("Digite 10 inteiros separados por espaço: ")
    Lista1 = n.split()
    
m = input("\nDigite MAIS 10 inteiros separados por espaço: ")
Lista2 = m.split()
while len(Lista2) != 10:
    print("Você errou na digitação! Siga estritamente o que lhe foi pedido!")
    m = input("Digite MAIS 10 inteiros separados por espaço: ")
    Lista2 = m.split()

i = 0
while i<10: # converter os valores de string para int
    Lista1[i] = int(Lista1[i])
    Lista2[i] = int(Lista2[i])
    i += 1

print("\nAs duas listas unidas formam:\n{}".format(Lista1+Lista2))
print("\n\nIsso é tudo pessoal.")
