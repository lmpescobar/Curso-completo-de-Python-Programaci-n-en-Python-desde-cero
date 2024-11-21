# Ejercicio
# Descifrar "Mensajes Secretos de una Carta de Amor" usando strings, indexación, slicing, stride y strings de múltiples líneas.

# Descripción:
# Dada una carta de amor con tres párrafos, se deben extraer mensajes secretos ocultos en cada uno usando técnicas de indexación, slicing y stride en Python.

# Instrucciones:
# 1. El mensaje secreto del primer párrafo se forma tomando cada decimoctavo (18) caracter, comenzando desde el segundo caracter.
# 2. El mensaje secreto del segundo párrafo está entre los caracteres 138 y 147 (inclusive).
# 3. En el tercer párrafo, se deben extraer letras en las siguientes posiciones: 125, 94, 35, 107, 20 y 1.
# 4. Utiliza la función `print` para mostrar los mensajes decodificados.

# Código en Python

# Párrafos proporcionados
parrafo1 = "Cada dia te quiero mas y nunca lo he olvidado."
parrafo2 = "En el corazón de una historia de amor tecnológica, Lucas y Carla compartían su pasión por la programación. Cada día, mientras aprendían a programar, sus corazones se sincronizaban con cada línea de código."
parrafo3 = "En cada amanecer, veo el brillo de tus ojos; en cada atardecer, siento el calor de tu abrazo; y en cada noche estrellada, me pierdo en el infinito de tu amor."

# 1. Primer párrafo: cada 18 caracteres, comenzando desde el segundo caracter
mensaje_secreto_1 = parrafo1[1::18]

# 2. Segundo párrafo: caracteres desde el 138 al 147 (inclusive)
mensaje_secreto_2 = parrafo2[138:148]

# 3. Tercer párrafo: posiciones específicas
mensaje_secreto_3 = (
    parrafo3[125] +  # Primera letra: posición 125
    parrafo3[94] +   # Segunda letra: posición 94
    parrafo3[35] +   # Tercera letra: posición 35
    parrafo3[107] +  # Cuarta letra: posición 107
    parrafo3[20] +   # Quinta letra: posición 20
    parrafo3[1]      # Sexta letra: posición 1
)

# Mostrar resultados
print("Mensajes Secretos Decodificados:")
print("Mensaje secreto 1:")
print(mensaje_secreto_1)  # Mensaje del primer párrafo.
print("\nMensaje secreto 2:")
print(mensaje_secreto_2)  # Mensaje del segundo párrafo.
print("\nMensaje secreto 3:")
print(mensaje_secreto_3)  # Letras del tercer párrafo.

# Explicación del código:
# - Se aplica slicing con un stride de 18 para el primer párrafo.
# - Se extraen caracteres específicos con slicing del segundo párrafo.
# - Se obtienen letras específicas del tercer párrafo con indexación directa.
# - Finalmente, se imprimen los mensajes secretos descifrados.