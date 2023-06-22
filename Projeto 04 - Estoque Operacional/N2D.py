print("Gustavo Pereira da Silva")
print("Vinicius Corrêa Carvalho")
print("Projeto 04 - Estoque Operacional\n")

arqProd = open("c1_produtos.txt", "r")
codProd = []
estProd = []
minProd = []
dadosProd = []

linha = arqProd.readline().rstrip()
while linha != '':
  dadosProd.append(linha.split(';'))
  linha = arqProd.readline().rstrip()
arqProd.close()

print(dadosProd)

arqVend = open("c1_vendas.txt", "r")
dadosVend = []

linha = arqVend.readline().rstrip()
while linha!= '':
  dadosVend.append(linha.split(';'))
  linha= arqVend.readline().rstrip()
arqVend.close()



# arqTRAF = open("TRANSFERE.TXT", "w")
# for i in range (len(lisCOD)):
#   if i == 0:
#     arqTRAF.write("Necessidade de Transferencia Armazem para CO\n\n")
#   arqTRAF.write("{}, {}, {} \n".format(lisCOD[i], lisQntINI[i], lisQntMIN[i]))