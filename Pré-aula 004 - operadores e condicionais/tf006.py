nome = str(input("Digite o nome do lutador: "))
peso = float(input("Digite o peso do lutador: "))
if peso<65:
    print("O lutador " , nome, " pesa ", peso, "kg e se enquadra na categoria Pena.")
elif peso < 72:
    print("O lutador " , nome, " pesa ", peso, "kg e se enquadra na categoria Leve.")
elif peso < 79:
    print("O lutador " , nome, " pesa ", peso, "kg e se enquadra na categoria Ligeiro.")
elif peso < 86:
    print("O lutador " , nome, " pesa ", peso, "kg e se enquadra na categoria Meio médio.")
elif peso < 93:
    print("O lutador " , nome, " pesa ", peso, "kg e se enquadra na categoria Médio.")
elif peso <100:
    print("O lutador " , nome, " pesa ", peso, "kg e se enquadra na categoria Meio pesado.")
else:
    print("O lutador " , nome, " pesa ", peso, "kg e se enquadra na categoria Pesado.")
