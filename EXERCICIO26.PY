#Verificador de Positivo, Negativo ou Zero - 
# Peça um número e classifique-o.

numero = int(input("informe um numero: "))

if numero > 0:
    print(f"O número {numero} é positivo")
elif numero < 0:
    print(f"O número {numero} é negativo")
else:
    print("O número informado é zero")