Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A = 10
>>> B = 15
>>> C = 4
>>> A < B and A < C or C != 0
True
>>> A < B and (A < C or C != 0)
True
>>> A = 1
>>> B = 9
>>> C = 0
>>> not (A >= 0 and B == C)
True
>>> C = 9
>>> not (A >= 0) and not (B == C)
False
>>> C = 0
>>> (A >= 0 or B == C) and B > A
True
