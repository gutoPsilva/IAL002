print("Gustavo Pereira da Silva")
print("Vinicius Corrêa Carvalho")
print("Projeto 04 - Estoque Operacional\n")

arqProd = open("c1_produtos.txt", "r")
lisCodProd = []
lisEmEstoq = []
lisMinEsto = []

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

linha = arqVend.readline().rstrip()
while linha!= '':
  dadoVend = linha.split(';')
  lisCodVend.append(dadoVend[0])
  lisQntVend.append(int(dadoVend[1]))
  lisSitVend.append(int(dadoVend[2]))
  lisCnlVend.append(int(dadoVend[3]))
  linha= arqVend.readline().rstrip()
arqVend.close()

# estas variáveis servem apenas para definir o espaçamento das colunas na função lá embaixo
compEstPV = 9 # 9 digitos, comprimento equivalente ao título
compNeces = 7 # 7 digitos
compTRF = 10 # 10 digitos

# quantidade de vendas por canal
representantesV = 0
websiteV = 0
mobAndroidV = 0
mobIphoneV = 0

todosProd = []
i = 0
totDiv = []
for cod in lisCodProd:
  linhaCod = []
  QtVendas = 0
  EstqPVendas = 0
  Necess = 0
  TransfPCO = 0
  j = 0

  for item in lisCodVend:
    if cod == item:
      if lisSitVend[j] == 100 or lisSitVend[j] == 102:
        QtVendas += lisQntVend[j]
        EstqPVendas = lisEmEstoq[i] - QtVendas

        if(EstqPVendas < lisMinEsto[i] and EstqPVendas < 0):
          Necess = abs(EstqPVendas) + abs(lisMinEsto[i])
        elif(EstqPVendas < lisMinEsto[i]):
          Necess = lisMinEsto[i] - EstqPVendas
        
        TransfPCO = 10 if Necess > 1 and Necess < 10 else Necess
        linhaCod = [cod, lisEmEstoq[i], lisMinEsto[i], QtVendas, EstqPVendas, Necess, TransfPCO]
        
        if len(str(EstqPVendas)) > compEstPV: compEstPV = len(str(EstqPVendas))
        if len(str(Necess)) > compNeces: compNeces = len(str(Necess))
        if len(str(TransfPCO)) > compTRF: compTRF = len(str(TransfPCO))

      elif lisSitVend[j] == 135:
        totDiv.append(str(j+1) + " - Venda cancelada")
      elif lisSitVend[j] == 190:
        totDiv.append(str(j+1) + " - Venda não finalizada")
      else: # só resta o código 999, erro desconhecido
        totDiv.append(str(j+1) + " - Erro desconhecido. Acionar a equipe de TI.")
    
    else:
      if lisSitVend[j] == 100 or lisSitVend[j] == 102:
        if lisCnlVend[j] == 1: 
          representantesV += lisQntVend[j]
        elif lisCnlVend[j] == 2:
          websiteV += lisQntVend[j]
        elif lisCnlVend[j] == 3:
          mobAndroidV += lisQntVend[j]
        else: # só resta o código 4, do iPhone
          mobIphoneV += lisQntVend[j]
    j += 1
  todosProd.append(linhaCod)
  i += 1

# todas as colunas exceto a de produto possuem comprimentos variáveis, para definir seu espaçamento basta medir o comprimento do maior inteiro daquela coluna, ou usar o próprio titulo como comprimento + 2 espaços em branco para distancia-los
def espacoMin(lista, tamTit):
  valorMax = int('9' * tamTit)
  if max(lista) > valorMax:
    espaco = len(str(max(lista)))
  else:
    espaco = tamTit
  return espaco + 2

def formatacao():
  compQtCO  = espacoMin(lisEmEstoq, 4)
  compQtMin = espacoMin(lisMinEsto, 5)
  compQtVen = espacoMin(lisQntVend, 8)
  # o comprimento das outras 3 colunas já foi definido anteriormente, mas sem considerar os 2 espaços em branco
  espacamento = "{:<7}{:>" + str(compQtCO) + "}{:>" + str(compQtMin) + "}{:>" + str(compQtVen) + "}{:>" + str(compEstPV+2) + "}{:>" + str(compNeces+2) + "}{:>" + str(compTRF+2) + "}\n"
  return espacamento

arqTRF = open("TRANSFERE.TXT", "w")
ini = True
for prod in todosProd:
  if ini:
    arqTRF.write("Necessidade de Transferência Armazém para CO\n\n")
    arqTRF.write(formatacao().format("Produto", "QtCO", "QtMin", "QtVendas", "Estq.após", "Necess.", "Transf. de"))
    arqTRF.write(formatacao().format("", "", "", "", "Vendas", "", "Arm p/ CO"))
    ini = False
  arqTRF.write(formatacao().format(prod[0], prod[1], prod[2], prod[3], prod[4], prod[5], prod[6]))
arqTRF.close()

# index dos cods invalidos para pegar seu valor e sua linha
i = 0
while i < len(lisCodVend):
  if lisCodVend[i] not in lisCodProd:
    totDiv.append(str(i+1) + " - Código de Produto não encontrado " + lisCodVend[i])
  i += 1

def printar(texto, qntd):
  return arqTOTCN.write("{:<21}{:>10}\n".format(texto, qntd))

arqTOTCN = open("TOTCANAIS.TXT", "w")
arqTOTCN.write("Quantidades de Vendas por canal\n\n")
printar("Canal", "QtVendas")
printar("1 - Representantes", representantesV)
printar("2 - Website", websiteV)
printar("3 - App movel Android", mobAndroidV+1)
printar("4 - App movel iPhone", mobIphoneV)
arqTOTCN.close()

# ordDiv = []
# arqDIV = open("DIVERGENCIAS.TXT", "w")

# for div in totDiv:
#   separar = div.split()
#   nmLinha = int(separar[0])
#   ordDiv.append(nmLinha)

# def myFunc(nmbr):
  

# ordDiv.sort(key=myFunc)
# print(ordDiv)
# print(totDiv)

# for item in ordDiv:
#   arqDIV.write("Linha " + "\n")
# arqDIV.close()
# for i in range(len(totDiv)):
#   separar = totDiv[i].split()
#   nmLinha = int(separar[0])
#   xDiv.append(nmLinha)
#   xDiv.sort()

# ordDiv = []
# i = 0
# while i < len(totDiv):
#   separar = totDiv[i].split()
#   nmLinha = int(separar[0])
#   ordDiv.append(nmLinha)
#   ordDiv.sort()
#   i+=1

