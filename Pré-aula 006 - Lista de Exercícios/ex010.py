N = int(input("Digite N: "))
i = a = 0
b = 1
Prim = int(input("Digite Prim: "))
while i < N:
    if a > Prim:  
        print(a)
        i+=1 # só reduz o loop caso A seja maior que Prim, atendendo os N termos maiores que Prim
    c = a + b
    a = b
    b = c
