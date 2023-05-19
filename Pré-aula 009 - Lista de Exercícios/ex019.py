# Ordenação por Inserção

L = []
X = int(input("Digite X: "))
while X > 0:
    i = 0
    while i < len(L) and L[i] < X: ## for menor que o len da lista e o valor for menor que os já inseridos,
        i+=1
    L.insert(i, X)
    X = int(input("Digite X: ")) # retoma toda a ação
print("Lista lida:\n{}".format(L))
