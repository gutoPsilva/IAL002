l1 = float(input("Digite o lado 1 do triângulo: "))
l2 = float(input("Digite o lado 2 do triângulo: "))
l3 = float(input("Digite o lado 3 do triângulo: "))
if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    if l1 == l2 and l2 == l3:
        tipo = "Equilátero."
        print("É um triângulo" , tipo)
    elif l1 == l2 or l1 == l3 or l2 == l3:
        tipo = "Isósceles."
        print("É um triângulo" , tipo)
    else:
        tipo = "Escaleno."
        print("É um triângulo" , tipo)
else:
    print("Não é um triângulo.")
