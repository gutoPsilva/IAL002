print("Gustavo Pereira da Silva")
print("Vinicius Corrêa Carvalho")
print("Projeto 04 - Estoque Operacional\n")

arqProd = open("c1_produtos.txt", "r")
lisCodProd = []
lisEmEstoq = []
lisMinEsto = []
dadosProd = [lisCodProd, lisEmEstoq, lisEmEstoq]

linha = arqProd.readline().rstrip()
while linha != '':
  dadoProd = linha.split(';')
  lisCodProd.append(int(dadoProd[0]))
  lisEmEstoq.append(int(dadoProd[1]))
  lisMinEsto.append(int(dadoProd[2]))
  linha = arqProd.readline().rstrip()
arqProd.close()



arqVend = open("c1_vendas.txt", "r")
lisCodVend = []
lisQntVend = []
lisSitVend = []
lisCnlVend = []
dadosVend = [lisCodVend, lisQntVend, lisSitVend, lisCnlVend]

linha = arqVend.readline().rstrip()
while linha!= '':
  dadoVend = linha.split(';')
  lisCodVend.append(int(dadoVend[0]))
  lisQntVend.append(int(dadoVend[1]))
  lisSitVend.append(int(dadoVend[2]))
  lisCnlVend.append(int(dadoVend[3]))
  linha= arqVend.readline().rstrip()
arqVend.close()

print(dadosProd)

x = input('sex: ')
if x == 's':
  y = 1
  for item in dadosVend:
    print("\nitem {}: {}\n".format(y, item))
    y += 1

lisNotInList = []
for item in lisCodVend:
  if item in lisCodProd:

  else:
    lisNotInLst.append(item)

# for item in range (len(dadosVend)):
#   codVen = i[0]
#   if codVen in listCodProd:
#     print(i)


# arqTRAF = open("TRANSFERE.TXT", "w")
# for i in range (len(lisCOD)):
#   if i == 0:
#     arqTRAF.write("Necessidade de Transferencia Armazem para CO\n\n")
#   arqTRAF.write("{}, {}, {} \n".format(lisCOD[i], lisQntINI[i], lisQntMIN[i]))