#Preço por Litro de Combustível - Peça a distância e o consumo do carro,
#calculando o custo da viagem.

distancia = float(input("informe a distancia: "))

consumo = float(input("informe o consumo do carro: "))

custo = consumo/distancia

print(f"A distancia {distancia} mais consumo de {consumo} dá o custo de:{custo}")