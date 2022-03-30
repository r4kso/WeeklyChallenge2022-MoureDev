"""
* Reto #10 - RESUELTO
 * EXPRESIONES EQUILIBRADAS
 * Fecha publicación enunciado: 07/03/22
 * Fecha publicación resolución: 14/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
"""
##################### IMPORTS & OTHERS #########################
PARENTHESIS_DICT = {
	"(": ")",
    "[": "]",
    "{": "}"
}

##################### LOGIC #########################
def balancedExpression(expression):
	parenthesisList = []

	invertedParenthesis = {value: key for key, value in PARENTHESIS_DICT.items()}

	isBalanced = True
	for letter in expression:
		if letter in PARENTHESIS_DICT.keys():
			parenthesisList.append(letter)
		elif letter in PARENTHESIS_DICT.values() and invertedParenthesis[letter] == parenthesisList[-1]:
			parenthesisList.pop()
		elif letter in PARENTHESIS_DICT.values():
			isBalanced = False
			break

	if len(parenthesisList) > 0:
		isBalanced = False

	print(isBalanced)

##################### TESTS #########################
balancedExpression("{ [ a ( c + d ) ] - 5 }")
"""
RESULTADOS:
True

Conclusion -> Correcto
"""

print("\nSiguiente test: \n")

balancedExpression("{ a ( c + d ) ] - 5 }")
"""
RESULTADOS:
False

Conclusion -> Correcto
"""