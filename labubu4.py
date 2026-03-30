import os
os.system('cls')

# Validador de contraseña:
# Solicita al usuario que cree una contraseña.
# Verifica si la contraseña cumple con los siguientes criterios:
# Tiene al menos 8 caracteres de longitud.
# Contiene al menos una letra mayúscula y una letra minúscula.
# Tiene al menos un número.
# Tiene al menos un carácter especial (por ejemplo, !, @, #, $, %, etc.).
# Informa al usuario si la contraseña es válida o no.

password = input("Por favor, ingresa una contraseña: ")
if (len(password) >= 8 and
    any(c.isupper() for c in password) and
    any(c.islower() for c in password) and
    any(c.isdigit() for c in password) and
    any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in password)):
    print("La contraseña es válida.")
else:
    print("La contraseña no es válida.")

# Ya lo hicimos con Postai.
