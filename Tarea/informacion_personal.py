# Tarea: Trabajando con Diccionarios en Python
# Objetivo: Practicar el uso de diccionarios en Python

# Paso 1: Crear el diccionario con información personal
informacion_personal = {
    "nombre": "Carlos Sánchez",   # nombre ficticio
    "edad": 22,                   # edad ficticia
    "ciudad": "Quito",            # ciudad inicial
    "profesion": "Estudiante"     # profesión inicial
}

# Paso 2: Acceder a la clave "ciudad" y modificar su valor
print("Ciudad antes del cambio:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Guayaquil"   # cambiamos la ciudad

# Paso 3: Agregar o modificar la clave "profesion"
informacion_personal["profesion"] = "Ingeniero en Software"

# Paso 4: Verificar si la clave "telefono" existe
# Si no existe, la agregamos con un número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0998765432"

# Paso 5: Eliminar la clave "edad" porque ya no es necesaria
informacion_personal.pop("edad", None)

# Paso 6: Imprimir el diccionario final
print("\nDiccionario final después de las modificaciones:")
print(informacion_personal)
