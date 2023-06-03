N = int(input())
if N>1 and N<1000:
    saida = N * 2
    p1 = p2 = p3 = 1
    xP2 = 2
    xP3 = 6
    montantexP3 = 12
    verifica = True
    contP1 = 0
    while saida>0:
        print(p1, p2, p3)
        
        # padrão p1
        if contP1 < 1:
            contP1+=1
        else:
            p1 += 1 # +1 a cada 2 linhas
            contP1 = 0
            
        # padrão p2  1 - 2 - 1 - 4 - 1 - 6 - ...
        # padrão p3  1 - 6(xP3) - 1 - 18(xP3+12) - 1 - 36(xP3+18) - ...
        if verifica: 
            p2 += 1 # soma 1
            p3 += 1
            verifica = False
        else:
            p2 += xP2
            xP2 += 2 # soma 2 - 4 - 6 - ...
            
            p3 += xP3 # p3 recebe o total do ciclo.
            xP3 += montantexP3 # recebe o montante do ciclo
            montantexP3 += 6 # +6 ao montante por ciclo: 6, 12, 18
            verifica = True
        saida-=1
