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