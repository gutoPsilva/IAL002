def EPrimo(X):
    if X == 2:
        return True
    elif X % 2 == 0:
        return False
    else:
        raiz = X ** 0.5
        resto = 1
        i = 3
        while i <= raiz and resto != 0:
            if (X % i == 0):
                return False
            i = i + 2
        return True        

n = int(input("Digite N: "))
primos = []
candidato = 2
while len(primos) < n:
    if EPrimo(candidato):
        primos.append(candidato)
    candidato+=1

print(primos)

print("\n\n Isso e tudo pessoal.")

