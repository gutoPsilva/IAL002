N = int(input('Digite um valor: '))
media = soma = 0
qntd = 0 # posição = quantidade de elementos
while N>0:
    soma += N
    qntd += 1 # entrada de um novo valor, posição nova
    media = soma / qntd
    if qntd==1 or N>maior: # recebe o primeiro elemento, depois compara o novo elemento
        maior = N
    if qntd==1 or N<menor:
        menor = N
    N = int(input('Digite um valor: '))
    
if qntd>0: # dados fornecidos
    print("O menor elemento é: {}, o maior é: {}".format(menor, maior))
    print("A soma total é: {}".format(soma))
    print("A média é: {}".format(media))
    print("A quantidade de elementos é: {}".format(qntd))
else:
    print("Dados não foram fornecidos.")

print("\n\nFim do Programa")
