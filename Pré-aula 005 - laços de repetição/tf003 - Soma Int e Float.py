nInt = int(input("Digite um número inteiro: "))
ini = 1
soma = nInt # daqui, basta somar os floats digitados no while. Poderiamos usar diretamente o nInt, mas acho mais didático criar uma variável separada para soma.
while ini != 0:
    nRea = float(input("Digite números reais: "))
    soma += nRea
    print('A soma até aqui é = %f' %soma)
