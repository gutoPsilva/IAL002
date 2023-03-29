A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
MaiorAB = (A+B+abs(A-B))/2 # ABS retorna o maior elemento
MaiorF = (MaiorAB+C+abs(MaiorAB-C))/2 # Pega o maior elementro entre A e B, e compara com C
print('%d' %MaiorF, 'eh o maior')
