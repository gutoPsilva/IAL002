n = int(input())

print(n)

n1 = n//100
n = n%100

n2 = n//50
n = n%50

n3 = n//20
n = n%20

n4 = n//10
n = n%10

n5 = n//5
n = n%5

n6 = n//2
n = n%2

print(n1, "nota(s) de R$ 100,00")
print(n2, "nota(s) de R$ 50,00")
print(n3, "nota(s) de R$ 20,00")
print(n4, "nota(s) de R$ 10,00")
print(n5, "nota(s) de R$ 5,00")
print(n6, "nota(s) de R$ 2,00")
print(n,  "nota(s) de R$ 1,00") # no fim, N já é o resto que não se enquadra em notas de 100 ou 2, logo apenas 1 real
