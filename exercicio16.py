def total_pagar(valor, quantidade):
    return valor * quantidade

valor = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade: "))

total = total_pagar(valor, quantidade)
print("Total a pagar:", total)