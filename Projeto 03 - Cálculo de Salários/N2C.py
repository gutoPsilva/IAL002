print("Gustavo Pereira da Silva")
print("Vinicius Corrêa Carvalho")
print("Projeto 03 - Cálculo de Salários\n")

arqSAL = open("SALARIO.TXT", "r")
arqCAL = open("CALCULOS.TXT", "w")

Salarios = []
salario = arqSAL.readline().rstrip()
while salario != '':
    Salarios.append(salario)
    salario = arqSAL.readline().rstrip()

def definirEspacamento(tipo, n = 'f'): # definir formatação de acordo com comprimento do maior salário ou dos títulos || caso n não seja fornecido, seu valor padrão é 'f'
    listAux = [] # lista cópia dos Salários para converter os itens em float e verificar qual o maior
    for salario in Salarios:
        listAux.append(float(salario))
    maiorComprimento = len(Salarios[listAux.index(max(listAux))]) # maior comprimento possivel vem do bruto,
    #1- pegar o index do maior salário float, 2 - ver qual o comprimento do item correspondente na lista de salarios
    # quando usada em strings, a função max retorna que '9' é maior que '89124.15', o que não é desejado
    # e quando convertemos salarios para float, os que terminam com .00 são reduzidos para .0, tirando 1 do len da string que também não é desejado

    espBruto  = 5 if maiorComprimento < 5 else maiorComprimento  # as colunas de tamanho variável devem ter um espaço mínimo que é o len do título ou o maiorComprimento possível caso passe do comprimento do título
    espBaseIR = 9 if maiorComprimento < 9 else maiorComprimento
    espVALIR  = 6 if maiorComprimento < 6 else maiorComprimento
    espLiqui  = 7 if maiorComprimento < 7 else maiorComprimento

    if tipo == 'num': # espacamento dos números, + pelo menos 2 espaços em branco nas colunas onde os números podem variar
        espacamento = '{:>' + str(espBruto + 2) + '.2f}{:>10.1f}{:>10.2f}{:>' + str(espBaseIR + 2) + '.2f}{:>8.1f}{:>'+ str(espVALIR + 2) +'.2f}{:>'+ str(espLiqui + 2) +'.2f}'
        if n == '\n': # adicionar quebra de linha quando for escrever no .txt
            espacamento = '\n' + espacamento
    else: # espacamento dos títulos
        espacamento = '{:>' + str(espBruto + 2) + '}{:>10}{:>10}{:>'+ str(espBaseIR + 2) + '}{:>8}{:>'+ str(espVALIR + 2) +'}{:>'+ str(espLiqui + 2) +'}'
    return espacamento

arqCAL.write(definirEspacamento('tit').format("Bruto", "AliqINSS", "Val.INSS", "Base I.R.", "AliqIR", "Val.IR", "Liquido"))
print(definirEspacamento('tit').format("Bruto", "AliqINSS", "Val.INSS", "Base I.R.", "AliqIR", "Val.IR", "Liquido"))

i = 0
while i < len(Salarios):
    SalBruto = float(Salarios[i])
    if SalBruto <= 1751.81: #Calculo do AliqINSS
        AliqINSS = 8.0
    elif SalBruto <= 2919.72:
        AliqINSS = 9.0
    elif SalBruto <= 5839.45:
        AliqINSS = 11.0
    else:
        AliqINSS = 0

    if SalBruto < 5839.46: #Calculo do VALINSS
        VALINSS = SalBruto * (AliqINSS/100)
        BaseIR = SalBruto - VALINSS
    else:
        VALINSS = 642.34
        BaseIR = SalBruto - VALINSS

    if BaseIR <= 1903.98: #Calculo da AliqIR e DeduçãoIR
        AliqIR = 0
        DeduçãoIR = 0
    elif BaseIR <= 2826.65:
        AliqIR = 7.5
        DeduçãoIR = 142.80
    elif BaseIR <= 3751.05:
        AliqIR = 15
        DeduçãoIR = 354.80
    elif BaseIR <= 4664.68:
        AliqIR = 22.5
        DeduçãoIR = 636.13
    else:
        AliqIR = 27.5
        DeduçãoIR = 869.36

    VALIRF = (SalBruto - VALINSS) * (AliqIR/100) - DeduçãoIR

    if VALIRF < 10:
        VALIR = 0
    else:
        VALIR = VALIRF

    SalLiquido = SalBruto - VALINSS - VALIR
    print(definirEspacamento('num').format(SalBruto, AliqINSS, VALINSS, BaseIR, AliqIR, VALIR, SalLiquido))
    arqCAL.write(definirEspacamento('num', '\n').format(SalBruto, AliqINSS, VALINSS, BaseIR, AliqIR, VALIR, SalLiquido))
    i += 1

arqCAL.close()
arqSAL.close()
