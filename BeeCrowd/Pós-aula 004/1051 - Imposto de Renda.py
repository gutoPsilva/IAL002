renda = float(input())
if renda >= 0 and renda <= 2000:
    print('Isento')
elif renda <= 3000:
    resto = renda - 2000 # retira variação isenta, o que resta é cobrado IR
    IRF = (resto * 8) / 100
    print('R$ %.2f' %IRF)
elif renda <= 4500:
    resto = renda - 2000 # retira a variação isenta
    resto1 = resto - 1000 # retira 1000 referente ao cobrado pelo IR de 8%
    IRF = 1000 * 8 / 100 # 8% de IR cobrado
    IRF1 = resto1 * 18 / 100 # 18% de IR cobrado pelo que ultrapassa os 3000
    print("R$ %.2f" %(IRF+IRF1))
else:
    resto = renda - 2000
    resto1 = resto - 1000 # variação que cobra 8%
    resto2 = resto1 - 1500 # variação que cobra 18%
    IRF = 1000 * 8 / 100
    IRF1 = 1500 * 18 / 100
    IRF2 = resto2 * 28 / 100 # 28% de IR pelo que extrapola 4500
    print('R$ %.2f' %(IRF+IRF1+IRF2))
