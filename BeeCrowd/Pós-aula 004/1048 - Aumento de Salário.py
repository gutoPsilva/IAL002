sal = float(input())
percent = 0
if sal<=400:
    percent = 15
elif sal<=800:
    percent = 12
elif sal<=1200:
    percent = 10
elif sal<=2000:
    percent = 7
else:
    percent = 4
reajuste = sal * percent / 100
sal += reajuste
print("Novo salario: %.2f" %sal)
print("Reajuste ganho: %.2f" %reajuste)
print("Em percentual:", percent, "%")
