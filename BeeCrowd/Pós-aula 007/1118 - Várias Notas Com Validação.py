nota = float(input())
cont = 0
media = 0
while cont<2:
    if nota>=0 and nota<=10:
        media += nota/2
        cont+=1
        if cont<= 1: # após 2 entradas corretas ele aguarda uma terceira que não altera o valor, esse if previne isso.
            nota = float(input())
    else:
        print('nota invalida')
        nota = float(input())
print('media = %.2f' %media)

print('novo calculo (1-sim 2-nao)')
n = int(input())
if n == 1:
    while n == 1:
        cont  = 0
        media = 0
        nota = float(input())
        while cont<2:
            if nota>=0 and nota<=10:
                media += nota/2
                cont+=1
                if cont<= 1: # após 2 entradas corretas ele aguarda uma terceira que não altera o valor, esse if previne isso.
                    nota = float(input())
            else:
                print('nota invalida')
                nota = float(input())
        print('media = %.2f' %media)
        if cont == 2:
            print('novo calculo (1-sim 2-nao)')
            n = int(input())
elif n != 2:
    print('novo calculo (1-sim 2-nao)')
    n = int(input())

