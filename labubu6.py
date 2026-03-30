import os
os.system('cls')

# 6- Administrador de tareas:
# Permite al usuario agregar tareas con una descripción y una fecha de vencimiento.
# Muestra la lista de tareas agregadas.
# Permite al usuario marcar una tarea como completada y eliminar tareas de la lista.

tareas = []
while True:
    addwork = input("Agrega una tarea (o escribe 'Fin' para detener): ")
    if addwork.lower() == 'fin':
        break
    
    desc = input("Agrega una descripción para la tarea: ")
    bloodline = input("Agrega una fecha de vencimiento para la tarea: ")
    
    if addwork and desc and bloodline:
        tareas.append((addwork, desc, bloodline))
    else:
        print("Por favor, completa todos los campos.")

tareas.append((addwork, desc, bloodline))

print("Tareas agregadas:", tareas)
