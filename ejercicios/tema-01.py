# =============================================================
# Tema 01 · Variables, tipos, entrada y salida · EJERCICIOS
# python-adso · SENA ADSO
#
# INSTRUCCIONES
#   1. Copia este archivo al repositorio de TU app como:
#        ejercicios/tema-01.py
#   2. Resuelve cada ejercicio debajo de su enunciado.
#   3. Ejecuta el archivo y prueba que todo funcione.
#   4. Súbelo a GitHub con el commit:
#        feat: tema 01 y bienvenida de la app
#
# Nombre completo: Juan Pablo Ramírez
# Mi app se llama: MediRecord
# =============================================================


# -------------------------------------------------------------
# EJERCICIO 1 · Tarjeta de presentación
# -------------------------------------------------------------
# Crea tres variables: tu nombre (texto), tu edad (entero) y tu
# estatura en metros (decimal). Muestra las tres con UN solo print
# usando f-string.
#
# Así debe verse:
#   Soy Ana, tengo 19 años y mido 1.62 m.

# Tu código aquí:

nombre = "Juan Pablo"
edad = 18
estatura = 1.72

print(f"-- Punto 1 --")
print(f"Soy {nombre}, tengo {edad} y mido {estatura}")

# -------------------------------------------------------------
# EJERCICIO 2 · ¿De qué tipo es?
# -------------------------------------------------------------
# Crea estas cuatro variables y muestra el tipo de cada una con type():
#   a = "100"
#   b = 100
#   c = 100.0
#   d = "cien"
#
# Después, en un comentario, responde: ¿por qué "100" y 100 no son
# lo mismo para Python?

# Tu código aquí:

a = "100"
b = 100
c = 100.0
d = "cien"

print(f"-- Punto 2 --")
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Respuesta: la variable a al tener las comillas esto hace que 
# python lo detecte como una variable de tipo str (texto).


# -------------------------------------------------------------
# EJERCICIO 3 · La cuenta del almuerzo
# -------------------------------------------------------------
# Pregunta con input():
#   - el valor de la cuenta
#   - cuántas personas van a pagar
#   - el porcentaje de propina (por ejemplo 10)
#
# Muestra: el valor de la propina, el total con propina y cuánto
# paga cada persona. Los valores en pesos, con separador de miles.
#
# Así debe verse (si escriben 85000, 3 y 10):
#   Propina:          $8,500
#   Total:            $93,500
#   Cada uno paga:    $31,167

# Tu código aquí:
# print(f"-- Punto 3 --")

valor_cuenta = float(input("Por favor ingresa el valor total de la cuenta: "))
numero_persona = int(input("¿Cuantas personas pagaran?(el precio se divide en partes iguales): "))
porcent_propina = float(input("Ingresa el % de propina que daran: "))

cal_propina = porcent_propina * valor_cuenta
propina = cal_propina / 100

valor_persona = valor_cuenta / numero_persona

print(f"- Propina: {propina}")
print(f"- Total:   {valor_cuenta}")
print(f"- Cada uno paga: {valor_persona}")

# -------------------------------------------------------------
# EJERCICIO 4 · Encuentra el error
# -------------------------------------------------------------
# Este código tiene 2 errores. Corrígelos y explica en un
# comentario qué estaba mal en cada uno.
#
#   precio = input("Precio del producto: ")
#   unidades = input("Unidades: ")
#   print("Total a pagar: " + precio * unidades)

# Tu código corregido aquí:

precio = float(input("Precio del producto: "))
unidades = float(input("Unidades: "))
print("Total a pagar: " + str(precio * unidades))

# Error 1: el primer error es que todo dato que ingresa 
# con input se toma como str, por lo que hay que parsear
# con float() para que ahora sea un dato tipo de numero decimal.

# Error 2: se esta concatenando con "+" un tipo str y float
# esto genera un error ya que concatenar con "+" solo acepta 
# variables del mis tipo de dato, es decir; en este caso se
# concatena dos variables de diferente tipo, una str y una float
# la forma correcta seria que las dos variables fueran str o float
# la primera solucion es parsear o coercionar la multiplicacion asi:
# str(precio * unidades) o concatenar de otra forma con f"" o con ",".

# -------------------------------------------------------------
# EJERCICIO 5 · Inventario rápido
# -------------------------------------------------------------
# Pregunta el nombre de un producto, cuántas unidades hay y el
# precio de cada unidad. Muestra un resumen como este:
#
#   ===== INVENTARIO =====
#   Producto:   Tabla de pino
#   Unidades:   40
#   Precio:     $18,000
#   Valor total: $720,000
#   ======================

# Tu código aquí:

nombre_producto = input("Ingresa nombre del producto: ")
unidades = int(input("Ingresa la cantidad de unidades del producto: "))
precio = float(input("Ingrese el precio c/u: "))
total = unidades * precio

print("=== INVENTARIO ===")
print(f"- Producto: {nombre_producto}")
print(f"- Unidades: {unidades}")
print(f"- Valor Total: {total}")
print("==================")

# =============================================================
# EJERCICIO 6 · LLÉVALO A TU APP  (va en tu app.py, no aquí)
# =============================================================
# En el archivo app.py de tu proyecto, crea la pantalla de bienvenida
# de tu app. Debe:
#   1. Mostrar el nombre de tu app con un encabezado visible.
#   2. Preguntarle al usuario al menos 2 datos con input()
#      (por ejemplo: su nombre y algo que tenga sentido en tu app).
#   3. Responder con un mensaje que use esos datos (f-string).
#   4. Al menos un dato debe ser un número con el que hagas una cuenta.
#
# Ejemplo para una app de citas de barbería:
#   ==============================
#        BARBERÍA EL CORTE
#   ==============================
#   ¿Cómo te llamas? Carlos
#   ¿Cuántos cortes quieres agendar? 2
#   Hola Carlos, tus 2 cortes cuestan $50,000.
#
# Este es el primer paso de tu app: en los próximos temas le
# agregamos el menú, las listas y todo lo demás.
# =============================================================
