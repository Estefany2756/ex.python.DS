id_vendedor = input ("Digite o ID do vendedor: ")
cod_peca = input ("Digite o código da peça: ")
preco_uni = float (input("Digite o valor da peça: "))
qtd = int (input("Digite a quantidade de peças vendidas: "))

total =  preco_uni * qtd
comissao = total * 0.05

print("ID do vendedor: ", id_vendedor)
print("Código da peça: ", cod_peca)
print("Valor total da venda: R$", total)
print("Comissão de 5%:R$", comissao)