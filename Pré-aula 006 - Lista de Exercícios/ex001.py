n = int(input())
mult = 1
while mult<11:
    res = mult * n
    print('{} x {:2d} = {}'.format(n, mult, res)) # 2 decimals no mult pq é até 10 fixo, os outros variam
    mult += 1
print('\n\nFim do Programa')
