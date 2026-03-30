import os
os.system('cls')

#Conversor de temperaturas:
# Pide al usuario que ingrese una temperatura en grados Celsius.
# Convierte la temperatura a grados Fahrenheit utilizando la fórmula: Fahrenheit = (Celsius * 9/5) + 32.
# Imprime la temperatura en grados Fahrenheit.

C = int(input("Ingrese una temperatura C° en números enteros: "))

F = (C * 9/5 ) + 32

print(f"Por sí las dudas, el calculo de tu temperatura en Celsius en Fahrenheit es {F}.")
