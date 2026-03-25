nome =input("Digite o nome do jogador: ")
salario = float(input("Digite seu salario atual: "))

if salario <= 1000:
    reajuste = salario * 0.20
elif salario <= 5000:
    reajuste = salario * 0.10
else:
    reajuste = salario * 0.05

novo_salario= salario + reajuste
print("Nome: ", nome)
print("Novo salário:R$", novo_salario)    