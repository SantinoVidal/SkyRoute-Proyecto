"""
Sistema de Gestión de Pasajes - SkyRoute

Propósito:
(Entrega de evidencia N2 del módulo programador)

Este programa permite gestionar un sistema de ventas de pasajes,
incluyendo la administración de clientes, destinos, ventas realizadas,
consultas, reportes e implementación de un botón de arrepentimiento.

Integrantes del grupo:
- Vidal Gallea Santino
- Esquivel Wanda
- Lencina Gino Agustín
- Lloveras Mateo
- Paez Ramos Constanza

Instrucciones de ejecución:
1. Ejecutar el archivo en una terminal que permita la entrada y salida de datos.
2. Interactuar con el sistema eligiendo las opciones del menú mediante el ingreso de números del 1 al 8.
3. Seguir las instrucciones que se presentan en pantalla para gestionar clientes, ventas y otras funciones.
"""

# Función que muestra el menú principal del sistema
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

# Listas globales para almacenar clientes, ventas y destinos.
listaClientes = []  # Lista donde se guardan los clientes (diccionarios con nombre, apellido, dni)
ventas = []         # Lista donde se guardan las ventas (diccionarios con cliente y destino)
listaDestinos = []  # Lista donde se guardan los destinos (nombres de destinos)

# Función para agregar una nueva venta
def agregar_venta(cliente, destino):
	venta = {"cliente": cliente, "destino": destino}  # Crear diccionario con datos de venta
	ventas.append(venta)                              # Agregar venta a la lista de ventas
	print(f"Venta agregada: {venta}")

# Función para deshacer la última venta (botón de arrepentimiento)
def arrepentimiento():
	if ventas:
		ultima_venta = ventas.pop()                    # Quitar la última venta agregada
		print(f" Se ha revertido la última venta: {ultima_venta}")
	else:
		print("No hay ventas para revertir")           # Avisar si no hay ventas para borrar

# Función auxiliar para buscar cliente por DNI
def buscar_cliente_por_dni(dni):
	for cliente in listaClientes:
		if cliente["dni"] == dni:
			return cliente
	return None

