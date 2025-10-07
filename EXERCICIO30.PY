#Classificador de Idade - Peça a idade e informe se a pessoa é criança,
#adolescente, adulta ou idosa.

idade = int(input("informe uma idade: "))

if idade<=10:
    print("E crianca")

if idade <=17:
    print("E adolescente")

if idade<=50:
    print(" E adulto ")

else:
    print( " E idoso")