#Tabuada - Peça um número e exiba a tabuada dele (de 1 a 10).

num1 = int(input("Informe o primeiro numero: "))

for i in range(1, 10):  
    print(f"{num1} * {i} = {num1*i}")
