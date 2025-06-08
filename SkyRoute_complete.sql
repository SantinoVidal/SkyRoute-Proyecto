-- CREACIÓN DE BASE DE DATOS
CREATE DATABASE IF NOT EXISTS skyroute_db;
USE skyroute_db;

-- TABLA CLIENTES
CREATE TABLE IF NOT EXISTS clientes (
  CUIT VARCHAR(20) PRIMARY KEY,
  razonSocial VARCHAR(100) NOT NULL,
  contacto VARCHAR(100)
);

-- TABLA DESTINOS
CREATE TABLE IF NOT EXISTS destinos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  ciudad VARCHAR(50) NOT NULL,
  país VARCHAR(50) NOT NULL,
  costo_base DECIMAL(10,2) NOT NULL
);

-- TABLA VENTAS
CREATE TABLE IF NOT EXISTS ventas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  cliente_cuit VARCHAR(20) NOT NULL,
  destino INT NOT NULL,
  fecha_de_venta DATETIME NOT NULL,
  costo DECIMAL(10,2) NOT NULL,
  estado ENUM('Activa', 'Anulada') NOT NULL DEFAULT 'Activa',
  fecha_anulacion DATETIME,
  FOREIGN KEY (cliente_cuit) REFERENCES clientes(cuit),
  FOREIGN KEY (destino_id) REFERENCES destinos(id)
);

-- DATOS DE EJEMPLO: CLIENTES
INSERT INTO clientes (cuit, razon_social, contacto) VALUES
('20-12345678-9', 'Cliente Uno', 'cliente1@mail.com'),
('20-23456789-0', 'Cliente Dos', 'cliente2@mail.com'),
('20-34567890-1', 'Cliente Tres', 'cliente3@mail.com');

-- DATOS DE EJEMPLO: DESTINOS
INSERT INTO destinos (ciudad, pais, costo_base) VALUES
('Buenos Aires', 'Argentina', 15000.00),
('Salta', 'Argentina', 30000.00),
('Santiago', 'Chile', 45000.00);

-- DATOS DE EJEMPLO: VENTAS
INSERT INTO ventas (cliente_cuit, destino_id, fecha_venta, costo, estado) VALUES
('20-12345678-9', 1, '2025-10-01 10:00:00', 15000.00, 'Activa'),
('20-23456789-0', 2, '2025-10-02 11:00:00', 30000.00, 'Activa'),
('20-34567890-1', 3, '2025-10-03 12:00:00', 45000.00, 'Activa');

-- CONSULTAS SQL (DML)

-- 1. Listar todos los clientes
SELECT * FROM clientes;

-- 2. Mostrar las ventas realizadas en una fecha específica
SELECT v.id, c.razon_social, d.ciudad, v.fecha_venta, v.costo, v.estado
FROM ventas v
JOIN clientes c ON v.cliente_cuit = c.cuit
JOIN destinos d ON v.destino_id = d.id
WHERE DATE(v.fecha_venta) = '2025-10-01';

-- 3. Obtener la última venta de cada cliente y su fecha
SELECT cliente_cuit, MAX(fecha_venta) AS ultima_venta
FROM ventas
GROUP BY cliente_cuit;

-- 4. Listar todos los destinos que empiezan con “S”
SELECT * FROM destinos WHERE ciudad LIKE 'S%';

-- 5. Mostrar cuántas ventas se realizaron por país
SELECT d.pais, COUNT(v.id) AS total_ventas
FROM ventas v
JOIN destinos d ON v.destino_id = d.id
GROUP BY d.pais;
