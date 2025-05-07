#Comparação de Três Números - Peça três números e diga qual é o maior e
#qual é o menor.

num1 = int(input("Informe o primeiro numero: "))

num2 = int(input("informe o segundo numero: "))

num3 = int(input("informe o terceiro numero: "))

if num1 >= num2 and num1 >= num3:
    maior = num1

elif num2 >= num1 and num2 >= num3:
    maior = num2

else:
    maior = num3

# Encontrar o menor número

if num1 <= num2 and num1 <= num3:
    menor = num1

elif num2 <= num1 and num2 <= num3:
    menor = num2
    
else:
    menor = num3

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
