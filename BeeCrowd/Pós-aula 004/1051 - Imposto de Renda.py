renda = float(input())
percent = 0
total = 0
if renda <= 2000:
    print('Isento')
elif renda <= 3000:
    percent = 8
    IRF = (renda-2000) * percent / 100
elif renda <= 4500:
    percent = 18
    IR1 = (renda-) * 8 / 100
    IR2 = (renda-3000) * 18 / 100
    IRF = IR1 + IR2
print("R$ %.2f" %IRF)
