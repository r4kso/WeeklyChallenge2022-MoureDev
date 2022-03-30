"""
* Reto #9
 * CÓDIGO MORSE - RESUELTO
 * Fecha publicación enunciado: 02/03/22
 * Fecha publicación resolución: 07/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 """
##################### IMPORTS & OTHERS #########################
# Morse dictionary
MORSE_CODE_DICT = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

##################### LOGIC #########################
# Detectar si es morse o texto natural
def isMorse(text):
    isMorse = False
    for i in text.lower().split():
        if i in MORSE_CODE_DICT.values():
            isMorse = True

    return isMorse

# Pasar de morse a texto natural
def morseToNatural(text):
    # Creamos un diccionario latin en base al diccionario morse
    natural_dict = {value: key for key, value in MORSE_CODE_DICT.items()}

    translatedText = ""
    for i in text.split():
        # Obtiene la letra del diccionario creado
        letter = natural_dict.get(i)

        if i == "....--.....---..-...-.. " or letter is None:
            translatedText += "*"
        else:
            translatedText += letter

        translatedText += " "       # Añade un espacio al final de la palabra
            
    return translatedText


# Pasar de texto natural a morse
def naturalToMorse(text):

    translatedText = ""
    for i in text.lower():
        # Traduce la letra a morse en base al diccionario previamente creado. Si no lo encuentra retonar None
        letter = MORSE_CODE_DICT.get(i)

        if letter == " ":
            translatedText += " "
        elif letter == None:
            translatedText += "....--.....---..-...-.. " # Error de transmisión. Protocolo morse.
        else:
            translatedText += f"{letter} "               # Añadimos el espacio

    return translatedText

# Main function
def main(text):
    if isMorse(text):
        print(morseToNatural(text))
    else:
        print(naturalToMorse(text))

##################### TESTS #########################
main(".... --- .-.. .-  -- ..- -. -.. ---  .---- -..-. ...--")
"""
RESULTADOS:
h o l a m u n d o 1 / 3 

Conclusion -> Correcto
"""
print("\nSiguiente test: \n")

main("mouredev")
"""
RESULTADOS:
-- --- ..- .-. . -.. . ...- 

Conclusion -> Correcto
"""
