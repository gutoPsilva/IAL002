cont = 1
pos = 0
XM = 0
while cont<=10:
    X = int(input())
    if XM < X:
        XM = X
        pos = cont
    cont+=1
print(XM)
print(pos)
