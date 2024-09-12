
CREATE DATABASE  tienda_tecnologia;

USE tienda_tecnologia;
CREATE TABLE Clientes (
    ID_Cliente INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Email VARCHAR(100),
    Telefono VARCHAR(20)
);

CREATE TABLE Pedidos (
    ID_Pedido INT PRIMARY KEY,
    ID_Cliente INT,
    Producto VARCHAR(100),
    Precio_ud DECIMAL(10, 2),
    Cantidad INT,
    Precio_total DECIMAL(10, 2),
);

CREATE TABLE Clientes_Pedidos (
    ID_Cliente INT,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Email VARCHAR(100),
    Telefono VARCHAR(20),
    ID_Pedido INT,
    Producto VARCHAR(100),
    Precio_ud DECIMAL(10, 2),
    Cantidad INT,
    Precio_total DECIMAL(10, 2),
);