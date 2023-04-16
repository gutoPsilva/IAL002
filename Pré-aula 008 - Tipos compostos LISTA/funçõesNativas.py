# append() aceita colocar apenas 1 valor por vez, no final da lista.
nums = ["um"]
nums.append("dois")
nums.append("três")
nums.append("quatro")
print(nums)

# index() retorna o index do valor do elemento pesquisado.
animals = ["ant", "bat", "cat"]
print("Index do bat: {}".format(animals.index("bat")))  # retorna o index do elemento "bat", que é 1

# caso não haja um elemento com esse valor, ocorrerá um erro.
# para evitar erros exibidos ao usuário, UTILIZE O IN

x = "dog" in animals # retorna um valor booleano, se "valor" estiver na lista
y = "cat" in animals
print(x, y)

# insert() inserir em determinado index SEM EXCLUIR
animals.insert(1, "dog") #insere "dog" na posição 1 sem excluir "bat"
print(animals)

# remove() remove apenas 1 elemento baseado no seu valor,
# REMOVE apenas o 1º QUE APARECER e caso ñ exista, ERRO É EXIBIDO IGUAL O INDEX()
animals.remove("dog")
print(animals)

# pop() remove baseando-se no índice e retorna o valor do elemento removido.
z = animals.pop(0) # ant
print("{} foi removido da lista {}".format(z, animals))

# del() remove pelo index e não retorna nada.
del(animals[0]) # bat
print(animals,"\n\n")

# sort() organiza a lista mas NÃO A RETORNA, É NECESSÁRIO PRINTAR A LISTA, NÃO O MÉTODO
lista = ["c", "b", "a"]
print(lista)

lista.sort() # organiza a lista em crescente baseado no ASCII ou valor numérico
print("Lista organizada: {}".format(lista))

# podemos usar o sort([valores]) para organizar valores inseridos naquele momento
# O SORTED RETORNA A LISTA, ENTÃO PODEMOS UTILIZALO NO PRINT
print(sorted([5, 2, 3, 1, 4]))


