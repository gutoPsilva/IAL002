print("Gustavo Pereira da Silva")
print("Vinicius Corrêa Carvalho")
print("Questão 03\n")

totalVarejo = 0
totalAtacado = 0
i = 0
NV = int(input("Digite o número de vendas realizadas: "))

while NV <= 0:
    print("O número de vendas precisa ser maior que zero!: ")
    NV = int(input("Digite o número de vendas realizadas: "))

while i < NV:
    codqv = input("Digite o código do produto e a quantidade de vendas: ").split()
    Cod = int(codqv[0])
    QV = int(codqv[1])

    if Cod == 16:
        precov = 14.35
        precoa = 12.93
        if QV >= 50:
            totalAtacado = totalAtacado + QV * precoa
        else:
            totalVarejo = totalVarejo + QV * precov
        i = i + 1

    elif Cod == 23:
        precov = 35.12
        precoa = 29.85
        if QV >= 100:
            totalAtacado = totalAtacado + QV * precoa
        else:
            totalVarejo = totalVarejo + QV * precov
        i = i + 1

    elif Cod == 27:
        precov = 19.35
        precoa = 16.76
        if QV >= 70:
            totalAtacado = totalAtacado + QV * precoa
        else:
            totalVarejo = totalVarejo + QV * precov
        i = i + 1

    elif Cod == 34:
        precov = 63.40
        precoa = 58.25
        if QV >= 40:
            totalAtacado = totalAtacado + QV * precoa
        else:
            totalVarejo = totalVarejo + QV * precov
        i = i + 1
    else:
        print("Código inválido")

vendast = totalVarejo+totalAtacado

print("\nTotal de Vendas do Grupo Varejo: R$ %.2f" % totalVarejo)
print("Total de Vendas do Grupo Atacado: R$ %.2f" % totalAtacado)
print("\nVendas Totais: R$%.2f" % vendast)

print("\n\nFim do Programa.")
