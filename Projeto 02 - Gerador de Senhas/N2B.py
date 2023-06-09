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

def geraSenha(Tipo, Tam):
  senha = ''
  while(len(senha) < Tam):
    randomCaracter = randint(0, 9) # sempre que tipoPossivel = 0 será usado esse randomCaracter dos algarismos, APENAS b vai alterar o randomCaracter quando o tipoPossivel for = 0 para ser maiúscula

    if(Tipo == 'b'): # ASCII A-z
      tipoPossivel = randint(0, 1) # 0 - maiuscula, 1 - minuscula
      
      if(tipoPossivel == 0): # maiúscula 
        randomCaracter = chr(randint(65, 90)) # chr() converte o número com o caracter correspondente da tabela ASCII
      else: # minúscula
        randomCaracter = chr(randint(97, 122))

    if(Tipo == 'c'):
      tipoPossivel = randint(0, 1) # 0 - algarismo, 1 - maiúscula
      if(tipoPossivel == 1): # minuscula
        randomCaracter = chr(randint(65, 90))
      
    if(Tipo == 'd'):
      tipoPossivel = randint(0, 2) # 0 - algarismo, 1 - maiuscula, 2 - minuscula
      if(tipoPossivel == 1):
        randomCaracter = chr(randint(65, 90))
      elif(tipoPossivel == 2):
        randomCaracter = chr(randint(97, 122))
      
    if(Tipo == 'e'):
      tipoPossivel = randint(0, 3) # 0 - algarismo, 1 - maiuscula, 2 - minuscula, 3 - especiais
      if(tipoPossivel == 1):
        randomCaracter = chr(randint(65, 90))
      elif(tipoPossivel == 2):
        randomCaracter = chr(randint(97, 122))
      elif(tipoPossivel == 3): # - 45 _ 95 : 58 @ 64 # 35 $ 36 & 38 ? 63
        listaEspecial = [45, 95, 58, 64, 35, 36, 38, 63]
        randomIndex = randint(0, 7)
        randomCaracter = chr(listaEspecial[randomIndex])

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