#Verificador de Positivo, Negativo ou Zero - 
# Peca um numero e classifique-o.

numero = int(input("informe um numero: "))

if numero > 0:
    print(f"O numero {numero} e positivo")
elif numero < 0:
    print(f"O numero {numero} e negativo")
else:
    print("O numero informado e zero")