#Maior de Dois - Peça dois números e exiba o maior deles.

num1 = int(input("Informe o primeiro numero: "))

num2 = int(input("Informe o segundo numero: "))

if(num1>num2):
    print(f"O número{num1} é o maior")

if(num2>num1):
    print(f"O número {num2} é o maior")

else:
    print(f"Nenhum dos dois números é o maior")