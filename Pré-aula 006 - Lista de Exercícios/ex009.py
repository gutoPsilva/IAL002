N = int(input("Digite N: "))
i = a = 0
b = 1
while i < N:
    print(a)
    c = a + b # gera terceiro valor, que é o NOVO segundo
    a = b # A recebe o NOVO PRIMEIRO valor
    b = c # B recebe o NOVO SEGUNDO valor
    i+=1
    
