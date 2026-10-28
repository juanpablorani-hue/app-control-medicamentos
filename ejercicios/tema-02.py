# =============================================================
# Tema 02 · Condicionales y menú con while · EJERCICIOS
# python-adso · SENA ADSO
#
# INSTRUCCIONES
#   1. Copia este archivo a tu repositorio practicas-python como:
#        tema-02.py
#   2. Resuelve cada ejercicio debajo de su enunciado.
#   3. Ejecuta el archivo y prueba cada caso (los que se cumplen
#      y los que no).
#   4. Súbelo a GitHub con el commit:
#        feat: ejercicios del tema 02
#
# Nombre completo: Juan Pablo Ramírez
# Mi app se llama: MediRecord
# =============================================================


# -------------------------------------------------------------
# EJERCICIO 1 · ¿Alcanza el dinero?
# -------------------------------------------------------------
# Pregunta con input() cuánto dinero tiene el usuario y cuánto
# cuesta lo que quiere comprar.
#   - Si le alcanza: muestra cuánto le sobra.
#   - Si no: muestra cuánto le falta.
#
# Así debe verse (si escribe 20000 y 26500):
#   Te faltan $6,500

# Tu código aquí: 

# dinero_usuario = int(input("¿Cuánto dinero tienes?: "))
# valor_objeto = int(input("¿Cuánto cuesta lo que quieres comprar?: "))

# if dinero_usuario > valor_objeto:
#     print(f"Te sobran ${dinero_usuario - valor_objeto}")
# elif valor_objeto > dinero_usuario:
#     print(f"Te faltan ${valor_objeto - dinero_usuario}")



# -------------------------------------------------------------
# EJERCICIO 2 · El nivel del usuario
# -------------------------------------------------------------
# Una app de ejercicio clasifica al usuario según los minutos que
# entrenó en la semana. Pregunta los minutos y muestra el nivel:
#   - 0 minutos:            "Sin actividad: ¡empieza hoy!"
#   - de 1 a 149 minutos:   "Nivel principiante"
#   - de 150 a 299 minutos: "Nivel activo"
#   - 300 o más:            "Nivel atleta"
#
# Usa if, elif y else. Prueba los cuatro casos.

# Tu código aquí:

# print("-- CALCULA TU NIVEL DE ENTRENAMIENTO SEMANAL --")
# minutos_entrenados = int(input("Favor ingrese los minutos que entreno en la semana: "))

# if minutos_entrenados == 0:
#     print("Sin actividad: ¡empieza hoy!")
# elif minutos_entrenados <= 149:
#     print("Nivel principiante")
# elif minutos_entrenados <= 299:
#     print("Nivel activo")
# else:
#     print("Nivel atleta")

    
# -------------------------------------------------------------
# EJERCICIO 3 · ¿Se puede agendar la cita?
# -------------------------------------------------------------
# Una barbería atiende de 8 a 19 horas, de lunes a sábado.
# Pregunta el día (en minúsculas) y la hora (número entero).
#   - Si es domingo:                 "Los domingos no atendemos"
#   - Si la hora está fuera de 8–19: "Fuera del horario de atención"
#   - Si todo está bien:             "Cita disponible"
#
# Usa and / or en al menos una condición.
#
# Pista: si el usuario escribe "Domingo" con mayúscula, tu if no lo
# reconoce. Prueba:  dia = input("Día: ").lower()
# .lower() convierte el texto a minúsculas (.upper() a mayúsculas).

# Tu código aquí:

# dia = input("Elige el dia para tu cita: ").lower()
# hora = int(input("Elige la hora para tu cita: "))

# if dia == "domingo":
#     print("Los domingos no atendemos")
# elif hora < 8 or hora > 19:
#     print("Fuera del horario de atención")
# else:
#     print("Cita disponible")


# -------------------------------------------------------------
# EJERCICIO 4 · Encuentra el error
# -------------------------------------------------------------
# Este código tiene 3 errores. Corrígelos y explica en un
# comentario qué estaba mal en cada uno.
#
#   clave = input("Clave: ")
#   if clave = "1234"
#   print("Bienvenido")
#   else:
#       print("Clave incorrecta")

# Tu código corregido aquí:

# clave = input("Clave: ")
# if clave == "1234":
#     print("Bienvenido")
# else:
#     print("Clave incorrecta")


# Error 1: se tiene que comparar con doble igual (==) no con uno solo
# Error 2: al final de cada condicional debe de ir dos puntos (:)
# Error 3: error de sangria en el ejecutable del if 


# -------------------------------------------------------------
# EJERCICIO 5 · Caja registradora con menú
# -------------------------------------------------------------
# Haz un menú con while que se repita hasta que el usuario elija
# salir:
#   1. Agregar un producto (pregunta el precio y súmalo al total)
#   2. Ver el total
#   3. Salir
#
# Si escribe una opción que no existe, muestra "Opción no válida".
# Pista: crea total = 0 antes del while y en la opción 1 haz
#        total = total + precio
#
# Así debe verse:
#   1. Agregar producto  2. Ver total  3. Salir
#   Opción: 1
#   Precio: 4500
#   Opción: 1
#   Precio: 2000
#   Opción: 2
#   Total: $6,500

# Tu código aquí:

# total = 0

# while True:
#     print("1. Agregar un producto")
#     print("2. Ver el total")
#     print("3. Salir")
#     opcion = int(input("Seleccione un opcion: "))

#     if opcion == 1:
#         precio = float(input("Ingresa el precio del producto: "))
#         total += precio
#     elif opcion == 2:
#         print(f"Su total ${total}")
#     elif opcion == 3:
#         break
#     else:
#         print("Opcion no valida. Favor intente de nuevo.")



# =============================================================
# EJERCICIO 6 · LLÉVALO A TU APP  (va en src/app.py de tu app, no aquí)
# =============================================================
# Tu app ya saluda (tema 01). Hoy le das un MENÚ. En el archivo
# src/app.py de tu app:
#   1. Deja la bienvenida al inicio.
#   2. Agrega un menú con while con al menos 3 opciones
#      que tengan sentido para tu app, más "Salir".
#   3. Cada opción hace algo (aunque sea sencillo): preguntar un
#      dato, calcular algo o mostrar un mensaje.
#   4. Al menos una opción valida un dato con if
#      (por ejemplo: que un número no sea negativo).
#   5. Si eligen una opción que no existe: "Opción no válida".
#
# Ejemplo para una app de citas de barbería:
#   ===== BARBERÍA EL CORTE =====
#   1. Ver precios
#   2. Agendar cita
#   3. Calcular total de cortes
#   4. Salir
#
# Con esto tu app ya se ve como una app de verdad. En el próximo
# tema guardamos varias citas, productos o registros en listas.
# =============================================================
