# ADICIONAR/ALTERAR VALORES #
# alterando valor pelo Index
L = [7, 17, 27, 37]
print(L)
L[1] = 123
print("Alterando valor do index 1:\n{}".format(L))

# acrescentando elemento
L.append(47)
print("Lista após .append:\n{}".format(L))

# acrescentando elemento numa posição específica, SEM EXCLUIR
L.insert(3, 99)
print("Inserindo elementos em posição específica com .insert:\n{}".format(L))

# COPIANDO LISTAS #

# se fizer L2 = L, ambos são considerados como a mesma coisa, então qql alteração afeta ambos.
# NÃO É CÓPIA!

L2 = L[:] # desse modo, ambas possuem os mesmos valores mas são distintas.

# JUNTANDO LISTAS #

m = [1, 2, 3]
n = [4, 5, 6]
o = m + n
print("juntando listas numa só: \n{}".format(o))
