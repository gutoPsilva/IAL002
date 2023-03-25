N = int(input())
totalC = 0
totalR = 0
totalS = 0
total  = 0
while N>0:
    entrada = input().split()
    Quantia = int(entrada[0])
    Tipo = str(entrada[1])
    if Quantia >= 1 and Quantia <=15:
        if Tipo == 'C':
            totalC += Quantia 
            total += Quantia
        elif Tipo == 'R':
            totalR += Quantia 
            total += Quantia
        elif Tipo == 'S':
            totalS += Quantia 
            total += Quantia
    N-=1
perC = totalC/total * 100
perR = totalR/total * 100
perS = totalS/total * 100
print("Total:", total, "cobaias")
print("Total de coelhos:", totalC)
print("Total de ratos:", totalR)
print("Total de sapos:", totalS)
print("Percentual de coelhos: %.2f" %perC, "%")
print("Percentual de ratos: %.2f" %perR, "%")
print("Percentual de sapos: %.2f" %perS, "%")
