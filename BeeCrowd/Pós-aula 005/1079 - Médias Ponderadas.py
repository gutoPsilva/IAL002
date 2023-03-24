N = int(input())
while N>0:
    X = input().split()
    l1 = float(X[0]) * 2
    l2 = float(X[1]) * 3
    l3 = float(X[2]) * 5
    mP = (l1 + l2 + l3) / 10
    print('%.1f' %mP)
    N-=1
