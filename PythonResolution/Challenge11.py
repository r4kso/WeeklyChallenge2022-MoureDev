"""
 * Reto #11
 * ELIMINANDO CARACTERES
 * Fecha publicación enunciado: 14/03/22
 * Fecha publicación resolución: 21/03/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
"""

##################### LOGIC #########################
def getRepeatedCharacters(str1, str2):
	out1 = str1.lower()
	out2 = str2.lower()

	chars_in_common = []

	for char in out1:
		if char in out2 and char != " ":
			chars_in_common.append(char)

	for char in chars_in_common:
		out1 = out1.replace(char, "")
		out2 = out2.replace(char, "")

	print(out1 + "\n" + out2)

##################### TESTS #########################
getRepeatedCharacters("Si eres bueno para algo", "Nunca lo hagas gratis")
"""
Deberia salir:
RESULTADOS:
' ee be p '
'c  h t'

Conclusion -> Correcto
"""