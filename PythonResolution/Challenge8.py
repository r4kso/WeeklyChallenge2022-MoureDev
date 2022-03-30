"""
* Reto #8 - RESUELTO
 * DECIMAL A BINARIO
 * Fecha publicación enunciado: 18/02/22
 * Fecha publicación resolución: 02/03/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
"""

##################### LOGIC #########################
def decToBin(decimalNum):
    num = decimalNum
    binary = ""
    binaryResult = ""

    if decimalNum == 0:
        return "0"
    else:
        while num != 0:
            module = num % 2    # Almacena el resto
            num = num // 2      # Almacena el resultado de la división entera
            binary += str(module)

        for i in binary[::-1]:  # Recorre el string de adelante hacia detrás
            binaryResult += i

        return binaryResult


##################### TESTS #########################
print(decToBin(15000))
"""
RESULTADOS:
11101010011000

Conclusión -> Correcto
"""

print("\nSiguiente test: \n")

print(decToBin(27))
"""
RESULTADOS:
11011

Conclusión -> Correcto
"""

print("\nSiguiente test: \n")

print(decToBin(0))
"""
RESULTADOS:
0

Conclusión -> Correcto
"""