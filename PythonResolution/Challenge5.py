"""
 * Reto #5 - NO RESUELTO - Solución en: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/pull/132/commits/a2a4608e64b649a1e057570379e61d239a3efcd9
 * ASPECT RATIO DE UNA IMAGEN
 * Fecha publicación enunciado: 01/02/22
 * Fecha publicación resolución: 07/02/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
 * - Nota: Esta prueba no se puede resolver con el playground online de Kotlin. Se necesita Android Studio.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
"""
import cv2           # Open source Computer Vision library. Recognize faces, identify objects...
import math
import wget

# Get Image
wget.download('https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png')

image = cv2.imread(r'C:\Users\franh\Documents\Desarrollo\WeeklyChallenge2022-MoureDev\PythonResolution\mouredev_github_profile.png')
h, w, c = image.shape()     # Height, width, number of channels
aspectRatio = ''

if h == w:
    aspectRatio = '1:1'

if w < h:
    temp = w
    w = h
    h = temp

divisor = math.gcd(w, h)    # Greatest Common Divisor

x = int(w / divisor) if not temp else int(h / divisor)
y = int(h / divisor) if not temp else int (w / divisor)

print(x + ':' + y)