print("Gustavo Pereira da Silva")
print("Vinicius Corrêa Carvalho")
print("Projeto 01 - Totalização Simples de Vendas de Produtos\n")

listaus = [] # armazena os codigos consultados não presentes no arquivo de texto mas dentro do intervalo
listinval = [] # armazena os códigos inválidos do arquivo de texto, ou seja, códigos fora do intervalo
listcod = [] # armazena todos os códigos válidos lidos
listquant = [] # armazena todos as quantidades de venda lidas
listvalor = [] # armazena todos os valores unitários lidos
arq = open("vendas.txt", "r")
linha = arq.readline().rstrip()
while linha != "":
    dados = linha.split(";")
    cod = int(dados[0])
    quant = int(dados[1])
    valor = float(dados[2])
    if cod >= 10000 and cod <= 21000: # se o código do arquivo for válido, basta adicionar os dados válidos nas respectivas listas
        listcod.append(cod)
        listquant.append(quant)
        listvalor.append(valor)
    else:
        listinval.append(cod)
    linha = arq.readline() .rstrip()
arq.close()

N = int(input("Digite o código a ser consultado: "))
while N != 0:
    if N < 10000 or N > 21000:
        print("{} Código inválido (deve ser entre 10000 e 21000)".format(N))
    else: # se estiver dentro do intervalo
        i = 0 # zera a variável para uma nova consulta
        total = 0 # zera a variável para uma nova consulta
        if N in listcod: # E se o código consultado está na lista de códigos válidos
            while i < len(listcod):
                if N == listcod[i]:
                    total = total + listvalor[i]*listquant[i] # soma o valor total de todas suas aparições, utilizando o i que é semelhante em todas as listas
                i = i + 1
            print("Total vendido do produto {} = R$ {:.2f}".format(N, total))
        else: # se o código não estiver na lista, significa que ele está dentro do intervalo mas não foi fornecido no arquivo de entrada, logo é ausente
            if N not in listaus:
                listaus.append(N)
            print("Total vendido do produto {} = R$ 0.00".format(N))

    N = int(input("\nDigite o código a ser consultado: "))

if len(listaus):
    print("\nForam consultados {} código(s) ausente(s) do arquivo de texto:".format(len(listaus)))
    print(listaus)

if len(listinval):
    print("\nForam consultados {} código(s) inválido(s) (fora do intervalo definido):".format(len(listinval)))
    print(listinval)

print("\n\nFim do Programa")