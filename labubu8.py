import os
os.system('cls')

# Un generador de contraseñas aleatorias crea combinaciones seguras de caracteres alfanuméricos y símbolos para proteger cuentas en línea. Su uso es fundamental para evitar ataques de fuerza bruta y mantener la seguridad digital.
#
#
#

import random

password = int(input("Ingresa cuantos carácteres quieres que tenga tú contraseña aesthethic: "))

minus = "abcdefghijklmnopqrstuvwxyz"
mayu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nmrs = "0123456789"
simb = "!@#$%^&*()-_=+[]{};:,.<>?/|"

posibilidades = minus + mayu + nmrs + simb

randompassword = ""

for i in range(password):
    i = random.randint(0, len(posibilidades)- 1)
    randompassword = randompassword + posibilidades[i]
    
print("Contraseña lista: ")
print(f"{randompassword}")
