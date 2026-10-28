
# Aquí empieza mi app

print("==============================")
print("=  MEDIRECORD                =")
print("=  CONTROL DE MEDICAMENTOS   =")
print("==============================")

nombre = input("¿Cómo te llamas? ")
medicamento = input("¿Qué medicamento deseas registrar? ")
cantidad = int(input("¿Cuántas tabletas debes tomar al día? "))

print("==============================")
print(f"Hola {nombre}, bienvenido a MediRecord.")
print(f"Medicamento: {medicamento}")
print(f"Tabletas al día: {cantidad}")
print(f"En 7 días tomarás {cantidad * 7} tabletas.")
print("==============================")


while True:
    print("===== MENÚ MEDIRECORD =====")
    print("1. Registrar otro medicamento")
    print("2. Consultar medicamento")
    print("3. Calcular tabletas para 7 días")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nuevo_medicamento = input("Nombre del medicamento: ")
        nueva_cantidad = int(input("¿Cuántas tabletas al día?: "))

        if nueva_cantidad < 0:
            print("La cantidad no puede ser negativa.")
        else:
            medicamento = nuevo_medicamento
            cantidad = nueva_cantidad
            print("Medicamento registrado correctamente.")

    elif opcion == "2":
        print("Entraste a la opción 2.")
        print(f"Nombre: {medicamento}")
        print(f"Tabletas al día: {cantidad}")

    elif opcion == "3":
        print("Entraste a la opción 3.")

        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
        else:
            total = cantidad * 7
            print(f"En 7 días tomarás {total} tabletas.")

    elif opcion == "4":
        print(f"Hasta pronto, {nombre}.")
        break

    else:
        print("Opción no válida")
