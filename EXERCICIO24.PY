#Calculadora Simples - Implemente as operações básicas (+, -, *, /) com entrada
#do usuário.

num1 = float(input("Digite o primeiro número: "))
operador = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

# Estrutura de decisão
if operador == "+":
    resultado = num1 + num2

elif operador == "-":
    resultado = num1 - num2

elif operador == "*":
    resultado = num1 * num2

elif operador == "/":
    
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero!"
else:
    resultado = "Operador inválido!"

# Saída
print("Resultado:", resultado)