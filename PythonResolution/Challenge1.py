"""
 Reto #1 - RESUELTO
 ¿ES UN ANAGRAMA?
 Fecha publicación enunciado: 03/01/22
 Fecha publicación resolución: 10/01/22
 Dificultad: MEDIA
 
 Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 NO hace falta comprobar que ambas palabras existan.
 Dos palabras exactamente iguales no son anagrama.
 
 Información adicional:
 - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 """
##################### LOGIC #########################
def isAnAnagram(string1, string2):
    # Igualamos los dos strings
    string1.lower()
    string2.lower()
    if (len(string1) == len(string2)):
        i = len(string1)
        stringReversed = ''
        while i > 0:
            characterString = string2[i-1]
            stringReversed = stringReversed + str(characterString)
            i = i - 1;
    else:
        return bool(0)

    return (string1.lower() == stringReversed)

##################### TESTS #########################
print(isAnAnagram("lana", "anal"))
"""
RESULTADOS:
True

Conclusion -> Correcto
"""
print("\nSiguiente test: \n")

print(isAnAnagram("hola", "adios"))
"""
RESULTADOS:
False

Conclusion -> Correcto
"""