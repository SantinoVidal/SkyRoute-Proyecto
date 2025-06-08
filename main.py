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

from datetime import datetime #Se utiliza para registrar la fecha de venta

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
listaClientes = []  # Lista donde se guardan los clientes (diccionarios con razón social, CUIT y contacto)
ventas = []         # Lista donde se guardan las ventas (diccionarios con cliente, destino y fechas)
listaDestinos = []  # Lista donde se guardan los destinos (nombres de destinos)

# Función para agregar una nueva venta
def agregar_venta(cuit, id_destino):
	fecha= datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Registra la fecha y hora de venta
	venta = {"cliente_cuit": cuit, "destino_id": id_destino, "fecha_de_venta" : fecha, "costo": costo_base, "estado":"Activa"}  # Crear diccionario con datos de venta
	ventas.append(venta)                              # Agregar venta a la lista de ventas
	print(f"Venta agregada: {venta}")

# Función para deshacer la última venta (botón de arrepentimiento)
from datetime import datetime, timedelta
def arrepentimiento():
    if ventas:
        ultima_venta = ventas.pop() #Quitar la última venta agregada
        fecha_venta = datetime.strptime(ultima_venta["fecha_de_venta"], "%Y-%m-%d %H:%M:%S")
        fecha_actual = datetime.now()

        # Contar días hábiles entre la venta y hoy
        dias_habiles = 0
        fecha_temp = fecha_venta

        while fecha_temp.date() <= fecha_actual.date():
            if fecha_temp.weekday() < 5:  # 0 a 4 = lunes a viernes
                dias_habiles += 1
            fecha_temp += timedelta(days=1)

        if dias_habiles <= 10:
            ultima_venta["estado"] = "Anulada"
            ultima_venta["fecha_anulación"] = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
            print("Venta anulada correctamente.")
        else:
            print("No se puede anular: han pasado más de 10 días hábiles.")
    else:
        print("No hay ventas para revertir.") # Avisar si no hay ventas para borrar

# Función auxiliar para buscar cliente por CUIT
def buscar_cliente_por_cuit(cuit):
	for cliente in listaClientes:
		if cliente["CUIT"] == cuit:
			return cliente
	return None

# Función auxiliar para buscar destino por ciudad
def buscar_destino_por_ciudad(ciudad):
	for destino in listaDestinos:
		if destino["ciudad"].lower() == ciudad.lower():
			return destino
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
						print(f"{cliente['razonSocial']} - CUIT: {cliente['CUIT']} - Contacto: {cliente['contacto']}")
				else:
					print("No hay clientes registrados.")

			elif opcionSubmenu == 2:
				# Agregar un nuevo cliente solicitando datos
				razonSocial = input("Ingrese la razón social del nuevo cliente: ")
				cuit = input("Ingrese el CUIT del nuevo cliente: ")
				contacto = input("Ingrese email de contacto: ")
				nuevoCliente = {"razonSocial": razonSocial, "CUIT": cuit, "contacto":contacto}
				listaClientes.append(nuevoCliente)  # Guardar nuevo cliente en la lista
				print(f"Cliente '{razonSocial}' agregado.")

			elif opcionSubmenu == 3:
				# Modificar datos de un cliente buscando por CUIT
				cuitAModificar = input("Ingrese el CUIT que desea modificar: ")
				cliente = buscar_cliente_por_cuit(cuitAModificar)
				if cliente:
					cliente["razón social"] = input("Nueva razón social: ")
					cliente["CUIT"] = input("Nuevo CUIT: ")
					cliente["contacto"] = input("Nuevo email de contacto: ")
					print("Cliente modificado.")
				else:
					print("Cliente no encontrado.")  # Si no encontró el CUIT

			elif opcionSubmenu == 4:
				# Eliminar cliente buscando por CUIT
				cuitAEliminar = input("Ingrese el CUIT que desea eliminar: ")
				cliente = buscar_cliente_por_cuit(cuitAEliminar)
				if cliente:
					listaClientes.remove(cliente)  # Quitar cliente de la lista
					print("Cliente eliminado.")
				else:
					print("Cliente no encontrado.")  # Si no encontró el CUIT

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
				ciudad = input("Ingrese el nombre de la ciudad: ")
				pais = input("Ingrese el nombre del país: ")
				costo_base = input("Ingrese costo base del viaje: ")
				nuevoDestino = {"ciudad": ciudad, "pais": pais, "costo_base": costo_base}
				listaDestinos.append(nuevoDestino)
				print(f"Destino '{nuevoDestino}' agregado correctamente.")

			elif opcionDestino == 3:
				# Cambiar el nombre de un destino existente
				ciudad_actual = input("Ingrese el nombre de la ciudad a modificar: ")
				destino_encontrado = False
				for destino in listaDestinos:
					if destino["ciudad"].lower() == ciudad_actual.lower():
						nueva_ciudad = input("Ingrese el nuevo nombre de la ciudad: ")
						nuevo_pais = input("Ingrese el nuevo nombre del país: ")
						nuevo_costo = input("Ingrese el nuevo costo base del viaje: ")
						destino["ciudad"] = nueva_ciudad
						destino["país"] = nuevo_pais
						destino["costo_base"] = nuevo_costo
						print("Destino modificado correctamente.")
						destino_encontrado = True
						break
					if not destino_encontrado:
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
				cuit_cliente = input("Ingrese CUIT del Cliente para la venta: ")
				cliente = buscar_cliente_por_cuit(cuit_cliente)
				if not cliente:
					print("Cliente no encontrado.")
					continue

				destino_venta = input("Ingrese la ciudad del destino: ")
				destino = buscar_destino_por_ciudad(destino_venta)
				if not destino:
					print("Destino no válido.")
					continue
				agregar_venta(cliente["razonSocial"], destino["ciudad"])

			elif opcionSubmenu == 2:
				# Modificar venta buscando por CUIT del cliente
				cuit_a_buscar = input("Ingrese el CUIT del cliente de la venta que desea modificar: ")
				cliente = buscar_cliente_por_cuit(cuit_a_buscar)
				if cliente:
					venta_encontrada = False
					for venta in ventas:
						if venta["cliente_cuit"] == cliente["CUIT"]:
							nuevo_cuit = input("Ingrese el nuevo CUIT del cliente: ")
							nuevo_destino = input("Ingrese el nuevo destino: ")
							venta["cliente_CUIT"] = nuevo_cuit
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
				# Eliminar venta buscando por CUIT del cliente
				cuit_a_eliminar = input("Ingrese el CUIT del cliente de la venta que desea eliminar: ")
				cliente = buscar_cliente_por_cuit(cuit_a_eliminar)
				if cliente:
					venta_encontrada = False
					for venta in ventas:
						if venta["cliente_cuit"] == cliente["CUIT"]:
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
						estado = venta.get("estado", "Desconocido")
						fecha_anulacion = venta.get("fecha_de_anulación", "No anulada")
						print(f"{i}. Cliente: {venta['cliente']}, Destino: {venta['destino']}, Fecha: {venta['fecha_de_venta']}, Estado: {estado}, Anulación: {fecha_anulacion}")
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
