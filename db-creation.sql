CREATE DATABASE IF NOT EXISTS tienda_tecnologia;

USE tienda_tecnologia;

-- Tabla para almacenar la información de productos
CREATE TABLE IF NOT EXISTS productos (
    ProductoID INT AUTO_INCREMENT PRIMARY KEY,
    NombreProducto VARCHAR(255) NOT NULL,
    Categoría VARCHAR(255) NOT NULL,
    Precio DECIMAL(10, 2) NOT NULL,
    Stock INT NOT NULL
);

-- Tabla para almacenar la información de clientes
CREATE TABLE IF NOT EXISTS clientes (
    ClienteID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Apellido VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Teléfono VARCHAR(20)
);