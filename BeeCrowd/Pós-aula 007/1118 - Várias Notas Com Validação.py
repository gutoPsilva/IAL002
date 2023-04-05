n = 1 # o programa inicia levando em conta o primeiro cenário.
ini = 1
while ini == 1: # laço ini em ação para encerrar o processo todo somente quando 2 for digitado.
    if n == 1: # iniciar/proseguir
        cont  = 0
        media = 0
        nota = float(input()) # valor inicial
        while cont<2: # insistir até ter 2 notas válidas
            if nota>=0 and nota<=10:
                media += nota/2
                cont+=1 # soma apenas se a nota for válida
                if cont<=1: # garante que não haja um terceiro input
                    nota = float(input())
            else:
                print('nota invalida')
                nota = float(input())
        print('media = %.2f' %media)
        if cont == 2: # após contabilizar 2 notas e exibir a média, pergunte se quer continuar ou não o programa.
            print('novo calculo (1-sim 2-nao)')
            n = int(input())
    while n != 1 and n != 2: # insistir até que 1 ou 2 sejam digitados
            print('novo calculo (1-sim 2-nao)')
            n = int(input())
    if n == 2: # fecha o laço geral
        ini = 0
