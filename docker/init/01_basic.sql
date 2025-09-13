SET search_path TO basic;

DROP TABLE IF EXISTS vendas;
DROP TABLE IF EXISTS clientes;

CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100),
    cidade VARCHAR(100),
    estado CHAR(2)
);

CREATE TABLE vendas (
    id_venda INT PRIMARY KEY,
    id_cliente INT REFERENCES clientes(id_cliente),
    data_venda DATE,
    valor_venda NUMERIC(12,2)
);
