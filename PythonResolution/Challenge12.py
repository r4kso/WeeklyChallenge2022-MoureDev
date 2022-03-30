"""
* Reto #12 - RESUELTO
 * ¿ES UN PALÍNDROMO?
 * Fecha publicación enunciado: 21/03/22
 * Fecha publicación resolución: 28/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
"""
##################### IMPORTS & OTHERS #########################
PUNCTUATION_SYMBOLS_DICT = [",", ";", ":", ".", "·", "¿", "?", "¡", "!", "(", ")", "-", "_", "<", ">", "*", "'", "{", "}",
                       "[", "]", "^", "%", "/", "|", "\\"]

ACCENT_MARKS_DICT = {
    "á": "a",
    "à": "a",
    "ä": "a",
    "â": "a",
    "é": "e",
    "è": "e",
    "ë": "e",
    "ê": "e",
    "í": "i",
    "ì": "i",
    "ï": "i",
    "î": "i",
    "ó": "o",
    "ò": "o",
    "ö": "o",
    "ô": "o",
    "ú": "u",
    "ù": "u",
    "ü": "u",
    "û": "u"
}

##################### LOGIC #########################
def removeCharacters(text):
	string = text.lower().replace(" ", "")

	for c in string:
		if c in PUNCTUATION_SYMBOLS_DICT:
			string = string.replace(c, "")
		if c in ACCENT_MARKS_DICT:
			string = string.replace(c, "")

	return string

def isPalindrome(text):
	modifiedText = removeCharacters(text)
	reversedText = modifiedText[::-1]

	if modifiedText == reversedText:
		print(True)
	else:
		print(False)


##################### TESTS #########################
isPalindrome("Ana lleva al oso la avellana.")
"""
RESULTADOS:
True

Conclusion -> Correcto
"""

print("\nSiguiente test: \n")

isPalindrome("Anita lava la tina")
"""
RESULTADOS:
True

Conclusion -> Correcto
"""

print("\nSiguiente test: \n")

isPalindrome("\\¿Qué tal Hackermen?")
"""
RESULTADOS:
False

Conclusion -> Correcto
"""
