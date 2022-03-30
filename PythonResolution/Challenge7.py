"""
* Reto #7 - RESUELTO
 * CONTANDO PALABRAS
 * Fecha publicación enunciado: 14/02/22
 * Fecha publicación resolución: 21/02/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
"""
##################### LOGIC #########################
def wordCleaner(text):
    puncChars = [".", ",", ":", ";", "!", "¡", "?", "¿", "(", ")", "{", "}", "[", "]", "-"]
    newString = ""

    for i in text:
        if i in puncChars:
            i = ""

        newString += i

    return newString.lower().split()

def wordCounter(text):
    wordList = wordCleaner(text)
    counter = {}

    for i in wordList:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1

    for i in counter:
        print(f"{i}: {counter[i]}")

##################### TESTS #########################
wordCounter("Esto esto no se se si funcionará funcionará funcionara")
"""
RESULTADOS:
esto: 2
no: 1
se: 2
si: 1
funcionará: 2
funcionara: 1

Conclusion -> Correcto
"""

print("\nSiguiente test: \n")

wordCounter("La . . verdad es que no lo se se se se se")
"""
RESULTADOS:
la: 1
verdad: 1
es: 1
que: 1
no: 1
lo: 1
se: 5

Conclusion -> Correcto
"""