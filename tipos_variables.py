 
from math import floor
import sys
import sysconfig

from numpy import ceil


num_entero = 10
num_real = 13.1415
tipo_cadena = "Hola Mundo"
tipo_bool = True


print ( num_entero) 
print ( num_real) 
print ( tipo_cadena) 
print ( tipo_bool) 

resultado_suma = 10 + 10.5
print(num_entero + num_real)


#existen ciertas funciones que nos facilitan operaciones matemáticas. Estas funciones se utilizan en una variedad de contextos, 
# desde la programación hasta la ciencia.


# Aquí hay algunos ejemplos de cómo se pueden utilizar estas funciones:

# round
print(round(3.14159, 2))  # 3.14  # round redondea un número a un número dado de decimales.

# floor 
print(floor(3.14159))  # 3 # floor redondea un número hacia abajo, al entero más cercano.


# ceil
print(ceil(3.14159))  # 4  # ceil redondea un número hacia arriba, al entero más cercano.


# abs
print(abs(-3.14159))  # 3.14159  # abs devuelve el valor absoluto de un número.

# max
print(max([1, 2, 3]))  # 3  # max devuelve el valor máximo de un conjunto de números.

# min
print(min([1, 2, 3]))  # 1  # min devuelve el valor mínimo de un conjunto de números.

# sum
print(sum([1, 2, 3]))  # 6  # sum suma los elementos de un conjunto de números.

# format
print(format(3.14159, ".2f"))  # 3.14  # format formatea un número de acuerdo con un formato especificado.

# Archivo: tipos_primitivos.py

# Define una variable de cada tipo de primitivo

variable_entero = 10
variable_flotante = 3.14159
variable_cadena = "Hola, mundo!"
variable_booleano = True

# 1 - Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable

resultado = variable_cadena + " " + str(variable_entero) + " " + str(variable_flotante) + " " + str(variable_booleano)

# 2 - Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo

# -  **Límite de los enteros**

# 4- El límite superior de los enteros en Python es `sys.maxsize`. El límite inferior es `-sys.maxsize - 1`.

# 5 -**Límite de los flotantes**

# El límite superior de los flotantes en Python es `sys.float_info.max`. El límite inferior es `sys.float_info.min`.

# 6 - Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable

n = variable_entero
suma_pares = 0
for i in range(1, n + 1):
  suma_pares += 2 * i

# Imprime los resultados de las tareas anteriores

print("Variable entero:", variable_entero)
print("Variable flotante:", variable_flotante)
print("Variable cadena:", variable_cadena)
print("Variable booleano:", variable_booleano)
print("Resultado de la concatenación:", resultado)
print("Límite superior de los enteros:", sysconfig.maxsize)
print("Límite inferior de los enteros:", -sys.maxsize - 1)
print("Límite superior de los flotantes:", sys.float_info.max)
print("Límite inferior de los flotantes:", sys.float_info.min)
print("Suma de los primeros n números pares:", suma_pares)