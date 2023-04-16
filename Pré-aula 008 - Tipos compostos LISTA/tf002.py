n = int(input("Digite um valor inteiro: "))
lista = []
while n > 0:
    lista.append(n)
    n = int(input("Digite um valor inteiro: "))

print("Método for:")
for elemento in lista:
    print(elemento)

# ou

i = 0
print("Método while:")
while i<len(lista): # enquanto i for menor q a qntd de elementos
    print(lista[i])
    i+=1
