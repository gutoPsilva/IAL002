from random import randint
nA = randint(1,15)
nB = randint(1,15)
while nA == nB:
    nB = randint(1,10)
nR = nA + nB

i = 0
A = []
B = []
R = []
while i < nA:
    x = randint(0,100)
    A.append(x)
    i += 1
i = 0

while i < nB:
    x = randint(0,100)
    B.append(x)
    i += 1
R = A + B
print("nA = {}, lista:\n{}".format(nA, A))
print("nB = {}, lista:\n{}".format(nB, B))
print("nR = {}, lista:\n{}".format(nR, R))
