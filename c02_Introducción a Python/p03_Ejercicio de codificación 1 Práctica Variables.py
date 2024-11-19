# Ejercicio
# Crear un "Menú del Día de un Restaurante Gourmet" usando variables y la función print.

# Instrucciones
# 1. Definir las variables para el nombre y el precio de cada plato.
# 2. Usar la función print para mostrar el menú en la consola.
# 3. Las variables deben tener los nombres indicados: nombre_entrante, precio_entrante, 
#    nombre_principal, precio_principal, nombre_postre, precio_postre.

# Código en Python
# Definición de variables para el menú
nombre_entrante = "Sopa de trufas"  # Nombre del entrante.
precio_entrante = 12  # Precio del entrante en euros.

nombre_principal = "Filete Mignon con salsa de vino tinto"  # Nombre del plato principal.
precio_principal = 30  # Precio del plato principal en euros.

nombre_postre = "Tiramisú casero"  # Nombre del postre.
precio_postre = 8  # Precio del postre en euros.

# Mostrar el menú del día en la consola
print("Menú del Día - Restaurante Gourmet")  # Título del menú.
print("\n-- Entrante --")  # Sección del entrante.
print(nombre_entrante)  # Mostrar el nombre del entrante.
print("Precio:\n", precio_entrante, "euros")  # Mostrar el precio del entrante.

print("\n-- Plato Principal --")  # Sección del plato principal.
print(nombre_principal)  # Mostrar el nombre del plato principal.
print("Precio:\n", precio_principal, "euros")  # Mostrar el precio del plato principal.

print("\n-- Postre --")  # Sección del postre.
print(nombre_postre)  # Mostrar el nombre del postre.
print("Precio:\n", precio_postre, "euros")  # Mostrar el precio del postre.

# Explicación del código:
# - Se crean variables para almacenar los nombres y precios de los platos.
# - Se usa la función print para estructurar el menú en secciones claras.
# - Se incluyen saltos de línea (\n) para una mejor presentación en la consola.