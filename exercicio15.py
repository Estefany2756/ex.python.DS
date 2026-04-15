def maior_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

idade = int(input("Digite sua idade: "))

resultado = maior_idade(idade)
print(resultado)