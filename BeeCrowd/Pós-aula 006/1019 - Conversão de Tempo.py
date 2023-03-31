N = int(input())
H = 0
M = 0
S = 0
if N/3600 >= 1:
    H = int(N/3600)
    N -= (H*3600)
if N/60 <= 59:
    M = int(N/60)
    N -= (M*60)
S = int(N)
print('{}:{}:{}'.format(H, M, S))
