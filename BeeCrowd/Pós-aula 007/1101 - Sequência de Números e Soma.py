ini = 1
while ini == 1:
    x = input().split()
    m = int(x[0])
    n = int(x[1])
    maior = max(m,n)
    menor = min(m,n)
    soma = 0
    linha = ''
    if maior <= 0 or menor <= 0: # encerra o processo
        ini = 0
    elif maior > menor:
        while maior >= menor:
            linha += str(menor) + ' '
            soma += menor
            menor += 1
        print("{}Sum={}".format(linha, soma))
