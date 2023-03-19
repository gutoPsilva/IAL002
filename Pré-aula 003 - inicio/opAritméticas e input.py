Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
base = 9
altura = 6
area = (9*6) / 2
print(area)
27.0

>>> hora = 14.25
>>> horaNormal = hora * 163
>>> horaExtra = 20 * (hora*2)
>>> salBruto = horaNormal + horaExtra
>>> print(salBruto)
2892.75
>>> 
>>> a = 4
>>> b = 5
>>> c = 1
>>> r = (a+b) / 2
>>> print(r)
4.5
>>> 
>>> r = (3*a + 2*b) / (a+b)
>>> print(r)
2.4444444444444446
>>> 
>>> delta = (b**2 - 4*a*c) ** (1/2)
>>> x = (-b + delta) / (2*a)
>>> print(x)
-0.25
>>> 
>>> z = (7.6*a) - (b**1.7)
>>> print(z)
14.974153431999758
>>> 
>>> nome = input('Digite seu nome: ')
Digite seu nome: Gustavo Pereira da Silva
>>> print('Seu nome e: ' , nome)
Seu nome e:  Gustavo Pereira da Silva
>>> 
>>> numero = input('Digite um número inteiro: ')
Digite um número inteiro: 9
>>> print('O número digitado foi: ', numero)
O número digitado foi:  9
>>> 
>>> numero = int(input('Digite um número INTEIRO:'))
Digite um número INTEIRO:9.5
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    numero = int(input('Digite um número INTEIRO:'))
ValueError: invalid literal for int() with base 10: '9.5'
