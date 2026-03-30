import os
os.system('cls')

# Juego de adivinanza de números:
# Genera un número aleatorio entre 1 y 100.
# Pide al usuario que adivine el número.
# Proporciona pistas al usuario si el número es demasiado alto o demasiado bajo.
# Continúa solicitando al usuario que adivine hasta que lo haga correctamente.
# Muestra el número de intentos necesarios para adivinar.

import random
nrandom = random.randint(1,100)
badtries = 0

while True:
    try:
        guess = int(input("Adivina el número entre 1 y 100: "))
        badtries += 1
        if guess == nrandom:
            print(f"Good try! el número lo encontraste en {badtries} intentos.")
            break
        elif guess < nrandom:
            print("El número es demasiado bajo.")
        else:
            print("El número es demasiado alto.")
    except ValueError:
        print("Un número del 1 al 100, tontp.")
