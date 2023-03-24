N = int(input())
vIn = 0
vOu = 0
while N>0:
    X = int(input())
    if X>=10 and X<=20:
        vIn += 1
    else:
        vOu +=1
    N-=1
print(vIn, 'in')
print(vOu, 'out')
