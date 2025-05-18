#Média Ponderada - Peça três notas e seus respectivos pesos e calcule a média
#ponderada.

n1 = (int(input("Informe a primeira nota: ")))
n2 = (int(input("Informe a segunda nota: ")))
n3 = (int(input("Informe a terceira nota: ")))

P1 = (int(input("Informe o peso da nota 1: ")))
P2 = (int(input("Informe o peso da nota 2: ")))
P3 = (int(input("Informe o peso da nota 3: ")))

mp = n1*P1 + n2*P2 + n3*P3/P1+P2+P3

print("A média ponderada das notas informada é: ",mp)