# Bucle principal del sistema que se repite hasta que el usuario elige salir
while True:
	menu_principal()
	ingresoNumero = int(input("Ingrese el número (1-8) de la opción a la que quiere acceder: "))

	# Gestión de clientes
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
				# Mostrar todos los clientes guardados
				if listaClientes:
					for cliente in listaClientes:
						print(f"{cliente['nombre']} {cliente['apellido']} - DNI: {cliente['dni']}")
				else:
					print("No hay clientes registrados.")

			elif opcionSubmenu == 2:
				# Agregar un nuevo cliente solicitando datos
				nombre = input("Ingrese el nombre del nuevo cliente: ")
				apellido = input("Ingrese el apellido del nuevo cliente: ")
				dni = input("Ingrese el DNI del nuevo cliente: ")
				nuevoCliente = {"nombre": nombre, "apellido": apellido, "dni": dni}
				listaClientes.append(nuevoCliente)  # Guardar nuevo cliente en la lista
				print(f"Cliente '{nombre} {apellido}' agregado.")

			elif opcionSubmenu == 3:
				# Modificar datos de un cliente buscando por DNI
				dniAModificar = input("Ingrese el DNI que desea modificar: ")
				cliente = buscar_cliente_por_dni(dniAModificar)
				if cliente:
					cliente["nombre"] = input("Nuevo nombre: ")
					cliente["apellido"] = input("Nuevo apellido: ")
					print("Cliente modificado.")
				else:
					print("Cliente no encontrado.")  # Si no encontró el DNI

			elif opcionSubmenu == 4:
				# Eliminar cliente buscando por DNI
				dniAEliminar = input("Ingrese el DNI que desea eliminar: ")
				cliente = buscar_cliente_por_dni(dniAEliminar)
				if cliente:
					listaClientes.remove(cliente)  # Quitar cliente de la lista
					print("Cliente eliminado.")
				else:
					print("Cliente no encontrado.")  # Si no encontró el DNI

			elif opcionSubmenu == 5:
				# Volver al menú principal
				break

			else:
				print("Opción no válida, intente nuevamente.")

	# Gestión de destinos
	elif ingresoNumero == 2:
		while True:
			print("-- GESTIONAR DESTINOS --")
			print("1. Mostrar destinos")
			print("2. Agregar destino")
			print("3. Cambiar nombre de destino")
			print("4. Quitar destino")
			print("5. Volver al menú principal")
			opcionDestino = int(input("Elija una opción: "))

			if opcionDestino == 1:
				# Mostrar todos los destinos guardados
				if listaDestinos:
					print("Destinos disponibles:")
					for indice, destino in enumerate(listaDestinos, 1):
						print(f"{indice}. {destino}")
				else:
					print("No hay destinos cargados.")

			elif opcionDestino == 2:
				# Agregar un nuevo destino a la lista
				nuevoDestino = input("Ingrese el nombre del nuevo destino: ")
				listaDestinos.append(nuevoDestino)
				print(f"Destino '{nuevoDestino}' agregado correctamente.")

			elif opcionDestino == 3:
				# Cambiar el nombre de un destino existente
				destinoViejo = input("Ingrese el nombre del destino a cambiar: ")
				if destinoViejo in listaDestinos:
					destinoNuevo = input("Ingrese el nuevo nombre del destino: ")
					pos = listaDestinos.index(destinoViejo)  # Buscar posición para modificar
					listaDestinos[pos] = destinoNuevo
					print(f"Destino '{destinoViejo}' cambiado a '{destinoNuevo}'.")
				else:
					print("Destino no encontrado.")

			elif opcionDestino == 4:
				# Quitar un destino de la lista
				destinoEliminar = input("Ingrese el nombre del destino a eliminar: ")
				if destinoEliminar in listaDestinos:
					listaDestinos.remove(destinoEliminar)
					print(f"Destino '{destinoEliminar}' eliminado.")
				else:
					print("Destino no encontrado.")

			elif opcionDestino == 5:
				# Volver al menú principal
				break

			else:
				print("Opción inválida, intente nuevamente.")

	# Gestión de ventas
	elif ingresoNumero == 3:
		while True:
			print("-- GESTIONAR VENTAS --")
			print("1. Agregar Venta")
			print("2. Modificar Venta")
			print("3. Eliminar Venta")
			print("4. Volver al Menú Principal")
			opcionSubmenu = int(input("Seleccione una opción: "))

			if opcionSubmenu == 1:
				# Agregar una nueva venta solicitando cliente y destino
				dni_cliente = input("Ingrese DNI del Cliente para la venta: ")
				cliente = buscar_cliente_por_dni(dni_cliente)
				if not cliente:
					print("Cliente no encontrado.")
					continue

				destino_venta = input("Ingrese el destino de la venta: ")
				if destino_venta not in listaDestinos:
					print("Destino no válido.")
					continue
				agregar_venta(cliente["nombre"], destino_venta)

			elif opcionSubmenu == 2:
				# Modificar venta buscando por DNI del cliente
				dni_a_buscar = input("Ingrese el DNI del cliente de la venta que desea modificar: ")
				cliente = buscar_cliente_por_dni(dni_a_buscar)
				if cliente:
					venta_encontrada = False
					for venta in ventas:
						if venta["cliente"] == cliente["nombre"]:
							nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
							nuevo_destino = input("Ingrese el nuevo destino: ")
							venta["cliente"] = nuevo_nombre
							venta["destino"] = nuevo_destino
							if nuevo_destino not in listaDestinos:
								print("Destino no válido.")
								continue
							print("Venta modificada correctamente.")
							venta_encontrada = True
							break
					if not venta_encontrada:
						print("No se encontró ninguna venta para ese cliente.")
				else:
					print("Cliente no encontrado.")

			elif opcionSubmenu == 3:
				# Eliminar venta buscando por DNI del cliente
				dni_a_eliminar = input("Ingrese el DNI del cliente de la venta que desea eliminar: ")
				cliente = buscar_cliente_por_dni(dni_a_eliminar)
				if cliente:
					venta_encontrada = False
					for venta in ventas:
						if venta["cliente"] == cliente["nombre"]:
							ventas.remove(venta)
							print("Venta eliminada correctamente.")
							venta_encontrada = True
							break
					if not venta_encontrada:
						print("No se encontró ninguna venta para ese cliente.")
				else:
					print("Cliente no encontrado.")

			elif opcionSubmenu == 4:
				# Volver al menú principal
				break

	# Consultar ventas
	elif ingresoNumero == 4:
		while True:
			print("-- CONSULTAR VENTAS --")
			print("1. Ver Ventas")
			print("2. Volver al Menú Principal")
			opcionSubmenu = int(input("Seleccione una opción: "))
			if opcionSubmenu == 1:
				# Mostrar todas las ventas registradas
				if ventas:
					print("Lista de ventas registradas:")
					for i, venta in enumerate(ventas, start=1):
						print(f"{i}. Cliente: {venta['cliente']}, Destino: {venta['destino']}")
				else:
					print("No hay ventas registradas.")
			elif opcionSubmenu == 2:
				# Volver al menú principal
				break

	# Botón de arrepentimiento (deshacer última venta)
	elif ingresoNumero == 5:
		while True:
			print("-- BOTÓN DE ARREPENTIMIENTO --")
			print("1. Deshacer última venta")
			print("2. Volver al Menú Principal")
			opcionSubmenu = int(input("Seleccione una opción: "))
			if opcionSubmenu == 1:
				arrepentimiento()
			elif opcionSubmenu == 2:
				break
			else:
				print("Opción inválida.")

	# Reporte general de ventas y clientes
	elif ingresoNumero == 6:
			print("-- REPORTE GENERAL --")
			print(f"Total Clientes: {len(listaClientes)}")
			print(f"Total Ventas: {len(ventas)}")
			print(f"Total Destinos: {len(listaDestinos)}")
			input("Ingrese cualquier número para volver al menú principal...")

	# Información acerca del sistema
	elif ingresoNumero == 7:
			print("Sistema de Gestión de Pasajes SkyRoute.")
			print("Desarrollado por el grupo integrado por Vidal, Esquivel, Lencina, Lloveras y Paez.")
			print("Entrega Evidencia N2.")
			input("Ingrese cualquier número para volver al menú principal...")

	# Salir del sistema
	elif ingresoNumero == 8:
		print("Gracias por usar SkyRoute. ¡Hasta luego!")
		break

	# Opción inválida
	else:
		print("-----")
		print("OPCIÓN INVÁLIDA, por favor ingrese un número entre 1 y 8.")
		print("-----")
