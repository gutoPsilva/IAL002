Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b = 15
>>> c = 4
>>> a < b and a < c
False
>>> a < b or a < c
True
>>> a = 1
>>> b = 9
>>> c = 0
>>> a >= 0 and b == c
False
>>> c = 9
>>> a >= 0 and b == c
True
>>> c = 0
>>> a >= 0 or b == c
True
>>> c = 9
>>> a >=0 or b ==c
True
>>> a = 0
>>> b = 0
>>> c = 0
>>> b != 0 and a != c
False
>>> c = 25
>>> b!=0 and a != c
False
>>> c = 0
>>> b != 0 or a != c
False
>>> c = 25
>>> b != 0 or a != c
True
