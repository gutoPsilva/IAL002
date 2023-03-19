A = float(input("Digite o número A: "))
B = float(input("Digite o número B: "))
C = float(input("Digite o número C: "))

delta = (B**2) - (4*A*C)
if delta > 0:
    x1 = (-B + (delta**0.5)) / (2*A)
    x2 = (-B - (delta**0.5)) / (2*A)
    print("As raízes são: ", x1 , "e" , x2)
elif delta == 0:
    x = (-B + (delta**0.5)) / (2*A)
    print("A única raíz existente é:" , x)
else:
    print("Não há raízes reais.")
