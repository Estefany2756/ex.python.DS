custo_carro = float(input("Digite o custo do carro: "))

imp = custo_carro * 0.05
total_imp = custo_carro + imp
lucro = total_imp * 0.12
final = lucro + total_imp

print("Valor de impostos:R$", imp)
print("Lucro do distribuidor:R$", lucro)
print("Preço final:R$", final)