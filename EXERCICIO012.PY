#Dias até o Fim do Ano - Peça uma data e calcule quantos dias faltam até o fim
#do ano.

from datetime import date 
data = date(input("Informe uma data: "))


resultado = data-301

print(f"falta {resultado} dias até o final do ano")


