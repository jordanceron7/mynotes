# Tarea: Trabajo con Archivos de Texto en Python

# Escritura en el archivo de texto
# Abrimos el archivo en modo escritura ("w"), si no existe lo crea
with open("my_notes.txt", "w") as file:
    # Escribimos tres notas personales en el archivo
    file.write("Nota 1: Hoy aprendí a trabajar con archivos en Python.\n")
    file.write("Nota 2: El método write() sirve para escribir en archivos.\n")
    file.write("Nota 3: El método readline() se usa para leer línea por línea.\n")

# Lectura del archivo de texto
# Abrimos el archivo en modo lectura ("r")
with open("my_notes.txt", "r") as file:
    # Leemos línea por línea usando un bucle
    line = file.readline()  # Leemos la primera línea
    while line:  # Mientras haya contenido
        print(line.strip())  # Mostramos en consola (strip() elimina saltos de línea extras)
        line = file.readline()  # Leemos la siguiente línea

# NOTA:
# Con el uso de "with open(...)" no es necesario llamar a close(),
# porque se cierra automáticamente al salir del bloque.
