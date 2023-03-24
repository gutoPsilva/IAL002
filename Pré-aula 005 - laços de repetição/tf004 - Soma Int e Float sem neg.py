nInt = int(input("Digite um número inteiro: "))
ini = 1
soma = nInt # daqui, basta somar os floats digitados no while. Poderiamos usar diretamente o nInt, mas acho mais didático criar uma variável separada para soma.
while ini!=0:
    nFlo = float(input("Digite números reais: "))
    if nFlo >= 0:
        soma += nFlo
        print("A soma até agora é = %f" %soma)
    else:
        print("Este algoritmo não soma negativos, a soma até agora é = %f" %soma)
