import os
os.system('cls')

# Calculadora de índice de masa corporal (IMC):
# Solicita al usuario que ingrese su peso en kg y su altura en metros.
# Calcula el IMC utilizando la fórmula: IMC = peso / (altura * altura).
# Muestra el IMC calculado y una categoría de peso según el IMC (talla s, talla m, talla l, talla xl).

print("Bienvenido a la calcula de IMC, por favor, ingrese los datos que se pidan:")
peso = float(input("Peso en kg:"))
h = float(input("Altura en m:"))

imc = peso / (h*h)

print(f"Tu índice de masa corporal es {imc}")
print("")

if (imc < 22):
    print(f"Tú categoría de peso es S.")
elif (imc >= 22 and imc < 24.9):
    print(f"Tú categoría de peso es M.")
elif (imc >= 25 and imc < 27):
    print(f"Tú categoría de peso es L.")
else:
    print(f"Tú categoría de peso es XL.")       
