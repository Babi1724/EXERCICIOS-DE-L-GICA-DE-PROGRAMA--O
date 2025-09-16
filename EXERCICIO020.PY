# Entrada dos coeficientes
a = int(input("Informe o 1º coeficiente (a): "))
b = int(input("Informe o 2º coeficiente (b): "))
c = int(input("Informe o 3º coeficiente (c): "))

# Calcular delta
delta = b**2 - 4*a*c

# Verificar se há raízes reais
if delta < 0:
    print("A equação não possui raízes reais.")
else:
    # Calcular as raízes
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print(f"As raízes da equação são: x1 = {x1} e x2 = {x2}")