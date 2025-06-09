import mysql.connector

# datos de conexion
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1111",
    database = "skyroute_db"
)

cursor = conexion.cursor()
# ejecutar una consulta

# Listar clientes 
print(" --- CLIENTES --- ")
cursor.execute("SELECT * FROM clientes")
for fila in cursor.fetchall():
    print(fila)

# Mostrar ventas realizadas en una fecha especifica 
print(" --- VENTAS DEL 2025-10-01 --- ")
consulta2 = """
SELECT v.id, c.razonSocial, d.ciudad, v.fecha_de_venta, v.costo, v.estado
FROM ventas v
JOIN clientes c ON v.cliente_cuit = c.cuit
JOIN destinos d ON v.destino = d.id
WHERE DATE(v.fecha_de_venta) = '2025-10-01'
"""
cursor.execute(consulta2)
for fila in cursor.fetchall():
    print(fila)

# Listar la ultima venta de cada cliente
print(" --- ULTIMA VENTA DE CADA CLIENTE --- ")
cursor.execute("SELECT cliente_cuit, MAX(fecha_de_venta) AS ultima_venta FROM ventas GROUP BY cliente_cuit")
for fila in cursor.fetchall():
    print(fila)

# Destinos que empiezan con S
print(" --- DESTINOS QUE EMPIEZAN CON 'S' --- ")
cursor.execute("SELECT * FROM destinos WHERE ciudad LIKE 'S%'")
for fila in cursor.fetchall():
    print(fila)


# Cerrar la conexion 
cursor.close()
conexion.close()