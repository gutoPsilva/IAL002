tempo = int(input("Digite a quantidade de segundos: "))
horas = 0
while(tempo >= 3600):
  tempo -= 3600
  horas+=1

minutos = 0
while(tempo>=60):
  tempo -= 60
  minutos += 1

segundos = tempo
print("\n{} hora(s), {} minuto(s) e {} segundo(s)".format(horas, minutos, segundos))
print("\n\n Fim do programa.")