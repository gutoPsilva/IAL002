from random import randint

print("Gustavo Pereira da Silva")
print("Vinicius Corrêa Carvalho")
print("Projeto 02 - Gerador de Senhas\n")

tipoSenha = input("Digite o tipo de senha: ")
while(tipoSenha != "a" and tipoSenha != "b" and tipoSenha != "c" and tipoSenha != "d" and tipoSenha != "e"):
  print("O tipo de senha deve ser um dos seguintes caracteres: a, b, c, d OU e.")
  tipoSenha = input("Digite o tipo de senha: ")

tamanhoSenha = int(input("Digite o comprimento da senha: "))
while(tamanhoSenha <= 0):
  print("A senha deve ter ao menos comprimento 1.")
  tamanhoSenha = input("Digite o comprimento da senha: ")

def geraCaracter(tipoPossivel):
  if tipoPossivel == 0: # Algarismos
      randomCaracter = randint(0, 9)   
  elif tipoPossivel == 1: # ASCII A-Z
      randomCaracter = chr(randint(65, 90)) # chr() converte o número para o caracter correspondente na tabela ASCII
  elif tipoPossivel == 2: # ASCII a-z
      randomCaracter = chr(randint(97,122))
  else: # ASCII caracteres especiais
      listEspecial = [45, 95, 58, 64, 35, 36, 38, 63]
      randomIndex = randint(0, 7)
      randomCaracter = chr(listEspecial[randomIndex])
  return randomCaracter

def geraSenha(Tipo, Tam):
  senha = ''
  while(len(senha) < Tam): 
    if (Tipo == "a"): # 0 - algarismo
      randomCaracter = geraCaracter(0) 

    elif(Tipo == 'b'): # 1 - maiuscula, 2 - minuscula
      randomCaracter = geraCaracter(randint(1, 2))

    elif(Tipo == 'c'): # 0 - algarismo, 1 - maiúscula
      randomCaracter = geraCaracter(randint(0, 1))
      
    elif(Tipo == 'd'): # 0 - algarismo, 1 - maiuscula, 2 - minuscula
      randomCaracter = geraCaracter(randint(0, 2))
      
    else: # 0 - algarismo, 1 - maiuscula, 2 - minuscula, 3 - especiais
      randomCaracter = geraCaracter(randint(0, 3))
      
    senha += str(randomCaracter)
  return senha

arqRM = open("MATR.TXT", "r")
arqSen = open("SENHAS.TXT", "w")

linhaRM = arqRM.readline().rstrip() # leitura do arquivo
while linhaRM != "":
  arqSen.write(linhaRM + ";" + geraSenha(tipoSenha, tamanhoSenha) + ";\n")
  linhaRM = arqRM.readline().rstrip()

arqSen.close()
arqRM.close()

print("\nSenhas geradas com sucesso! Verifique o arquivo 'SENHAS.TXT'")
print("\nFim do Programa.")