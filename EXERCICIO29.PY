#Calculo de Desconto Progressivo - Peca o valor de uma compra e aplique
#descontos de acordo com faixas de preco.

valor = int(input("informe um valor: "))

if valor <= 100:
    desconto = 0.05
elif valor <= 500:
    desconto = 0.10
else:
    desconto = 0.15

# Calcula o valor com desconto
valor_final = valor * (1 - desconto)

print("O valor final com desconto e: ",valor_final)
