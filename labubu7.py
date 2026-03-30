import os
os.system('cls')

# Calculadora de descuento de compra:
# Solicita al usuario que ingrese el precio original del artículo y el porcentaje de descuento.
# Calcula el precio final después del descuento.
# Muestra el precio final al usuario.

precio = float(input("Ingrese el precio del artículo: "))
descuento = int(input("Ponga el descuento con números enteros: "))

fprecio = precio * (descuento/100)

print(f"El precio final, es de {fprecio}.")
