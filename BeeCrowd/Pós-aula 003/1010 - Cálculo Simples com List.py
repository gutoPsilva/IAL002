linha = input().split()
linha2 = input().split()

a1 = int(linha[1])
a2 = float(linha[2])
b1 = int(linha2[1])
b2 = float(linha2[2])

total = a1 * a2 + b1 * b2
print("VALOR A PAGAR: R$ %.2f" %total)
