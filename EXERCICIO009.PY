#Conversor de Idade - Peça a idade em anos e exiba em meses e dias


idade_em_anos = int(input("informe a sua idade em anos: "))


meses = idade_em_anos * 12
dias = idade_em_anos * 365

print(f"A idade em anos {idade_em_anos}  em dias é: ",dias)
print(f"A idade em anos {idade_em_anos} em meses é: ",meses)