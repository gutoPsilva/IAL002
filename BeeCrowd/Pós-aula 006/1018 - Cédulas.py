n = int(input())
print(n)
while n != 0 and n<1000000:
    n1 = n//100
    n -= n1 * 100
    n2 = n//50
    n -= n2 * 50
    n3 = n//20
    n -= n3 * 20
    n4 = n//10
    n -= n4 * 10
    n5 = n//5
    n -= n5 * 5
    n6 = n//2
    n -= n6 * 2
    n7 = n//1
    n -= n7 * 1    
print(n1,'nota(s) de RS 100,00')
print(n2,'nota(s) de RS 50,00')
print(n3,'nota(s) de RS 20,00')
print(n4,'nota(s) de RS 10,00')
print(n5,'nota(s) de RS 5,00')
print(n6,'nota(s) de RS 2,00')
print(n7,'nota(s) de RS 1,00')
