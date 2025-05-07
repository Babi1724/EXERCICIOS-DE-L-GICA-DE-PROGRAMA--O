#Conversor de Segundos - Peça um valor em segundos e converta para horas,
#minutos e segundos.

segundos = float(input("informe o segundos: "))

minutos = segundos/60

horas = minutos/60

print(f"{horas} horas,{minutos}minutos,{segundos}segundos")
