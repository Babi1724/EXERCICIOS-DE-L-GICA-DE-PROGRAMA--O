#Calcular IMC - Peça peso e altura e calcule o Índice
#  de Massa Corporal (IMC).

peso = int(input("informe o peso: "))

altura = float(input("informe a altura: "))

IMC = peso/(altura*altura)

print("O IMC do peso e altura informado é: ",round(IMC))