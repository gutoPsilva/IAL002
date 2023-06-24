print("Gustavo Pereira da Silva")
print("Vinicius Corrêa Carvalho")
print("Projeto 04 - Estoque Operacional\n")

arqProd = open("c1_produtos.txt", "r")
lisCodProd = []
lisEmEstoq = []
lisMinEsto = []
# dadosProd = [lisCodProd, lisEmEstoq, lisEmEstoq]

linha = arqProd.readline().rstrip()
while linha != '':
  dadoProd = linha.split(';')
  lisCodProd.append(dadoProd[0])
  lisEmEstoq.append(int(dadoProd[1]))
  lisMinEsto.append(int(dadoProd[2]))
  linha = arqProd.readline().rstrip()
arqProd.close()

arqVend = open("c1_vendas.txt", "r")
lisCodVend = []
lisQntVend = []
lisSitVend = []
lisCnlVend = []
# dadosVend = [lisCodVend, lisQntVend, lisSitVend, lisCnlVend]

linha = arqVend.readline().rstrip()
while linha!= '':
  dadoVend = linha.split(';')
  lisCodVend.append(dadoVend[0])
  lisQntVend.append(int(dadoVend[1]))
  lisSitVend.append(int(dadoVend[2]))
  lisCnlVend.append(int(dadoVend[3]))
  linha= arqVend.readline().rstrip()
arqVend.close()

# print(dadosProd)

# x = input('x: ')
# if x == 's':
#   y = 1
#   for item in dadosVend:
#     print("\nitem {}: {}\n".format(y, item))
#     y += 1

todosProd = []
i = 0
for cod in lisCodProd:
  linhaCod = []
  QtVendas = 0
  EstqPVendas = 0
  Necess = 0
  TransfPCO = 0
  j = 0
  for item in lisCodVend:
    if cod == item:
      QtVendas += lisQntVend[j] if lisSitVend[j] == 100 or lisSitVend[j] == 102 else 0
      EstqPVendas = lisEmEstoq[i] - QtVendas

      if(EstqPVendas < lisMinEsto[i] and EstqPVendas < 0):
        Necess = abs(EstqPVendas) + abs(lisMinEsto[i])
      elif(EstqPVendas < lisMinEsto[i]):
        Necess = lisMinEsto[i] - EstqPVendas
      
      TransfPCO = 10 if Necess > 1 and Necess < 10 else Necess

      linhaCod = [cod, lisEmEstoq[i], lisMinEsto[i], QtVendas, EstqPVendas, Necess, TransfPCO]
    j += 1
  todosProd.append(linhaCod)
  i += 1

for linha in todosProd:
  print('{}\n'.format(linha))

arqTRF = open("TRANSFERE.TXT", "w")

ini = True
for prod in todosProd:
  if ini:
    arqTRAF.write("Necessidade de Transferencia Armazem para CO\n\n")
    
    ini = False
  arqTRAF.write("{}, {}, {} \n".format(lisCOD[i], lisQntINI[i], lisQntMIN[i]))

# index dos cods invalidos para pegar seu valor e sua linha
# lisInvalidCodIndex = []
# for item in lisCodVend:
#   if item not in lisCodProd:
#     lisInvalidCodIndex.append(lisCodVend.index(item))

# for item in lisCodVend:
#   if item in lisCodProd:
#     itemIndex = lisCodVend.index(item)
#     lisQntVend[itemIndex]
#   else:
#     lisInvalidCod.append(item)
    # print(lisCodVend.index(item))

# for item in range (len(dadosVend)):
#   codVen = i[0]
#   if codVen in listCodProd:
#     print(i)

