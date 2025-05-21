def menu_principal():
	print("¡Bienvenido a SkyRoute - Sistema de Gestión de Pasajes!")
	print("Acá podrás controlar las ventas de pasajes, llevar un registro de clientes, consultar los destinos disponibles, y mucho más.")
	print("-----")
	print("1. Gestionar Clientes")
	print("2. Gestionar Destinos")
	print("3. Gestionar Ventas")
	print("4. Consultar Ventas")
	print("5. Botón de Arrepentimiento")
	print("6. Ver Reporte General")
	print("7. Acerca del Sistema")
	print("8. Salir")


listaClientes = []  # Lista de clientes

while True:
	menu_principal()
	ingresoNumero = int(input("Ingrese el número (1-8) de la opción a la que quiere acceder: "))

	if ingresoNumero == 1:
		while True:
			print("-- GESTIONAR CLIENTES --")
			print("1. Ver Clientes")
			print("2. Agregar Cliente")
			print("3. Modificar Cliente")
			print("4. Eliminar Cliente")
			print("5. Volver al Menú Principal")
			opcionSubmenu = int(input("Seleccione una opción: "))

			if opcionSubmenu == 1:
				print(f"La lista de clientes es la siguiente: {listaClientes}")

			elif opcionSubmenu == 2:
				nombre = input("Ingrese el nombre del nuevo cliente: ")
				apellido = input("Ingrese el apellido del nuevo cliente: ")
				dni = input("Ingrese el DNI del nuevo cliente: ")
				nuevoCliente = {"nombre": nombre, "apellido": apellido, "dni": dni}
				listaClientes.append(nuevoCliente)
				print(f"Cliente '{nombre} {apellido}' agregado.")

			elif opcionSubmenu == 3:
				dniAModificar = input("Ingrese el DNI que desea modificar: ")

				for cliente in listaClientes:
					if cliente["dni"] == dniAModificar:
						cliente["nombre"] = input("Nuevo nombre: ")
						cliente["apellido"] = input("Nuevo apellido: ")
						print("Cliente modificado.")
						break
				else:
					print("Cliente no encontrado.")

			elif opcionSubmenu == 4:
				dniAEliminar = input("Ingrese el DNI que desea eliminar: ")
				for cliente in listaClientes:
					if cliente["dni"] == dniAEliminar:
						listaClientes.remove(cliente)
						print("Cliente eliminado.")
						break
				else:
					print("Cliente no encontrado.")

			elif opcionSubmenu == 5:
				break

			else:
				print("Opción no válida, intente nuevamente.")

	elif ingresoNumero == 2:
		while True:
			print("-- GESTIONAR DESTINOS --")
			print("1. Ver Destinos")
			print("2. Agregar Destino")
			print("3. Modificar Destino")
			print("4. Eliminar Destino")
			print("5. Volver al Menú Principal")
			opcionSubmenu = int(input("Seleccione una opción: "))
			if opcionSubmenu == 5:
				break

	elif ingresoNumero == 3:
		while True:
			print("-- GESTIONAR VENTAS --")
			print("1. Agregar Venta")
			print("2. Modificar Venta")
			print("3. Eliminar Venta")
			print("4. Volver al Menú Principal")
			opcionSubmenu = int(input("Seleccione una opción: "))
			if opcionSubmenu == 4:
				break

	elif ingresoNumero == 4:
		while True:
			print("-- CONSULTAR VENTAS --")
			print("1. Ver Ventas")
			print("2. Volver al Menú Principal")
			opcionSubmenu = int(input("Seleccione una opción: "))
			if opcionSubmenu == 2:
				break

	elif ingresoNumero == 5:
		while True:
			print("-- BOTÓN DE ARREPENTIMIENTO --")
			print("1. Enviar solicitud de arrepentimiento")
			print("2. Volver al Menú Principal")
			opcionSubmenu = int(input("Seleccione una opción: "))
			if opcionSubmenu == 2:
				break

	elif ingresoNumero == 6:
		print("-- VER REPORTE GENERAL --")
		# print(reporteGeneral)

	elif ingresoNumero == 7:
		print("-- ACERCA DEL SISTEMA --")
		# print(sistema)

	elif ingresoNumero == 8:
		print("Gracias por usar SkyRoute. ¡Hasta pronto!")
		break

	else:
		print("Opción no válida. Intente nuevamente.")