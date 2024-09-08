-- Crear base de datos si no existe
CREATE DATABASE IF NOT EXISTS tienda_tecnologia;

-- Usar la base de datos creada
USE tienda_tecnologia;

-- Crear tabla de productos si no existe
CREATE TABLE IF NOT EXISTS productos (
    producto_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(255) NOT NULL,
    categoria VARCHAR(255) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL CHECK (precio >= 0),  -- Asegura que el precio no sea negativo
    stock INT NOT NULL CHECK (stock >= 0),  -- Asegura que el stock no sea negativo
    INDEX idx_nombre_producto (nombre_producto),  -- Índice para mejorar búsquedas por nombre de producto
    INDEX idx_categoria (categoria)  -- Índice para mejorar búsquedas por categoría
);

-- Crear tabla de clientes si no existe
CREATE TABLE IF NOT EXISTS clientes (
    cliente_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    telefono VARCHAR(20),  -- Puedes agregar validaciones o formato dependiendo de las necesidades
    CHECK (email LIKE '%_@__%.__%')  -- Verifica que el email tenga un formato básico válido
);

-- Opcional: Crear índices adicionales para optimizar búsquedas por nombre y apellido
CREATE INDEX idx_nombre_apellido ON clientes (nombre, apellido);